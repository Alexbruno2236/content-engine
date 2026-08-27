#!/usr/bin/env python3
"""Monta o .txt de prompts de imagem em lote a partir das cenas.

Cada cena e uma linha do arquivo de entrada, na mesma ordem dos beats. O script
anexa a cada uma o style block e o closer do estilo escolhido, produzindo blocos
autossuficientes separados por linha em branco, prontos para geracao em lote.

Uso:
    python3 tools/build_prompts.py <cenas.txt> [--style motion-design] [--ratio 9:16]
        > output/<slug>/<slug>-prompts.txt

Motivo de existir: o style block tem 119 palavras e o closer 67. Repetir isso a mao
em 27 beats e onde os erros entram, uma virgula trocada num bloco e a imagem sai de
outra familia visual. O arquivo de cenas fica legivel e revisavel; a repeticao e
mecanica e o script cuida dela.
"""
import argparse
import sys
from pathlib import Path

STYLES_DIR = Path(__file__).resolve().parent.parent / "brand" / "styles"


def read_lines(path: Path) -> list[str]:
    with path.open(encoding="utf-8") as fh:
        return [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("scenes", type=Path, help="arquivo com uma cena por linha")
    ap.add_argument("--style", default="motion-design", help="nome do estilo em brand/styles/")
    ap.add_argument("--ratio", default="9:16", help="proporcao, substitui {RATIO} no closer")
    args = ap.parse_args()

    style_file = STYLES_DIR / f"{args.style}.style"
    closer_file = STYLES_DIR / f"{args.style}.closer"

    for f in (args.scenes, style_file, closer_file):
        if not f.exists():
            print(f"nao encontrado: {f}", file=sys.stderr)
            return 1

    style = " ".join(read_lines(style_file))
    closer = " ".join(read_lines(closer_file)).replace("{RATIO}", args.ratio)
    scenes = read_lines(args.scenes)

    if not scenes:
        print(f"nenhuma cena em {args.scenes}", file=sys.stderr)
        return 1

    print("\n\n".join(f"{scene} {style} {closer}" for scene in scenes))
    print(f"{len(scenes)} blocos gerados, estilo {args.style}, {args.ratio}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
