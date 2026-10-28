// CELLOG feedback — the in-game "Report a bug or suggestion" form posts here.
// Each report becomes an issue in the private feedback repo (GitHub emails
// the owner); GET ?ids=3,7 returns just those issues' status for the
// player's "My reports" list. No player accounts: the game remembers which
// report numbers are theirs, on their device. Each report gets a key (an
// HMAC of its number) that only the sender's device holds: its 📣 notes are
// shown only to someone with the key. A report also carries a reference
// (rid) chosen by the device, so a resend finds the same issue instead of
// opening another.
//
// Needs FEEDBACK_GITHUB_TOKEN in the Vercel project's environment variables:
// a fine-grained token with Issues read/write on that one repo only.

const crypto = require("crypto");
const REPO = process.env.FEEDBACK_REPO || "shilk3/cellog-feedback";
const LIMITS = { text: 4000, email: 200, log: 8000, context: 3000, save: 600000 };
const SAVE_CHUNK = 60000; // an issue comment holds 65,536 characters
const RATE = { max: 6, windowMs: 10 * 60 * 1000 }; // reports per address, best effort
const STATUS_RATE = { max: 30, windowMs: 10 * 60 * 1000 }; // status checks per address
const STATUS_IDS = 20; // reports per status check
const recent = new Map();
const recentStatus = new Map();
const sentRids = new Map(); // rid → issue number, while this instance lives

// The live game, its GitHub Pages copy, Vercel previews of it, and local dev.
function allowedOrigin(origin) {
  return (
    origin === "https://cellog.vercel.app" ||
    origin === "https://shilk3.github.io" ||
    /^https:\/\/cellog[-a-z0-9]*\.vercel\.app$/.test(origin) ||
    /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(origin)
  );
}

