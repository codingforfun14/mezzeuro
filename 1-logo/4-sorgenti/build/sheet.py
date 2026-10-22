"""Lay out several SVG files on one sheet (nested <svg>), for looking at a set in a single render.

  python3 build/sheet.py out.svg --cols 3 --cell 256 256 --gap 24 a.svg b.svg c.svg
"""
import argparse
import re

ap = argparse.ArgumentParser()
ap.add_argument("out")
ap.add_argument("files", nargs="+")
ap.add_argument("--cols", type=int, default=3)
ap.add_argument("--cell", type=float, nargs=2, default=(256, 256))
ap.add_argument("--gap", type=float, default=24)
ap.add_argument("--bg", default="#ffffff")
a = ap.parse_args()

cw, ch = a.cell
rows = (len(a.files) + a.cols - 1) // a.cols
W = a.cols * cw + (a.cols + 1) * a.gap
H = rows * ch + (rows + 1) * a.gap
parts = [f'<rect width="{W}" height="{H}" fill="{a.bg}"/>']
for i, fn in enumerate(a.files):
    src = open(fn, encoding="utf-8").read()
    vb = re.search(r'viewBox="([^"]+)"', src).group(1)
    inner = re.sub(r"^.*?<svg[^>]*>", "", src, flags=re.S).rsplit("</svg>", 1)[0]
    x = a.gap + (i % a.cols) * (cw + a.gap)
    y = a.gap + (i // a.cols) * (ch + a.gap)
    parts.append(f'<svg x="{x}" y="{y}" width="{cw}" height="{ch}" viewBox="{vb}" '
                 f'preserveAspectRatio="xMidYMid meet">{inner}</svg>')
with open(a.out, "w", encoding="utf-8") as fh:
    fh.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
             + "".join(parts) + "</svg>\n")
print(f"wrote {a.out} ({W:g}x{H:g})")
