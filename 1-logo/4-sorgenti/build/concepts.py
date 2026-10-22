"""Builds the three mezzeuro concepts (symbol + lockup each) as black-on-white SVG.

  python3 build/concepts.py v1      -> concepts/v1/{a,b,c}-{symbol,lockup}.svg

Fonts are macOS system fonts outlined via CoreText (exploration only: see the licence note in the README).
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mz  # noqa: E402

VER = sys.argv[1] if len(sys.argv) > 1 else "v1"
OUT = os.path.normpath(os.path.join(mz.HERE, "..", "concepts", VER))
INK = "#111111"
BODONI = "BodoniSvtyTwoITCTT-Book"
BODONI_B = "BodoniSvtyTwoITCTT-Bold"

# Bodoni 72 Book's own euro sign, in font units: bar thickness 36, gap between bars 62, overhang ~50.
EURO_T, EURO_GAP, EURO_OVER = 36, 62, 54


def euro_bars(x0, x1, mid, k):
    """Two horizontal bars centred on `mid`, scaled from Bodoni's euro by factor k."""
    t, gap = EURO_T * k, EURO_GAP * k
    return mz.rect(x0, mid - gap / 2 - t, x1 - x0, t) + mz.rect(x0, mid + gap / 2, x1 - x0, t)


def save(name, w, h, body, title):
    p = mz.write(os.path.join(OUT, name), mz.svg(w, h, body, title))
    print("wrote", os.path.relpath(p, os.path.join(mz.HERE, "..")))


# ---- A · La valuta: the m becomes a currency sign ----------------------------------------------

def a_mark(cx, cy, width):
    """Bodoni m, ink width `width`, centred on (cx, cy); bars cross the whole letter (₩-style)."""
    d, bb = mz.text(BODONI, 1000, "m")
    k = width / (bb[2] - bb[0])
    top, bot = bb[1] * k, bb[3] * k
    left = cx - width / 2
    base = cy - (top + bot) / 2
    dm = mz.affine(d, k, left - bb[0] * k, base)
    over = EURO_OVER * k
    bars = euro_bars(left - over, left + width + over, base + top / 2, k)
    return mz.path(dm, INK) + mz.path(bars, INK), width + 2 * over


def build_a():
    body, total = a_mark(128, 126, 166)
    save("a-symbol.svg", 256, 256, f'<g id="symbol">{body}</g>', "mezzeuro · A · La valuta")

    # Lockup: the wordmark itself, its first m carrying the bars.
    xh = 96                                  # x-height of the wordmark on the 256-high canvas
    k = xh / mz.shape(BODONI, 1000, "x")["xHeight"]
    info = mz.shape(BODONI, 1000, "mezzeuro")
    g0, gl = info["glyphs"][0], info["glyphs"][-1]
    over = EURO_OVER * k
    pad = 28
    x0 = pad + over - g0["bbox"][0] * k      # so the bars start at `pad`
    base = 128 + xh / 2
    d, bb = mz.text(BODONI, 1000, "mezzeuro")
    dw = mz.affine(d, k, x0, base)
    m_left, m_right = x0 + g0["bbox"][0] * k, x0 + (g0["x"] + g0["bbox"][2]) * k
    bars = euro_bars(m_left - over, m_right + 2, base - xh / 2, k)
    w = x0 + (gl["x"] + gl["bbox"][2]) * k + pad
    save("a-lockup.svg", w, 256, f'<g id="wordmark">{mz.path(dw, INK)}{mz.path(bars, INK)}</g>',
         "mezzeuro · A · wordmark")


# ---- B · La colonna: coins stacked into an Ionic column ------------------------------------------

def rrect(x, y, w, h, r):
    return (f"M{mz.f(x + r)} {mz.f(y)}H{mz.f(x + w - r)}A{r} {r} 0 0 1 {mz.f(x + w)} {mz.f(y + r)}"
            f"V{mz.f(y + h - r)}A{r} {r} 0 0 1 {mz.f(x + w - r)} {mz.f(y + h)}H{mz.f(x + r)}"
            f"A{r} {r} 0 0 1 {mz.f(x)} {mz.f(y + h - r)}V{mz.f(y + r)}A{r} {r} 0 0 1 {mz.f(x + r)} {mz.f(y)}Z")


COIN_H, COIN_GAP, COINS = 17, 7, 5          # gaps >= 7 units stay open at a 32 px avatar


