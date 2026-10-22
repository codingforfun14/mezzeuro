"""mezzeuro, template Instagram (caroselli 1080x1350, reel 1080x1920), allineati al kit del logo "La valuta".
Uso: python3 genera_template.py  -> scrive HTML in sorgenti/html e PNG in carosello/ e reel/.
Font: Bodoni Moda per i titoli, Inter 400 e 800 per testi e numeri (entrambi SIL OFL).
Il logo arriva dai file ufficiali in logo/ (copiati da 1-logo/logo). Serve Chromium headless.
"""
import math, os, subprocess
from PIL import Image

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, 'sorgenti')
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

# Palette del kit del logo + due neutri (6 colori)
BORDEAUX, AVORIO, ORO, INK, GRAFITE, FILO = '#6E1E2C', '#F5EFE4', '#C6A15B', '#1F1A1C', '#6B6264', '#E3D9CB'
# alias usati dai componenti: fondo chiaro = Avorio, fondo scuro = Bordeaux
CARTA, ORO_B = AVORIO, BORDEAUX
GRANA = open(os.path.join(SRC, 'grana.b64')).read()
_L = lambda n: open(os.path.join(BASE, 'logo', n)).read()
LOGHI = {'chiaro': _L('mezzeuro-orizzontale.svg'), 'scuro': _L('mezzeuro-orizzontale-negativo.svg'),
         'oro': _L('mezzeuro-orizzontale-oro.svg')}


def logo(h, dark=False, oro=False):
    s = LOGHI['oro' if oro else ('scuro' if dark else 'chiaro')]
    return s.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block" ', 1)


# --- Guilloché (incisione da banconota) -------------------------------------
def _ring(cx, cy, R, A, k, copies, steps=1400):
    out = []
    for c in range(copies):
        pts = []
        for i in range(steps + 1):
            t = 2 * math.pi * i / steps
            r = R + A * math.sin(k * t + c * 2 * math.pi / copies)
            pts.append(f'{cx + r * math.cos(t):.1f} {cy + r * math.sin(t):.1f}')
        out.append('M' + ' L'.join(pts) + 'Z')
    return out


def rosone(cx, cy, s=1.0, col=ORO, op=1.0):
    g = [(1.0, .6, _ring(cx, cy, 290 * s, 20 * s, 22, 14)),
         (.9, .5, _ring(cx, cy, 215 * s, 15 * s, 16, 12)),
         (.8, .45, _ring(cx, cy, 145 * s, 40 * s, 10, 10))]
    out = [f'<g opacity="{op}">']
    for w, o, ps in g:
        out.append(f'<g fill="none" stroke="{col}" stroke-width="{w}" opacity="{o}">' + ''.join(f'<path d="{d}"/>' for d in ps) + '</g>')
    for r, o in ((332, .45), (338, .3), (250, .35), (182, .3)):
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r * s:.1f}" fill="none" stroke="{col}" stroke-width="1" opacity="{o}"/>')
    out.append('</g>')
    return ''.join(out)


def bordo(y0, W, col=ORO, op=1.0):
    out = [f'<g opacity="{op}"><g fill="none" stroke="{col}" stroke-width=".9" opacity=".5">']
    for j in range(10):
        ph = 2 * math.pi * j / 10
        pts = []
        for i in range(701):
            x = -10 + (W + 20) * i / 700
            y = y0 + 22 * math.sin(2 * math.pi * x / 180 + ph) * math.cos(math.pi * x / 540 + ph / 2)
            pts.append(f'{x:.1f} {y:.1f}')
        out.append('<path d="M' + ' L'.join(pts) + '"/>')
    out.append('</g>')
    for dy in (-35, 35):
        out.append(f'<line x1="0" y1="{y0 + dy}" x2="{W}" y2="{y0 + dy}" stroke="{col}" stroke-width="1" opacity=".4"/>')
    out.append('</g>')
    return ''.join(out)


def deco(W, H, parts):
    return f'<svg class="deco" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'


