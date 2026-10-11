#!/usr/bin/env python3
"""Builds the in-game guide pages from the two claude.ai artifacts' sources.

  python3 tools/build_guides.py <infographic Main.dc.html> <mechanics map .html>

Writes guide/infographic.html and guide/map.html. Run it whenever either
artifact changes (the standing rule: mechanic changes update both), then bump
APP_VERSION / CACHE_NAME as for any deploy.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = re.search(r'APP_VERSION = "([^"]+)"', (ROOT / "game.js").read_text()).group(1)

BACK_CSS = """
.cellog-back{position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:10px;
  padding:calc(8px + env(safe-area-inset-top,0px)) 16px 8px;background:#0b1220;border-bottom:1px solid #263149;
  font:600 14px -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.cellog-back a{color:#34d0a0;text-decoration:none}
.cellog-back span{color:#93a1bd;font-weight:500;font-size:12.5px;margin-left:auto}
"""


def back_bar(other_href, other_label):
    return (f'<nav class="cellog-back"><a href="../index.html">← Back to CELLOG</a>'
            f'<a href="{other_href}">{other_label}</a><span>v{VERSION}</span></nav>')


def head(title, extra=""):
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<title>{title}</title>\n<style>{BACK_CSS}</style>\n{extra}</head>\n')


def build_infographic(src):
    s = Path(src).read_text()
    style = re.search(r"<helmet>(.*?)</helmet>", s, re.S).group(1)
    body = s.split("</helmet>", 1)[1]
    body = re.split(r"<script type=\"text/x-dc\"", body)[0]
    body = body.replace("</x-dc>", "")
    # Version pill follows the game.
    body = re.sub(r'(font-family:ui-monospace,monospace;">)v[\d.]+(</div>)', rf"\g<1>v{VERSION}\2", body, count=1)
    # It's a fixed-width desktop design: keep it full size in its own
    # sideways scroller (the page itself never scrolls sideways), with a
    # Fit width toggle for an overview — pinch to zoom from there.
    fit_css = ("<style>.ig-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}.ig-wrap{min-width:1180px}"
               ".cellog-back button{font:600 13px inherit;color:#e7edf7;background:#131c2e;border:1px solid #263149;"
               "border-radius:8px;padding:4px 10px}</style>\n")
    fit_js = ("<script>(function(){var b=document.getElementById('igFit'),w=document.querySelector('.ig-wrap'),on=false;"
              "if(!b||!w)return;b.addEventListener('click',function(){on=!on;w.style.zoom=on?Math.min(1,(innerWidth-4)/1320):'';"
              "b.textContent=on?'Full size':'Fit width';});if(innerWidth>=1180)b.hidden=true;})();</script>\n")
    bar = back_bar("map.html", "🗺️ Map").replace("<span>", '<button type="button" id="igFit">Fit width</button><span>', 1)
    out = (head("CELLOG Infographic", style + fit_css) + "<body>\n" + bar
           + '<div class="ig-scroll"><div class="ig-wrap">' + body + "</div></div>\n" + fit_js + "</body>\n</html>\n")
    (ROOT / "guide" / "infographic.html").write_text(out)


def build_map(src):
    s = Path(src).read_text()
    m = re.match(r"\s*<title>.*?</title>\s*", s, re.S)
    rest = s[m.end():]
    # The artifact skeleton's reset, which the page relies on.
    reset = ("<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
             "body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}"
             ".cellog-back{padding-top:8px}</style>\n")
    links = "".join(l + "\n" for l in re.findall(r"<link[^>]*>", rest[:2000]))
    rest = re.sub(r"<link[^>]*>\s*", "", rest, count=3)
    out = head("CELLOG Mechanics Map", reset + links) + "<body>\n" + back_bar("infographic.html", "📊 Infographic") + "\n" + rest + "\n</body>\n</html>\n"
    out = out.replace("(v4.70)", f"(v{VERSION})")
    (ROOT / "guide" / "map.html").write_text(out)


if __name__ == "__main__":
    build_infographic(sys.argv[1])
    build_map(sys.argv[2])
    print("guide/infographic.html, guide/map.html built for v" + VERSION)
