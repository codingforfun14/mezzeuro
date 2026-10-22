# Kit dei post Instagram, mezzeuro (ottobre 2026)

Template per caroselli e reel, allineati al kit del logo «La valuta» (`1-logo/`). Logo, colori e font arrivano da lì: questo kit dice solo come usarli nei post.

Posizionamento: per i ragazzi italiani tra 18 e 30 anni, mezzeuro è il canale di educazione finanziaria che spiega in 60 secondi le cose sui soldi che a scuola non ti spiegano, con il tono di un fratello maggiore e senza promesse di guadagno.

## Colori
| Nome | HEX | Compito nei post |
|---|---|---|
| Bordeaux | #6E1E2C | Fondo delle slide forti (copertina, passaggi, chiusura); numeri e titoli su Avorio |
| Avorio | #F5EFE4 | Fondo delle slide di lettura; testo su Bordeaux (9,7:1) |
| Oro nordico | #C6A15B | Numeri grandi, evidenziatore dei sottotitoli, spunte e guilloché. Su Bordeaux (4,6:1) e, come testo, solo da 56 px in su. Su Avorio solo nel guilloché decorativo |
| Inchiostro | #1F1A1C | Titoli e testi su Avorio (15:1) |
| Grafite | #6B6264 | Testo secondario e disclaimer su Avorio (5,2:1). Neutro aggiunto per i post |
| Filo | #E3D9CB | Linee e binari delle barre su Avorio, mai testo. Neutro aggiunto per i post |

Regola dei numeri: su Bordeaux numero Oro; su Avorio numero Bordeaux. Su Avorio l'oro non si usa per testi, numeri o barre (2,1:1).

## Font
- Bodoni Moda 500 per titoli, copertine e citazioni (file in `font/`, SIL OFL).
- Inter 800 e 400 per numeri, testi, sottotitoli e didascalie (SIL OFL).
- Riserva: 'Inter', 'Helvetica Neue', Arial, sans-serif.

## Logo e avatar
- Si usano sempre i file originali di `1-logo/logo`, copiati in `logo/`. Il nome non si riscrive con un font.
- Nei piè di pagina va l'orizzontale a 36 px di altezza (circa 250 px di larghezza, sopra il minimo di 120 px).
- La versione con le barre oro va solo in grande (chiusure).
- Foto profilo: la m avorio su bordeaux del kit, `logo/mezzeuro-avatar-instagram.png` (la stessa di `1-logo/social/instagram-profilo-avorio-1080.png`).

## Formati
- Carosello 1080×1350, margini 88 px, 6-8 slide: copertina (Bordeaux), problema (Avorio), passaggio (Bordeaux), esempio (Avorio), da salvare (Avorio), chiusura (Bordeaux).
- Reel 1080×1920: zone libere 220 px in alto, 420 in basso, 140 a destra (indicative). La copertina sta dentro il 1080×1440 centrale, che è il ritaglio della griglia del profilo. Guida in `reel/reel-guida-zone-sicure.png`.
- Storia 1080×1920: `storie/storia-01-intro.png`.

## Da non fare
1. Testo, numeri o barre oro su Avorio, oppure testo oro sotto i 56 px.
2. Loghi, carte o schermate reali di banche e app.
3. Cifre senza etichetta "Esempio", immagini di lusso o mazzette.

## File
- `logo/` SVG ufficiali e avatar
- `font/` Bodoni Moda e licenza
- `carosello/`, `reel/`, `storie/` PNG dei template
- `sorgenti/genera_template.py` rigenera tutti i template: si cambiano i testi nello script. Serve Chromium.