async function gh(path, method = "GET", body) {
  const res = await fetch(path.startsWith("/search/") ? `https://api.github.com${path}` : `https://api.github.com/repos/${REPO}${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${process.env.FEEDBACK_GITHUB_TOKEN}`,
      Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
      "User-Agent": "cellog-feedback",
      ...(body ? { "Content-Type": "application/json" } : {}),
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw Object.assign(new Error(data.message || `GitHub ${res.status}`), { status: res.status });
  return data;
}

const str = (v, max) => (typeof v === "string" ? v.slice(0, max) : "");
// Player text goes in as written, minus anything that would ping a GitHub user.
const quiet = (s) => s.replace(/@(?=[A-Za-z0-9])/g, "@​");
const cell = (s) => quiet(String(s)).replace(/\|/g, "\\|").replace(/\n/g, " ");

function rateLimited(ip, map = recent, rate = RATE) {
  const now = Date.now();
  const hits = (map.get(ip) || []).filter((t) => now - t < rate.windowMs);
  hits.push(now);
  map.set(ip, hits);
  return hits.length > rate.max;
}
const ipOf = (req) => String(req.headers["x-forwarded-for"] || "").split(",")[0].trim() || "unknown";
// A report's key: only the device that sent it gets it back.
const SECRET = process.env.FEEDBACK_SECRET || crypto.createHash("sha256").update(String(process.env.FEEDBACK_GITHUB_TOKEN)).digest("hex");
const keyOf = (n) => crypto.createHmac("sha256", SECRET).update(String(n)).digest("hex").slice(0, 16);
const keyOk = (n, key) => /^[0-9a-f]{16}$/.test(key || "") && crypto.timingSafeEqual(Buffer.from(key), Buffer.from(keyOf(n)));

// Open / in progress / fixed / won't do / closed, from the issue's labels.
function statusOf(issue) {
  const labels = (issue.labels || []).map((l) => (typeof l === "string" ? l : l.name));
  if (labels.includes("fixed")) return "fixed";
  if (labels.includes("won't do")) return "wontdo";
  if (issue.state === "closed") return "closed";
  if (labels.includes("in progress")) return "progress";
  return "open";
}

// A comment starting with 📣 is a note for the player, shown in My reports.
async function playerNote(issue) {
  if (!issue.comments) return "";
  const comments = await gh(`/issues/${issue.number}/comments?per_page=100`);
  const note = comments.reverse().find((c) => (c.body || "").trim().startsWith("📣"));
  // (minus any signature footer under a --- rule)
  return note ? note.body.trim().replace(/^📣\s*/, "").replace(/\n+-{3,}\n[\s\S]*$/, "").trim().slice(0, 300) : "";
}

// ?ids=12:key,7 — with a report's key: its status and 📣 note; without
// (reports sent before keys): its status only.
async function status(req, res) {
  if (rateLimited(ipOf(req), recentStatus, STATUS_RATE)) return res.status(429).json({ error: "Too many checks — try again in a few minutes." });
  const ids = String(req.query.ids || "")
    .split(",")
    .map((s) => {
      const [n, key] = s.split(":");
      return { n: Number(n), key };
    })
    .filter(({ n }) => Number.isInteger(n) && n > 0)
    .slice(0, STATUS_IDS);
  const reports = await Promise.all(
    ids.map(async ({ n, key }) => {
      try {
        const issue = await gh(`/issues/${n}`);
        return keyOk(n, key) ? { n, status: statusOf(issue), note: await playerNote(issue) } : { n, status: statusOf(issue) };
      } catch (e) {
        return { n, status: "unknown" };
      }
    })
  );
  res.status(200).json({ reports });
}

async function create(req, res) {
  const b = typeof req.body === "string" ? JSON.parse(req.body || "{}") : req.body || {};
  if (b.website) return res.status(200).json({ ok: true }); // the hidden field: a bot filled it in
  const type = b.type === "suggestion" ? "suggestion" : "bug";
  const text = str(b.text, LIMITS.text).trim();
  if (text.length < 5) return res.status(400).json({ error: "Please say a little more." });
  const email = str(b.email, LIMITS.email).trim();
  if (email && !/^[^\s@`]+@[^\s@`]+\.[^\s@`]+$/.test(email)) return res.status(400).json({ error: "That email doesn't look right." });
  // Sent before (the reply was lost, say): the same issue, not another.
  const rid = /^[a-z0-9]{8,40}$/.test(b.rid || "") ? b.rid : "";
  if (rid) {
    let number = sentRids.get(rid);
    if (!number) {
      try {
        const found = await gh(`/search/issues?q=${encodeURIComponent(`repo:${REPO} in:body "ref ${rid}"`)}`);
        number = found.items && found.items[0] && found.items[0].number;
      } catch (e) {
        // search unavailable: carry on and create it
      }
    }
    if (number) return res.status(200).json({ ok: true, number, key: keyOf(number) });
  }
  if (rateLimited(ipOf(req))) return res.status(429).json({ error: "That's a lot of reports in a short time — please try again in a few minutes." });

  const ctx = b.context && typeof b.context === "object" ? b.context : {};
  const ctxRows = Object.entries(ctx)
    .slice(0, 20)
    .map(([k, v]) => `| ${cell(str(k, 40))} | ${cell(str(String(v), 300))} |`)
    .join("\n")
    .slice(0, LIMITS.context);
  const log = str(Array.isArray(b.log) ? b.log.join("\n") : b.log, LIMITS.log).replace(/```/g, "ˋˋˋ");
  // A save code is its prefix and base64 — anything else isn't attached.
  const save = (() => {
    const s = str(b.save, LIMITS.save).replace(/\s+/g, "");
    return /^CG1[zj]:[A-Za-z0-9+/=]+$/.test(s) ? s : "";
  })();
  const firstLine = text.split("\n")[0].replace(/\s+/g, " ").trim();
  const title = quiet(`${type === "bug" ? "🐞" : "💡"} ${firstLine.length > 70 ? firstLine.slice(0, 69) + "…" : firstLine}`);
  const body = [
    `**${type === "bug" ? "🐞 Bug" : "💡 Suggestion"}** · ${email ? `reply to \`${email}\`` : "_no email given_"}`,
    "",
    quiet(text),
    "",
    "### Game",
    "| | |",
    "|---|---|",
    ctxRows || "| (none) | |",
    log ? `\n<details><summary>Last log lines</summary>\n\n\`\`\`text\n${log}\n\`\`\`\n</details>` : "",
    save ? `\n💾 Save attached in the comments below (${Math.ceil(save.length / SAVE_CHUNK)} part${save.length > SAVE_CHUNK ? "s" : ""}).` : "",
    "",
    `<sub>Sent from the in-game form${rid ? ` (ref ${rid})` : ""}. A comment starting with 📣 shows in the player's My reports.</sub>`,
  ].join("\n");

  const issue = await gh("/issues", "POST", { title, body, labels: [type] });
  if (rid) sentRids.set(rid, issue.number);
  // The report's in: a save that can't be attached doesn't undo it (a
  // failure here would only make the device send it all again).
  if (save) {
    const parts = Math.ceil(save.length / SAVE_CHUNK);
    try {
      for (let i = 0; i < parts; i++) {
        const chunk = save.slice(i * SAVE_CHUNK, (i + 1) * SAVE_CHUNK);
        const head = parts > 1 ? `💾 Save code, part ${i + 1} of ${parts} — join the parts in order, then paste into Export / Import Save.` : "💾 Save code — paste into Export / Import Save.";
        await gh(`/issues/${issue.number}/comments`, "POST", { body: `${head}\n\n\`\`\`\n${chunk}\n\`\`\`` });
      }
    } catch (e) {
      await gh(`/issues/${issue.number}/comments`, "POST", { body: "💾 The save couldn't be attached in full (GitHub refused part of it)." }).catch(() => {});
    }
  }
  res.status(200).json({ ok: true, number: issue.number, key: keyOf(issue.number) });
}

module.exports = async (req, res) => {
  const origin = req.headers.origin || "";
  if (allowedOrigin(origin)) {
    res.setHeader("Access-Control-Allow-Origin", origin);
    res.setHeader("Vary", "Origin");
    res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  }
  res.setHeader("Cache-Control", "no-store");
  if (req.method === "OPTIONS") return res.status(204).end();
  if (!process.env.FEEDBACK_GITHUB_TOKEN) return res.status(503).json({ error: "not-configured" });
  try {
    if (req.method === "GET") return await status(req, res);
    if (req.method === "POST") return await create(req, res);
    res.status(405).json({ error: "Method not allowed" });
  } catch (e) {
    res.status(502).json({ error: "Couldn't reach the report log just now." });
  }
};
