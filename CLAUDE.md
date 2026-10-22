# mezzeuro · istruzioni per Claude

Canale Instagram di educazione finanziaria per ragazzi italiani 18-30 anni ("le cose sui soldi che a scuola non ti spiegano, in 60 secondi"). Tono da fratello maggiore, niente promesse di guadagno. Si scrive in italiano.

## Dove sono le cose

- `1-logo/`: kit del logo "La valuta" (Bordeaux #6E1E2C, Oro nordico #C6A15B, Avorio #F5EFE4, Inchiostro #1F1A1C; Bodoni Moda + Inter).
- `2-post instagram/kit post/`: regole e template dei post. Ogni carosello si genera con uno script come `carosello-03-fondo-emergenze/genera.py`.
- `2-post instagram/CALENDARIO.md`: calendario editoriale. "genera ep N" vuol dire produrre l'episodio N come scritto lì e segnarlo ✅.
- `2-post instagram/reel-01/` e `metodo-crediti-kling.md`: reel con la mascotte Mezzo e budget crediti Kling.
- Copia sul Mac di Fede: `~/Desktop/CLAUDE/MEZZEURO/` (stessa struttura). I file finiti vanno copiati anche lì.

## Regola fissa: la finestra di caricamento

Per ogni lavoro mezzeuro con più passi (carosello, reel o video, piano, calendario, qualsiasi richiesta che richiede più di un passo) aggiorna la pagina **https://claude.ai/artifact/Kj58Fd43wZBzvKFqG7mTEE** ("mezzeuro in lavorazione"): Fede la tiene aperta per vedere a che punto sei.

- Si aggiorna con il tool `ArtifactData` sul documento `stato/corrente` (collection `stato`, doc_id `corrente`). Leggilo prima (`get`) e passa `if_version` nelle scritture.
- All'inizio: `set` con `titolo`, `percentuale` 0, `passo`, `passi` (lista `{testo, stato}` con stato `fatto` | `in corso` | `da fare`), `inizio` e `fineStimata` (ISO, stima onesta), `prodotti` `{fatti, totale, unita}` con unita "Slide" o "Fotogrammi", `aggiornato`.
- A ogni passo: `update` di `percentuale`, `passo`, `passi`, `prodotti` (es. slide renderizzate, fotogrammi del render), `fineStimata` se la stima cambia, `aggiornato`.
- Alla fine: `percentuale` 100, tutti i passi `fatto`. La pagina fa partire l'animazione di chiusura.
- Non scrivere nient'altro in quel database e non mettere dati personali.

## Regole dei contenuti

- Disclaimer in ogni post: "Contenuto a scopo educativo. Non è consulenza finanziaria, fiscale o legale. Per la tua situazione parla con un professionista abilitato."
- Cifre tonde marcate "Esempio"; niente nomi o loghi di banche, app o prodotti; niente lusso o mazzette.
- Oro mai su Avorio per testi o numeri; mai due slide Bordeaux di fila.
- Cifre di legge (bollo, aliquote, contributi) verificate su fonti ufficiali al momento di generare.
- Non pubblicare su nessun account senza l'ok esplicito di Fede.
