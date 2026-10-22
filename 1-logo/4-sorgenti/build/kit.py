"""Builds the mezzeuro logo kit (direction A · La valuta) from Bodoni Moda (SIL OFL 1.1).

  python3 4-sorgenti/build/kit.py masters     -> 1-logo/logo/*.svg + 4-sorgenti/exploration/kit-masters.png
  python3 4-sorgenti/build/kit.py all         -> masters + social + web + PNG + PDF (run from the MEZZEURO folder)

The m is Bodoni Moda (variable: weight, optical size); the two bars are the concept's euro bars, sized from the
m's x-height (thickness 36, gap 62, overhang 54 per 439 units), so every instance keeps the same proportions.
"""
import json
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mz  # noqa: E402

ROOT = os.path.normpath(os.path.join(mz.HERE, ".."))
KIT = os.path.normpath(os.path.join(ROOT, "..", "1-logo"))      # the delivered kit sits next to 4-sorgenti
VF = os.path.join(ROOT, "fonts", "BodoniModa-VF.ttf")
SKILL = os.path.expanduser("~/.claude/skills/logo-design/scripts")

COL = {"bordeaux": "#6E1E2C", "oro": "#C6A15B", "avorio": "#F5EFE4", "inchiostro": "#1F1A1C"}

# Bodoni Moda instances (weight, optical size)
SYMBOL, SYMBOL_REV, SMALL = (600, 18), (580, 18), (680, 10)
WORD, WORD_REV = (560, 24), (540, 24)
T, GAP, OVER, XREF = 36, 62, 54, 439        # bar proportions, normalised to a 439-unit x-height
SMALL_BARS = (1.5, 1.45, 0.8)                # thickness, gap, overhang multipliers for the small-size cut
REV_BARS = (0.95, 1.0, 1.0)                  # reversed: thin the bars like the letter (irradiation)


def font(inst):
    return f"{VF}@wght={inst[0]},opsz={inst[1]}"


def bars(x0, x1, mid, t, gap, ccw):
    return mz.rect(x0, mid - gap / 2 - t, x1 - x0, t, ccw) + mz.rect(x0, mid + gap / 2, x1 - x0, t, ccw)


def barred_m(inst, width, cx, cy, mult=(1, 1, 1)):
    """The m (ink `width` wide, ink box centred on cx, cy) and its bars. Returns letter_d, bars_d, box."""
    d, bb = mz.text(font(inst), 1000, "m")
    xh = -bb[1]
    k = width / (bb[2] - bb[0])
    left = cx - width / 2
    letter = mz.affine(d, k, left - bb[0] * k, cy + xh * k / 2)
    q = k * XREF / xh
    t, gap, over = T * q * mult[0], GAP * q * mult[1], OVER * q * mult[2]
    b = bars(left - over, left + width + over, cy, t, gap, mz.outer_is_ccw(letter))
    return letter, b, (left - over, cy - xh * k / 2, left + width + over, cy + xh * k / 2)


def word(inst, xh_target, x, baseline, barred=True, mult=(1, 1, 1)):
    """'mezzeuro' with its ink starting at x; the first m carries the bars. Returns letter_d, bars_d, box."""
    info = mz.shape(font(inst), 1000, "mezzeuro")
    d, bb = mz.text(font(inst), 1000, "mezzeuro")
    xh = -bb[1]
    k = xh_target / xh
    q = k * XREF / xh
    t, gap, over = T * q * mult[0], GAP * q * mult[1], OVER * q * mult[2]
    x0 = x + (over if barred else 0)
    letters = mz.affine(d, k, x0 - bb[0] * k, baseline)
    g0 = info["glyphs"][0]
    m_left = x0 + (g0["x"] + g0["bbox"][0] - bb[0]) * k
    m_right = x0 + (g0["x"] + g0["bbox"][2] - bb[0]) * k
    b = bars(m_left - over, m_right, baseline - xh_target / 2, t, gap, mz.outer_is_ccw(letters)) if barred else ""
    return letters, b, (x, baseline - xh_target, x0 + (bb[2] - bb[0]) * k, baseline + bb[3] * k)


def art(letter, bar, ink, bar_ink=None, ident="logo"):
    """One merged path when single-colour; letter and bars as separate groups for the two-colour version."""
    if bar_ink is None or bar_ink == ink:
        return f'<g id="{ident}">{mz.path(letter + bar, ink)}</g>'
    return f'<g id="{ident}"><g id="bars">{mz.path(bar, bar_ink)}</g><g id="m">{mz.path(letter, ink)}</g></g>'


def save(rel, w, h, body, title):
    p = mz.write(os.path.join(KIT, rel), mz.svg(w, h, body, title))
    return p


