# mezzeuro — kit del logo

**Direzione:** A · La valuta. È la m di mezzeuro attraversata dalle due barre dell'euro: il canale ha la sua moneta.
**Carattere:** Bodoni Moda (SIL Open Font License 1.1: uso commerciale e nel logo libero).
**Colori:** Bordeaux `#6E1E2C` · Oro nordico `#C6A15B` · Avorio `#F5EFE4` · Inchiostro `#1F1A1C`.

La guida d'uso di una pagina è in [`guida/mezzeuro-guida.pdf`](guida/mezzeuro-guida.pdf). La tavola con i mockup è in
[`presentazione/mezzeuro-presentazione.html`](presentazione/mezzeuro-presentazione.html), con le slide PNG in `presentazione/slide/`.

## Quale file uso?

| Dove | File |
|---|---|
| Foto profilo Instagram | `social/instagram-profilo-avorio-1080.png` |
| Foto profilo YouTube | `social/youtube-profilo-avorio-800.png` |
| Filigrana dei video YouTube | `social/youtube-filigrana-avorio-150.png` (Studio › Personalizzazione › Branding) |
| Logo su fondo chiaro (sito, documenti) | `logo/mezzeuro-orizzontale.svg` · PNG in `logo/png/` |
| Logo su fondo bordeaux o scuro | `logo/mezzeuro-orizzontale-negativo.svg` |
| Copertine, merchandising, stampa grande | versioni `-oro` (barre oro, solo su bordeaux) |
| Spazi quadrati o verticali | `logo/mezzeuro-verticale*.svg`, `logo/mezzeuro-simbolo*.svg` |
| Sotto i 40 px | versioni `-piccolo` (barre più spesse e distanziate) |
| Stampa a un colore | versioni `-black` / `-white` |
| Tipografia | `logo/pdf/` (PDF vettoriali, RGB) |
| Sito web | `web/`: copia i file nella radice del sito e incolla `head-snippet.html` nel `<head>` |

Le foto profilo esistono anche nelle varianti `-oro` (barre oro) e `-chiaro` (fondo avorio). Per la foto profilo usa
quella avorio: sotto i 56 px le barre oro spariscono.

## Controlli fatti

- **Audit SVG della skill:** simboli 99/100, un colore, niente testo vivo, immagini o effetti. Nelle scritte risultano
  segnalate le diagonali della «z» (121,8° invece di 120°): è il disegno del carattere, non un errore.
- **Foto profilo:** provata a 160, 56 e 32 px. **Favicon:** provata a 16 e 32 px, su schede del browser chiare e scure.
- **Contrasti:** avorio su bordeaux 9,7:1 · oro su bordeaux 4,6:1 · oro su avorio 2,1:1 (troppo poco: non usarlo).
- **PDF:** vettoriali, una pagina, senza immagini raster.

## Da fare fuori dal kit

- **Ricerca di marchio** (UIBM, EUIPO, WIPO, ricerca inversa per immagini) prima di registrarlo o stamparlo in quantità.
- **Prova colore in tipografia:** i valori CMYK e Pantone della guida sono indicativi. I PDF sono in RGB; se la
  tipografia vuole CMYK o EPS, li converte un grafico in Illustrator o Affinity.
- **Unione dei tracciati per taglio e ricamo:** la m e le barre si sovrappongono in un unico tracciato, e a schermo e in
  stampa non si vede. Per plotter da taglio o ricamo serve un *Unisci* in un editor vettoriale.

## Rigenerare

Gli script sono in `../4-sorgenti/`. Dalla cartella `MEZZEURO`:

```bash
python3 4-sorgenti/build/kit.py all          # master, social, web, PNG, PDF
python3 4-sorgenti/build/guide.py            # guida d'uso
cd 1-logo/presentazione && python3 ../../4-sorgenti/build/board_it.py spec.json -o mezzeuro-presentazione.html --png-dir slide
```

Le misure del segno sono in `4-sorgenti/build/kit.py`. Le barre derivano dall'altezza della m (spessore 36,
distanza 62, sporgenza 54 su 439), quindi restano proporzionate in ogni versione.
