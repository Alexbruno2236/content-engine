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

## Passo 1, vincular o repositório

1. Abrir https://claude.ai/code/routines
2. Clicar na rotina **Daily cleaning content trends**
3. Clicar no ícone de lápis para abrir **Edit routine**
4. Em **Select repositories**, adicionar `Alexbruno2236/content-engine`
5. Salvar

A partir da próxima execução a rotina clona o repositório, enxerga
`.claude/skills/content-engine/`, lê `brand/` e `trends/`, e consegue commitar.

Se a rotina também for produzir peças do Meu Shop Favorito, adicionar
`Alexbruno2236/meushopfavorito-remotion` na mesma lista. O campo aceita múltiplos.

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

Commite em uma branch claude/trends-<AAAA-MM-DD> e abra PR.

Notifique apenas se houver tendência nova de janela curta, algo que expire em menos de
duas semanas, ou se a pesquisa falhar. Dia sem novidade não gera notificação.
```

## Passo 3, verificar

Na página da rotina, clicar em **Run now**. A execução deve terminar com um PR abrindo
`trends/<data>.md`. Se o arquivo não aparecer, o repositório não foi vinculado.

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
