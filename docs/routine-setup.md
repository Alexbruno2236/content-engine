# Ligar a rotina de pesquisa ao motor

Hoje a rotina diária roda sem repositório. Ela pesquisa, escreve o resultado num
container efêmero e o container morre. Nada chega ao motor.

A documentação é explícita sobre a causa:

> "Routines run autonomously as full Claude Code cloud sessions... The session can run
> shell commands, use **skills committed to the cloned repository**, and call any
> connectors you include."

Skill de projeto vem do repositório clonado. Sem repositório, não há skill. É por isso
que `/trends` e `/daily` aparecem nos chats abertos sobre o `meushopfavorito-remotion` e
não aparecem na sessão da rotina.

Não é o environment. Environment controla rede, variáveis e setup script. Repositório é
campo separado do formulário.

---

## Passo 1, dar acesso ao repositório

### O caminho oficial, que hoje está quebrado

Editar a rotina em https://claude.ai/code/routines e adicionar o repositório em
**Select repository**, o controle logo abaixo da caixa de Instructions.

**Isso pode não funcionar.** Existe bug conhecido em que repositórios de conta pessoal
não aparecem no seletor, mesmo com o Claude GitHub App instalado com acesso a todos os
repositórios. Repositório de organização aparece; pessoal não.

- [#18467](https://github.com/anthropics/claude-code/issues/18467), **aberta**, sem
  resposta da Anthropic
- [#12839](https://github.com/anthropics/claude-code/issues/12839), fechada como
  duplicata. O autor já tentou reinstalar o App e limpar cookies, sem sucesso.
- [#27155](https://github.com/anthropics/claude-code/issues/27155), fechada como
  duplicata das duas acima

É indexação no backend. Reinstalar o App não resolve.

### Contorno 1, `/web-setup`

Caminho de autenticação **diferente** do GitHub App: sincroniza o token do `gh` CLI
local com a conta Claude. Nenhuma das três issues registra ter testado.

```bash
gh auth status          # precisa estar autenticado
claude                  # no terminal local
/web-setup
```

Depois reabrir o formulário da rotina e checar o seletor.

### Contorno 2, `/schedule` pelo CLI

Outro caminho de código, que não passa pelo seletor da web.

```bash
cd /f/content-engine
claude
/schedule update
```

Descrever em linguagem natural que a rotina deve usar este repositório.

### Contorno 3, rotina local no Desktop

Contorna o problema inteiro, e para este projeto provavelmente é a arquitetura melhor.

| | Nuvem | Local (Desktop) |
|---|---|---|
| Acesso a arquivos locais | não, clone novo | **sim** |
| Precisa da máquina ligada | não | sim |
| Skills do repositório | só do clone | do diretório de trabalho |
| Intervalo mínimo | 1 hora | 1 minuto |

No app Desktop, aba **Code** → **Routines** → **New routine** → **Local**. Pasta de
trabalho: `F:\content-engine`. Instruções: o prompt do Passo 2.

Rodando local, a rotina escreve direto em `trends/`, enxerga `/content-engine` e commita
com as suas credenciais. O problema do container efêmero deixa de existir, porque não há
container. O preço é que a máquina precisa estar ligada com o app aberto.

## Passo 2, trocar as instruções da rotina

O prompt atual pesquisa e devolve texto. Substituir pelo abaixo, que pesquisa, grava no
formato do índice e commita. Colar em **Instructions**.

```
Pesquise tendências de busca, comportamento e conteúdo nos Estados Unidos ligadas a
serviços de limpeza profissional e manutenção predial, cobrindo Google Trends, Reddit,
TikTok, Instagram, YouTube e sazonalidade da semana corrente.

Escreva o resultado em trends/<AAAA-MM-DD>.md do repositório content-engine, seguindo
exatamente o formato de trends/2026-08-27.md: um índice em tabela no topo e um registro
por tópico abaixo.

Cada tópico precisa de:
- slug estável em kebab-case, único e reutilizável entre dias
- serviço, usando os IDs canônicos de brand/DNA.md
- trilho A (motion design) ou B (filmagem real). Sujeira real é sempre B.
- evidência concreta, com número, data ou citação
- gancho local exigido
- janela de validade
- fontes com URL

Se um tópico já existe num arquivo de trends anterior, reutilize o mesmo slug em vez de
criar outro. Consulte queue.md e não repita o que já foi produzido.

Commite em uma branch trends/<AAAA-MM-DD> e abra PR. Se estiver rodando localmente,
pode commitar direto na main.

Notifique apenas se houver tendência nova de janela curta, algo que expire em menos de
duas semanas, ou se a pesquisa falhar. Dia sem novidade não gera notificação.
```

## Passo 3, verificar

Clicar em **Run now**. A execução deve terminar com `trends/<data>.md` escrito. Se o
arquivo não aparecer, o repositório não foi vinculado e nenhum dos contornos pegou.

Atenção ao aviso da documentação: status verde significa que a sessão iniciou e terminou
sem erro de infraestrutura, não que a tarefa deu certo. Abrir a execução e conferir.

---

## Fluxo depois de ligado

```
rotina das 9h  →  clona content-engine
               →  pesquisa
               →  escreve trends/<data>.md com slugs estáveis
               →  commita e abre PR
                        ↓
você revisa e faz merge
                        ↓
sessão sua  →  /content-engine <slug>
            →  máquina de estados com aprovação por etapa
            →  output/<slug>/
```

O slug é a costura. A rotina o cria com registro completo e fontes, você o digita, o
motor o resolve de volta para o registro. Ninguém precisa descrever o tópico em texto
livre em momento nenhum, que é onde o contexto se perderia.

## Por que não deixar a rotina produzir sozinha

O `--auto` existe e funciona, mas produzir sem revisão humana é ruim aqui por dois
motivos concretos: o roteiro afirma lei e valor em dólar, onde um erro custa
credibilidade, e a escolha de trilho decide gasto de geração de imagem. Rotina pesquisa
e propõe. Pessoa escolhe. Motor produz.
