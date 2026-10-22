# Prompt Kling · Mezzo e le scene del reel 01

E1 è approvata: [E1-figura-intera.png](kling/E1-figura-intera.png). Da qui in poi Mezzo deve restare identico: stessa testa, stessi ciuffi sulle orecchie, stesso pelo, stessi vestiti.

## Come impostare Kling

- **Modello:** Kling IMAGE 3.0, 4 immagini per generazione, risoluzione massima.
- **Formato:** sceglilo nelle impostazioni di Kling, non basta scriverlo nel prompt. E1 è uscita 16:9 perché il formato non era selezionato. Usa **3:4** per E2-E4 e **9:16** per K1-K7.
- **Riferimenti:** se c'è un cursore di somiglianza o di forza del riferimento, alzalo verso il massimo per il personaggio.
- **Negative:** il prompt negativo comune è in fondo. Ogni prompt ha anche delle aggiunte sue.
- **Lunghezza:** i prompt sono lunghi apposta. Se Kling ne taglia uno, togli prima la frase di stile finale, che è la parte meno importante.

## Quali immagini mettere come riferimento

| Immagine | Riferimento 1 | Riferimento 2 |
|---|---|---|
| E2 · tre quarti | E1-figura-intera.png | mezzeuro-spilla-riferimento.png |
| E3 · profilo | E1-figura-intera.png | nessuno |
| E4 · primo piano | E1-figura-intera.png | mezzeuro-spilla-riferimento.png |
| Element "Mezzo" | E1 principale, poi E2, E3, E4 | nessuno |
| K1-K7 · scene | Element "Mezzo" | nessuno |

Se nella modalità immagine non riesci a usare l'Element, carica E1 ed E4 insieme come riferimenti del personaggio. La spilla col logo serve solo dove si vede da vicino: nelle scene la ricompongo io in post con il logo vero.

**Ordine:** prima E2, E3 ed E4, poi crei l'Element, poi le scene del test (K1, K5, K6). Le altre scene le fai solo se decidiamo di fare tutto il reel.

---

## E2 · Tre quarti (3:4)

```
Full-body shot, eye level, 85mm lens, character centered with generous empty space around him. Mezzo, the anthropomorphic Eurasian red squirrel from the reference image, photorealistic, standing upright on his hind legs with exactly the same proportions as the reference: slightly large rounded head, tall pointed ears ending in long russet ear tufts, long fine white whiskers, round glossy black eyes, small pink nose, cream-white muzzle and chest, rich russet-orange fur, small furry paws with slim fingers, and a huge bushy russet tail. He wears a tailored deep bordeaux wool blazer with notch lapels, two dark buttons and patch pockets, a plain ivory crew-neck t-shirt, charcoal wool trousers with a small turn-up, small clean white leather sneakers, and a small round bordeaux enamel pin with a thin gold rim on his left lapel, like the second reference image. Pose: body turned 45 degrees toward the right side of the frame, head turned back to the camera, looking into the lens with a friendly confident half-smile, paws relaxed by his sides, the tail rising behind his back in a big soft S-curve, fully visible. Same seamless warm ivory fabric backdrop with soft folds as the reference, soft contact shadow under the sneakers. Soft key light from the front left, warm rim light outlining the fur. Keep the face, fur color, ear tufts, proportions, outfit and lapel pin identical to the reference image. Photorealistic cinematic still, fine individual fur hairs, visible wool weave, natural squirrel anatomy, warm palette of deep bordeaux red, warm ivory and muted antique gold, subtle film grain.
```
Aggiunte al negative: `different outfit, cropped tail, cropped feet`

## E3 · Profilo (3:4)

