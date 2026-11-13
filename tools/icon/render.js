// Renders tools/icon/icon.svg to the app's PNG icons (node tools/icon/render.js).
// Needs Playwright's Chromium (CHROME env var or the default sandbox path).
const path = require("path"), fs = require("fs");
const { chromium } = require(process.env.PW || "playwright-core");
(async () => {
  const svg = fs.readFileSync(path.join(__dirname, "icon.svg"), "utf8");
  // Maskable: the artwork shrunk into the 80% safe circle, background full-bleed.
  const maskable = svg.replace('<g id="art">', '<g id="art" transform="translate(256 256) scale(.78) translate(-256 -256)">');
  const out = path.join(__dirname, "..", "..", "icons");
  const b = await chromium.launch({ executablePath: process.env.CHROME || "/opt/pw-browsers/chromium-1194/chrome-linux/chrome", args: ["--no-sandbox"] });
  const p = await b.newPage();
  for (const [file, size, src] of [["apple-touch-icon.png", 180, svg], ["icon-192.png", 192, svg], ["icon-512.png", 512, svg], ["icon-maskable-512.png", 512, maskable]]) {
    await p.setViewportSize({ width: size, height: size });
    await p.setContent(`<html><body style="margin:0">${src.replace("<svg ", `<svg width="${size}" height="${size}" `)}</body></html>`);
    await p.screenshot({ path: path.join(out, file), clip: { x: 0, y: 0, width: size, height: size } });
    console.log(file, size);
  }
  await b.close();
})();
