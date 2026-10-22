"""mezzeuro, carosello episodio 3: il fondo emergenze (8 slide 1080x1350).
Usa stile, logo e componenti di ../kit post/sorgenti/genera_template.py.
Uso: python3 genera.py  -> scrive html/ e png/ in questa cartella. Serve Chromium.
"""
import os, sys, subprocess
from urllib.parse import quote
from PIL import Image

QUI = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(os.path.dirname(QUI), 'kit post')
sys.path.insert(0, os.path.join(KIT, 'sorgenti'))
import genera_template as G
from genera_template import (page, pill, footer, logo, icon, rosone, bordo,
                             BORDEAUX, AVORIO, ORO, INK, GRAFITE, FILO)

G.ICON['scudo'] = '<path d="M50 12 L82 24 V48 C82 70 68 82 50 90 C32 82 18 70 18 48 V24 Z"/><path d="M36 50 L46 60 L66 38"/>'
G.ICON['croce'] = '<path d="M30 30 L70 70 M70 30 L30 70"/>'

W, H, TOT = 1080, 1350, 8
car = {}

# 1 · Copertina (Bordeaux)
car['01-copertina'] = page(W, H, True, f"""
<div class="abs" style="left:88px;top:100px">{logo(52, dark=True)}</div>
<div class="abs eyebrow" style="left:88px;top:420px">Stagione 1 · Episodio 3</div>
<div class="abs bodoni" style="left:86px;top:480px;font-size:104px;line-height:1.02">Il fondo<br>emergenze</div>
<div class="abs d1 num" style="left:80px;top:720px;font-size:190px">3–6 mesi</div>
<div class="abs body" style="left:88px;top:930px;width:820px">Quanto tenere da parte per gli imprevisti, e dove.</div>
<div class="abs" style="left:88px;top:{H - 200}px">{pill('Scorri', 330, 112, dark=True)}</div>
<div class="abs cnt" style="right:88px;top:{H - 158}px">1/{TOT}</div>
""", [rosone(1000, 120, 1, ORO, .55)])

# 2 · Il problema (Avorio)
car['02-problema'] = page(W, H, False, f"""
<div class="abs eyebrow" style="left:88px;top:110px">Il problema</div>
<div class="abs h1" style="left:88px;top:270px;width:900px;font-size:104px">Si rompe il telefono. È il 15 del mese.</div>
<div class="abs body sec" style="left:88px;top:740px;width:840px">Senza soldi da parte, l’imprevisto finisce a rate, sulla carta di credito o in una telefonata a casa.</div>
{footer(W, H, 2, TOT)}
""", [bordo(1110, W, ORO, .9)])

# 3 · Passaggio 1: quanto (Bordeaux)
car['03-quanto'] = page(W, H, True, f"""
<div class="abs eyebrow" style="left:88px;top:110px">Passaggio 1 di 3 · Quanto</div>
<div class="abs" style="left:88px;top:270px">{icon('scudo', 110, ORO, 6)}</div>
<div class="abs d1 num" style="left:76px;top:420px;font-size:300px">3–6</div>
<div class="abs h1" style="left:88px;top:720px">mesi di spese</div>
<div class="abs body" style="left:88px;top:860px;width:860px">Affitto, bollette, spesa, trasporti: le spese essenziali, non lo stipendio intero. Primo traguardo: <span class="xb">1 mese.</span></div>
{footer(W, H, 3, TOT, dark=True)}
""", [rosone(1040, 240, .9, ORO, .5)])

# 4 · Esempio (Avorio): tappe con 280 € al mese (il 20% dell'episodio 2)
def tappa(lab, val, pct, col, nota):
    return f"""<div style="display:flex;flex-direction:column;gap:14px">
  <div style="display:flex;align-items:baseline;justify-content:space-between">
    <span class="xb" style="font-size:44px">{lab}</span>
    <span class="xb" style="font-size:52px;font-variant-numeric:tabular-nums">{val}</span></div>
  <div style="height:22px;border-radius:999px;background:{FILO}">
    <div style="height:100%;width:{pct}%;border-radius:999px;background:{col}"></div></div>
  <span class="body sec" style="font-size:30px">{nota}</span></div>"""

tappe = ''.join([
    tappa('1 mese', '700 €', 17, BORDEAUX, 'primo traguardo, in 3 mesi'),
    tappa('3 mesi', '2.100 €', 50, GRAFITE, 'ci arrivi in 8 mesi'),
    tappa('6 mesi', '4.200 €', 100, INK, 'ci arrivi in 15 mesi'),
])
car['04-esempio'] = page(W, H, False, f"""
<div class="abs" style="left:88px;top:96px"><span class="tag">Esempio</span></div>
<div class="abs body sec" style="left:88px;top:200px">Spese essenziali al mese</div>
<div class="abs d1 num" style="left:82px;top:262px;font-size:160px">700 €</div>
<div class="abs body" style="left:88px;top:448px;width:904px;font-size:34px">Con <span class="xb">280 € al mese</span>, il 20% dell’episodio scorso:</div>
<div class="abs" style="left:88px;top:560px;width:904px;display:flex;flex-direction:column;gap:40px">{tappe}</div>
<div class="abs disc" style="left:88px;top:1150px">Cifre tonde, solo come esempio.</div>
{footer(W, H, 4, TOT)}
""")

