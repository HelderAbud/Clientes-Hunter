# AGENTS.md - Clientes Hunter

Base operacional alinhada ao Helder Method v1.2 e ao Superpowers Cursor Playbook: contexto claro, triagem por risco, plano antes de tarefa relevante, fatias pequenas, validacao objetiva e gate humano em dados sensiveis ou mudancas de contrato.

## Visao Geral

- Produto: sistema de captacao e prospeccao comercial B2B para representantes de moda masculina no DF e Norte de Goias.
- Fase atual: MVP manual com Google Sheets, CSVs versionados, Markdown, Cursor e WhatsApp Business manual com aprovacao humana.
- Objetivo operacional: encontrar, qualificar e priorizar lojas masculinas multimarcas ate o agendamento de visita com mostruario.
- KPI principal: `agendamentos confirmados / leads qualificados`.
- Fonte curta de dominio: `CONTEXT.md`.
- Regras completas: `REGRAS-CLIENTES-HUNTER.md`.
- Privacidade e LGPD: `SEGURANCA-LGPD.md`.

## Comandos Operacionais

| Objetivo | Como trabalhar |
|----------|----------------|
| Iniciar rotina diaria | Ler `DIA-A-DIA-CLIENTES-HUNTER.md` e seguir o bloco `Iniciar Dia N` |
| Validar entrega do dia | Usar o checklist do dia e `CHECKLIST_FINAL.md` quando aplicavel |
| Configurar planilha | Seguir `templates/planilha/SETUP-GOOGLE-SHEETS.md` |
| Revisar colaboracao | Ler `CONTRIBUTING.md` antes de alterar arquivos |
| Verificar dados sensiveis | Revisar `git diff` e `SEGURANCA-LGPD.md` antes de commit/push |

Este repositorio ainda nao tem backend, build ou testes automatizados. Validacoes sao documentais, CSV/planilha e checklist manual ate o gate tecnico do Dia 22.

## Regras de Arquitetura e Produto

- Manter o MVP atual como Google Sheets + CSV + Markdown + WhatsApp manual (HITL).
- **Coleta assistida** via Google Places API e permitida sob [ADR 0004](docs/adr/0004-coleta-assistida-google-places.md) (piloto; CSV em `data/exports/`; triagem humana). Nao confundir com scraping.
- Nao implementar PostgreSQL, n8n, Evolution API, JWT, painel Kanban ou scraping Instagram/Maps HTML sem decisao registrada (Dia 22 / ADR).
- Toda mudanca de regra de negocio deve atualizar primeiro o contrato minimo correto: `CONTEXT.md`, `REGRAS-CLIENTES-HUNTER.md`, plano aprovado ou ADR.
- Preservar o vocabulario canonico: lead, **candidato**, lead qualificado, coleta assistida, geo-cerca, multimarcas real, ja cliente, reativacao, score, funil, descartado e opt-out.
- Preferir fatias verticais: cada entrega deve fechar valor operacional verificavel, nao apenas uma camada solta.
- Evitar refactors amplos e abstracoes sem necessidade clara.

## Workflow

### Triagem

- Hotfix: producao ou operacao real quebrada/degradada; corrigir o minimo e provar o sintoma.
- Complex: varios sistemas, alto custo de erro, backend, automacao, LGPD sensivel ou decisao arquitetural.
- Normal: tarefa relevante que precisa de escopo fechado, contrato minimo ou plano salvo.
- Simple: mudanca pequena, localizada, baixa ambiguidade e sem contrato publico novo.

### Execucao

- Simple: contexto rapido, diff pequeno, validacao objetiva e explicacao final.
- Normal: brainstorming curto, Plan Mode, plano em `.cursor/plans/`, implementacao em fatias, validacao e revisao.
- Complex: discovery, spec/ADR quando necessario, gates humanos entre fases sensiveis, validacao e registro final.
- Hotfix: diagnostico sistematico, patch minimo, smoke/regressao que prove a correcao e registro do aceite.

### Git (branches e autor)

- Nunca commit/push direto em `Main`: criar `feat/`, `docs/` ou `fix/` a partir de `Main` atualizada, abrir PR, conferir, so entao merge; depois `git pull` em `Main`.
- Detalhe do fluxo: `CONTRIBUTING.md` §6.
- Nao incluir `Co-authored-by: Cursor` / `cursoragent` nos commits; autor unico Helder Abud.

### Gates Humanos

Pedir aprovacao explicita antes de:

- usar ou expor dados reais de clientes, CNPJ, telefones, PDFs, exports ou backups;
- mudar contrato de planilha, funil, score, geo-cerca, templates WhatsApp ou KPI;
- automatizar WhatsApp, scraping HTML, n8n, Evolution API ou backend Postgres;
- expor `data/clientes-existentes.csv`, exports Places com telefones, ou `.env`;
- criar migrations, banco, API publica ou qualquer operacao destrutiva;
- commitar, pushar ou abrir PR quando houver arquivos sensiveis ou escopo duvidoso.

## Seguranca e LGPD

- Nunca commitar `data/clientes-existentes.csv`, `data/_pdf_raw.txt`, PDFs de clientes, `.env`, cookies/sessoes ou exports com telefones reais (`data/exports/`).
- Nunca abrir o CSV real de clientes no chat; usar example ou recortes mascarados.
- Antes de usar IA, mascarar telefone como `TELEFONE_OCULTO` e CNPJ como `CNPJ_OCULTO`.
- Leads devem armazenar apenas o necessario para prospeccao B2B: nome fantasia, cidade, Instagram, WhatsApp comercial e notas curtas.
- Opt-out sempre vira `Descartado` com motivo `Opt-out`; nao reabordar.
- Instagram no MVP e manual, apenas perfis publicos, com limite de 8-12 perfis triados por dia.
- WhatsApp frio e manual, 5-8 abordagens por dia, horario 9h-17h e nunca depois das 18h.

## Testes e Validacao

- Mudanca de regra de negocio: validar contra `CONTEXT.md` e `REGRAS-CLIENTES-HUNTER.md`.
- Mudanca em planilha/CSV: conferir dropdowns, formulas, exemplo sem dados reais e setup no Google Sheets.
- Bugfix documental: revisar links internos, nomenclatura e checklist afetado.
- Antes de concluir: explicar o que foi verificado e o que nao foi possivel verificar.

## Caminhos Importantes

| Caminho | Conteudo |
|---------|----------|
| `README.md` | Visao geral, stack atual, progresso e roadmap |
| `CONTEXT.md` | Vocabulario canonico e KPIs |
| `REGRAS-CLIENTES-HUNTER.md` | Regras operacionais de qualificacao e funil |
| `SEGURANCA-LGPD.md` | Privacidade, IA, WhatsApp, Instagram e dados proibidos |
| `DIA-A-DIA-CLIENTES-HUNTER.md` | Roteiro diario de execucao |
| `CONTRIBUTING.md` | Colaboracao, commits, branches e fluxo dos 4 especialistas |
| `CHECKLIST_FINAL.md` | Auditoria antes de push, PR ou apresentacao |
| `templates/planilha/` | CSVs e guias para Google Sheets |
| `data/geo-cerca-cidades.csv` | Lista oficial de cidades permitidas |
| `docs/adr/` | Decisoes arquiteturais |
| `docs/grill-logs/` | Registros de revisao/validacao operacional |
| `.cursor/rules/` | Regras persistentes do Cursor |
| `.cursor/plans/` | Planos aprovados para tarefas relevantes |

