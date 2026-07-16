# Trilha dia a dia — Clientes Hunter

> **Metodologia:** [Helder Method v1.2](../Agentes/helder-method-v1.2-resumo-compartilhavel.md) + [skills-pessoal](../Agentes/skills-pessoal/skills-pessoal/README-pt_br.md) ([WORKFLOW](../Agentes/skills-pessoal/skills-pessoal/WORKFLOW.md))  
> **Iniciativa:** MVP manual + apresentação de portfólio (produto/operação)  
> **Triagem Helder:** **Normal** (regras de negócio, LGPD, contrato de planilha)  
> **Custo:** R$ 0 · **Backend/cloud:** só após gate Dia 22  

**Complementa:** [`DIA-A-DIA-CLIENTES-HUNTER.md`](DIA-A-DIA-CLIENTES-HUNTER.md) (roteiro operacional original).

---

## Como usar esta trilha

1. **Manhã (15 min):** leia o dia, confira trilha Helder e gates HITL.
2. **Cursor:** abra o prompt do dia; em Normal/Complex use `to-spec` → `to-issues` antes de editar.
3. **Tarde:** execute a fatia vertical do dia (MVP manual = build documental, sem `tdd`).
4. **Fim do dia:** marque checklist; registre `docs/grill-logs/validation-YYYY-MM-DD-dia-N.md` se aplicável; use `slice-verification` mental (checklist + LGPD).
5. **Planos por fatia:** `.cursor/plans/plan-YYYY-MM-DD-hunter-*.md` quando o dia pedir.
6. **Commit/push/PR:** só com pedido explícito (HITL).

### Helder → skills-pessoal

| Trilha Helder | Caminho |
|---------------|---------|
| **Simple** | Fast path: fazer → verificar → resumir |
| **Normal** | `to-spec` → `to-issues` → build documental → `slice-verification` → `code-review` (proporcional) |
| **Complex** | igual Normal + HITL entre fases; `context-discovery` antes de mudar `CONTEXT.md` / `REGRAS` / ADR |
| **Hotfix** | `diagnose` → patch mínimo → regressão → só então retomar a trilha |

### Core Workflow (mapa)

| Fase | Skill |
|------|-------|
| Spec | `to-spec` |
| Plan | `to-issues` |
| Branch | `git-workflow-and-versioning` |
| Build | documental / checklist (sem `tdd` no MVP manual) |
| Verify | `slice-verification` (checklist + LGPD) |
| Review | `code-review` |
| Simplify | `code-simplification` (se houver drift documental) |
| Ship | `finishing-a-development-branch` |

### Artefatos Helder (este projeto)

| Tipo | Onde | Quando |
|------|------|--------|
| Contrato mínimo | `CONTEXT.md`, `REGRAS-CLIENTES-HUNTER.md` | Antes de mudar funil/score/geo-cerca |
| Plano fatia | `.cursor/plans/plan-YYYY-MM-DD-hunter-*.md` | Dias Normal/Complex |
| Validação | `docs/grill-logs/validation-*` | Fim de cada bloco (Dias 9, 15, 22) |
| Changelog | commit message + nota no grill-log | Cada entrega |

### Gates HITL (humano aprova antes de continuar)

- Usar ou expor `data/clientes-existentes.csv` ou telefones reais
- Mudar contrato de planilha (colunas, dropdowns, KPI)
- Enviar WhatsApp frio em massa ou fora dos limites (5–8/dia, 9h–17h)
- Iniciar backend/API (após Dia 22)
- Commit, push ou PR

---

## Visão das fases

| Fase | Dias | Foco | Trilha |
|------|------|------|--------|
| A — Higiene + apresentação | 1–2 | README, docs portfólio | Simple |
| B — Operação (roteiro) | 3–17 | Dias 7–15 do plano original | Normal |
| C — Evidência campo | 18–21 | KPI, resultados agregados | Normal |
| D — Gate + decisão | 22–24 | Backend sim/não | Complex (gate) |
| E — Manutenção | 25+ | LinkedIn, revisão mensal | Simple |

---

## Fase A — Higiene e apresentação

### Dia 1 — README e conflito de merge

| Campo | Conteúdo |
|-------|----------|
| **Fatia vertical** | Repositório apresentável no GitHub em 30 segundos |
| **Trilha** | Simple (Express se só README; Assistida se tocar CONTRIBUTING) |
| **Skills** | Fast path (Simple) ou `to-spec` → `to-issues` → diff → `code-review` |

**Tarefas**
- [x] Resolver conflito `<<<<<<< HEAD` no README (manter versão completa com badges)
- [x] Conferir links internos (CONTRIBUTING, SEGURANCA-LGPD, DIA-A-DIA)
- [x] Adicionar seção **Pitch 1 linha** no topo