```
Full-body shot, eye level, 85mm lens, character centered. Mezzo, the anthropomorphic Eurasian red squirrel from the reference image, photorealistic, standing upright on his hind legs with exactly the same proportions as the reference: slightly large rounded head, tall pointed ears ending in long russet ear tufts, long fine white whiskers, round glossy black eyes, small pink nose, cream-white muzzle and chest, rich russet-orange fur and a huge bushy russet tail. He wears the same tailored deep bordeaux wool blazer, plain ivory crew-neck t-shirt, charcoal wool trousers with a small turn-up and small clean white leather sneakers. Pose: perfect side profile facing the left edge of the frame, standing straight and calm, one foot slightly ahead of the other, paws relaxed, chin slightly up with a subtle confident smile. The profile clearly shows the shape of the muzzle, the whiskers, the ear tufts and the side seam and patch pocket of the blazer. The tail rises from behind his back in a tall S-curve, fully inside the frame. Same seamless warm ivory fabric backdrop with soft folds as the reference, soft contact shadow under the sneakers. Soft key light from the left, warm rim light along his back and tail. Keep the face, fur color, ear tufts, proportions and outfit identical to the reference image. Photorealistic cinematic still, fine individual fur hairs, visible wool weave, natural squirrel anatomy, warm palette of deep bordeaux red, warm ivory and muted antique gold, subtle film grain.
```
Aggiunte al negative: `three-quarter view, looking at camera, cropped tail`

## E4 · Primo piano (3:4)

```
Close-up portrait, head and shoulders, eye level, 100mm portrait lens at f/2.8. Mezzo, the anthropomorphic Eurasian red squirrel from the first reference image, photorealistic, with exactly the same face: slightly large rounded head, tall pointed ears ending in long russet ear tufts fully inside the frame, long fine white whiskers in sharp focus, round glossy black eyes with a small warm catchlight, small pink nose, cream-white muzzle and throat, rich russet-orange fur with individual hairs visible on the cheeks and forehead. He looks straight into the lens with a confident closed-mouth half-smile and one brow slightly raised, like a big brother about to explain something. Visible at the bottom of the frame: the collar of the plain ivory crew-neck t-shirt, the notch lapels of the deep bordeaux wool blazer, and on his left lapel the round bordeaux enamel pin with a gold rim, the ivory letter m and two thin gold horizontal bars, exactly like the second reference image, in focus. Background: the same warm ivory fabric backdrop, softly out of focus. Soft key light from the front left, gentle warm rim light on the ears and the top of the head. Keep the face, fur color, ear tufts and outfit identical to the first reference image. Photorealistic cinematic portrait, fine individual fur hairs, visible wool weave, warm palette of deep bordeaux red, warm ivory and muted antique gold, subtle film grain.
```
Aggiunte al negative: `open mouth, teeth, cropped ears, distorted pin`

## Creare l'Element

In Kling: Elements, nuovo Element dalle immagini. Carica E1 come immagine principale ed E2, E3 ed E4 come viste aggiuntive. Nome: `Mezzo`. Descrizione:

```
Mezzo, a photorealistic anthropomorphic Eurasian red squirrel standing upright on his hind legs, slightly large rounded head, tall ears with long russet tufts, long white whiskers, round glossy black eyes, cream-white muzzle and chest, russet-orange fur, huge bushy tail. Wears a tailored deep bordeaux wool blazer, plain ivory crew-neck t-shirt, charcoal trousers with turn-ups, white leather sneakers and a round bordeaux and gold lapel pin.
```

---

## Le scene (9:16, riferimento: Element "Mezzo")

Ogni scena lascia libere le zone dove vanno i sottotitoli e l'interfaccia di Instagram: niente di importante nel 10% in alto e nel 20% in basso, sottotitoli intorno al 60-65% dell'altezza.

### K1 · Hook, il portafoglio vuoto · TEST (scena 1)

```
Medium close-up from the waist up, very slightly low angle, 50mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, round bordeaux and gold lapel pin). He stands in a small cozy Italian student bedroom at dusk and holds an open brown leather bifold wallet with both paws at chest height, tilted toward the camera so we clearly see it is completely empty inside: no cards, no banknotes, no coins. He looks straight into the lens with one brow raised and a flat, unimpressed, slightly ironic expression, ears upright, whiskers forward. Background softly out of focus: a wall painted deep bordeaux, a single bed with rumpled ivory linen, a small brass bedside lamp switched on, a plain paper wall calendar with blank pages, a window on the right with cool blue evening light. Composition: his eyes about one third from the top of the frame, the wallet in the center, the lower quarter calm and uncluttered, nothing important in the top tenth. Lighting: warm tungsten key light from the lamp on the left, cool blue window fill from the right, soft warm rim light on the fur. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, fine individual fur hairs, visible wool and leather texture, palette of deep bordeaux red, warm ivory and muted antique gold, shallow depth of field, subtle film grain.
```
Aggiunte al negative: `money in the wallet, credit cards, numbers on the calendar, smiling`