# ---- masters ---------------------------------------------------------------------------------------

def symbol_svg(inst, ink, bar_ink=None, mult=(1, 1, 1), width=172):
    letter, b, _ = barred_m(inst, width, 128, 126, mult)
    return mz.svg(256, 256, art(letter, b, ink, bar_ink, "simbolo"), "mezzeuro")


def horizontal(inst, ink, bar_ink=None, mult=(1, 1, 1)):
    xh, pad = 96, 20
    letter, b, box = word(inst, xh, pad, pad + xh, True, mult)
    w, h = box[2] + pad, xh + 2 * pad + max(0, box[3] - (pad + xh))
    return w, h, art(letter, b, ink, bar_ink, "logo-orizzontale")


def stacked(sym_inst, word_inst, ink, bar_ink=None, mult=(1, 1, 1)):
    """Symbol above the plain wordmark; the wordmark's x-height is 20 % of the symbol's ink width."""
    sym_w, gap, wxh, pad = 170, 26, 34, 20
    probe_l, _, pbox = word(word_inst, wxh, 0, 0, barred=False)
    word_w = pbox[2] - pbox[0]
    letter, b, sbox = barred_m(sym_inst, sym_w, 0, 0, mult)
    sym_h = sbox[3] - sbox[1]
    W = max(sbox[2] - sbox[0], word_w) + 2 * pad
    cx = W / 2
    letter, b, sbox = barred_m(sym_inst, sym_w, cx, pad + sym_h / 2, mult)
    wl, _, wbox = word(word_inst, wxh, cx - word_w / 2, pad + sym_h + gap + wxh, barred=False)
    H = pad + sym_h + gap + wxh + pad
    body = art(letter, b, ink, bar_ink, "simbolo") + f'<g id="scritta">{mz.path(wl, ink)}</g>'
    return W, H, body


def build_masters():
    B, A, O = COL["bordeaux"], COL["avorio"], COL["oro"]
    out = []
    out.append(mz.write(os.path.join(KIT, "logo", "mezzeuro-simbolo.svg"), symbol_svg(SYMBOL, B)))
    out.append(mz.write(os.path.join(KIT, "logo", "mezzeuro-simbolo-negativo.svg"),
                        symbol_svg(SYMBOL_REV, A, mult=REV_BARS)))
    out.append(mz.write(os.path.join(KIT, "logo", "mezzeuro-simbolo-oro.svg"),
                        symbol_svg(SYMBOL_REV, A, O, mult=REV_BARS)))
    out.append(mz.write(os.path.join(KIT, "logo", "mezzeuro-simbolo-piccolo.svg"),
                        symbol_svg(SMALL, B, mult=SMALL_BARS, width=180)))
    out.append(mz.write(os.path.join(KIT, "logo", "mezzeuro-simbolo-piccolo-negativo.svg"),
                        symbol_svg(SMALL, A, mult=SMALL_BARS, width=180)))
    for suffix, inst, ink, bar_ink, mult in (("", WORD, B, None, (1, 1, 1)),
                                             ("-negativo", WORD_REV, A, None, REV_BARS),
                                             ("-oro", WORD_REV, A, O, REV_BARS)):
        w, h, body = horizontal(inst, ink, bar_ink, mult)
        out.append(save(f"logo/mezzeuro-orizzontale{suffix}.svg", w, h, body, "mezzeuro"))
        sym = SYMBOL if suffix == "" else SYMBOL_REV
        w, h, body = stacked(sym, inst, ink, bar_ink, mult)
        out.append(save(f"logo/mezzeuro-verticale{suffix}.svg", w, h, body, "mezzeuro"))
    for p in out:
        print("wrote", os.path.relpath(p, ROOT))
    return out


def preview_masters():
    """All masters on their intended backgrounds, one sheet, for looking."""
    L = os.path.join(KIT, "logo")
    light = ["mezzeuro-simbolo", "mezzeuro-simbolo-piccolo", "mezzeuro-orizzontale", "mezzeuro-verticale"]
    dark = ["mezzeuro-simbolo-negativo", "mezzeuro-simbolo-oro", "mezzeuro-simbolo-piccolo-negativo",
            "mezzeuro-orizzontale-negativo", "mezzeuro-orizzontale-oro", "mezzeuro-verticale-oro"]
    cells, rel = [], os.path.relpath(os.path.join(KIT, "logo"), os.path.join(ROOT, "exploration"))
    for names, bg in ((light, COL["avorio"]), (dark, COL["bordeaux"])):
        for n in names:
            cells.append(f'<div class="c" style="background:{bg}"><img src="{rel}/{n}.svg"><span>{n}</span></div>')
    html = ("<!doctype html><meta charset='utf-8'><style>body{margin:16px;font:12px Helvetica;background:#fff}"
            ".g{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}"
            ".c{height:230px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;"
            "border-radius:6px}.c img{max-width:86%;max-height:160px}.c span{color:#999;font-size:11px}</style>"
            f"<div class='g'>{''.join(cells)}</div>")
    page = os.path.join(ROOT, "exploration", "kit-masters.html")
    with open(page, "w", encoding="utf-8") as fh:
        fh.write(html)
    subprocess.run([sys.executable, "-I", os.path.join(SKILL, "render_png.py"), page, "-o",
                    os.path.join(ROOT, "exploration", "kit-masters.png"), "--width", "1200", "--height", "760"],
                   check=True)


