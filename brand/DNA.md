# BRAND DNA

Fonte de verdade do motor. O engine lê este arquivo em toda execução.
Campos marcados `TODO` precisam ser preenchidos por você antes da primeira publicação.

---

## 1. Identidade

- **Marcas:** duas, `sharon-maid` e `victoria-general`. Cada uma tem paleta e registro
  próprios em `brand/brands/`. Tudo o mais neste arquivo é comum às duas.
- **Vertical ativa:** limpeza e manutenção predial (residencial + comercial)
- **Mercado geográfico:** Flórida, EUA. Cidade e raio de atendimento: TODO por marca
- **Idioma do conteúdo:** inglês (EUA)
- **Idioma do trabalho interno:** português

> **Nota crítica sobre geografia.** Serviço é negócio local. Uma peça com muitas
> visualizações nacionais e nenhuma na área de atendimento não gera orçamento.
> Toda peça deve ter pelo menos um gancho local: o estado, a lei estadual, a
> data do calendário local, o preço praticado na região.

### O que ser da Flórida muda no conteúdo

Legislação de referência para peças de `moveinout`: **Fla. Stat. 83.49**. Prazo de 15
dias para devolver quando não há retenção, 30 dias para notificar por escrito quando há,
perda do direito de reter se o prazo estourar, 15 dias para o inquilino contestar, e
honorários de advogado para a parte vencedora. Desde 1 de julho de 2025 a notificação
pode ir por e-mail, se as duas partes concordaram por escrito (HB 615, Fla. Stat. 83.505).

A Flórida também reordena a prioridade das tendências. Três serviços saem na frente aqui
por razões estruturais, não sazonais:

- `powerwash` — clima subtropical, mofo e limo em fachada o ano inteiro, mais temporada
  de furacões de junho a novembro. É o serviço com maior demanda recorrente do estado.
- `rental` — densidade de aluguel de temporada entre as maiores do país, turnover alto
  o ano todo em vez de concentrado no verão.
- `moveinout` — mercado de locação grande e rotativo, com influxo constante de quem
  chega de fora do estado.

Neve, isolamento térmico, preparação de inverno e degelo não existem aqui. Nunca
produzir peça sazonal de clima frio.

## 2. Serviços (categorias canônicas)

Todo conteúdo produzido deve mapear para pelo menos uma:

| ID | Serviço | Uso típico no conteúdo |
|----|---------|------------------------|
| `standard` | Standard Cleaning | recorrência, manutenção da rotina |
| `deep` | Deep Cleaning | sazonal, acúmulo, pré-evento |
| `rental` | Vacation Rental Cleaning | turnover Airbnb/VRBO, avaliação de hóspede |
| `moveinout` | Move In/Out Cleaning | caução, vistoria, fim de contrato |
| `handyman` | Handyman Services | pequenos reparos, pacotes de manutenção |
| `commercial` | Commercial Cleaning | escritório, creche, retorno presencial |
| `postconstruction` | Post Construction Cleaning | pós-obra, pós-reforma |
| `powerwash` | Power Washing | fachada, calçada, pós-tempestade |
| `windows` | Door and Window Cleaning | vidro, esquadria, trilho |
| `touchup` | Touch Up Cleaning | retoque rápido, pré-visita, pré-foto |

## 3. Público

- **Primário:** proprietário ou inquilino, 28 a 55 anos, renda média a média-alta,
  tempo é o recurso escasso, não dinheiro.
- **Secundário:** anfitrião de aluguel de temporada, síndico, gestor de escritório,
  diretor de creche, corretor de imóveis.
- **Estado mental no scroll:** não está procurando faxina. Está passando o dedo.
  A peça precisa ganhar a atenção com um custo, um prazo ou uma perda reconhecível
  nos primeiros três segundos.

## 4. Posicionamento

Somos a fonte que explica o que ninguém explica: as regras, os prazos, os preços
reais e o que a vistoria realmente checa. A prestação de serviço é a consequência
óbvia de entender o problema, nunca a mensagem principal.

## 5. Regras invioláveis

1. **A peça precisa servir sozinha.** O espectador tem que sair melhor informado
   mesmo que nunca contrate. Se o conteúdo só faz sentido como anúncio, não publica.
