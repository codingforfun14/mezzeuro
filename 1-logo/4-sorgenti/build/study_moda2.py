"""Focused study: Bodoni Moda instances for the symbol, judged in a circular avatar at real sizes."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mz  # noqa: E402

ROOT = os.path.normpath(os.path.join(mz.HERE, ".."))
VF = os.path.join(ROOT, "fonts", "BodoniModa-VF.ttf")
RENDER = os.path.expanduser("~/.claude/skills/logo-design/scripts/render_png.py")
CANDS = [(560, 24), (600, 18), (620, 14), (660, 12)]
T, GAP, OVER = 36, 62, 54
BG, INK = "#6E1E2C", "#F5EFE4"


def mark(font, width=174):
    d, bb = mz.text(font, 1000, "m")
    xh = -bb[1]
    k = width / (bb[2] - bb[0])
    left = 128 - width / 2
    base = 127 + xh * k / 2
    mid = base - xh * k / 2
    q = k * 439 / xh
    t, gap, over = T * q, GAP * q, OVER * q
    bars = (mz.rect(left - over, mid - gap / 2 - t, width + 2 * over, t)
            + mz.rect(left - over, mid + gap / 2, width + 2 * over, t))
    return mz.affine(d, k, left - bb[0] * k, base) + bars


work = os.path.join(ROOT, "exploration", "study-moda2")
os.makedirs(work, exist_ok=True)
rows = []
for w, o in CANDS:
    font = f"{VF}@wght={w},opsz={o}"
    svg = mz.svg(256, 256, f'<circle cx="128" cy="128" r="128" fill="{BG}"/>'
                 f'<g transform="translate(15.36 15.36) scale(0.88)">{mz.path(mark(font), INK)}</g>')
    base = os.path.join(work, f"m-{w}-{o}")
    mz.write(base + ".svg", svg)
    cells = []
    for px in (160, 56, 32):
        subprocess.run([sys.executable, "-I", RENDER, base + ".svg", "-o", f"{base}-{px}.png", "--size", str(px)],
                       check=True, capture_output=True)
        cells.append(f'<img src="m-{w}-{o}-{px}.png" width="{px}">')
    cells.append(f'<img class="px" src="m-{w}-{o}-32.png" width="128">')
    rows.append(f'<div class="row"><b>wght {w} · opsz {o}</b>{"".join(cells)}</div>')
html = ("<!doctype html><meta charset='utf-8'><style>body{margin:20px;font:13px Helvetica;background:#fff}"
        ".row{display:flex;align-items:center;gap:22px;margin-bottom:18px}.row b{width:130px}"
        "img.px{image-rendering:pixelated}</style>" + "".join(rows))
with open(os.path.join(work, "index.html"), "w", encoding="utf-8") as fh:
    fh.write(html)
subprocess.run([sys.executable, "-I", RENDER, os.path.join(work, "index.html"), "-o",
                os.path.join(ROOT, "exploration", "study-moda2.png"), "--width", "700", "--height", "760"], check=True)
