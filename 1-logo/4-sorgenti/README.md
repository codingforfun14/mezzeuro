# mezzeuro — logo sources

Sources for the mezzeuro logo kit. The delivered kit is in [`../1-logo/`](../1-logo/LEGGIMI.md); the project overview
is in [`../LEGGIMI.md`](../LEGGIMI.md).

## History

- Round 1 concepts, greyscale: [`mezzeuro-concepts.png`](mezzeuro-concepts.png). They are A · La valuta, B · La colonna and C · Il conio.
  The SVGs in `concepts/` were outlined from macOS Bodoni 72 and are exploration only. Don't use them as artwork.
- On Oct 16 2026 the client picked **A · La valuta**, with Bodoni Moda (OFL) and the bordeaux + gold palette.

## Layout

- `build/` — generators. Run from the `MEZZEURO` folder:
  - `python3 4-sorgenti/build/kit.py all` — masters, social, web, PNG, PDF into `1-logo/`
  - `python3 4-sorgenti/build/guide.py` — one-page guide into `1-logo/guida/`
  - `cd 1-logo/presentazione && python3 ../../4-sorgenti/build/board_it.py spec.json -o mezzeuro-presentazione.html --png-dir slide`
  - `ctpaths.swift` outlines fonts via CoreText and is compiled on first use into `build/.cache/`. Needs macOS with Xcode command line tools.
  - The kit needs the logo-design skill in `~/.claude/skills/logo-design` (render, export and board scripts).
- `fonts/BodoniModa-VF.ttf` + `OFL.txt` — from github.com/google/fonts (ofl/bodonimoda). Instances: symbol 600/opsz 18,
  reversed 580/18, small cut 680/10, wordmark 560/24.
- `concepts/`, `renders/`, `exploration/` — round-1 work, type studies, avatar and icon tests.
