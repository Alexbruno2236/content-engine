# CONTENT ENGINE

Motor de produção de conteúdo narrado a partir de tendências pesquisadas.
Vertical ativa: limpeza e manutenção predial (EUA).

## Como rodar

```
/content-engine                          # interativo, motion design, 9:16
/content-engine --style real-footage     # trilho de filmagem
/content-engine --ratio 16:9             # YouTube longo
/content-engine --auto                   # sem paradas, para execução agendada
```

## Estrutura

```
brand/DNA.md                  fonte de verdade: marca, serviços, público, regras
brand/narration-dna.md        tom de narração "Documentary Utility"
brand/styles/*.md             style blocks trocáveis por trilho
trends/YYYY-MM-DD.md          saída da pesquisa diária, entrada do motor
queue.md                      fila e histórico de produção
output/<slug>/                entregáveis de cada peça
.claude/skills/content-engine/SKILL.md   a máquina de estados
```

## Fluxo de ponta a ponta

1. A rotina agendada de pesquisa roda às 9h e escreve `trends/<data>.md`. Como cada
   execução agendada acontece num container efêmero e isolado, o commit neste
   repositório é o que faz a pesquisa sobreviver e chegar ao motor.
2. `/content-engine` lê o DNA e o arquivo de tendências mais recente.
3. Máquina de estados com aprovação a cada etapa: tópico, dez ideias, duração,
   roteiro, locução, beats, prompts de imagem, prompt de vídeo, thumbnails.
4. O `.txt` de prompts vai para o gerador de imagem em lote. As imagens voltam e
   recebem o prompt universal de vídeo. O editor monta contra a locução.

## Regras que não se negociam

- Sem travessão (em dash) em nenhuma saída. Quebra a cadência do TTS.
- Nenhum número, data ou lei sem fonte verificada.
- A peça precisa valer sozinha, sem a menção ao serviço.
- Sujeira real é trilho de filmagem, nunca motion design.
- Imóvel de cliente só com autorização escrita, sem nada identificável.

## Estado do projeto

Piloto de validação: tendência 2, leis de caução de 2026. Ver `output/`.
Segunda vertical prevista (Meu Shop Favorito, produtos de afiliado) só depois da
validação desta.
