// Bump this on every deploy that changes cached files — it's what makes the
// browser notice this file changed and install a new service worker.
const CACHE_NAME = "cellog-v216";
const ASSETS = [
  "./",
  "index.html",
  "style.css",
  "game.js",
  "edu-functions.js",
  "edu-banks.js",
  "edu-general.js",
  "edu-inv.js",
  "edu-pqgroups.js",
  "manifest.webmanifest",
  "icons/icon-192.png",
  "icons/icon-512.png",
  "icons/apple-touch-icon.png",
  "icons/icon-maskable-512.png",
  "guide/infographic.html",
  "guide/map.html",
];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k))))
  );
  self.clients.claim();
});

// Network-first, always checked with the server: { cache: "no-cache" }
// skips the browser's own HTTP cache unless the server confirms it's still
// current (a quick 304), so a plain fetch() can't hand back a stale copy
// under GitHub Pages' Cache-Control headers, and unchanged files aren't
// downloaded again. Our own cache is the fallback: offline, or when the
// network hangs for NETWORK_WAIT_MS (it still finishes and updates the
// cache for next time).
const NETWORK_WAIT_MS = 5000;
self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;
  // Bug reports and their status are always live — never cached.
  if (new URL(event.request.url).pathname.startsWith("/api/")) return;
  const req = event.request;
  const network = fetch(req, { cache: "no-cache" }).then((response) => {
    if (response && response.status === 200) {
      const clone = response.clone();
      caches.open(CACHE_NAME).then((cache) => cache.put(req, clone));
    }
    return response;
  });
  event.waitUntil(network.catch(() => {}));
  event.respondWith(
    (async () => {
      try {
        const first = await Promise.race([network, new Promise((done) => setTimeout(done, NETWORK_WAIT_MS, null))]);
        if (first) return first;
        return (await caches.match(req)) || (await network);
      } catch (e) {
        const cached = await caches.match(req);
        if (cached) return cached;
        throw e;
      }
    })()
  );
});
