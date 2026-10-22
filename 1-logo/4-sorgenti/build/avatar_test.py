"""Avatar test: each symbol in a circular profile picture (light and dark), rendered at the real Instagram /
YouTube display sizes, shown at 1x and enlarged 4x (pixelated) on one sheet.

  python3 build/avatar_test.py concepts/v3      -> exploration/avatar-<ver>.png
"""
import os
import re
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
RENDER = os.path.expanduser("~/.claude/skills/logo-design/scripts/render_png.py")
SIZES = [160, 56, 32, 24]
FILL = {"a": 0.84, "b": 0.86, "c": 1.0}          # share of the circle the 256 canvas occupies
THEMES = {"light": ("#E9E6E1", "#111111"), "dark": ("#111111", "#F4F1EC")}

src_dir = os.path.join(ROOT, sys.argv[1] if len(sys.argv) > 1 else "concepts/v3")
ver = os.path.basename(os.path.normpath(src_dir))
work = os.path.join(ROOT, "exploration", f"avatar-{ver}")
os.makedirs(work, exist_ok=True)

rows = []
for c in "abc":
    src = open(os.path.join(src_dir, f"{c}-symbol.svg"), encoding="utf-8").read()
    inner = re.sub(r"^.*?<svg[^>]*>", "", src, flags=re.S).rsplit("</svg>", 1)[0]
    inner = re.sub(r"<title[^>]*>.*?</title>", "", inner)
    for theme, (bg, ink) in THEMES.items():
        s = 256 * FILL[c]
        o = (256 - s) / 2
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256">'
               f'<circle cx="128" cy="128" r="128" fill="{bg}"/>'
               f'<svg x="{o}" y="{o}" width="{s}" height="{s}" viewBox="0 0 256 256">'
               f'{inner.replace("#111111", ink)}</svg></svg>')
        base = os.path.join(work, f"{c}-{theme}")
        with open(base + ".svg", "w", encoding="utf-8") as fh:
            fh.write(svg)
        for px in SIZES:
            subprocess.run([sys.executable, "-I", RENDER, base + ".svg", "-o", f"{base}-{px}.png", "--size", str(px)],
                           check=True, capture_output=True)
        cells = "".join(f'<div class="c"><img src="{c}-{theme}-{px}.png" width="{px}" height="{px}"><span>{px}</span></div>'
                        for px in SIZES)
        big = "".join(f'<div class="c"><img class="px" src="{c}-{theme}-{px}.png" width="{px * 4}" height="{px * 4}">'
                      f'<span>{px} px ×4</span></div>' for px in (32, 24))
        rows.append(f'<div class="row"><b>{c.upper()} · {theme}</b>{cells}{big}</div>')

html = ("<!doctype html><meta charset='utf-8'><style>body{margin:24px;font:13px Helvetica;background:#fff;color:#555}"
        ".row{display:flex;align-items:flex-end;gap:22px;margin:0 0 26px}.row b{width:70px;color:#111}"
        ".c{display:flex;flex-direction:column;align-items:center;gap:6px}"
        "img.px{image-rendering:pixelated}</style>" + "".join(rows))
page = os.path.join(work, "index.html")
with open(page, "w", encoding="utf-8") as fh:
    fh.write(html)
out = os.path.join(ROOT, "exploration", f"avatar-{ver}.png")
subprocess.run([sys.executable, "-I", RENDER, page, "-o", out, "--width", "1000", "--height", "1360"], check=True)
print("wrote", os.path.relpath(out, ROOT))
