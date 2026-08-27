TARGET: 150 palavras / 60 segundos
SERVIÇO: `moveinout`
ESTILO: motion-design · 9:16
TENDÊNCIA: `fl-deposit-deadline-2026`
MERCADO: Flórida

FONTES:
- Fla. Stat. 83.49, Deposit money or advance rent, duty of landlord and tenant
- CS/CS/CS/HB 615 (2025), Electronic Delivery of Notices Between Landlords and Tenants,
  cria a Fla. Stat. 83.505, vigência 1 de julho de 2025
- The Complete Lawyer, Florida Security Deposit Return Law, the 15-Day Rule
- Justia, 2025 Florida Statutes 83.49

---

Thirty days. That is how long a Florida landlord has to tell you why they are keeping
your security deposit. Miss it by one day and they forfeit the right to keep any of it.
Most tenants never check the date. The rule is Florida Statute 83.49. If the landlord is
keeping nothing, the deposit comes back within fifteen days. If they are keeping
anything, they have thirty days to send written notice. Certified mail, or email, if you
both agreed to that in writing. The notice has to name the amount and the reason. Once
you receive it, you have fifteen days to object. And if this reaches a court, the loser
pays the winner's attorney fees. That is why your photos matter as much as your
cleaning. Clean the place, then prove you did. Every room, the day you move in and the
day you leave. Same angles.

---

FINAL: 150 palavras · 60,0 s a 2,5 p/s · 27 beats

## Por que este ângulo é mais forte que o do Colorado

A peça do Colorado contava uma mudança de lei: "a regra mudou, sujeira agora é desgaste
normal". Boa, mas tem prazo de validade e só serve a quem mora lá.

Esta conta alavancagem, e alavancagem não expira. O senhorio tem prazo curto, perde o
direito inteiro se estourar, e a parte vencedora na justiça recebe honorários de
advogado da parte perdedora. Esse último fato é o mais poderoso e quase ninguém sabe:
ele transforma uma disputa de 400 dólares, que normalmente não compensa brigar, em algo
que o senhorio prefere evitar.

## Checagem contra o DNA

| Regra | Situação |
|-------|----------|
| Abertura em custo ou prazo, não em pergunta | ok, abre em "Thirty days." |
| Regra dos 60 por cento de valor utilizável | ok, praticamente 100 por cento |
| Serviço mencionado no máximo uma vez | ok, zero menção direta. A conexão é "Clean the place, then prove you did", que mantém a limpeza necessária sem virar oferta |
| Zero CTA na narração | ok, o CTA vive na legenda |
| Todo número com fonte | ok, ver FONTES |
| Sem travessão | ok |
| Fechamento com 12 palavras ou menos | ok, 2 palavras, padrão 4 |
| Sem promessa de resultado garantido | ok, descreve prazo e direito, não promete devolução |
| Gancho local | ok, Flórida no beat 2 e o estatuto estadual no beat 8 |

## Decisão editorial que vale registrar

O beat 23 equilibra foto e limpeza na mesma balança em vez de dizer que documentação
importa mais. A primeira versão dizia que um move-out documentado supera um impecável,
o que é verdade e é péssimo para quem vende limpeza. O ajuste mantém a honestidade e
não serra o galho: as duas coisas pesam igual, e é isso que a lei de fato diz.

## Produção

```bash
python3 tools/beats.py output/fl-deposit-deadline-2026/beats.txt
python3 tools/build_prompts.py output/fl-deposit-deadline-2026/scenes.txt \
  > output/fl-deposit-deadline-2026/fl-deposit-deadline-2026-prompts.txt
```
