#!/usr/bin/env python3
"""Bloqueia a publicação enquanto houver trechos pendentes de aprovação."""
import re, sys
from pathlib import Path
raiz = Path(__file__).resolve().parent / "public"
pad = re.compile(r"data-pendente|\[confirmar|\[a definir|\[tema a definir|\[prazo")
n = 0
for p in sorted(raiz.rglob("*.html")):
    for i, l in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if pad.search(l):
            n += 1
            print(f"{p.relative_to(raiz)}:{i}")
print(f"\n{n} linhas com pendência. NÃO publicar." if n else "Sem pendências.")
sys.exit(1 if n else 0)
