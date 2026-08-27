# Victoria General Cleaning

Paleta em `victoria-general.palette`, que é o arquivo que o motor lê. Este aqui
documenta as decisões.

## Cores

| Cor | Hex | Papel | Origem |
|-----|-----|-------|--------|
| Azul-marinho profundo | `#001139` | `INK` | observada em uso no carrossel, é a cor do texto principal |
| Azul vívido | `#0098F4` | `PRIMARY` | observada em uso, é a ênfase secundária |
| Magenta | `#FF30C8` | `SIGNAL` | paleta oficial |
| Rosa claro | `#FEADFF` | `SECONDARY` | paleta oficial |
| Branco | `#FFFFFF` | `BASE` | paleta oficial |
| Azul-gelo | `#60DBFD` | reserva | paleta oficial, muito próximo do `#0098F4`. Usar só quando os dois azuis aparecerem juntos e precisarem se distinguir. |

**Derivado, único:** `NEUTRAL` = `#A6ACBA`, que é o próprio `#001139` clareado sobre
branco a 35 por cento. Não é cor nova, é a cor da marca em tom baixo.

Uma versão anterior deste arquivo propunha `#1B1140` como `INK`. Foi descartada: o
`#001139` real da marca faz o mesmo trabalho e é o que já está publicado.

## Sistema tipográfico observado

O carrossel revela uma gramática consistente que vale replicar nas thumbnails:

1. **Título em sans bold, `INK`.** Peso alto, caixa mista, várias linhas curtas.
2. **Uma palavra por linha em `SIGNAL`.** A palavra que carrega o gancho, nunca duas
   por linha. No exemplo: "Cat" e "Odor".
3. **Uma expressão em `PRIMARY`.** O contraponto, geralmente o que o espectador
   acredita erroneamente. No exemplo: "stain disappear" e "clean".
4. **Traço de destaque em `SIGNAL`**, feito à mão, sublinhando a expressão em `PRIMARY`.
5. **Subtexto em serifa itálica**, menor, com a mesma regra de palavra colorida.
6. **Seta desenhada em `PRIMARY`** apontando para o objeto da foto.

A hierarquia é sempre a mesma: o `INK` carrega a frase, o `SIGNAL` marca o problema, o
`PRIMARY` marca a crença equivocada. É um sistema bom e coerente.

## Diferença de formato que precisa ficar registrada

O carrossel usa **fotografia real** com tipografia por cima. O motor produz **motion
design vetorial**. São linguagens diferentes.

Isso não é um conflito, e sim uma divisão de formato: carrossel estático fica com foto,
vídeo narrado fica com vetor. Mas as duas precisam parecer da mesma casa, e o que
costura é a tipografia e o uso de cor acima, não o tipo de imagem. Por isso o sistema
foi documentado aqui.

Se você preferir que o vídeo também use fotografia, é outro estilo, e o motor suporta:
cria `brand/styles/photo-type.style` e passa `--style photo-type`. As cenas não mudam,
só o bloco de estilo.

## Tom de voz

O carrossel abre com "Cat accident? Don't just make the stain disappear." É uma pergunta
retórica, que o `narration-dna.md` proíbe na abertura de vídeo narrado.

Não é contradição. São dois contextos: no carrossel a imagem já ganhou a atenção e o
texto pode se dar ao luxo de perguntar. No vídeo, os primeiros três segundos disputam
com o polegar, e pergunta retórica é o sinal mais reconhecível de anúncio. A regra
continua valendo para narração.

O que o carrossel acerta e vale carregar para o vídeo: ele avisa de um problema que o
espectador não sabe que tem (cheiro persiste mesmo com a mancha invisível) e entrega a
informação antes de qualquer oferta. Isso é exatamente Documentary Utility.

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
