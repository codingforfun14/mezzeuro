# Prompt Kling · reel 01 v2 (budget 100 crediti)

Tutto quello che serve per il piano v2: la correzione di K1, 8 immagini nuove, 8 varianti veloci per far muovere Mezzo e 2 clip video da 3 secondi, V1 (apertura) e V11 (finale). K8 (albero) e K9 (lavagna) ci sono già: sono K5-v1 e K6-v1. Costo stimato: **circa 75-85 crediti**. Il metodo per restare sotto i 100 crediti a reel è in [metodo-crediti-kling.md](../metodo-crediti-kling.md).

## Ordine di lavoro

1. **K1 corretto** (portafoglio vuoto): fa da riferimento per K2 e K3.
2. **Immagini nuove** K2, K3, K4, K5, K6, K7, K10, K11.
3. **Varianti** K1b, K6b, K8b, K11b e gli occhi chiusi di K4, K5, K7 e K9: sono modifiche delle immagini già fatte.
4. **Clip video** V1 e V11, da 3 secondi, solo dopo che ho controllato le immagini.

Mandami le immagini appena le hai, prima delle varianti e delle clip. Così controllo gratis che Mezzo sia coerente e che ci sia spazio per i sottotitoli, e le clip partono da immagini già buone.

## Impostazioni

**Immagini**
- Modello: Kling IMAGE 3.0, **2 immagini per generazione** (con 4 spendi il doppio), risoluzione massima.
- Formato: **9:16**, da impostare nelle impostazioni di Kling.
- Personaggio: Element "Mezzo". Se non riesci a usarlo, al suo posto carica `kling/E1-figura-intera.png`.
- Negative comune:
  ```
  cartoon, illustration, anime, plush toy, human hands, extra fingers, deformed paws, extra tail, text, letters, watermark
  ```
  Ogni prompt ha anche delle aggiunte sue.

**Clip video**
- Modello: Kling VIDEO 3.0, Image to Video, con l'immagine come primo fotogramma. Se puoi mettere anche l'ultimo fotogramma senza pagare di più, usa K1b per V1 e K11b per V11: il movimento viene più preciso.
- Durata: **3 s**, non 5, perché le inquadrature durano meno di 3 secondi. Formato: quello dell'immagine (9:16). Qualità: **1080p**, non 4K: il 4K costa quasi 4 volte tanto e per il reel non serve.
- Prima di generare guarda il costo sul tasto: per 3 s in 1080p senza audio dovrebbe essere 24 crediti. Se è molto di più, o se la durata di 3 s non c'è, scrivimi prima di generare.
- **Audio: spento.** Se non si spegne, lo tolgo io.
- Camera: se Kling ha il controllo camera, mettilo su statico/fisso.
- Negative comune:
  ```
  camera movement, zoom, pan, morphing, warping, extra fingers, deformed paws, text
  ```

Nelle clip la camera deve stare ferma: zoom, movimenti e scritte li aggiungo io dopo.

## Riferimenti

Sotto ogni prompt c'è la riga **Riferimenti** con i file da caricare. I percorsi sono dentro la cartella reel-01 sul tuo Mac. Ogni immagine che approvo la salvo io in reel-01/kling con il suo nome (K2.png, K3.png…), così la trovi quando serve come riferimento per quelle dopo.

---

## K1 corretto · il portafoglio vuoto (modifica di K1-v1)

**Fatta e approvata:** è `kling/K1.png`.

Usa la modifica immagine di Kling con K1-v1 come immagine di partenza.

```
Keep everything else unchanged: the same squirrel with the same face, expression, ear tufts and whiskers, the same deep bordeaux blazer, ivory t-shirt and lapel pin, the same bedroom background, the same lighting and the same framing. Modify only the wallet: make it a completely empty open brown leather bifold wallet held with both paws at chest height and tilted toward the camera, with no banknotes, no cards and no coins, the empty inner pockets and the worn leather lining clearly visible. Remove all the banknotes from his paws and from the wallet.
```
Aggiunte al negative: `banknotes, money, credit cards, coins, paper`

## K2 · dettaglio del portafoglio vuoto, la falena (inquadratura 2)

**Riferimenti:** Element Mezzo + `kling/K1.png` (stessa stanza e stesso portafoglio).

