TARGET: 150 palavras / 60 segundos
SERVIÇO: `powerwash`, `deep`
TRILHO: **B, filmagem real.** Não há geração de imagem nesta peça.
FORMATO: 9:16
TENDÊNCIA: `snowbird-return-exterior-reset`
MERCADO: Flórida

FONTES:
- Fla. Stat. 720.305, multa máxima de 100 dólares por dia, teto de 1.000 por violação
  contínua, 14 dias de aviso por escrito, comitê independente de no mínimo três membros
  que não sejam diretores, dirigentes, empregados ou parentes destes. Multa sem
  audiência é inexequível.
- BEBR, University of Florida, cerca de 1 milhão de residentes sazonais passam um mês ou
  mais na Flórida por ano
- Temporada de chuva da Flórida, junho a setembro

---

One hundred dollars a day. That is what a Florida HOA can fine you for algae on your roof
or mildew on your stucco. It caps at a thousand for one continuing violation. About a
million people winter in Florida and summer somewhere else. Their houses sit empty from
June through September. That is the rainy season, and the fastest growing season of the
year for anything living on an exterior surface. Nobody is there to watch it spread. But
the association cannot just send a bill. Under Florida Statute 720.305, you get fourteen
days written notice and a hearing. The fine needs a committee of three, none of them
officers or directors. A fine imposed without that hearing is unenforceable. The cheapest
version of this is the one that never starts. Clean it in September, before the flight
back. Come home to a house. Not a letter.

---

FINAL: 148 palavras · 59,2 s a 2,5 p/s · 27 beats

## Checagem contra o DNA

| Regra | Situação |
|-------|----------|
| Abertura em custo | ok, abre em "One hundred dollars a day" |
| Regra dos 60 por cento de valor | ok. A proteção processual é a parte mais útil e quase ninguém sabe dela |
| Sem alarme sem remédio | ok, a multa vem com o prazo, o comitê e o que fazer em setembro |
| Serviço mencionado no máximo uma vez | ok, zero menção. "Clean it in September" é instrução, não oferta |
| Todo número com fonte | ok, ver FONTES |
| Sem travessão | ok |
| Fechamento com 12 palavras ou menos | ok, 3 palavras |
| Sem promessa de resultado garantido | ok, não promete anular multa nem aprovar em nada |
| Gancho local | ok, estatuto estadual, temporada de chuva da Flórida, snowbird |
| Regra 8, competência | ok. A violação é sobre fachada suja e o remédio é lavagem. Isso é o serviço, não o trabalho de outro profissional. |

## Por que esta peça funciona

O espectador acha que vai ouvir sobre limpeza e ouve sobre um direito que ele tem. A
associação não pode simplesmente cobrar: ela deve 14 dias de aviso, uma audiência, e um
comitê de três pessoas que não sejam diretores nem parentes deles. Multa sem isso é
inexequível.

Quem descobre isso lembra de onde ouviu. E a conclusão de que vale limpar em setembro o
espectador tira sozinho, que é o objetivo do tom.

## Uma limitação de arquitetura que esta peça revelou

Onze dos 27 beats falam de lei, prazo e procedimento. Em motion design seriam gráficos.
Aqui viram **objeto em cena**: uma carta impressa, um calendário, um cartão de embarque.

Funciona, e até melhor, porque objeto real na mesa tem peso que vetor não tem. Mas
expõe que o motor hoje força um trilho por peça inteira, quando na prática um beat
poderia ser filmagem e o seguinte gráfico. Registrado para decidir depois. Não vale
mudar o motor por causa de uma peça.

## Produção

```bash
python3 tools/beats.py output/snowbird-return-exterior-reset/beats.txt
```

Shotlist em `shotlist.md`. Não existe `prompts.txt` nem `video-prompt.txt` nesta peça,
porque não há imagem gerada.
