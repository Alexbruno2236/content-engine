# Ligar a rotina de pesquisa ao motor

A rotina diária pesquisa bem, mas o resultado morre com o container. Este documento
resolve isso.

O diagnóstico original: skill de projeto só carrega do repositório clonado, e a rotina
não tinha repositório. Mas para a **pesquisa** isso é secundário. Ela não precisa do
motor, precisa escrever um arquivo. Quem precisa do motor é a produção, e essa roda
local de qualquer forma.

---

## O bug do seletor

Repositório de conta pessoal não aparece em **Select a repository**, mesmo com o Claude
GitHub App em "All repositories". Confirmado nesta conta depois de `/login` e
`/web-setup`: o seletor continua listando só dois repositórios antigos.

- [#18467](https://github.com/anthropics/claude-code/issues/18467), **aberta**, sem
  resposta da Anthropic
- [#12839](https://github.com/anthropics/claude-code/issues/12839) e
  [#27155](https://github.com/anthropics/claude-code/issues/27155), fechadas como
  duplicatas

É indexação no backend. Reinstalar o App não resolve, já foi tentado por outros.

---

## A arquitetura escolhida

```
NUVEM, 9h                              LOCAL, quando você quiser
┌──────────────────────────┐          ┌──────────────────────────────┐
│ rotina de pesquisa       │          │ F:\content-engine            │
│  ├ WebSearch             │          │  /content-engine <slug>      │
│  ├ lê o repo via MCP     │          │   ├ máquina de estados       │
│  ├ escreve trends/<data> │  ──PR──▶ │   ├ aprovação por etapa      │
│  ├ abre PR               │          │   └ output/<slug>/           │
│  └ notifica o celular    │          │  git push                    │
└──────────────────────────┘          └──────────────────────────────┘
   roda com o PC desligado               precisa de você presente
```

A divisão não é contorno, é a natureza de cada etapa. Pesquisa é desatendida e se
beneficia de rodar sem a máquina. Produção afirma lei e valor em dólar, e decide gasto
de geração de imagem, então precisa de revisão humana etapa por etapa.

O slug é a costura entre as duas. A rotina cria com registro completo e fontes, você
digita, o motor resolve de volta.

---

## Configurar a rotina de nuvem

Não precisa criar task nova. Editar a existente em https://claude.ai/code/routines.

### 1. Conector

Em **Connectors**, garantir que **GitHub MCP** está na lista. Autenticar antes com
`/mcp` no CLI local, se ainda não estiver conectado.

Remover os conectores que a rotina não usa. A documentação é direta sobre isso: Claude
pode usar qualquer ferramenta de um conector incluído, incluindo escrita, sem pedir
permissão durante a execução.

### 2. Instruções

Substituir o conteúdo de **Instructions** por:

```
Pesquise tendências de busca, comportamento e conteúdo nos Estados Unidos ligadas a
serviços de limpeza profissional e manutenção predial, cobrindo Google Trends, Reddit,
TikTok, Instagram, YouTube e a sazonalidade da semana corrente. O mercado atendido é a
Flórida.

O repositório de destino é Alexbruno2236/content-engine. Você NÃO tem clone local dele.
Use o conector GitHub MCP para ler e escrever.

Antes de pesquisar, leia por MCP:
- o arquivo mais recente de trends/, para reaproveitar os slugs que já existem
- queue.md, para não repetir o que já foi produzido
- brand/DNA.md, para os IDs canônicos de serviço e o contexto de mercado

Escreva o resultado em trends/<AAAA-MM-DD>.md seguindo exatamente o formato de
trends/2026-08-27.md: um índice em tabela no topo e um registro por tópico abaixo.

Cada tópico precisa de:
- slug estável em kebab-case, reutilizável entre dias
- serviço, com os IDs canônicos de brand/DNA.md
- trilho A (motion design) ou B (filmagem real). Se envolve sujeira real, é sempre B.
- evidência concreta, com número, data ou citação
- gancho local da Flórida
- janela de validade
- fontes com URL

Reaproveite o slug quando o tópico já existir em arquivo anterior. Nunca crie slug novo
para tópico já registrado, porque é o slug que liga a pesquisa à produção.

Nunca afirme número, data ou nome de lei sem fonte verificada. Dado incerto sai do texto.

Crie a branch trends/<AAAA-MM-DD> e abra PR contra main, pelo conector.

Notifique apenas se houver tendência nova com janela expirando em menos de duas semanas,
ou se a pesquisa ou a escrita falharem. Dia sem novidade não gera notificação.

Se o conector não conseguir escrever no repositório, não invente e não tente contornar:
devolva o conteúdo completo do arquivo na notificação e diga que a escrita falhou.
```

### 3. Verificar

**Run now**, e conferir se o PR aparece no repositório.

Atenção ao aviso da documentação: status verde significa que a sessão iniciou e terminou
sem erro de infraestrutura, não que a tarefa deu certo. Abrir a execução e ler.

### O que mudou em relação ao prompt antigo

O anterior pedia pesquisa e devolvia texto no chat. Este lê o estado do projeto antes de
pesquisar, escreve no formato do índice, reaproveita slug, exige fonte, abre PR e só
notifica quando há algo acionável. E degrada com elegância se o conector falhar, em vez
de fingir que escreveu.

---

## Se o conector não conseguir escrever

Aí sim vale a rotina local, e nesse caso é task nova: não dá para converter uma de
nuvem em local.

No app Desktop, aba **Code** → **Routines** → **New routine** → **Local**. Pasta de
trabalho `F:\content-engine`, e o mesmo prompt acima sem a parte de MCP, já que
localmente os arquivos estão em disco.

### Limitações que valem **só** para a versão local

1. A máquina precisa estar ligada com o app aberto. Se dormir no horário, a execução é
   pulada. O Desktop faz **uma** recuperação ao acordar, para o horário perdido mais
   recente dos últimos 7 dias, e descarta o resto. Uma semana de viagem gera uma
   pesquisa, não sete.
2. A recuperação pode disparar em horário estranho. Uma tarefa das 9h pode rodar às 23h.
   Se isso importar, o prompt precisa se defender.
3. Notificação fica no desktop, não chega no celular.
4. Só gatilho de horário, sem API e sem evento do GitHub.
5. A rotina morre com o PC. O repositório no GitHub é o que impede isso de virar ponto
   único de falha do projeto.
6. Prompt de permissão trava a execução. Depois de criar, clicar em **Run now**,
   acompanhar e marcar "always allow" em cada ferramenta.

Nenhuma delas vale para a rotina de nuvem, que roda com a máquina desligada e notifica
o celular.

---

## Requisito comum

Login pela conta claude.ai, não por chave de API. Se o rodapé do CLI mostrar
**API Usage Billing** e `Not logged in`, rodar `/login`. Chave em `ANTHROPIC_API_KEY`,
`ANTHROPIC_AUTH_TOKEN` ou `apiKeyHelper` no `settings.json` tem precedência sobre a
conta e precisa sair primeiro.

## Por que a produção não vira automática

O `--auto` existe, mas produzir sem revisão é ruim aqui por dois motivos concretos: o
roteiro afirma lei e valor em dólar, onde um erro custa a credibilidade que a peça
existe para construir, e a escolha de trilho decide gasto de geração de imagem.

Rotina pesquisa e propõe. Pessoa escolhe. Motor produz.