2. **Nada de número inventado.** Preço, data, estatística e nome de lei precisam ter
   fonte. Se o dado é incerto, reescreve a frase sem ele.
3. **Sem alarme sem remédio.** Não citamos um risco sem dar, na mesma peça, o que
   fazer a respeito.
4. **Sem menosprezo ao espectador.** Nunca "você está limpando errado". A sujeira
   nunca é culpa de quem assiste.
5. **Privacidade do cliente.** Imóvel de cliente só aparece com autorização escrita.
   Nada de rosto, endereço, correspondência, documento ou item pessoal identificável.
6. **Sem promessa de resultado garantido.** Nem de devolução de caução, nem de
   aprovação em vistoria, nem de remoção total de mancha.
7. **Sem travessão (em dash) em narração e em texto publicado.** Vírgula, dois-pontos,
   parênteses ou hífen simples. A regra existe pela cadência do TTS e vale para roteiro,
   legenda, rótulo em tela e prompt. Documentação interna deste repositório não conta.
8. **Não saia da sua competência.** Só produzimos sobre o que a empresa efetivamente faz.
   Lei de locação e prazo de caução: sim, porque a limpeza de saída está dentro. Lei de
   segurança estrutural, laudo de engenharia, seguro, tributo: não, mesmo quando o prazo
   é real e o gancho é bom.

   O teste: a peça descreve algo que a nossa equipe executa, ou algo que outro
   profissional executa? Se for o segundo, o único recorte aceitável é o preparo que
   antecede o trabalho dele, e a peça precisa deixar isso explícito.

   Exemplo real, agosto de 2026: a pesquisa trouxe a vistoria de marco da Fla. Stat.
   553.899, com prazo em 31 de dezembro. O prazo existe e é relevante, mas a lei é de
   segurança estrutural. O recorte aceitável é estreito: antes da vistoria, o inspetor
   precisa enxergar a superfície, e concreto coberto de mofo atrapalha. Isso é lavagem de
   fachada, que é nosso. Explicar a lei em si não é.

## 6. Papéis de cor

O motor não conhece cor, só papel. As cenas escrevem `{INK_DESC}`, `{PRIMARY_DESC}` e
afins; a marca escolhida em `--brand` resolve cada papel para nome e hex.

| Papel | Função |
|-------|--------|
| `BASE` | fundo da tela |
| `INK` | texto, traço, massa escura. Sem ele o rótulo não lê em celular. |
| `NEUTRAL` | elemento de apoio, sem peso narrativo |
| `PRIMARY` | acento de marca, elemento herói |
| `SECONDARY` | destaque suave |
| `SIGNAL` | **somente** custo, risco, prazo vencendo |

Regra de uso: `SIGNAL` nunca decora. Se aparecer em todo beat, perde a função e o
espectador para de notar o beat que importa.

Valores em `brand/brands/<marca>.palette`. Trocar um hex ali regenera todos os prompts
sem tocar em nenhuma cena.

## 7. Formatos e proporções

| Destino | Proporção | Duração alvo |
|---------|-----------|--------------|
| TikTok, Reels, Shorts | `9:16` (padrão) | 30 a 60 s |
| YouTube longo, site | `16:9` | 2 a 5 min |
| Carrossel Instagram | `4:5` | estático |

Padrão do motor: `9:16`, 60 segundos. Sobrescreva com `--ratio` e a duração.

## 8. Chamada para ação

Não existe CTA dentro da narração. O CTA vive na legenda do post e no perfil.

- **Legenda padrão:** TODO (uma linha, sem urgência falsa)
- **Link:** TODO

## 9. Trilhos de produção

O motor não serve para tudo. Dois trilhos:

- **Trilho A, motion design (este motor).** Conteúdo sem filmagem possível: leis,
  prazos, números, sazonalidade, comparativos, explicações de processo.
  Aproximadamente 30 por cento do volume.
- **Trilho B, filmagem real.** Antes e depois, demonstração de produto, bastidor,
  equipe. Aproximadamente 70 por cento do volume. O motor gera o roteiro de
  gravação, não imagem. Ver `brand/styles/real-footage.md`.

Escolher o trilho errado é o erro mais caro. Gadget viral, mancha, resultado de
lavagem: filmagem. Lei, prazo, preço, calendário: motion design.