# --- Icone (tratto semplice, 6px a 1080) -------------------------------------
ICON = {
    'casa': '<path d="M14 46 L50 16 L86 46 M24 38 V84 H76 V38 M42 84 V60 H58 V84"/>',
    'borsa': '<path d="M20 34 H80 L74 86 H26 Z M36 34 V28 A14 14 0 0 1 64 28 V34"/>',
    'cassaforte': '<rect x="16" y="18" width="68" height="64" rx="8"/><circle cx="50" cy="50" r="15"/><path d="M50 35 V41 M50 59 V65 M35 50 H41 M59 50 H65 M24 82 V90 M76 82 V90"/>',
    'segnalibro': '<path d="M28 14 H72 V88 L50 70 L28 88 Z"/>',
    'freccia': '<path d="M18 50 H80 M56 26 L80 50 L56 74"/>',
    'spunta': '<path d="M22 52 L42 72 L80 30"/>',
}


def icon(name, size, col, sw=7):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 100 100" fill="none" stroke="{col}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" style="display:block">{ICON[name]}</svg>')

# --- Stile comune -----------------------------------------------------------
# Fondo chiaro = Avorio con testi Inchiostro e numeri Bordeaux.
# Fondo scuro = Bordeaux con testi Avorio e numeri Oro nordico (l'oro non va mai su Avorio: 2,1:1).
# Guida del logo: l'oro come testo solo da 56 px in su; sotto, solo come fondo o forma (evidenziatore, cerchio, spunta).
def css(W, H, dark):
    bg, fg = (BORDEAUX, AVORIO) if dark else (AVORIO, INK)
    return f"""
@font-face{{font-family:'Bodoni Moda';src:url('../../font/BodoniModa-VF.ttf') format('truetype');font-weight:400 900;font-style:normal}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{background:{bg};color:{fg};font-family:'Inter',sans-serif;font-weight:400;position:relative}}
.deco{{position:absolute;left:0;top:0}}
.grana{{position:absolute;inset:0;background:url(data:image/png;base64,{GRANA});background-size:256px;opacity:{.3 if dark else .6};{'mix-blend-mode:screen;' if dark else ''}}}
.abs{{position:absolute}}
.eyebrow{{font-weight:800;font-size:26px;letter-spacing:.22em;text-transform:uppercase;color:{AVORIO if dark else BORDEAUX}}}
.xb{{font-weight:800}}
.bodoni{{font-family:'Bodoni Moda',serif;font-weight:500;letter-spacing:-.01em;font-optical-sizing:auto}}
.d1{{font-weight:800;letter-spacing:-.045em;line-height:.9}}
.h1{{font-family:'Bodoni Moda',serif;font-weight:500;font-size:96px;line-height:1.04;letter-spacing:-.015em}}
.h2{{font-weight:800;font-size:69px;line-height:1.05;letter-spacing:-.025em}}
.body{{font-size:44px;line-height:1.3;color:{fg}}}
.sec{{color:{AVORIO if dark else GRAFITE}}}
.num{{color:{ORO if dark else BORDEAUX};font-weight:800}}
.cnt{{font-weight:800;font-size:26px;letter-spacing:.08em;color:{AVORIO if dark else GRAFITE};font-variant-numeric:tabular-nums}}
.tag{{display:inline-flex;align-items:center;height:56px;padding:0 26px;border-radius:999px;border:2.5px solid {fg};font-weight:800;font-size:24px;letter-spacing:.2em}}
.pill{{display:flex;align-items:center;justify-content:space-between;background:{AVORIO if dark else BORDEAUX};color:{BORDEAUX if dark else AVORIO};border-radius:999px;box-shadow:0 18px 40px rgba(31,26,28,.2)}}
.pill .t{{font-weight:800;letter-spacing:.01em}}
.pill .c{{border-radius:50%;background:{BORDEAUX if dark else ORO};display:flex;align-items:center;justify-content:center}}
.disc{{font-size:26px;line-height:1.4;color:{AVORIO if dark else GRAFITE}}}
.sub{{display:inline-block;padding:18px 34px;border-radius:999px;font-weight:800;font-size:46px;line-height:1.2;letter-spacing:-.01em}}
.sub.su-chiaro{{background:{BORDEAUX};color:{AVORIO}}}
.sub.su-scuro{{background:transparent;color:{AVORIO};padding:0}}
.sub b{{background:{ORO};color:{BORDEAUX};font-weight:800;border-radius:14px;padding:0 12px;margin:0 -2px}}
"""


