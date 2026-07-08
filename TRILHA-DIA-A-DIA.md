# Trilha dia a dia — Clientes Hunter

> **Metodologia:** [Rheyder Method v1.2](../Agentes/rheyder-method-v1.2-resumo-compartilhavel.md) + [Superpowers Cursor Playbook](../Skills/superpowers-cursor-playbook.md)  
> **Iniciativa:** MVP manual + apresentação de portfólio (produto/operação)  
> **Triagem Rheyder:** **Normal** (regras de negócio, LGPD, contrato de planilha)  
> **Custo:** R$ 0 · **Backend/cloud:** só após gate Dia 22  

**Complementa:** [`DIA-A-DIA-CLIENTES-HUNTER.md`](DIA-A-DIA-CLIENTES-HUNTER.md) (roteiro operacional original).

---

## Como usar esta trilha

1. **Manhã (15 min):** leia o dia, confira trilha Rheyder e gates HITL.
2. **Cursor:** use o prompt do dia em **Plan Mode** antes de editar.
3. **Tarde:** execute a fatia vertical do dia.
4. **Fim do dia:** marque checklist, registre `docs/grill-logs/validation-YYYY-MM-DD-dia-N.md` se aplicável.
4. **Planos por fatia:** salve em `.cursor/plans/plan-YYYY-MM-DD-assunto.md` quando o dia pedir.

### Artefatos Rheyder (este projeto)

| Tipo | Onde | Quando |
|------|------|--------|
| Contrato mínimo | `CONTEXT.md`, `REGRAS-CLIENTES-HUNTER.md` | Antes de mudar funil/score/geo-cerca |
| Plano fatia | `.cursor/plans/plan-*` | Dias com ⬜ Plan Mode |
| Validação | `docs/grill-logs/validation-*` | Fim de cada bloco (Dias 9, 15, 22) |
| Changelog | commit message + nota no grill-log | Cada entrega |

### Gates HITL (humano aprova antes de continuar)

- Usar ou expor `data/clientes-existentes.csv` ou telefones reais
- Mudar contrato de planilha (colunas, dropdowns, KPI)
- Enviar WhatsApp frio em massa ou fora dos limites (5–8/dia, 9h–17h)
- Iniciar backend/API (após Dia 22)

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
| **Superpowers** | Brainstorm → plano 1 página → executar → revisão diff |

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
Não alterar regras de negócio. Plan Mode → diff mínimo → checklist DoD.
```

**HITL:** revisar diff antes de commit.

---

### Dia 2 — Portfólio visual (sem dados reais)

| Campo | Conteúdo |
|-------|----------|
| **Fatia vertical** | Evidência visual + narrativa 5 etapas |
| **Trilha** | Simple |

**Tarefas**
- [ ] Criar `docs/portfolio/etapas.md` (5 etapas operacionais — ver modelo abaixo)
- [ ] Diagrama Mermaid do funil no README ou em `docs/portfolio/etapas.md`
- [ ] Preparar screenshot planilha **demo** (dados fictícios) → `docs/screenshots/planilha-demo.png`
- [ ] Atualizar README com imagem do funil ou planilha demo

**Modelo `docs/portfolio/etapas.md`**
1. Regras + geo-cerca (`REGRAS`, CSV cidades)
2. Planilha operacional v1 (templates)
3. Templates WhatsApp HITL
4. Captação Instagram manual (8–12/dia)
5. KPI agendamentos / leads qualificados

**Validação**
- [ ] Nenhum telefone/CNPJ real em screenshots
- [ ] Etapas numeradas com tags: `Geo-cerca`, `HITL`, `KPI`

**Prompt Cursor**
```text
Dia 2 Clientes Hunter — criar docs/portfolio/etapas.md e diagrama funil Mermaid.
Screenshot só com dados fictícios. Trilha Simple. Não implementar backend.
```

---

## Fase B — Operação (alinhar ao DIA-A-DIA original)

> **Referência:** [`DIA-A-DIA-CLIENTES-HUNTER.md`](DIA-A-DIA-CLIENTES-HUNTER.md) — Dias 7–15.

### Dia 3 — Iniciar Dia 7 (biblioteca + preparação Instagram)

| Trilha | Normal |
|--------|--------|

**Tarefas**
- [ ] Cursor: `Iniciar Dia 7`
- [ ] Revisar biblioteca de marcas / critérios multimarcas
- [ ] Plan Mode: fatia do dia em `.cursor/plans/plan-YYYY-MM-DD-dia-7.md`

**Validação:** checklist do Dia 7 em DIA-A-DIA marcado.

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

**Superpowers (bug/regra):** se dúvida de qualificação → Plan Mode + consultar `REGRAS-CLIENTES-HUNTER.md` antes de mudar planilha.

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

### Dia 18 — Preparação gate

| Trilha | Complex (só planejamento — spike sem código) |

**Tarefas**
- [ ] Ler `PLANO-CLIENTES-HUNTER.md` fase 3
- [ ] Plan Mode: `.cursor/plans/plan-YYYY-MM-DD-gate-dia-22.md`
- [ ] Decidir: **seguir manual** ou **autorizar backend** (PostgreSQL, API)
- [ ] Se não autorizar: registrar decisão no plano + adiar Fase 3

**HITL obrigatório:** decisão de backend é humana — agente não implementa API sem OK explícito.

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

*Trilha v1.0 — 2026-07-07 — alinhada Rheyder v1.2 + Superpowers*