**Validação (DoD)**
- [x] `git diff` sem markers de merge
- [x] README renderiza badges e funil
- [x] Nenhum dado sensível no diff

**Registro:** [`docs/grill-logs/validation-2026-07-08-trilha-dia-1.md`](docs/grill-logs/validation-2026-07-08-trilha-dia-1.md)

**Prompt Cursor**
```text
Trilha Simple — Clientes Hunter Dia 1.
Resolver conflito README, manter versão com badges e progresso Dias 1-6.
Não alterar regras de negócio. Fast path → diff mínimo → checklist DoD.
```

**HITL:** revisar diff antes de commit.

---

### Dia 2 — Portfólio visual (sem dados reais)

| Campo | Conteúdo |
|-------|----------|
| **Fatia vertical** | Evidência visual + narrativa 5 etapas |
| **Trilha** | Simple |

**Tarefas**
- [x] Criar `docs/portfolio/etapas.md` (5 etapas operacionais — ver modelo abaixo)
- [x] Diagrama Mermaid do funil no README ou em `docs/portfolio/etapas.md`
- [ ] Preparar screenshot planilha **demo** (dados fictícios) → `docs/screenshots/planilha-demo.png` *(guia: [`docs/screenshots/README.md`](docs/screenshots/README.md))*
- [x] Atualizar README com Mermaid do funil + link para `docs/portfolio/etapas.md` *(imagem PNG ainda pendente)*

**Modelo `docs/portfolio/etapas.md`**
1. Regras + geo-cerca (`REGRAS`, CSV cidades)
2. Planilha operacional v1 (templates)
3. Templates WhatsApp HITL
4. Captação Instagram manual (8–12/dia)
5. KPI agendamentos / leads qualificados

**Validação**
- [x] Nenhum telefone/CNPJ real nos artefatos criados (docs/README; PNG ainda não existe)
- [x] Etapas numeradas com tags: `Geo-cerca`, `HITL`, `KPI`
- [ ] Revisar PNG quando existir (zero PII) antes de commit

**Prompt Cursor**
```text
Dia 2 Clientes Hunter — criar docs/portfolio/etapas.md e diagrama funil Mermaid.
Screenshot só com dados fictícios. Trilha Simple. Não implementar backend.
```

---

## Fase B — Operação (alinhar ao DIA-A-DIA original)

> **Referência:** [`DIA-A-DIA-CLIENTES-HUNTER.md`](DIA-A-DIA-CLIENTES-HUNTER.md) — Dias 7–15.

### Dia 3 — Iniciar Dia 7 (biblioteca WhatsApp)

| Trilha | Normal |
|--------|--------|

**Tarefas**
- [x] Cursor: `Iniciar Dia 7` — templates já prontos
- [x] Kits de fotos **descontinuados** (2026-07-15) — ver plano + grill
- [x] Plano: [`.cursor/plans/plan-2026-07-15-hunter-dia-7.md`](.cursor/plans/plan-2026-07-15-hunter-dia-7.md)

**Validação:** checklist do Dia 7 em DIA-A-DIA marcado (Task A3 fechada sem kits).

---

### Dia 4 — Dia 8

- [ ] `Iniciar Dia 8` — triagem Instagram (8–12 perfis)
- [ ] Registrar leads na planilha (status `Novo lead`)
- [ ] **HITL:** aprovar cada lead antes de qualificar

---

### Dia 5 — Dia 9 + validação bloco

- [ ] `Iniciar Dia 9` — fechar bloco biblioteca + Instagram
- [ ] `Validar Dia 9`
- [ ] Criar `docs/grill-logs/validation-YYYY-MM-DD-bloco-dias-7-9.md`

**DoD Normal:** validation aceito + nenhuma violação LGPD.

---

### Dias 6–10 — Campo real (Dias 10–14 do roteiro)

| Dia trilha | Roteiro original | Meta |
|------------|------------------|------|
| 6 | Dia 10 | 4 leads qualificados |
| 7 | Dia 11 | 4 leads + 1 abordagem WhatsApp (manual) |
| 8 | Dia 12 | 4 leads + follow-up |
| 9 | Dia 13 | 4 leads |
| 10 | Dia 14 | 4 leads — total ~20 no período |

**Regras diárias**
- Máx. 5–8 abordagens WhatsApp frias/dia
- Horário 9h–17h
- Opt-out → `Descartado` / motivo `Opt-out`

**Skills (bug/regra):** se dúvida de qualificação → `context-discovery` + `REGRAS-CLIENTES-HUNTER.md` antes de mudar planilha.

---

### Dias 11–12 — Dia 15 + consolidação

- [ ] `Iniciar Dia 15` — revisar funil completo
- [ ] `Validar Dia 15`
- [ ] Atualizar badge progresso no README (Dias 7–15 ✅)

---

## Fase C — Evidência de portfólio

### Dia 13 — Resultados agregados