```
Extreme close-up, macro 100mm lens, eye level, vertical frame. Mezzo's two small furry russet paws, from the reference, with the cuffs of his deep bordeaux wool blazer visible at the bottom edge, hold an open empty brown leather bifold wallet facing the camera, filling the center of the frame. The wallet is completely empty: worn leather lining, empty card slots, nothing inside. A single small pale dusty moth flutters out of the wallet toward the camera, its wings softly motion-blurred, a few specks of dust floating in the light. Background: the same cozy bedroom at dusk as the reference image, completely out of focus, deep bordeaux wall and a warm lamp glow as round bokeh. Composition: wallet in the center at about 45% of the frame height, the moth in the upper middle, the lower quarter calm and dark. Lighting: warm tungsten key light from the left raking across the leather texture, cool blue fill from the right. Photorealistic cinematic still, same rendering style and color grade as the reference, visible leather grain and stitching, fine fur hairs on the paws, palette of deep bordeaux red, warm ivory and muted antique gold, very shallow depth of field, subtle film grain.
```
Aggiunte al negative: `banknotes, cards, coins, face, human fingers, butterfly with bright colors`

## K3 · spallucce (inquadratura 3)

**Riferimenti:** Element Mezzo + `kling/K1.png` (stessa stanza).

```
Medium full shot from the knees up, eye level, 35mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, charcoal trousers, round bordeaux and gold lapel pin). Same cozy Italian student bedroom at dusk as the reference image: deep bordeaux wall, single bed with rumpled ivory linen, brass bedside lamp switched on, window with cool blue evening light. He shrugs with both shoulders raised, both arms open and palms turned up, the empty brown leather wallet hanging open from his left paw, eyebrows raised and a resigned ironic half-smile, as if saying "what can you do". The tail rises behind him in a soft curve. Composition: his head about one third from the top of the frame, nothing important in the top tenth, the lower third calm with the dark floor and the edge of the bed. Lighting: warm tungsten key light from the lamp on the left, cool blue fill from the window, soft warm rim light on the fur. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, fine individual fur hairs, visible wool weave, palette of deep bordeaux red, warm ivory and muted antique gold, shallow depth of field, subtle film grain.
```
Aggiunte al negative: `money, coins, cards, sad expression`

## K4 · la scrivania con le tre buste (inquadrature 5 e 7, clip V4)

**Riferimenti:** solo Element Mezzo.

```
Medium shot from a slightly high angle, straight-on, 40mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, round bordeaux and gold lapel pin). He sits behind a tidy dark walnut desk, facing the camera, and rests his paws lightly on three plain ivory paper envelopes lined up side by side in front of him, perfectly spaced, flaps closed and facing up, the three envelopes clearly separated with some desk visible between them. Next to the right envelope, a small neat stack of plain gold coins. He looks into the lens with a calm, confident half-smile, like a teacher about to explain a rule. Room: deep bordeaux wall, a single brass desk lamp casting a warm circle of light on the desk, softly out of focus. Composition: his head in the upper third of the frame, the three envelopes side by side across the center of the frame at about 55% of the height, the bottom fifth taken by the dark front edge of the desk. Lighting: warm desk lamp as key light from above left, soft dark falloff in the room, warm rim light on the fur. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, paper and wood texture, palette of deep bordeaux red, warm ivory and muted antique gold, shallow depth of field, subtle film grain.
```
Aggiunte al negative: `writing on envelopes, stamps, open envelopes, banknotes, overlapping envelopes`

## K5 · le scale con la spesa (inquadrature 9 e 10)

**Riferimenti:** solo Element Mezzo.

```
Medium full shot, slightly low angle looking up the staircase, 35mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, charcoal trousers, white leather sneakers, round bordeaux and gold lapel pin). He climbs the worn stone stairs of an old Italian apartment building, one foot on the next step, carrying a brown paper grocery bag in his left arm with a baguette and fresh leeks sticking out, a small set of keys dangling from his right paw. He looks toward the camera with a slightly tired but composed expression, ears a little lowered. Setting: grey stone steps, a black wrought-iron railing with simple curls, ivory plaster walls, a deep bordeaux wooden apartment door on the landing above, a tall window with soft afternoon daylight. Composition: Mezzo in the center, his face large and clearly lit in the upper third of the frame, the staircase rising diagonally behind him, the lower third simple steps. Lighting: soft daylight from the window above right, gentle bounce on the stone, warm rim light on the tail. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, stone and paper texture, palette of deep bordeaux red, warm ivory and muted antique gold, shallow depth of field, subtle film grain.
```
Aggiunte al negative: `labels on products, brand logos, text on the bag, face in shadow`