### K5 · Risparmio, l'albero delle monete · TEST (scena 6)

```
Medium shot, three-quarter view from his left side, eye level, 50mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, charcoal trousers, round bordeaux and gold lapel pin). He stands next to a huge old oak trunk in an autumn forest at golden hour. In the trunk, at the height of his chest, there is a round natural hollow, and inside it dozens of plain smooth gold coins are neatly stacked in small piles, glowing softly. With his right paw he holds a single plain gold coin between thumb and finger, just above the opening, about to drop it in. He looks at the coin with a calm, quietly satisfied smile, ears relaxed, tail curled up behind him. A few bordeaux and amber leaves drift through the air, the forest floor is covered in fallen leaves. Composition: Mezzo in the left half with his head about one third from the top, the trunk and the hollow filling the right third, the bottom fifth simple and dark with leaves. Lighting: low golden sun backlighting through the trees, warm gold light bouncing from the coins onto his face, paws and blazer, gentle haze between the trunks. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, fine individual fur hairs, rough oak bark texture, palette of deep bordeaux red, warm ivory and muted antique gold, shallow depth of field, subtle film grain.
```
Aggiunte al negative: `engraved coins, euro symbols, letters on coins, acorns, overflowing pile`

### K6 · Esempio, la lavagna vuota · TEST (scena 7)

```
Full-body shot, straight-on eye level, 35mm lens, symmetrical one-point perspective, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, charcoal trousers, white leather sneakers, round bordeaux and gold lapel pin). He stands on the left side of a small elegant study room and points with his right arm fully extended and one finger toward a large blank board on the wall to his right. He looks at the camera with a confident, friendly expression, mouth slightly open as if explaining something. The board is a large matte warm ivory rectangle, completely empty, with no lines, no writing and no marks, perfectly flat and parallel to the camera with no perspective distortion, framed by a thin oak frame, occupying the right two thirds of the frame width, from about 20% to 60% of the frame height. The wall is painted deep bordeaux, the floor is warm oak parquet, a low wooden bench sits at the bottom edge of the frame. Lighting: soft even daylight from a window on the left, gentle warm rim light on his fur, the board evenly lit without reflections. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, fine individual fur hairs, visible wool weave, palette of deep bordeaux red, warm ivory and muted antique gold, subtle film grain.
```
Aggiunte al negative: `writing on the board, chalk marks, glare on the board, tilted board, charts`

---

## Le altre scene (solo se facciamo tutto il reel)

### K1b · Problema, "allarga le braccia" (scena 2)

```
Medium full shot from the knees up, eye level, 35mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, charcoal trousers, round bordeaux and gold lapel pin). Same small cozy Italian student bedroom at dusk as before: deep bordeaux wall, single bed with ivory linen, brass bedside lamp switched on, window with cool blue evening light. He shrugs with both arms open and palms up, an empty brown leather wallet hanging open from his left paw, eyebrows raised and a resigned half-smile, as if saying "what can you do". The tail rises behind him in a soft curve. Composition: his head about one third from the top, empty wall space above and to the right of him for falling coins added later, lower fifth calm. Lighting: warm tungsten key from the lamp on the left, cool blue fill from the window, soft warm rim light. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, palette of deep bordeaux red, warm ivory and muted antique gold, shallow depth of field, subtle film grain.
```
Aggiunte al negative: `money, coins, cards`

### K2 · Le tre buste (scena 3)

```
Medium shot from a slightly high angle, three-quarter view, 50mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, round bordeaux and gold lapel pin). He sits at a tidy dark walnut desk and, with both paws, lines up three plain ivory paper envelopes side by side in front of him, perfectly spaced, flaps closed. Next to the envelopes, a small neat stack of plain gold coins. He looks down at the envelopes with a focused, organized expression. Room: deep bordeaux wall, a single brass desk lamp casting a warm circle of light on the desk, a closed notebook and a pen at the edge. Composition: his head in the upper third, the three envelopes clearly readable in the center of the frame, the bottom fifth taken by the dark front edge of the desk. Lighting: warm desk lamp as key light from above left, soft dark falloff in the room, warm rim light on the fur. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, paper and wood texture, palette of deep bordeaux red, warm ivory and muted antique gold, shallow depth of field, subtle film grain.
```
Aggiunte al negative: `writing on envelopes, stamps, open envelopes, banknotes`

