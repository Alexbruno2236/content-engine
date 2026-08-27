#!/usr/bin/env python3
"""Calcula timecodes cumulativos de beats a 2,5 palavras por segundo.

Uso:
    python3 tools/beats.py beats.txt

Entrada: um beat por linha, texto puro. Linhas vazias e que comecam com # sao ignoradas.
Saida: tabela markdown com numero, timecode de inicio, duracao, palavras e narracao.
"""
import sys

WPS = 2.5


def timecode(seconds: float) -> str:
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{s:05.2f}"


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2

    with open(sys.argv[1], encoding="utf-8") as fh:
        beats = [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]

    print("| # | Início | Dur. | Pal. | Narração |")
    print("|---|--------|------|------|----------|")

    clock = 0.0
    total_words = 0
    for i, text in enumerate(beats, 1):
        words = len(text.split())
        dur = words / WPS
        print(f"| {i} | {timecode(clock)} | {dur:.1f}s | {words} | {text} |")
        clock += dur
        total_words += words

    print()
    print(f"**{len(beats)} beats · {total_words} palavras · {clock:.1f}s "
          f"({timecode(clock)}) a {WPS} p/s**")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
