# Victoria General Cleaning

Paleta em `victoria-general.palette`, que é o arquivo que o motor lê. Este aqui
documenta as decisões.

## Cores oficiais, fornecidas pela marca

| Cor | Hex | Papel atribuído |
|-----|-----|-----------------|
| Azul claro | `#60DBFD` | `PRIMARY`, acento principal e elemento herói |
| Rosa claro | `#FEADFF` | `SECONDARY`, destaque suave |
| Magenta | `#FF30C8` | `SIGNAL`, custo, risco e prazo |
| Branco | `#FFFFFF` | `BASE`, fundo |

Esta paleta cobre quatro dos seis papéis sozinha, e o magenta `#FF30C8` é um sinal de
alerta excelente: saturado, quente e impossível de ignorar em miniatura. Melhor
encaixe que a da Sharon Maid.

## Tokens derivados, precisam da sua aprovação

| Token | Hex proposto | De onde veio |
|-------|--------------|--------------|
| `INK` | `#1B1140` | quase-preto violeta profundo, derivado do eixo magenta-azul da marca. Um preto neutro brigaria com o magenta; este assenta embaixo dele. |
| `NEUTRAL` | `#A9B4C2` | cinza frio puxando para o azul, para não competir com o rosa nem esfriar demais. |

## Caráter visual

Magenta com azul elétrico lê como energia e contemporaneidade. Aguenta conteúdo mais
assertivo, com número grande e afirmação direta, melhor que a Sharon Maid.

## Campos a preencher

- **Cidade e raio de atendimento:** TODO
- **Legenda padrão:** TODO
- **Link:** TODO

---

## Questão em aberto, e ela é estratégica

As duas empresas atendem a Flórida e o motor produz um roteiro só, porque o tom
**Documentary Utility** proíbe menção de marca dentro da narração. Isso é uma vantagem
técnica: a mesma peça se veste de qualquer uma das duas trocando um argumento.

Mas publicar a mesma peça nas duas contas, no mesmo mercado, cria dois problemas
concretos. As plataformas tratam conteúdo idêntico como duplicado e reduzem alcance de
uma das cópias. E as duas empresas passam a disputar o mesmo espectador, canibalizando
o resultado uma da outra.

Três saídas possíveis, e a escolha é sua:

1. **Dividir por serviço.** Uma fica com `moveinout` e `rental`, a outra com `powerwash`
   e `commercial`. Cada peça sai uma vez só, na marca certa.
2. **Dividir por geografia.** Se as áreas de atendimento não se sobrepõem, publicar nas
   duas é legítimo, e o gancho local muda em cada versão.
3. **Dividir por público.** Uma para residencial, outra para comercial e temporada.

Enquanto isso não for decidido, o motor produz para uma marca por vez, via `--brand`, e
não gera as duas versões automaticamente. Foi decisão deliberada: gerar as duas por
padrão facilitaria publicar duplicado sem perceber.