| Trilha | Normal |

**Tarefas**
- [ ] Criar `docs/resultados-piloto.md` — só números agregados (sem PII):
  - leads triados, qualificados, descartados (motivos), agendamentos
- [ ] Atualizar `docs/portfolio/etapas.md` com link para resultados

**HITL:** humano valida que nenhum dado identificável vazou.

---

### Dia 14 — LinkedIn + pitch

- [ ] Publicar 1 post (ângulo **produto + operação**, não AWS)
- [ ] Usar pitch: *Prospecção B2B multimarcas — geo-cerca, score, funil, KPI, LGPD*
- [ ] Fixar link GitHub no perfil

---

### Dias 15–17 — Dias 16–18 roteiro (visitas + IA assistida)

- [ ] Seguir `DIA-A-DIA` Dias 16–18
- [ ] IA só com dados mascarados (`TELEFONE_OCULTO`, `CNPJ_OCULTO`)
- [ ] Documentar 1 exemplo de prompt Cursor (sem dados reais) em `docs/portfolio/exemplo-ia-hitl.md`

---

## Fase D — Gate Dia 22

> **Paralelo (2026-07-16):** coleta assistida Places autorizada ([ADR 0004](docs/adr/0004-coleta-assistida-google-places.md), plano [`.cursor/plans/plan-2026-07-16-coleta-assistida-places.md`](.cursor/plans/plan-2026-07-16-coleta-assistida-places.md)). CRM permanece Sheets; WA HITL. Postgres continua decisão do Dia 22.

### Dia 18 — Preparação gate

| Trilha | Complex (só planejamento — spike sem código) |

**Tarefas**
- [ ] Ler `PLANO-CLIENTES-HUNTER.md` fase 3
- [ ] `to-spec` + `to-issues`: `.cursor/plans/plan-YYYY-MM-DD-hunter-gate-dia-22.md`
- [ ] Decidir: **seguir manual (Sheets)** ou **autorizar backend** (PostgreSQL, API)
- [ ] Se não autorizar: registrar decisão no plano + adiar Fase 3
- [x] Coleta Places: **já decidida** (ADR 0004) — não reabrir no Dia 22 salvo mudança de escopo

**HITL obrigatório:** decisão de backend é humana — agente não implementa API/Postgres sem OK explícito.

---

### Dias 19–20 — Dia 19–21 roteiro

- [ ] Executar Dias 19–21 do DIA-A-DIA
- [ ] Checklist [`CHECKLIST_FINAL.md`](CHECKLIST_FINAL.md)

---

### Dia 21 — Dia 22 + validation final

- [ ] `Validar Dia 22`
- [ ] `docs/grill-logs/validation-YYYY-MM-DD-dia-22.md`
- [ ] Atualizar README progresso

**DoD Complex (gate):** validation + decisão backend registrada + CONTRIBUTING respeitado.

---

## Fase E — Manutenção (1 dia/mês)

### Ritual mensal (repeat)

- [ ] Revisar opt-outs e clientes existentes (offline)
- [ ] Atualizar KPI no `docs/resultados-piloto.md`
- [ ] 1 grill-log se mudou regra → atualizar `CONTEXT.md` primeiro

---

## Calendário resumido

| Dia trilha | Foco |
|------------|------|
| 1 | README |
| 2 | docs/portfolio |
| 3–5 | Dias 7–9 operação |
| 6–10 | Dias 10–14 campo |
| 11–12 | Dia 15 |
| 13–14 | Resultados + LinkedIn |
| 15–17 | Dias 16–18 |
| 18 | Gate backend (só plano) |
| 19–21 | Dias 19–22 + validation |

---

## Referências rápidas

| Documento | Uso |
|-----------|-----|
| [`AGENTS.md`](AGENTS.md) | Contexto agente |
| [`REGRAS-CLIENTES-HUNTER.md`](REGRAS-CLIENTES-HUNTER.md) | Contrato negócio |
| [`SEGURANCA-LGPD.md`](SEGURANCA-LGPD.md) | Antes de IA/dados |
| [`.cursor/plans/`](.cursor/plans/) | Planos por fatia |

---

## Prompt base Cursor

```text
Clientes Hunter — Dia N do TRILHA-DIA-A-DIA.md.
Helder [Simple|Normal|Complex|Hotfix] + skills-pessoal.
Normal/Complex: to-spec → to-issues → fatia vertical → slice-verification (checklist + LGPD).
MVP manual: sem tdd; context-discovery antes de mudar CONTEXT/REGRAS.
HITL: dados reais, contrato de planilha, WhatsApp fora dos limites, backend, commit/push.
Referências: AGENTS.md, REGRAS-CLIENTES-HUNTER.md, SEGURANCA-LGPD.md.
```

---

*Trilha v1.1 — 2026-07-09 — Helder v1.2 + skills-pessoal*