# ---- social: profile pictures and video watermark -------------------------------------------------

AVATARS = {   # name: (background, letter, bars, instance, bar multipliers, letter on top of bars?)
    "oro": (COL["bordeaux"], COL["avorio"], COL["oro"], SYMBOL_REV, REV_BARS),
    "avorio": (COL["bordeaux"], COL["avorio"], None, SYMBOL_REV, REV_BARS),
    "chiaro": (COL["avorio"], COL["bordeaux"], None, SYMBOL, (1, 1, 1)),
}


def avatar_svg(bg, ink, bar_ink, inst, mult, width=150):
    """Square, full-bleed background (the platforms crop the circle); mark sized for the inscribed circle."""
    letter, b, _ = barred_m(inst, width, 128, 127, mult)
    return mz.svg(256, 256, f'<rect width="256" height="256" fill="{bg}"/>' + art(letter, b, ink, bar_ink), "mezzeuro")


def build_social():
    out_dir = os.path.join(KIT, "social")
    render = os.path.join(SKILL, "render_png.py")
    for name, (bg, ink, bar_ink, inst, mult) in AVATARS.items():
        src = mz.write(os.path.join(out_dir, "sorgenti", f"profilo-{name}.svg"), avatar_svg(bg, ink, bar_ink, inst, mult))
        for platform, px in (("instagram", 1080), ("youtube", 800)):
            subprocess.run([sys.executable, "-I", render, src, "-o",
                            os.path.join(out_dir, f"{platform}-profilo-{name}-{px}.png"), "--size", str(px)],
                           check=True, capture_output=True)
    # Round version for the presentation board's profile mockup (the platforms want the square upload above)
    letter, b, _ = barred_m(SYMBOL_REV, 150, 128, 127, REV_BARS)
    mz.write(os.path.join(out_dir, "sorgenti", "profilo-avorio-cerchio.svg"),
             mz.svg(256, 256, f'<circle cx="128" cy="128" r="128" fill="{COL["bordeaux"]}"/>'
                    + art(letter, b, COL["avorio"]), "mezzeuro"))
    # YouTube watermark (150 x 150, transparent): the small-size cut, since it shows at ~40-60 px over video
    for name, ink in (("avorio", COL["avorio"]), ("bianco", "#FFFFFF")):
        letter, b, _ = barred_m(SMALL, 196, 128, 128, SMALL_BARS)
        src = mz.write(os.path.join(out_dir, "sorgenti", f"filigrana-{name}.svg"), mz.svg(256, 256, art(letter, b, ink)))
        subprocess.run([sys.executable, "-I", render, src, "-o", os.path.join(out_dir, f"youtube-filigrana-{name}-150.png"),
                        "--size", "150"], check=True, capture_output=True)
    print("wrote", os.path.relpath(out_dir, ROOT))


# ---- web: favicon on a tile (a bare bordeaux m disappears on dark browser tabs) ---------------------

def build_web():
    """export_variants --web-icons writes the app/touch/maskable icons, manifest and head snippet; then the
    favicon set is replaced with the small-size cut in avorio on a bordeaux rounded tile."""
    web = os.path.join(KIT, "web")
    render = os.path.join(SKILL, "render_png.py")
    subprocess.run([sys.executable, "-I", os.path.join(SKILL, "export_variants.py"),
                    os.path.join(KIT, "logo", "mezzeuro-simbolo.svg"), "--out-dir", web, "--name", "mezzeuro",
                    "--title", "mezzeuro", "--icon-bg", COL["bordeaux"], "--icon-fg", COL["avorio"], "--icon-scale", "0.68",
                    "--favicon-source", os.path.join(KIT, "logo", "mezzeuro-simbolo-piccolo.svg"),
                    "--only", "app-icon", "--web-icons"], check=True, capture_output=True)
    letter, b, _ = barred_m(SMALL, 176, 128, 128, SMALL_BARS)
    tile = (f'<rect width="256" height="256" rx="56" fill="{COL["bordeaux"]}"/>'
            + art(letter, b, COL["avorio"], ident="simbolo"))
    src = mz.write(os.path.join(web, "favicon.svg"), mz.svg(256, 256, tile, "mezzeuro"))
    for px in (16, 32, 48):
        subprocess.run([sys.executable, "-I", render, src, "-o", os.path.join(web, f"favicon-{px}.png"), "--size", str(px)],
                       check=True, capture_output=True)
    subprocess.run([sys.executable, "-I", render, src, "--ico", os.path.join(web, "favicon.ico"),
                    "--ico-sizes", "16", "32", "48"], check=True, capture_output=True)
    print("wrote", os.path.relpath(web, ROOT), "favicon set (tile)")


