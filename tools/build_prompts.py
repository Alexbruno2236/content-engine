#!/usr/bin/env python3
"""Monta o .txt de prompts de imagem em lote a partir das cenas, resolvido por marca.

As cenas descrevem PAPEIS de cor, nunca valores: {INK_DESC}, {PRIMARY_DESC},
{SIGNAL_DESC}, {BASE_DESC}, {NEUTRAL_DESC}, {SECONDARY_DESC}. A marca escolhida
resolve cada papel para o nome e o hex da sua paleta. A mesma cena, portanto, gera
peca da Sharon Maid ou da Victoria General Cleaning sem reescrever uma linha.

Uso:
    python3 tools/build_prompts.py output/<slug>/scenes.txt --brand sharon-maid
    python3 tools/build_prompts.py output/<slug>/scenes.txt --brand victoria-general \\
        --style motion-design --ratio 9:16

Motivo de existir: o style block tem mais de cem palavras e o closer quase setenta.
Repetir isso a mao em 27 beats, vezes duas marcas, e onde os erros entram. Uma cor
trocada num bloco e a imagem sai de outra familia visual, e ninguem percebe ate ver
o video montado.
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STYLES_DIR = ROOT / "brand" / "styles"
BRANDS_DIR = ROOT / "brand" / "brands"

ROLES = ("BASE", "INK", "NEUTRAL", "PRIMARY", "SECONDARY", "SIGNAL")


def read_lines(path):
    with path.open(encoding="utf-8") as fh:
        return [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]


def load_palette(name):
    path = BRANDS_DIR / f"{name}.palette"
    if not path.exists():
        available = sorted(p.stem for p in BRANDS_DIR.glob("*.palette"))
        sys.exit(f"marca nao encontrada: {name}. Disponiveis: {', '.join(available)}")

    tokens = {}
    for line in read_lines(path):
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        tokens[key.strip()] = value.strip()

    missing = [f"{r}/{r}_DESC" for r in ROLES
               if r not in tokens or f"{r}_DESC" not in tokens]
    if missing:
        sys.exit(f"{path.name} nao define: {', '.join(missing)}")
    return tokens


def resolve(text, tokens, ratio):
    """Substitui {ROLE_DESC} pelo nome da cor e {ROLE} pelo hex, mais {RATIO}."""
    # _DESC primeiro: {INK} e prefixo de {INK_DESC} e comeria a substituicao.
    for role in ROLES:
        text = text.replace(f"{{{role}_DESC}}", tokens[f"{role}_DESC"])
    for role in ROLES:
        text = text.replace(f"{{{role}}}", tokens[role])
    return text.replace("{RATIO}", ratio)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("scenes", type=Path, help="arquivo com uma cena por linha")
    ap.add_argument("--brand", required=True, help="nome do arquivo em brand/brands/")
    ap.add_argument("--style", default="motion-design", help="nome do estilo em brand/styles/")
    ap.add_argument("--ratio", default="9:16", help="proporcao, substitui {RATIO}")
    args = ap.parse_args()

    style_file = STYLES_DIR / f"{args.style}.style"
    closer_file = STYLES_DIR / f"{args.style}.closer"
    for f in (args.scenes, style_file, closer_file):
        if not f.exists():
            sys.exit(f"nao encontrado: {f}")

    tokens = load_palette(args.brand)
    style = resolve(" ".join(read_lines(style_file)), tokens, args.ratio)
    closer = resolve(" ".join(read_lines(closer_file)), tokens, args.ratio)
    scenes = [resolve(s, tokens, args.ratio) for s in read_lines(args.scenes)]

    if not scenes:
        sys.exit(f"nenhuma cena em {args.scenes}")

    leftovers = {b for s in scenes + [style, closer] for b in (s,) if "{" in b}
    if leftovers:
        print("aviso: sobrou placeholder nao resolvido em algum bloco", file=sys.stderr)

    print("\n\n".join(f"{scene} {style} {closer}" for scene in scenes))
    print(f"{len(scenes)} blocos, marca {tokens['NAME']}, estilo {args.style}, {args.ratio}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