## K6 · pizza e concerto (inquadratura 12, clip V6)

**Riferimenti:** solo Element Mezzo.

```
Medium shot from the waist up, eye level, 50mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, round bordeaux and gold lapel pin). He stands on a lively narrow Italian street at night outside a small pizzeria, holding a whole folded slice of margherita pizza in his right paw, raised close to his mouth, about to take the first bite, and a plain paper concert ticket between two fingers of his left paw at chest height. Big content smile, eyes bright, ears relaxed. Background softly out of focus: warm string lights crossing above the street, the glowing pizzeria window, blurred silhouettes of young people chatting, cobblestones. Composition: his head about one third from the top, pizza and ticket clearly visible, the lower quarter soft bokeh. Lighting: warm glow from the pizzeria and string lights as key from the right, cool blue night ambience on the left, warm rim light on the fur. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, palette of deep bordeaux red, warm ivory and muted antique gold, shallow depth of field with round bokeh, subtle film grain.
```
Aggiunte al negative: `bitten pizza, text on the ticket, shop sign lettering, logos, crowd faces in focus`

## K7 · il divano e l'abbonamento (inquadratura 13)

**Riferimenti:** solo Element Mezzo.

```
Medium shot, eye level, 35mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, charcoal trousers, round bordeaux and gold lapel pin). He is slumped deep into a worn deep bordeaux velvet sofa in a dim living room at night, legs stretched out, holding a plain black TV remote loosely in one paw pointed at an off-screen TV. Half-closed bored eyes, ears drooping, a flat expression of total boredom, his tail draped over the armrest. His face and the front of his blazer are lit by the cool flickering blue light of the off-screen TV. A small untouched bowl of popcorn on the cushion beside him. Composition: Mezzo in the left two thirds of the frame, his head about one third from the top, the right third of the frame darker and calm, the lower quarter simple. Lighting: cool blue TV light from the front right as key, a small warm lamp far in the background, warm rim light on the fur. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, velvet and fur texture, palette of deep bordeaux red, warm ivory and muted antique gold with a cool blue accent, shallow depth of field, subtle film grain.
```
Aggiunte al negative: `visible TV screen, logos, phone, smiling`

## K10 · "Salvalo" (inquadratura 19)

**Riferimenti:** Element Mezzo + `riferimenti-kling/mezzeuro-spilla-riferimento.png` (la spilla si vede da vicino).

```
Medium shot from the waist up, eye level, 85mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, round bordeaux enamel lapel pin with a gold rim, the ivory letter m and two thin gold bars, like the pin in the reference photo of the pin). He stands slightly to the left of center and points with his right arm and index finger toward the right edge of the frame, slightly downward, as if pointing at a button next to him, while looking into the lens with a complicit, knowing smile and one eyebrow raised. Background: plain seamless deep bordeaux studio backdrop with a soft lighter glow behind him, no objects. Composition: his head about one third from the top, the right third of the frame at mid height completely empty, the lower quarter plain backdrop. Lighting: soft key light from the front left, warm golden rim light outlining ears, whiskers and tail. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, fine individual fur hairs, visible wool weave, palette of deep bordeaux red, warm ivory and muted antique gold, subtle film grain.
```
Aggiunte al negative: `props, phone, both arms raised, distorted pin`

## K11 · occhiolino e moneta (inquadratura 20, clip V11)

**Riferimenti:** Element Mezzo + `riferimenti-kling/mezzeuro-spilla-riferimento.png` (la spilla si vede da vicino).

```
Medium shot from the waist up, eye level, 85mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, round bordeaux enamel lapel pin with a gold rim, the ivory letter m and two thin gold bars, like the pin in the reference photo of the pin). He holds his right paw in front of his chest with a single plain smooth gold coin balanced on his curled thumb, ready to flick it up, and looks into the lens with a sly confident half-smile, as if about to wink. His tail curls up behind his shoulder. Background: plain seamless deep bordeaux studio backdrop with a soft lighter glow behind him, no objects. Composition: his head in the center of the frame at about 40% of the height, the upper quarter of the frame completely empty, the lower fifth plain backdrop. Lighting: soft key light from the front left, strong warm golden rim light outlining his ears, whiskers and tail, a small bright highlight on the coin. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, fine individual fur hairs, visible wool weave, palette of deep bordeaux red, warm ivory and muted antique gold, subtle film grain.
```
Aggiunte al negative: `engraved coin, euro symbol, letters, coin in the air, distorted pin`