def page(W, H, dark, body, decoparts=()):
    return (f'<!doctype html><html lang="it"><head><meta charset="utf-8"><style>{css(W, H, dark)}</style></head><body>'
            f'{deco(W, H, decoparts) if decoparts else ""}<div class="grana"></div>{body}</body></html>')


def pill(text, w, h, ic='freccia', dark=False):
    c = h - 30
    return (f'<div class="pill" style="width:{w}px;height:{h}px;padding:0 15px 0 {int(h * .42)}px">'
            f'<span class="t" style="font-size:{int(h * .3)}px">{text}</span>'
            f'<span class="c" style="width:{c}px;height:{c}px">{icon(ic, int(c * .5), ORO if dark else BORDEAUX, 9)}</span></div>')


def footer(W, H, n, tot, dark=False, y=None):
    y = y if y is not None else H - 120
    return (f'<div class="abs" style="left:88px;top:{y - 4}px">{logo(36, dark)}</div>'
            f'<div class="abs cnt" style="right:88px;top:{y}px">{n}/{tot}</div>')


def bar_rows(rows, dark, width):
    out = []
    for lab, val, pct, col, ic in rows:
        out.append(f"""<div style="display:flex;flex-direction:column;gap:18px">
  <div style="display:flex;align-items:center;justify-content:space-between">
    <div style="display:flex;align-items:center;gap:22px">{icon(ic, 54, AVORIO if dark else INK, 7)}<span class="xb" style="font-size:44px">{lab}</span></div>
    <span class="xb" style="font-size:52px;font-variant-numeric:tabular-nums">{val}</span></div>
  <div style="height:22px;border-radius:999px;background:{'rgba(245,239,228,.16)' if dark else FILO}">
    <div style="height:100%;width:{pct}%;border-radius:999px;background:{col}"></div></div></div>""")
    return f'<div style="display:flex;flex-direction:column;gap:46px;width:{width}px">{"".join(out)}</div>'


# --- Caroselli 1080x1350 -----------------------------------------------------
# Ritmo: Bordeaux per copertina, passaggi e chiusura; Avorio per il resto. Mai due Bordeaux di fila.
W, H = 1080, 1350
TOT = 6
car = {}

car['carosello-01-copertina'] = page(W, H, True, f"""
<div class="abs" style="left:88px;top:100px">{logo(52, dark=True)}</div>
<div class="abs eyebrow" style="left:88px;top:440px">Stagione 1 · Episodio 2</div>
<div class="abs bodoni" style="left:86px;top:500px;font-size:104px">La regola</div>
<div class="abs d1 num" style="left:80px;top:640px;font-size:208px">50<span style="font-weight:400">/</span>30<span style="font-weight:400">/</span>20</div>
<div class="abs body" style="left:88px;top:880px;width:760px">Dove far andare lo stipendio, ogni mese.</div>
<div class="abs" style="left:88px;top:{H - 200}px">{pill('Scorri', 330, 112, dark=True)}</div>
<div class="abs cnt" style="right:88px;top:{H - 158}px">1/{TOT}</div>
""", [rosone(1000, 120, 1, ORO, .55)])

car['carosello-02-problema'] = page(W, H, False, f"""
<div class="abs eyebrow" style="left:88px;top:110px">Il problema</div>
<div class="abs h1" style="left:88px;top:270px;width:900px;font-size:104px">Lo stipendio arriva il 27. Il 15 è già finito.</div>
<div class="abs body sec" style="left:88px;top:740px;width:820px">Succede quando i soldi non hanno un piano prima di arrivare sul conto.</div>
{footer(W, H, 2, TOT)}
""", [bordo(1110, W, ORO, .9)])

