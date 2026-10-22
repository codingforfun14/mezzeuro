"""Runs the logo-design skill's presentation_board.py with Italian labels, patched in memory (the installed
skill stays untouched).

  cd 1-logo/presentazione && python3 ../../4-sorgenti/build/board_it.py spec.json -o mezzeuro-presentazione.html --png-dir slide
"""
import os
import sys

SRC = os.path.expanduser("~/.claude/skills/logo-design/scripts/presentation_board.py")
REPL = [
    ("<b>Alex Morgan</b><br>Founder<br>alex@{handle}.com", "<b>Nome Cognome</b><br>Creator<br>@{handle}"),
    (">Business cards<", ">Biglietti da visita<"),
    (">App icon<", ">Icona app<"),
    (">Website<", ">Sito web<"),
    (">Social profile<", ">Profilo social<"),
    (">ALEX MORGAN<", ">NOME COGNOME<"),
    (">Payment card<", ">Carta di pagamento<"),
    ("{n} — Home<", "{n} — YouTube<"),
    ("https://{handle}.com", "youtube.com/@{handle}"),
    (">Browser tab<", ">Scheda del browser<"),
    (">What we heard<", ">Cosa ci hai chiesto<"),
    ("<h2>The brief</h2>", "<h2>Il brief</h2>"),
    ("{label} · in use<", "{label} · in uso<"),
    ('title = "Notes" if final', 'title = "Note" if final'),
    ("'Next steps' if final", "'Prossimi passi' if final"),
]

code = open(SRC, encoding="utf-8").read()
for old, new in REPL:
    if old not in code:
        sys.exit(f"board_it: label not found in the skill script (skill updated?): {old!r}")
    code = code.replace(old, new)
sys.argv = [SRC] + sys.argv[1:]
exec(compile(code, SRC, "exec"), {"__name__": "__main__", "__file__": SRC})
