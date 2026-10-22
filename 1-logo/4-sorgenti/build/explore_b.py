"""Two replacement candidates for concept B, side by side: a classical column built from coins, and an m/€
monogram set as a typographic fraction."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mz  # noqa: E402

INK = "#111111"
BODONI = "BodoniSvtyTwoITCTT-Book"
OUT = os.path.normpath(os.path.join(mz.HERE, "..", "exploration"))


def rrect(x, y, w, h, r):
    return (f"M{mz.f(x + r)} {mz.f(y)}H{mz.f(x + w - r)}A{r} {r} 0 0 1 {mz.f(x + w)} {mz.f(y + r)}"
            f"V{mz.f(y + h - r)}A{r} {r} 0 0 1 {mz.f(x + w - r)} {mz.f(y + h)}H{mz.f(x + r)}"
            f"A{r} {r} 0 0 1 {mz.f(x)} {mz.f(y + h - r)}V{mz.f(y + r)}A{r} {r} 0 0 1 {mz.f(x + r)} {mz.f(y)}Z")


def column(cx=128, top=38):
    """Ionic column: abacus + two volutes, a shaft of five stacked coins, torus + plinth."""
    p = []
    y = top
    p.append(mz.rect(cx - 64, y, 128, 11))                        # abacus
    y += 11
    for vx in (cx - 50, cx + 50):                                  # volutes: ring with an eye
        p.append(mz.circle(vx, y + 13, 15) + mz.circle(vx, y + 13, 5, ccw=True))
    p.append(mz.rect(cx - 50, y, 100, 16))                        # echinus band between volutes
    y += 34
    for i in range(5):                                             # coins
        p.append(rrect(cx - 44, y, 88, 19, 5))
        y += 19 + 6
    p.append(rrect(cx - 54, y, 108, 10, 5))                       # torus
    y += 14
    p.append(mz.rect(cx - 64, y, 128, 11))                        # plinth
    return mz.path("".join(p), INK, evenodd=False)


def fraction(cx=128, cy=128):
    dm, bm = mz.text(BODONI, 1000, "m")
    de, be = mz.text(BODONI, 1000, "€")
    km = 104 / (bm[2] - bm[0])            # m: ink width 104
    ke = 92 / (be[3] - be[1])             # €: ink height 92
    m = mz.affine(dm, km, cx - 22 - (bm[0] + bm[2]) / 2 * km, cy - 40 - (bm[1] + bm[3]) / 2 * km)
    e = mz.affine(de, ke, cx + 40 - (be[0] + be[2]) / 2 * ke, cy + 38 - (be[1] + be[3]) / 2 * ke)
    # fraction slash: parallelogram at 60 degrees, 7 units thick horizontally
    x0, y0, x1, y1, t = cx - 40, cy + 84, cx + 40, cy - 84, 7
    slash = f"M{x0} {y0}L{x1} {y1}H{x1 + t}L{x0 + t} {y0}Z"
    return mz.path(m + e + slash, INK)


body = ['<rect width="560" height="280" fill="#fff"/>',
        f'<g transform="translate(12 12)">{column()}</g>',
        f'<g transform="translate(292 12)">{fraction()}</g>']
mz.write(os.path.join(OUT, "explore-b.svg"), mz.svg(560, 280, "".join(body)))
print("wrote exploration/explore-b.svg")