def b_mark(cx=128, top=34):
    """Abacus 120 wide, two volutes (ring + eye) on an echinus band, five coins 82 x 17 (gap 7),
    torus and plinth. Vertical extent 34..216 on the 256 grid (centre 125, optically high)."""
    p = [mz.rect(cx - 60, top, 120, 9)]                                   # abacus
    vy = top + 21
    for vx in (cx - 48, cx + 48):                                          # volutes: spiral read as ring + eye
        p.append(mz.circle(vx, vy, 15) + mz.circle(vx, vy, 9, ccw=True) + mz.circle(vx, vy, 4.5))
    p.append(mz.rect(cx - 48, top + 9, 96, 15))                           # echinus band
    y = top + 41
    for _ in range(COINS):                                                 # the shaft: stacked coins
        p.append(rrect(cx - 41, y, 82, COIN_H, 3))
        y += COIN_H + COIN_GAP
    p.append(rrect(cx - 50, y, 100, 9, 4.5))                              # torus
    p.append(mz.rect(cx - 60, y + 13, 120, 10))                           # plinth
    return mz.path("".join(p), INK)


def build_b():
    save("b-symbol.svg", 256, 256, f'<g id="symbol">{b_mark()}</g>', "mezzeuro · B · La colonna")
    xh = 72
    k = xh / mz.shape(BODONI, 1000, "x")["xHeight"]
    cx = 88                                    # column spans cx ± 60
    x_word = cx + 60 + 44
    d, bb = mz.text(BODONI, 1000, "mezzeuro")
    dw = mz.affine(d, k, x_word - bb[0] * k, 126 + xh / 2)
    w = x_word + (bb[2] - bb[0]) * k + 28
    body = f'<g id="symbol">{b_mark(cx)}</g><g id="wordmark">{mz.path(dw, INK)}</g>'
    save("b-lockup.svg", w, 256, body, "mezzeuro · B · lockup")


# ---- C · Il conio: a classical half-euro coin ---------------------------------------------------

def c_mark(cx, cy):
    parts = [mz.path(mz.ring(cx, cy, 122, 114), INK)]
    n, rb, br = 60, 105, 2.8
    beads = "".join(mz.circle(cx + rb * math.cos(2 * math.pi * i / n), cy + rb * math.sin(2 * math.pi * i / n), br)
                    for i in range(n))
    parts.append(mz.path(beads, INK))

    cap = 19                                   # legend cap height (Bold: hairlines survive at avatar size)
    size = cap * 1000 / mz.shape(BODONI_B, 1000, "H")["capHeight"]
    r_in = 74                                  # legend band: r_in .. r_in + cap
    track = 0.22 * size
    top = mz.arc_text(BODONI_B, size, "MEZZEURO", cx, cy, r_in, "top", track)
    bottom = mz.arc_text(BODONI_B, size, "FINANZA", cx, cy, r_in + cap, "bottom", track)
    parts.append(mz.path(top + bottom, INK))

    rd, s = r_in + cap / 2, 3.6                # separator diamonds at 9 and 3 o'clock
    seps = "".join(f"M{mz.f(x)} {mz.f(cy - s)}L{mz.f(x + s)} {mz.f(cy)}L{mz.f(x)} {mz.f(cy + s)}"
                   f"L{mz.f(x - s)} {mz.f(cy)}Z" for x in (cx - rd, cx + rd))
    parts.append(mz.path(seps, INK))

    d, bb = mz.text(BODONI, 1000, "½")
    k = 84 / (bb[2] - bb[0])
    gx = cx - (bb[0] + bb[2]) / 2 * k
    gy = cy + 2 - (bb[1] + bb[3]) / 2 * k
    parts.append(mz.path(mz.affine(d, k, gx, gy), INK))
    return "".join(parts)


def build_c():
    save("c-symbol.svg", 256, 256, f'<g id="symbol">{c_mark(128, 128)}</g>', "mezzeuro · C · Il conio")
    cap = 52
    size = cap * 1000 / mz.shape(BODONI, 1000, "H")["capHeight"]
    x_word = 256 + 30
    d, bb = mz.text(BODONI, size, "MEZZEURO", tracking=0.14 * size)
    dw = mz.affine(d, 1, x_word - bb[0], 128 + cap / 2)
    w = x_word + (bb[2] - bb[0]) + 28
    body = f'<g id="symbol">{c_mark(128, 128)}</g><g id="wordmark">{mz.path(dw, INK)}</g>'
    save("c-lockup.svg", w, 256, body, "mezzeuro · C · lockup")


if __name__ == "__main__":
    build_a()
    build_b()
    build_c()