# 5 · Passaggio 2: dove (Bordeaux)
car['05-dove'] = page(W, H, True, f"""
<div class="abs eyebrow" style="left:88px;top:110px">Passaggio 2 di 3 · Dove</div>
<div class="abs" style="left:88px;top:270px">{icon('cassaforte', 110, ORO, 6)}</div>
<div class="abs h1" style="left:88px;top:430px;width:900px">Separato, ma <span style="color:{ORO}">a portata di mano.</span></div>
<div class="abs body" style="left:88px;top:700px;width:860px">Su un conto a parte, che non tocchi per le spese di tutti i giorni e che puoi usare in giornata.</div>
<div class="abs body" style="left:88px;top:930px;width:860px;opacity:.8">Non in Borsa: il giorno che ti serve potrebbe valere meno.</div>
{footer(W, H, 5, TOT, dark=True)}
""", [rosone(1040, 240, .9, ORO, .5)])

# 6 · Passaggio 3: quando (Avorio)
def voce(t, si):
    bg, ic, ico = (BORDEAUX, ORO, 'spunta') if si else (FILO, GRAFITE, 'croce')
    return (f'<div style="display:flex;gap:26px;align-items:center">'
            f'<div style="flex:none;width:58px;height:58px;border-radius:50%;background:{bg};display:flex;align-items:center;justify-content:center">{icon(ico, 32, ic, 12)}</div>'
            f'<div class="body" style="font-size:38px;line-height:1.2">{t}</div></div>')

si = ''.join(voce(t, True) for t in ('Il dentista che non puoi rimandare', 'L’auto o la bici per andare al lavoro', 'Un mese senza stipendio'))
no = ''.join(voce(t, False) for t in ('I saldi', 'Il telefono nuovo perché è uscito', 'Il weekend con gli amici'))
car['06-quando'] = page(W, H, False, f"""
<div class="abs eyebrow" style="left:88px;top:110px">Passaggio 3 di 3 · Quando</div>
<div class="abs h1" style="left:88px;top:200px;font-size:88px">È un’emergenza?</div>
<div class="abs xb" style="left:88px;top:370px;font-size:30px;letter-spacing:.18em;color:{BORDEAUX}">SÌ</div>
<div class="abs" style="left:88px;top:430px;width:904px;display:flex;flex-direction:column;gap:26px">{si}</div>
<div class="abs xb" style="left:88px;top:730px;font-size:30px;letter-spacing:.18em;color:{GRAFITE}">NO</div>
<div class="abs" style="left:88px;top:790px;width:904px;display:flex;flex-direction:column;gap:26px">{no}</div>
{footer(W, H, 6, TOT)}
""")

# 7 · Da salvare (Avorio)
mosse = ['Somma le spese essenziali di un mese',
         'Primo traguardo 1 mese, poi 3. Fino a 6 se il lavoro è incerto',
         'Tienilo su un conto separato, sempre disponibile',
         'Bonifico automatico il giorno dopo lo stipendio. Se lo usi, ricaricalo per primo']
check = ''.join(f"""<div style="display:flex;gap:30px;align-items:flex-start">
<div style="flex:none;width:64px;height:64px;border-radius:50%;background:{BORDEAUX};display:flex;align-items:center;justify-content:center">{icon('spunta', 36, ORO, 12)}</div>
<div class="body" style="font-size:40px;padding-top:4px">{t}</div></div>""" for t in mosse)
car['07-da-salvare'] = page(W, H, False, f"""
<div class="abs eyebrow" style="left:88px;top:110px;display:flex;align-items:center;gap:16px">{icon('segnalibro', 40, BORDEAUX, 9)}Da salvare</div>
<div class="abs h1" style="left:88px;top:220px;width:880px;font-size:84px">Il fondo emergenze in quattro mosse</div>
<div class="abs" style="left:88px;top:480px;width:880px;display:flex;flex-direction:column;gap:40px">{check}</div>
{footer(W, H, 7, TOT)}
""")

# 8 · Chiusura (Bordeaux)
car['08-chiusura'] = page(W, H, True, f"""
<div class="abs" style="left:88px;top:300px">{logo(110, oro=True)}</div>
<div class="abs body" style="left:88px;top:490px;width:860px">Prossimo episodio: <span class="xb">lordo e netto, cosa sparisce dalla busta paga.</span></div>
<div class="abs" style="left:88px;top:720px">{pill('Salva per dopo', 904, 150, 'segnalibro', dark=True)}</div>
<div class="abs disc" style="left:88px;top:930px;width:880px">Contenuto a scopo educativo. Non è consulenza finanziaria, fiscale o legale. Per la tua situazione parla con un professionista abilitato.</div>
<div class="abs cnt" style="right:88px;top:{H - 122}px">{TOT}/{TOT}</div>
""", [rosone(1010, 70, .85, ORO, .55), bordo(1250, W, ORO, .7)])


def render(name, html):
    font = 'file://' + quote(os.path.join(KIT, 'font')) + '/'
    html = html.replace("url('../../font/", f"url('{font}")
    for d in ('html', 'png'):
        os.makedirs(os.path.join(QUI, d), exist_ok=True)
    hp = os.path.join(QUI, 'html', name + '.html')
    open(hp, 'w').write(html)
    tmp = os.path.join(QUI, 'png', '_tmp.png')
    subprocess.run([G.CHROME, '--headless', '--no-sandbox', '--hide-scrollbars', '--allow-file-access-from-files',
                    f'--window-size={W},{H + 200}', f'--screenshot={tmp}', hp], capture_output=True)
    Image.open(tmp).crop((0, 0, W, H)).save(os.path.join(QUI, 'png', f'mezzeuro-ep03-{name}.png'))
    os.remove(tmp)


if __name__ == '__main__':
    for n, h in car.items():
        render(n, h)
    print('fatto')
