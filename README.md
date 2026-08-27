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
/content-engine                          # interativo, mostra o índice de tendências
/content-engine co-deposit-rule-2026     # entra direto num tópico, por slug
/content-engine <slug> --style real-footage
/content-engine <slug> --ratio 16:9      # YouTube longo
/content-engine --auto                   # sem paradas, para execução agendada
```

O tópico é sempre um **slug** do índice de `trends/`, nunca texto livre. O slug resolve
para um registro com serviço, trilho, evidência, gancho local e fontes. O contexto mora
no arquivo committado, não na frase digitada, que é o que impede um tema ambíguo de
virar peça errada.

## Ligar a rotina de pesquisa

A pesquisa roda na nuvem e escreve em `trends/` pelo conector GitHub MCP, porque o
seletor de repositório tem bug conhecido com conta pessoal. A produção roda local, onde
a skill e os arquivos estão. Configuração em
[`docs/routine-setup.md`](docs/routine-setup.md).

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
# timecodes cumulativos a 2,5 palavras por segundo
python3 tools/beats.py output/<slug>/beats.txt

# monta o .txt de prompts resolvendo os papéis de cor pela marca escolhida
python3 tools/build_prompts.py output/<slug>/scenes.txt --brand sharon-maid \
  > output/<slug>/prompts-sharon-maid.txt
```

## Piloto

`output/fl-deposit-deadline-2026/` é a peça de referência: o prazo de caução da Flórida
sob a Fla. Stat. 83.49, 60 segundos, 27 beats, 150 palavras. Um roteiro só, dois jogos
de prompts, um por marca. Serve para medir custo e tempo reais de ponta a ponta antes
de industrializar.

`output/co-deposit-rule-2026/` é a versão do Colorado, escrita antes do mercado ser
definido. Fica como modelo de estrutura, marcada como não publicável.

## Duas marcas

`sharon-maid` e `victoria-general`. O roteiro é comum às duas, porque o tom proíbe
menção de marca dentro da narração. Só a pele visual muda, via `--brand`.

O motor **não** gera as duas versões de uma vez, de propósito. Publicar a mesma peça
nas duas contas no mesmo mercado derruba o alcance de uma das cópias e faz as empresas
disputarem o mesmo espectador. A divisão editorial entre elas está em aberto e está
descrita no fim de `brand/brands/victoria-general.md`.

## Antes da primeira publicação

Preencher os `TODO`: cidade e raio de atendimento e legenda padrão, em cada arquivo de
`brand/brands/`. Os tokens derivados da Sharon Maid (`INK` e `SIGNAL`) estão aprovados como
solução provisória. A Victoria usa cores reais observadas no material publicado.

## Roadmap

Segunda vertical (Meu Shop Favorito, produtos de afiliado) só depois da validação
desta. O motor foi construído com o DNA separado da máquina de estados justamente
para que a troca de vertical seja troca de arquivo, não reescrita.