car['carosello-03-passaggio'] = page(W, H, True, f"""
<div class="abs eyebrow" style="left:88px;top:110px">Passaggio 1 di 3</div>
<div class="abs" style="left:88px;top:300px">{icon('casa', 110, ORO, 6)}</div>
<div class="abs d1 num" style="left:76px;top:450px;font-size:300px">50%</div>
<div class="abs h1" style="left:88px;top:750px">Bisogni</div>
<div class="abs body" style="left:88px;top:880px;width:830px">Affitto, bollette, spesa, trasporti. Quello che paghi comunque.</div>
{footer(W, H, 3, TOT, dark=True)}
""", [rosone(1040, 240, .9, ORO, .5)])

car['carosello-04-esempio'] = page(W, H, False, f"""
<div class="abs" style="left:88px;top:96px"><span class="tag">Esempio</span></div>
<div class="abs body sec" style="left:88px;top:250px">Stipendio netto</div>
<div class="abs d1 num" style="left:82px;top:320px;font-size:170px">1.400 €</div>
<div class="abs" style="left:88px;top:600px">{bar_rows([('Bisogni', '700 €', 50, BORDEAUX, 'casa'), ('Desideri', '420 €', 30, GRAFITE, 'borsa'), ('Risparmio', '280 €', 20, INK, 'cassaforte')], False, 904)}</div>
<div class="abs disc" style="left:88px;top:1110px">Cifre tonde, solo come esempio.</div>
{footer(W, H, 4, TOT)}
""")

items = ['Guarda il netto medio degli ultimi 3 mesi', 'Elenca le spese fisse del mese', 'Separa i risparmi su un conto o salvadanaio a parte', 'Programma un bonifico il giorno dopo lo stipendio']
check = ''.join(f"""<div style="display:flex;gap:30px;align-items:flex-start">
<div style="flex:none;width:64px;height:64px;border-radius:50%;background:{BORDEAUX};display:flex;align-items:center;justify-content:center">{icon('spunta', 36, ORO, 12)}</div>
<div class="body" style="font-size:42px;padding-top:4px">{t}</div></div>""" for t in items)
car['carosello-05-checklist'] = page(W, H, False, f"""
<div class="abs eyebrow" style="left:88px;top:110px;display:flex;align-items:center;gap:16px">{icon('segnalibro', 40, BORDEAUX, 9)}Da salvare</div>
<div class="abs h1" style="left:88px;top:220px;width:880px;font-size:84px">Il 50/30/20 in quattro mosse</div>
<div class="abs" style="left:88px;top:480px;width:880px;display:flex;flex-direction:column;gap:44px">{check}</div>
{footer(W, H, 5, TOT)}
""")

car['carosello-06-chiusura'] = page(W, H, True, f"""
<div class="abs" style="left:88px;top:300px">{logo(110, oro=True)}</div>
<div class="abs body" style="left:88px;top:490px;width:840px">Prossimo episodio: <span class="xb">il fondo emergenze.</span></div>
<div class="abs" style="left:88px;top:700px">{pill('Salva per dopo', 904, 150, 'segnalibro', dark=True)}</div>
<div class="abs disc" style="left:88px;top:910px;width:880px">Contenuto a scopo educativo. Non è consulenza finanziaria, fiscale o legale. Per la tua situazione parla con un professionista abilitato.</div>
<div class="abs cnt" style="right:88px;top:{H - 122}px">6/{TOT}</div>
""", [rosone(1010, 70, .85, ORO, .55), bordo(1250, W, ORO, .7)])

# --- Reel 1080x1920 -----------------------------------------------------------
RW, RH = 1080, 1920
reel = {}


def subtitle(words, active, dark, y):
    t = ' '.join(f'<b>{w}</b>' if i == active else w for i, w in enumerate(words.split()))
    cls = 'su-scuro' if dark else 'su-chiaro'
    return f'<div class="abs" style="left:0;right:140px;top:{y}px;text-align:center;padding-left:64px"><span class="sub {cls}">{t}</span></div>'


def progress(n, tot, dark):
    segs = ''.join(f'<div style="flex:1;height:10px;border-radius:999px;background:{(ORO if dark else BORDEAUX) if i < n else ("rgba(245,239,228,.2)" if dark else FILO)}"></div>' for i in range(tot))
    return f'<div class="abs" style="left:88px;right:140px;top:250px;display:flex;gap:14px">{segs}</div>'