# ---- one-colour SVGs and PNG exports ----------------------------------------------------------------

PNG_LONG_SIDE = {"simbolo": (512, 1024), "orizzontale": (1600,), "verticale": (1200,)}


def build_png():
    logo = os.path.join(KIT, "logo")
    export, render = os.path.join(SKILL, "export_variants.py"), os.path.join(SKILL, "render_png.py")
    for name in ("mezzeuro-simbolo", "mezzeuro-simbolo-piccolo", "mezzeuro-orizzontale", "mezzeuro-verticale"):
        subprocess.run([sys.executable, "-I", export, os.path.join(logo, name + ".svg"), "--only", "black", "white",
                        "--title", "mezzeuro"], check=True, capture_output=True)
    out = os.path.join(logo, "png")
    os.makedirs(out, exist_ok=True)
    for fn in sorted(os.listdir(logo)):
        if not fn.endswith(".svg") or "piccolo" in fn:
            continue
        kind = next(k for k in PNG_LONG_SIDE if f"-{k}" in fn)
        vb = [float(v) for v in open(os.path.join(logo, fn), encoding="utf-8").read()
              .split('viewBox="', 1)[1].split('"', 1)[0].split()]
        for long_side in PNG_LONG_SIDE[kind]:
            s = long_side / max(vb[2], vb[3])
            w, h = round(vb[2] * s), round(vb[3] * s)
            dst = os.path.join(out, fn[:-4] + (f"-{long_side}" if len(PNG_LONG_SIDE[kind]) > 1 else "") + ".png")
            subprocess.run([sys.executable, "-I", render, os.path.join(logo, fn), "-o", dst, "--width", str(w),
                            "--height", str(h)], check=True, capture_output=True)
    print("wrote", os.path.relpath(out, ROOT), len(os.listdir(out)), "PNG")


# ---- vector PDFs for printers (RGB; Chrome cannot write CMYK) --------------------------------------

PDF_WIDTH_MM = {"orizzontale": 120, "verticale": 70, "simbolo": 50}


def build_pdf():
    import tempfile
    sys.path.insert(0, SKILL)
    import render_png  # noqa: E402
    chrome = render_png.find_chrome()
    logo, out = os.path.join(KIT, "logo"), os.path.join(KIT, "logo", "pdf")
    os.makedirs(out, exist_ok=True)
    names = [f"mezzeuro-{k}{v}" for k in PDF_WIDTH_MM for v in ("", "-black")]
    with tempfile.TemporaryDirectory() as tmp:
        for name in names:
            src = open(os.path.join(logo, name + ".svg"), encoding="utf-8").read()
            vb = [float(v) for v in src.split('viewBox="', 1)[1].split('"', 1)[0].split()]
            w = PDF_WIDTH_MM[name.split("-")[1]]
            h = round(w * vb[3] / vb[2], 2)
            svg = src.replace("<svg ", f'<svg style="display:block;width:{w}mm;height:{h}mm" ', 1)
            page = os.path.join(tmp, name + ".html")
            with open(page, "w", encoding="utf-8") as fh:
                fh.write(f"<!doctype html><style>@page{{size:{w}mm {h}mm;margin:0}}html,body{{margin:0}}</style>{svg}")
            subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--no-first-run",
                            f"--user-data-dir={os.path.join(tmp, 'profile')}",
                            f"--print-to-pdf={os.path.join(out, name + '.pdf')}", "file://" + page],
                           check=True, capture_output=True, timeout=90)
    print("wrote", os.path.relpath(out, ROOT), len(names), "PDF")


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "masters"
    if what in ("masters", "all"):
        build_masters()
        preview_masters()
    if what in ("social", "all"):
        build_social()
    if what in ("web", "all"):
        build_web()
    if what in ("png", "all"):
        build_png()
    if what in ("pdf", "all"):
        build_pdf()