### K3 · Bisogni, la spesa sulle scale (scena 4)

```
Full-body shot, low angle looking up the staircase, 28mm lens, strong vertical composition. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, charcoal trousers, white leather sneakers, round bordeaux and gold lapel pin). He climbs the worn stone stairs of an old Italian apartment building, one foot on the next step, carrying a brown paper grocery bag in his left arm with a baguette and fresh leeks sticking out, a small set of keys dangling from his right paw. Expression: a little tired but composed, looking up toward the next landing. Setting: grey stone steps, a black wrought-iron railing with simple curls, ivory plaster walls with a deep bordeaux wooden apartment door on the landing above, a tall window letting in soft afternoon daylight. Composition: Mezzo in the center of the frame, the staircase rising diagonally toward the top, the bottom fifth simple steps. Lighting: soft daylight from the window above right, gentle bounce on the stone, warm rim light on the tail. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, stone and paper texture, palette of deep bordeaux red, warm ivory and muted antique gold, subtle film grain.
```
Aggiunte al negative: `labels on products, brand logos, text on the bag`

### K4 · Desideri, pizza e concerto (scena 5)

```
Medium shot from the waist up, eye level, 50mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, round bordeaux and gold lapel pin). He stands on a lively narrow Italian street at night outside a small pizzeria, holding a folded slice of margherita pizza in his right paw, a bite already taken, and a plain paper concert ticket between two fingers of his left paw. His eyes are half closed in pure enjoyment, a big content smile, ears relaxed. Background softly out of focus: warm string lights crossing above the street, the pizzeria window glowing warm, the blurred silhouettes of young people chatting, cobblestones. Composition: his head about one third from the top, the pizza slice and ticket clearly visible at chest height, lower fifth soft bokeh. Lighting: warm glow from the pizzeria and string lights as key from the right, cool blue night ambience on the left, warm rim light on the fur. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, palette of deep bordeaux red, warm ivory and muted antique gold, shallow depth of field with round bokeh, subtle film grain.
```
Aggiunte al negative: `text on the ticket, shop sign lettering, logos, crowd faces in focus`

### K7 · Chiusura, occhiolino e moneta (scena 9)

```
Medium shot from the waist up, eye level, 85mm lens, vertical frame. Mezzo, the red squirrel from the reference (same face, long russet ear tufts, white whiskers, russet fur, cream chest, huge bushy tail, deep bordeaux wool blazer, ivory crew-neck t-shirt, round bordeaux and gold lapel pin). He winks at the viewer with his left eye and a confident half-smile, and flips a single plain smooth gold coin into the air with the thumb of his right paw; the coin floats just above his paw, slightly motion-blurred, catching the light. His tail curls up behind his shoulder. Background: a plain seamless deep bordeaux studio backdrop with a soft lighter glow behind him, no objects. Composition: his head in the center of the frame at about 45% height, the upper third of the frame completely empty for the logo, lower fifth plain backdrop. Lighting: soft key light from the front left, strong warm golden rim light outlining his ears, whiskers and tail, a small highlight on the coin. Photorealistic cinematic still, same rendering style, fur detail and color grade as the reference, fine individual fur hairs, visible wool weave, palette of deep bordeaux red, warm ivory and muted antique gold, subtle film grain.
```
Aggiunte al negative: `engraved coin, euro symbol, letters, both eyes closed, props`

---

## Negative comune (tutte le immagini)

```
cartoon, illustration, anime, plush toy, human hands, extra fingers, deformed paws, extra tail, text, letters, watermark
```

## Cosa mandarmi

- E2, E3 ed E4: la versione migliore di ciascuna, così controllo che Mezzo sia coerente prima che tu crei l'Element.
- Le scene, chiamate K1, K5, K6 e così via, alla risoluzione massima e senza scritte.