---

## Le varianti (modifica immagine, 1 immagine per generazione)

Ognuna parte da un'immagine già fatta e cambia solo un dettaglio. Io allineo la variante all'originale e prendo solo la parte che cambia: così, senza clip, Mezzo sbatte le palpebre, alza lo sguardo, morde la pizza e fa l'occhiolino. Per questo devono restare il più possibile identiche all'originale. Se una variante sposta tutta la scena, rifalla una volta; se succede ancora, mandamela lo stesso.

Aggiunte al negative di tutte le varianti: `changed pose, changed framing, changed background, different squirrel`

### K1b · da K1 corretto, lo sguardo in camera (inquadratura 1)

**Riferimenti:** solo `kling/K1.png` come immagine da modificare, senza Element.

```
Keep everything else unchanged: the same squirrel, the same pose, the same empty open wallet held with both paws, the same deep bordeaux blazer, ivory t-shirt and lapel pin, the same bedroom background, the same lighting and the same framing. Modify only his head and eyes: he now looks straight into the lens with one eyebrow raised and a flat, unimpressed expression, ears turned slightly forward.
```
Aggiunte al negative: `banknotes, money, cards, coins, open mouth`

### K6b · da K6, il morso (inquadratura 12)

**Riferimenti:** solo K6 come immagine da modificare, senza Element.

```
Keep everything else unchanged: the same squirrel, the same pose, the same concert ticket in his left paw, the same blazer and lapel pin, the same street background, the same lighting and the same framing. Modify only the pizza and his face: one small bite is now missing from the tip of the pizza slice, and he chews with his eyes closed in pure enjoyment and a happy closed-mouth smile.
```
Aggiunte al negative: `text on the ticket, extra pizza, open mouth`

### K8b · da K8 (K5-v1), la moneta lasciata (inquadratura 14)

**Riferimenti:** solo `kling/K8 (era K5-v1).png` come immagine da modificare, senza Element.

```
Keep everything else unchanged: the same squirrel, the same pose, the same blazer and lapel pin, the same tree, the same lighting and the same framing. Modify only his paw, the coin and the glow: his paw is now open and empty just above the hollow of the trunk, the gold coin is no longer in his paw, the warm golden glow inside the hollow is brighter and lights his face a little more, and he has a small satisfied smile.
```
Aggiunte al negative: `coin in the paw, coins flying, engraved coins`

### K11b · da K11, l'occhiolino (inquadratura 20)

**Riferimenti:** solo K11 come immagine da modificare, senza Element.

```
Keep everything else unchanged: the same squirrel, the same blazer, t-shirt and lapel pin, the same bordeaux backdrop, the same rim lighting and the same framing. Modify only his face and right paw: he now winks at the camera with his left eye fully closed and his right eye open, with a bigger confident smile, and his right thumb is flicked upward with no coin on it.
```
Aggiunte al negative: `coin, both eyes closed, distorted pin`

### Occhi chiusi · da K4, K5, K7 e K9 (K6-v1)

**Riferimenti:** ogni volta una sola immagine da modificare, senza Element: K4, K5, K7 oppure `kling/K9 (era K6-v1).png`.

Lo stesso prompt per tutte e quattro, ognuna partendo dalla sua immagine. Chiamale K4-occhi, K5-occhi, K7-occhi e K9-occhi.

```
Keep absolutely everything unchanged: the same squirrel, the same pose, the same expression, the same outfit and lapel pin, the same background, the same lighting and the same framing. Modify only his eyes: both eyes are gently closed, as in the middle of a natural blink, eyelids relaxed.
```
Aggiunte al negative: `changed expression, open eyes, squinting`

---

## Le clip video (Image to Video, 3 s)

Per questo reel ne facciamo due: **V1** (apertura, i primi secondi decidono se la gente resta) e **V11** (finale). V11 la riuso alla fine di ogni reel, quindi si paga una volta sola. Fai comunque K1b e K11b: se una clip non viene, non la rifacciamo e uso la variante ferma. V8, V9, V4 e V6 restano qui per un reel con più budget; in questo le sostituisco con le varianti e le mie animazioni.

