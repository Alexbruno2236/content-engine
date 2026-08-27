# Content Engine

Motor de produção de conteúdo narrado para serviços de limpeza e manutenção predial.
Transforma uma tendência pesquisada numa peça de vídeo pronta para produção: roteiro,
locução, beats visuais, prompts de imagem em lote, prompt de vídeo e thumbnails.

Adaptado de um motor de documentário policial. O que sobreviveu foi o workflow (a
máquina de estados com aprovação a cada etapa). O tom e a estética foram refeitos: em
vez de colagem de papel e narração de true crime, motion design editorial e um tom
chamado **Documentary Utility**, onde a peça precisa valer sozinha mesmo que o
espectador nunca contrate o serviço.

## Uso

```bash
/content-engine                        # interativo, motion design, 9:16, padrão
/content-engine --style real-footage   # trilho de filmagem, gera shotlist
/content-engine --ratio 16:9           # YouTube longo
/content-engine --topic "..."          # pula a seleção de tendência
/content-engine --auto                 # sem paradas, para execução agendada
```

## Máquina de estados

| State | Etapa | Saída |
|-------|-------|-------|
| 0 | Carregar DNA | confirmação de uma linha |
| 1 | Tópico | tendências disponíveis, com trilho marcado |
| 2 | Dez ideias | 10 títulos com gancho concreto |
| 3 | Duração | 30 s a 5 min |
| 4 | Roteiro | `script.md` com contagem e fontes |
| 5 | Locução | mp3 ou bloco para ElevenLabs |
| 6 | Beats | `beats.md` com timecodes |
| 7 | Prompts de imagem | `<slug>-prompts.txt` para geração em lote |
| 8 | Prompt de vídeo | `video-prompt.txt` |
| 9 | Thumbnails | `thumbnails.txt` |

Cada estado para e espera aprovação. `--auto` desliga as paradas.

## Dois trilhos

**Trilho A, motion design.** Leis, prazos, números, sazonalidade, comparativos.
Cerca de 30 por cento do volume. É onde o motor gera imagem.

**Trilho B, filmagem real.** Antes e depois, demonstração, produto, bastidor.
Cerca de 70 por cento do volume. O motor gera roteiro de gravação, não imagem.

A regra é simples: se existe sujeira real envolvida, é filmagem. Geração de IA não
compete com gordura saindo de uma boca de fogão em tempo real.

## Ferramentas

```bash
python3 tools/beats.py <arquivo>   # timecodes cumulativos a 2,5 palavras por segundo
```

## Piloto

`output/co-deposit-rule-2026/` é a primeira peça completa: as novas leis de caução de
2026, 60 segundos, 26 beats. Serve para medir custo e tempo reais de ponta a ponta
antes de industrializar.

## Antes da primeira publicação

Preencher os campos `TODO` em `brand/DNA.md`: nome da empresa, mercado geográfico e
legenda padrão. O piloto usa a legislação do Colorado. Se a área de atendimento for
outro estado, o roteiro precisa ser refeito com a lei correta. A estrutura se mantém,
os números mudam.

## Roadmap

Segunda vertical (Meu Shop Favorito, produtos de afiliado) só depois da validação
desta. O motor foi construído com o DNA separado da máquina de estados justamente
para que a troca de vertical seja troca de arquivo, não reescrita.