reel['reel-00-copertina'] = page(RW, RH, True, f"""
<div class="abs" style="left:88px;top:300px">{logo(50, dark=True)}</div>
<div class="abs eyebrow" style="left:88px;top:700px">Stagione 1 · Episodio 2</div>
<div class="abs bodoni" style="left:86px;top:760px;font-size:110px">La regola</div>
<div class="abs d1 num" style="left:78px;top:905px;font-size:208px">50<span style="font-weight:400">/</span>30<span style="font-weight:400">/</span>20</div>
<div class="abs body" style="left:88px;top:1150px;width:780px;font-size:52px">Dove va lo stipendio, in 60 secondi.</div>
""", [rosone(1000, 260, 1, ORO, .55), bordo(1800, RW, ORO, .6)])

reel['reel-01-hook'] = page(RW, RH, True, f"""
<div class="abs eyebrow" style="left:88px;top:330px">Episodio 2 · Le basi</div>
<div class="abs h1" style="left:88px;top:500px;width:860px;font-size:124px;line-height:1">A metà mese lo stipendio è <span style="color:{ORO}">già finito?</span></div>
{subtitle('Capita spesso, e c’è un motivo.', 5, True, 1290)}
""", [rosone(1050, 1500, 1.1, ORO, .45)])

reel['reel-02-passaggio'] = page(RW, RH, False, f"""
{progress(1, 3, False)}
<div class="abs eyebrow" style="left:88px;top:330px">Passaggio 1 di 3</div>
<div class="abs" style="left:88px;top:470px">{icon('casa', 130, BORDEAUX, 6)}</div>
<div class="abs d1 num" style="left:74px;top:640px;font-size:300px">50%</div>
<div class="abs h1" style="left:88px;top:940px;font-size:116px">Bisogni</div>
<div class="abs body sec" style="left:88px;top:1100px;width:820px">Affitto, bollette, spesa, trasporti.</div>
{subtitle('la metà va alle spese fisse', 1, False, 1350)}
""")

reel['reel-03-esempio'] = page(RW, RH, True, f"""
<div class="abs" style="left:88px;top:300px"><span class="tag">Esempio</span></div>
<div class="abs body" style="left:88px;top:440px">Stipendio netto</div>
<div class="abs d1 num" style="left:80px;top:510px;font-size:200px">1.400 €</div>
<div class="abs" style="left:88px;top:800px">{bar_rows([('Bisogni', '700 €', 50, AVORIO, 'casa'), ('Desideri', '420 €', 30, ORO, 'borsa'), ('Risparmio', '280 €', 20, 'rgba(245,239,228,.55)', 'cassaforte')], True, 852)}</div>
<div class="abs disc" style="left:88px;top:1270px">Cifre tonde, solo come esempio.</div>
{subtitle('280 euro restano a te ogni mese', 0, True, 1370)}
""")

recap = ''.join(f"""<div style="display:flex;align-items:baseline;gap:34px;padding:34px 0;border-top:2px solid {FILO}">
<span class="d1 num" style="font-size:150px;width:330px;display:inline-block">{n}%</span><span class="h1" style="font-size:84px">{t}</span></div>""" for n, t in (('50', 'Bisogni'), ('30', 'Desideri'), ('20', 'Risparmio')))
reel['reel-04-recap'] = page(RW, RH, False, f"""
{progress(3, 3, False)}
<div class="abs eyebrow" style="left:88px;top:330px">Recap</div>
<div class="abs" style="left:88px;top:430px;width:852px;border-bottom:2px solid {FILO}">{recap}</div>
{subtitle('cinquanta, trenta, venti. Fine.', 3, False, 1350)}
""", [rosone(1060, 1700, .8, ORO, .8)])

