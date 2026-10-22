"""One-page logo usage guide (A4) for mezzeuro: 1-logo/guida/mezzeuro-guida.{html,pdf,png}.

  python3 4-sorgenti/build/guide.py      (from the MEZZEURO folder)
"""
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kit  # noqa: E402
import mz  # noqa: E402

OUT = os.path.join(kit.KIT, "guida")
FONT_URL = os.path.relpath(kit.VF, OUT)
LOGO = os.path.join(kit.KIT, "logo")
C = kit.COL


def inline(name, cls="", style="", recolor=None):
    src = open(os.path.join(LOGO, name), encoding="utf-8").read()
    src = re.sub(r"<title[^>]*>.*?</title>", "", src)
    src = re.sub(r'\s(width|height)="[^"]*"', "", src, count=2)
    src = src.replace("<svg ", f'<svg class="{cls}" style="{style}" ', 1)
    for a, b in (recolor or {}).items():
        src = src.replace(a, b)
    return src.strip()


def lum(hex_):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hex_[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def clear_space_svg():
    """Horizontal logo inside its clear-space zone: x = half the height of the m."""
    src = open(os.path.join(LOGO, "mezzeuro-orizzontale.svg"), encoding="utf-8").read()
    W, H = (float(v) for v in re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', src).groups())
    body = re.sub(r"^.*?<svg[^>]*>", "", src, flags=re.S).rsplit("</svg>", 1)[0]
    body = re.sub(r"<title[^>]*>.*?</title>", "", body)
    pad, x = 20, 48                                   # file padding; clear space = 96 / 2
    ink = (pad, pad, W - pad, H - pad)
    m = 10
    vb = (ink[0] - x - m, ink[1] - x - m, ink[2] - ink[0] + 2 * x + 2 * m, ink[3] - ink[1] + 2 * x + 2 * m)
    zone = (ink[0] - x, ink[1] - x, ink[2] - ink[0] + 2 * x, ink[3] - ink[1] + 2 * x)
    tint = "#E9DCD5"
    marks = "".join(f'<rect x="{mz.f(px)}" y="{mz.f(py)}" width="{x}" height="{x}" fill="{tint}"/>'
                    for px, py in ((zone[0], ink[1]), (ink[2], ink[1]), (ink[0], zone[1]), (ink[0], ink[3])))
    labels = "".join(f'<text x="{mz.f(px + x / 2)}" y="{mz.f(py + x / 2 + 9)}" font-size="26" text-anchor="middle" '
                     f'font-family="Helvetica" fill="{C["bordeaux"]}">x</text>'
                     for px, py in ((zone[0], ink[1]), (ink[2], ink[1]), (ink[0], zone[1]), (ink[0], ink[3])))
    return (f'<svg class="cs" viewBox="{" ".join(mz.f(v) for v in vb)}" xmlns="http://www.w3.org/2000/svg">'
            f'<rect x="{mz.f(zone[0])}" y="{mz.f(zone[1])}" width="{mz.f(zone[2])}" height="{mz.f(zone[3])}" '
            f'fill="none" stroke="{C["bordeaux"]}" stroke-width="2" stroke-dasharray="8 6"/>{marks}{labels}{body}</svg>')


def avatar(size):
    src = open(os.path.join(kit.KIT, "social", "sorgenti", "profilo-avorio-cerchio.svg"), encoding="utf-8").read()
    src = re.sub(r"<title[^>]*>.*?</title>", "", src)
    src = re.sub(r'\s(width|height)="[^"]*"', "", src, count=2)
    return src.replace("<svg ", f'<svg style="width:{size};height:{size}" ', 1).strip()


def watermark():
    src = open(os.path.join(kit.KIT, "social", "sorgenti", "filigrana-avorio.svg"), encoding="utf-8").read()
    src = re.sub(r"<title[^>]*>.*?</title>", "", src)
    return re.sub(r'\s(width|height)="[^"]*"', "", src, count=2).strip()


def no_bars_svg():
    letters, _, box = kit.word(kit.WORD, 96, 20, 116, barred=False)
    return (f'<svg viewBox="0 0 {mz.f(box[2] + 20)} 140" xmlns="http://www.w3.org/2000/svg">'
            f'{mz.path(letters, C["bordeaux"])}</svg>')


def main():
    swatches = [
        ("Bordeaux", C["bordeaux"], "110 30 44", "C30 M95 Y70 K40", "≈ 188 C", "colore principale"),
        ("Oro nordico", C["oro"], "198 161 91", "C20 M35 Y75 K5", "≈ 7562 C · 871 C met.", "accento, mai sotto i 56 px"),
        ("Avorio", C["avorio"], "245 239 228", "C2 M4 Y10 K0", "carta avorio", "fondo chiaro"),
        ("Inchiostro", C["inchiostro"], "31 26 28", "C0 M15 Y10 K90", "≈ Neutral Black C", "testi"),
    ]
    sw = "".join(
        f'<div class="sw"><div class="chip" style="background:{h};{"border:1px solid #ddd;" if n == "Avorio" else ""}"></div>'
        f'<b>{n} <i>· {use}</i></b><span>{h} · RGB {rgb}</span><span>{cmyk} · Pantone {pms}</span></div>'
        for n, h, rgb, cmyk, pms, use in swatches)
    pairs = [("Avorio su bordeaux", C["avorio"], C["bordeaux"]), ("Bordeaux su avorio", C["bordeaux"], C["avorio"]),
             ("Oro su bordeaux", C["oro"], C["bordeaux"]), ("Oro su avorio", C["oro"], C["avorio"])]
    cr = " · ".join(f"{n} {contrast(a, b):.1f}:1" for n, a, b in pairs)

    hz = "mezzeuro-orizzontale.svg"
    donts = [
        ("Non deformarlo", inline(hz, "dn", "width:60%;transform:scaleX(1.4) scaleY(.7)")),
        ("Non cambiare i colori", inline(hz, "dn", "", {C["bordeaux"]: "#1E5AA8"})),
        ("Non togliere le barre", no_bars_svg().replace("<svg ", '<svg class="dn" ', 1)),
        ("Non ruotarlo", inline(hz, "dn", "transform:rotate(-9deg)")),
        ("Niente ombre o effetti", inline(hz, "dn", "filter:drop-shadow(3px 4px 2px rgba(0,0,0,.55))")),
        ("Non su sfondi confusi", inline(hz, "dn", "")),
    ]
    dn = "".join(
        f'<div class="d{" busy" if t.startswith("Non su") else ""}"><div class="dbox">{s}</div><span>✕ {t}</span></div>'
        for t, s in donts)

    sym, sym_neg, sym_oro = "mezzeuro-simbolo.svg", "mezzeuro-simbolo-negativo.svg", "mezzeuro-simbolo-oro.svg"
    bgs = [
        (C["avorio"], inline(sym, "bgl"), "Bordeaux su avorio"),
        ("#FFFFFF", inline(sym, "bgl"), "Bordeaux su bianco"),
        (C["bordeaux"], inline(sym_neg, "bgl"), "Avorio su bordeaux"),
        (C["bordeaux"], inline(sym_oro, "bgl"), "Barre oro, solo in grande"),
        ("linear-gradient(135deg,#3a2a26,#1d1716)", inline(sym_neg, "bgl"), "Su foto scura e calma"),
    ]
    bg = "".join(f'<div class="bg"><div class="tile" style="background:{b}">{s}</div><span>{t}</span></div>'
                 for b, s, t in bgs)

    css = f"""
@font-face{{font-family:"Bodoni Moda";src:url("{FONT_URL}");font-weight:400 900}}
@page{{size:A4;margin:0}}
*{{box-sizing:border-box}}
html,body{{margin:0;background:#fff}}
body{{width:210mm;height:297mm;padding:10mm 13mm 10mm;font:8.1pt/1.34 -apple-system,"Helvetica Neue",Helvetica,Arial,sans-serif;color:{C["inchiostro"]};overflow:hidden}}
h1{{font:500 19pt/1 "Bodoni Moda",serif;margin:0;color:{C["bordeaux"]};font-variation-settings:"opsz" 24}}
h2{{font:600 9pt/1 -apple-system,"Helvetica Neue",sans-serif;letter-spacing:.08em;text-transform:uppercase;margin:0 0 2.2mm;color:{C["bordeaux"]}}}
.top{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:.3mm solid {C["bordeaux"]};padding-bottom:2mm;margin-bottom:3mm}}
.top span{{color:#777}}
section{{margin-bottom:3.2mm}}
.hero{{display:grid;grid-template-columns:1.25fr 1fr;gap:5mm;align-items:stretch}}
.heroL{{background:{C["avorio"]};border-radius:2mm;display:flex;align-items:center;justify-content:center;padding:5mm 7mm}}
.heroL svg{{width:100%}}
.vers{{display:grid;grid-template-columns:1.6fr 1fr .8fr;gap:2.5mm;margin-top:2.5mm}}
.v{{border:.25mm solid #e6e0d6;border-radius:1.5mm;height:16mm;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1.2mm;padding:2mm}}
.v svg{{max-width:92%;max-height:9mm}} .v span{{font-size:7pt;color:#777}}
.two{{display:grid;grid-template-columns:1.1fr 1fr;gap:6mm}}
.cs{{width:100%;background:#fbf9f5;border-radius:1.5mm}}
table{{border-collapse:collapse;width:100%}} td,th{{text-align:left;padding:.7mm 1.5mm;border-bottom:.2mm solid #eee}} th{{font-weight:600;color:#555}}
.sws{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm}}
.sw{{display:flex;flex-direction:column;gap:.35mm}} .sw .chip{{height:7mm;border-radius:1.2mm;margin-bottom:.8mm}}
.sw span{{color:#555;font-size:7.6pt}} .sw i{{color:#888;font-size:7.2pt}}
.note{{color:#777;font-size:7.4pt;margin-top:1.6mm}}
.bgs{{display:grid;grid-template-columns:repeat(5,1fr);gap:2.4mm}}
.bg span,.d span{{display:block;font-size:7.2pt;color:#666;margin-top:1mm}}
.tile{{height:12mm;border-radius:1.5mm;display:flex;align-items:center;justify-content:center;border:.2mm solid #eee;overflow:hidden}}
.tile svg{{width:17mm;height:17mm;flex:none}}
.av{{display:flex;align-items:flex-end;gap:4mm;flex:none}}
.row{{display:flex;gap:4mm;align-items:center}} .row .note{{margin:0}}
.two56{{display:grid;grid-template-columns:.85fr 1.15fr;gap:6mm}} .av .c{{display:flex;flex-direction:column;align-items:center;gap:1mm;font-size:7pt;color:#777}}
.av .c svg{{border-radius:50%;display:block}}
.frame{{position:relative;width:34mm;height:19mm;border-radius:1.5mm;background:linear-gradient(160deg,#5b6b78,#26303a 60%,#151a20)}}
.frame svg{{position:absolute;right:2mm;bottom:1.5mm;width:7mm;height:7mm;opacity:.9}}
.ds{{display:grid;grid-template-columns:repeat(6,1fr);gap:2.4mm}}
.dbox{{height:10mm;border-radius:1.5mm;background:#faf8f4;display:flex;align-items:center;justify-content:center;overflow:hidden;padding:0 2mm}}
.dn{{width:88%}} .d span{{color:#b0262c}}
.busy .dbox{{background:repeating-linear-gradient(45deg,#d9c7a8 0 3px,#8b6b4a 3px 6px,#efe6d6 6px 9px)}}
.type{{display:grid;grid-template-columns:1fr 1fr;gap:4mm}}
.type .s{{font:500 15pt/1.1 "Bodoni Moda",serif;color:{C["bordeaux"]};font-variation-settings:"opsz" 24}}
.type .t{{font:400 11pt/1.2 -apple-system,"Helvetica Neue",sans-serif}}
footer{{position:absolute;bottom:9mm;left:13mm;right:13mm;color:#888;font-size:7pt;border-top:.2mm solid #eee;padding-top:2mm}}
"""
    html = f"""<!doctype html><html lang="it"><meta charset="utf-8"><title>mezzeuro · guida d'uso del logo</title>
<style>{css}</style><body>
<div class="top"><h1>mezzeuro · guida d'uso del logo</h1><span>v1.0 · ottobre 2026</span></div>

<section class="hero"><div class="heroL">{inline(hz)}</div><div>
<h2>1 · Il logo</h2>
<p style="margin:0 0 2mm">La <b>m</b> di mezzeuro è attraversata dalle due barre dell'euro, come in un simbolo di valuta (€, ¥, ₩): il canale ha la sua moneta.
Lettere in Bodoni Moda, erede del carattere di Giambattista Bodoni, tipografo a Parma.</p>
<p style="margin:0;color:#666">Usa sempre i file originali, non riscrivere il nome con un font. Tre versioni:</p>
<div class="vers"><div class="v">{inline(hz)}<span>orizzontale (principale)</span></div>
<div class="v">{inline("mezzeuro-verticale.svg")}<span>verticale</span></div>
<div class="v">{inline("mezzeuro-simbolo.svg", "", "max-height:15mm")}<span>simbolo</span></div></div>
</div></section>

<section class="two"><div><h2>2 · Spazio di rispetto</h2>{clear_space_svg()}
<div class="note">Attorno al logo lascia libero almeno <b>x</b> = metà dell'altezza della m, su ogni lato. Lo spazio cresce con il logo.</div></div>
<div><h2>3 · Dimensioni minime</h2><table>
<tr><th>Versione</th><th>Schermo</th><th>Stampa</th></tr>
<tr><td>Orizzontale</td><td>120 px di larghezza</td><td>30 mm</td></tr>
<tr><td>Verticale</td><td>80 px</td><td>20 mm</td></tr>
<tr><td>Simbolo</td><td>40 px</td><td>10 mm</td></tr>
<tr><td>Simbolo «piccolo»</td><td>da 16 a 40 px</td><td>da 5 a 10 mm</td></tr></table>
<div class="note">Sotto i 40 px usa i file <b>-piccolo</b>: barre più spesse e distanziate, per non impastarsi.
La foto profilo è già pronta in <b>social/</b>.</div></div></section>

<section><h2>4 · Colori</h2><div class="sws">{sw}</div>
<div class="note">Contrasto: {cr}. L'oro su avorio non basta per il logo: usalo solo su bordeaux. CMYK e Pantone sono indicativi: chiedi una prova colore alla tipografia.</div></section>

<section class="two56"><div><h2>5 · Caratteri</h2><div class="type">
<div><div class="s">Bodoni Moda</div><span class="note">titoli, copertine, citazioni</span></div>
<div><div class="t">Inter</div><span class="note">testi, sottotitoli, didascalie</span></div></div>
<div class="note">Entrambi gratuiti su Google Fonts, licenza SIL Open Font License (uso commerciale libero). Massimo due caratteri.</div></div>
<div><h2>6 · Sfondi consentiti</h2><div class="bgs">{bg}</div></div></section>

<section><h2>7 · Da evitare</h2><div class="ds">{dn}</div></section>

<section class="two"><div><h2>8 · Foto profilo</h2><div class="row"><div class="av">
<div class="c">{avatar("15mm")}160 px</div><div class="c">{avatar("9mm")}56 px</div><div class="c">{avatar("5.5mm")}32 px</div></div>
<div class="note">Carica il quadrato pieno (<b>instagram-profilo-avorio-1080.png</b>, <b>youtube-profilo-avorio-800.png</b>): la piattaforma lo ritaglia a cerchio.
È la versione tutta avorio: le barre oro sotto i 56 px spariscono.</div></div></div>
<div><h2>9 · Filigrana dei video</h2><div class="row"><div class="av"><div class="frame">{watermark()}</div></div>
<div class="note">YouTube Studio › Personalizzazione › Branding › Filigrana del video: carica <b>youtube-filigrana-avorio-150.png</b>.
È il taglio «piccolo», leggibile in un angolo del video.</div></div></div></section>

<footer>File: <b>kit/logo</b> (SVG master e PNG) · <b>kit/social</b> (foto profilo Instagram 1080 px, YouTube 800 px, filigrana 150 px) ·
<b>kit/web</b> (favicon e icone) · <b>kit/presentazione</b> · Font: Bodoni Moda © The Bodoni Moda Project Authors, SIL OFL 1.1</footer>
</body></html>"""
    page = mz.write(os.path.join(OUT, "mezzeuro-guida.html"), html)

    sys.path.insert(0, kit.SKILL)
    import render_png  # noqa: E402
    chrome = render_png.find_chrome()
    pdf = os.path.join(OUT, "mezzeuro-guida.pdf")
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--no-first-run",
                        f"--user-data-dir={tmp}", f"--print-to-pdf={pdf}", "file://" + page],
                       check=True, capture_output=True, timeout=90)
    png = os.path.join(OUT, "mezzeuro-guida.png")
    subprocess.run(["sips", "-s", "format", "png", "--resampleWidth", "1654", pdf, "--out", png],
                   check=True, capture_output=True)
    print("wrote", os.path.relpath(page, kit.ROOT), "+ pdf + png;", cr)


if __name__ == "__main__":
    main()
