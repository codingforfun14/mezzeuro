"""Compare the concept's Bodoni 72 m with Bodoni Moda instances (weight / optical size), bars included."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mz  # noqa: E402

VF = os.path.normpath(os.path.join(mz.HERE, "..", "fonts", "BodoniModa-VF.ttf"))
SPECS = [
    ("BodoniSvtyTwoITCTT-Book", "concept · Bodoni 72"),
    (f"{VF}@wght=400,opsz=96", "Moda 400 · opsz 96"),
    (f"{VF}@wght=500,opsz=96", "Moda 500 · opsz 96"),
    (f"{VF}@wght=500,opsz=48", "Moda 500 · opsz 48"),
    (f"{VF}@wght=600,opsz=28", "Moda 600 · opsz 28"),
    (f"{VF}@wght=700,opsz=11", "Moda 700 · opsz 11"),
]
T, GAP, OVER = 36, 62, 54          # bar proportions per 1000 units of font size (the concept's)


def mark(font, ox, oy, width=166):
    d, bb = mz.text(font, 1000, "m")
    xh = -bb[1]
    k = width / (bb[2] - bb[0])
    left = ox + 128 - width / 2
    base = oy + 126 + xh * k / 2
    dm = mz.affine(d, k, left - bb[0] * k, base)
    mid = base - xh * k / 2
    s = k * 1000 / 1000 * (439 / xh)   # keep bars proportional to the x-height, as in the concept
    t, gap, over = T * k * 439 / xh, GAP * k * 439 / xh, OVER * k * 439 / xh
    bars = (mz.rect(left - over, mid - gap / 2 - t, width + 2 * over, t)
            + mz.rect(left - over, mid + gap / 2, width + 2 * over, t))
    return mz.path(dm) + mz.path(bars)


def word(font, ox, oy, width=236):
    d, bb = mz.text(font, 1000, "mezzeuro")
    k = width / (bb[2] - bb[0])
    return mz.path(mz.affine(d, k, ox + 128 - width / 2 - bb[0] * k, oy + 330))


W = 256 * len(SPECS)
body = [f'<rect width="{W}" height="400" fill="#fff"/>']
for i, (font, label) in enumerate(SPECS):
    body.append(mark(font, i * 256, 0))
    body.append(word(font, i * 256, 0))
    body.append(f'<text x="{i * 256 + 128}" y="388" font-family="Helvetica" font-size="15" text-anchor="middle" '
                f'fill="#666">{label}</text>')
out = mz.write(os.path.join(mz.HERE, "..", "exploration", "study-moda.svg"), mz.svg(W, 400, "".join(body)))
print("wrote", os.path.relpath(out, os.path.join(mz.HERE, "..")))
