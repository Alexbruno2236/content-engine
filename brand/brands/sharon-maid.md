# Sharon Maid

Paleta em `sharon-maid.palette`, que é o arquivo que o motor lê. Este aqui documenta
as decisões.

## Cores oficiais, fornecidas pela marca

| Cor | Hex | Papel atribuído |
|-----|-----|-----------------|
| Turquesa | `#0ABAB5` | `PRIMARY`, acento principal e elemento herói |
| Rosa | `#FB9FDE` | `SECONDARY`, destaque suave |
| Cinza claro | `#D0CDCE` | `NEUTRAL`, elemento de apoio |

## Tokens derivados, **aprovados**

A paleta entregue não tem tom escuro nem cor de alerta. Motion design em 9:16 precisa
das duas: sem escuro, rótulo de 1 a 4 palavras não é legível em tela de celular; sem
alerta, o beat que fala de custo ou prazo perde a única marcação que o separa do resto.

| Token | Hex | De onde veio |
|-------|--------------|--------------|
| `INK` | `#0B2B2A` | quase-preto com viés de verde-azulado, derivado do turquesa oficial. Escurece sem introduzir uma família de cor nova. |
| `SIGNAL` | `#EE4FB6` | o rosa oficial `#FB9FDE` com saturação alta e luminosidade baixa, mesmo matiz. É a marca falando mais alto, não uma cor estrangeira. |

Rosa claro não funciona como sinal de alerta: ele é acolhedor, e o beat de custo precisa
de tensão. Por isso a versão profunda.

Estes dois foram aprovados em 27 de agosto de 2026 como solução provisória. Se a marca
vier a definir um escuro e um alerta oficiais, é trocar dois hex no `.palette` e todos
os prompts se regeneram sem tocar em nenhuma cena.

> **Pendência.** Ao contrário da Victoria, não temos peça publicada da Sharon Maid para
> observar. Se existir carrossel ou post dela, vale olhar antes de fechar estes valores:
> no caso da Victoria, o material publicado revelou um `INK` real melhor que o derivado.

`BASE` ficou `#FFFFFF`. O cinza claro oficial é bom como elemento, ruim como fundo de
tela inteira, porque suja o branco e reduz o contraste dos rótulos.

## Caráter visual

Turquesa com rosa lê como cuidado, limpeza e leveza. Combina com conteúdo de rotina,
manutenção e tranquilidade. É a paleta menos agressiva das duas.

## Campos a preencher

- **Cidade e raio de atendimento:** TODO
- **Legenda padrão:** TODO
- **Link:** TODO