reel['reel-05-chiusura'] = page(RW, RH, True, f"""
<div class="abs" style="left:88px;top:420px">{logo(118, oro=True)}</div>
<div class="abs body" style="left:88px;top:620px;width:840px">Prossimo episodio: <span class="xb">il fondo emergenze.</span></div>
<div class="abs" style="left:88px;top:860px">{pill('Salva per dopo', 852, 150, 'segnalibro', dark=True)}</div>
<div class="abs disc" style="left:88px;top:1080px;width:852px">Contenuto a scopo educativo. Non è consulenza finanziaria, fiscale o legale. Per la tua situazione parla con un professionista abilitato.</div>
""", [rosone(1010, 90, .85, ORO, .55), bordo(1800, RW, ORO, .6)])

# Guida zone sicure (sopra la chiusura)
reel['reel-guida-zone-sicure'] = reel['reel-05-chiusura'].replace('</body>', f"""
<div class="abs" style="left:0;top:0;width:{RW}px;height:220px;background:rgba(198,161,91,.45);border-bottom:3px dashed {AVORIO}"></div>
<div class="abs" style="left:0;top:{RH - 420}px;width:{RW}px;height:420px;background:rgba(198,161,91,.45);border-top:3px dashed {AVORIO}"></div>
<div class="abs" style="right:0;top:220px;width:140px;height:{RH - 640}px;background:rgba(198,161,91,.3);border-left:3px dashed {AVORIO}"></div>
<div class="abs" style="left:0;top:240px;width:{RW}px;height:1440px;border:4px solid {AVORIO};border-radius:4px"></div>
<div class="abs xb" style="left:88px;top:90px;font-size:30px;color:{AVORIO}">Interfaccia Instagram · 220 px</div>
<div class="abs xb" style="left:88px;top:{RH - 190}px;font-size:30px;color:{AVORIO}">Didascalia e pulsanti · 420 px</div>
<div class="abs xb" style="left:88px;top:1440px;font-size:28px;color:{AVORIO}">Ritaglio griglia profilo 3:4 · 1080×1440</div>
<div class="abs xb" style="right:14px;top:700px;font-size:26px;color:{AVORIO};writing-mode:vertical-rl">Pulsanti · 140 px</div>
</body>""")

# --- Storia 1080x1920 ---------------------------------------------------------
storie = {}
storie['storia-01-intro'] = page(RW, RH, False, f"""
<div class="abs" style="left:96px;top:470px">{logo(118)}</div>
<div class="abs" style="left:100px;top:690px;width:120px;height:4px;background:{BORDEAUX}"></div>
<div class="abs h1" style="left:96px;top:760px;width:880px;font-size:92px;line-height:1.08">Le cose sui soldi che a scuola <i style="font-style:normal;color:{BORDEAUX}">non ti spiegano.</i></div>
<div class="abs body sec" style="left:96px;top:1110px">In <span class="num">60</span> secondi.</div>
<div class="abs" style="left:72px;top:1500px">{pill('Segui per iniziare', 936, 164)}</div>
<div class="abs disc" style="left:0;right:0;top:1700px;text-align:center;font-style:italic;font-size:22px">Contenuto educativo. Non è consulenza finanziaria.</div>
""", [rosone(985, 95, 1, ORO, .9), bordo(1845, RW, ORO, .9)])


def render(name, html, w, h, outdir):
    os.makedirs(os.path.join(SRC, 'html'), exist_ok=True)
    os.makedirs(outdir, exist_ok=True)
    hp = os.path.join(SRC, 'html', name + '.html')
    open(hp, 'w').write(html)
    tmp = os.path.join(outdir, '_tmp.png')
    subprocess.run([CHROME, '--headless', '--no-sandbox', '--hide-scrollbars', f'--window-size={w},{h + 200}',
                    f'--screenshot={tmp}', hp], capture_output=True)
    Image.open(tmp).crop((0, 0, w, h)).save(os.path.join(outdir, name + '.png'))
    os.remove(tmp)


if __name__ == '__main__':
    for n, h in car.items():
        render(n, h, W, H, os.path.join(BASE, 'carosello'))
    for n, h in reel.items():
        render(n, h, RW, RH, os.path.join(BASE, 'reel'))
    for n, h in storie.items():
        render(n, h, RW, RH, os.path.join(BASE, 'storie'))
    print('fatto')
