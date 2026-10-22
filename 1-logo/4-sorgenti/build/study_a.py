"""Type study for concept A: a serif lowercase m crossed by the two euro bars, across 8 installed serifs."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mz  # noqa: E402

FONTS = [
    ("BodoniSvtyTwoITCTT-Bold", "Bodoni 72 Bold"),
    ("BodoniSvtyTwoITCTT-Book", "Bodoni 72 Book"),
    ("Didot-Bold", "Didot Bold"),
    ("Baskerville-SemiBold", "Baskerville SemiBold"),
    ("BigCaslon-Medium", "Big Caslon"),
    ("HoeflerText-Black", "Hoefler Black"),
    ("Cochin-Bold", "Cochin Bold"),
    ("BodoniSvtyTwoOSITCTT-Bold", "Bodoni 72 Oldstyle Bold"),
]
T, GAP, OVER = 9, 12, 12  # bar thickness, gap between bars, overhang


def tile(font, mode, ox, oy):
    d, bb = mz.text(font, 1000, "m")
    k = 168 / (bb[2] - bb[0])
    top, bottom = bb[1] * k, bb[3] * k
    base = 126 - (top + bottom) / 2 + oy
    left = 128 - 84 + ox
    dm = mz.affine(d, k, left - bb[0] * k, base)
    mid = base + top / 2
    y1, y2 = mid - GAP / 2 - T, mid + GAP / 2
    if mode == "full":
        x0, x1 = left - OVER, left + 168 + OVER
    else:
        x0, x1 = left - 18, left + 0.30 * 168
    bars = mz.rect(x0, y1, x1 - x0, T) + mz.rect(x0, y2, x1 - x0, T)
    return mz.path(dm) + mz.path(bars)


body = ['<rect width="2048" height="600" fill="#fff"/>']
for col, (font, label) in enumerate(FONTS):
    for row, mode in enumerate(("full", "left")):
        body.append(tile(font, mode, col * 256, row * 270))
    body.append(f'<text x="{col * 256 + 128}" y="575" font-family="Helvetica" font-size="17" '
                f'text-anchor="middle" fill="#555">{label}</text>')
out = mz.write(os.path.join(mz.HERE, "..", "exploration", "study-a-type.svg"), mz.svg(2048, 600, "".join(body)))
print("wrote", os.path.normpath(out))