Il prompt descrive solo il movimento: la scena la prende dall'immagine.

### V1 · da K1 corretto (inquadratura 1)

**Riferimenti:** primo fotogramma `kling/K1.png`; ultimo fotogramma K1b, se Kling te lo fa mettere senza costi in più.

```
Static locked-off camera, no zoom, no camera movement. Mezzo slowly tilts the open empty wallet toward himself and glances down into it, then raises his eyes back to the lens and lifts one eyebrow with a flat, unimpressed expression. Subtle natural motion: his ears twitch once, his whiskers move as he breathes, the tail sways gently. The bedroom background stays still. Keep his face, fur, outfit, lapel pin and the empty wallet identical to the start frame.
```
Aggiunte al negative: `money appearing, cards, talking`

### V4 · da K4 (inquadratura 5)

**Riferimenti:** primo fotogramma K4.

```
Static locked-off camera, no zoom, no camera movement. Mezzo places his paws on the three ivory envelopes and slides them a few centimeters forward toward the camera, keeping them in a neat row, then looks up into the lens with a small confident smile. The coins, the lamp and the room stay still. Keep his face, fur, outfit and the three envelopes identical to the start frame.
```
Aggiunte al negative: `writing on envelopes, envelopes opening, extra envelopes`

### V6 · da K6 (inquadratura 12)

**Riferimenti:** primo fotogramma K6.

```
Static locked-off camera, no zoom, no camera movement. Mezzo takes a small bite of the pizza slice and chews with his eyes half closed in pure enjoyment and a happy smile, the concert ticket stays between the fingers of his other paw. In the background the string lights twinkle softly and the blurred people move slowly. Keep his face, fur and outfit identical to the start frame.
```
Aggiunte al negative: `text on the ticket, extra pizza, melting face`

### V8 · da K8, cioè K5-v1 (inquadratura 14)

**Riferimenti:** primo fotogramma `kling/K8 (era K5-v1).png`.

```
Static locked-off camera, no zoom, no camera movement. Mezzo lets go of the gold coin: it drops into the hollow of the trunk and lands on the stacked coins with a small bounce, the warm golden glow inside the hollow brightens slightly and lights his face, and he gives a small satisfied nod. Two or three autumn leaves drift slowly down through the light. Keep his face, fur, outfit and the tree identical to the start frame.
```
Aggiunte al negative: `coins multiplying, coins flying out, engraved coins`

### V9 · da K9, cioè K6-v1 (inquadratura 17)

**Riferimenti:** primo fotogramma `kling/K9 (era K6-v1).png`.

```
Static locked-off camera, no zoom, no camera movement. Mezzo keeps his right arm extended, pointing at the blank board, and gives two small confident nods toward the camera, tapping the air once with his pointing finger. His ears and whiskers move naturally and the tail sways slightly. The board stays perfectly blank, flat and still, with nothing written on it. Keep his face, fur, outfit and the room identical to the start frame.
```
Aggiunte al negative: `writing on the board, letters, numbers, chart, arm moving away from the board`

### V11 · da K11 (inquadratura 20)

**Riferimenti:** primo fotogramma K11; ultimo fotogramma K11b, se Kling te lo fa mettere senza costi in più.

```
Static locked-off camera, no zoom, no camera movement. Mezzo winks at the camera with his left eye and flicks the gold coin upward with his thumb: the coin spins up through the warm rim light and leaves the top of the frame, and he follows it with his eyes and smiles. The plain bordeaux backdrop stays still. Keep his face, fur, outfit and lapel pin identical to the start frame.
```
Aggiunte al negative: `extra coins, engraved coin, both eyes closed, talking`

---

## Cosa mandarmi

- Le immagini chiamate K1, K2, K3, K4, K5, K6, K7, K10 e K11, alla risoluzione massima. Basta la versione migliore di ognuna.
- Le varianti chiamate K1b, K6b, K8b, K11b, K4-occhi, K5-occhi, K7-occhi e K9-occhi.
- Le clip V1 e V11, in MP4 alla qualità massima.
- Se una clip ha un difetto solo in un tratto (una mano strana a metà, per esempio), mandamela lo stesso: spesso mi basta un pezzo di 2 secondi.
