# Plan — Coleta assistida Places (piloto Brasília) + proteção de dados

| Campo | Valor |
|-------|--------|
| **Status** | Fatias 0–2 + 3b + 4 OK · **Fatia 5 EM ANDAMENTO** (HITL — aguarda dry-run do representante) |
| **Data** | 2026-07-16 |
| **Trilha** | Complex |
| **Spec** | [spec-2026-07-16-coleta-assistida-places.md](spec-2026-07-16-coleta-assistida-places.md) v1.1 |
| **ADR** | [0004](../../docs/adr/0004-coleta-assistida-google-places.md) |
| **Skill** | `to-issues` |

---

## Análise — proteção de dados de clientes (Gate 4)

### O que já está protegido (verificado agora)

| Item | Estado |
|------|--------|
| `data/clientes-existentes.csv` | No `.gitignore` e **não** está no índice Git (`git ls-files` não lista) |
| `.env` | Ignorado |
| `data/exports/` | Ignorado (destino natural do CSV Places real) |
| `data/backups/`, `*.pdf`, cookies/sessão | Ignorados |
| Versionado em `data/` | Só `README.md`, `geo-cerca-cidades.csv`, `clientes-existentes.example.csv` (exemplo sem carteira real) |

### Lacunas / reforços necessários (Fatia 0)

| Lacuna | Risco | Ação proposta |
|--------|-------|----------------|
| CSV de candidatos reais fora de `data/exports/` | Commit acidental se salvar na raiz | Ignorar `*candidatos*.csv`, `**/places-out/**`, reforçar `data/exports/` |
| Script imprimir telefones no terminal → colar no chat | PII na IA | Default: não dumpar telefone no stdout; modo `--verbose` opt-in |
| Cursor/agente ler `clientes-existentes.csv` | Exposição no contexto | Regra operacional: **nunca** abrir/colar o arquivo real na sessão; só `example` ou contagem agregada |
| Commit sem checklist | Humano esquece | Antes de qualquer commit: `git status` + `git diff` sem arquivos sensíveis; HITL |
| Compartilhar planilha Google com telefones | Link público | Fora do Git, mas documentar: planilha **não** publicar na web |

### Regra permanente (contrato desta iniciativa)

> Arquivos com dados reais de clientes/candidatos/leads (**telefone, CNPJ, carteira**) **nunca** são commitados, pushados, colados em chat de IA sem máscara, nem compartilhados publicamente.  
> Templates e examples usam só dados fictícios (`TELEFONE_OCULTO` / números 9000…).

Isso alinha ADR 0003 + SEGURANCA e será reforçado na Fatia 0 (gitignore + SEGURANCA + nota no script).

---

## Fatias verticais

### Fatia 0 — Blindagem LGPD / Git *(nova, a pedido)*

| Campo | Valor |
|-------|--------|
| **Tipo** | AFK + HITL review do diff |
| **Blocked by** | Nenhum |

**What to build:** Reforçar `.gitignore` (candidatos/Places/exports); parágrafo explícito em `SEGURANCA-LGPD.md` sobre coleta Places + proibição de commit/share; `data/exports/README.md` (só instrução, sem dados); nunca tocar no CSV real de clientes.

**Acceptance**
- [x] Padrões novos no `.gitignore` cobrem CSV de candidatos e saída do script
- [x] SEGURANCA lista Places exports como proibidos no Git
- [x] `git check-ignore` valida caminhos de exemplo (`exports/*.csv` ignorado; `exports/README.md` commitável)
- [x] Diff sem PII (`clientes-existentes.csv` não lido/alterado)

**Verification:** concluída 2026-07-16 — Fatia 0 OK.

---

### Fatia 1 — Contrato de domínio

| Campo | Valor |
|-------|--------|
| **Tipo** | AFK + HITL |
| **Blocked by** | Fatia 0 |

**What to build:** Atualizar `CONTEXT.md` (candidato, coleta assistida), `REGRAS` (canal Places), `SEGURANCA` (já reforçada), `TRILHA`/`DIA-A-DIA` nota de piloto, link ADR 0004.

**Acceptance**
- [x] Glossário com candidato ≠ lead
- [x] Places permitido; scrape/WA auto proibidos
- [x] Sem PII no diff

**Verification:** leitura cruzada CONTEXT ↔ ADR 0004 ↔ spec. **Concluída 2026-07-16.**

---

### Fatia 2 — Template CSV candidatos

| Campo | Valor |
|-------|--------|
| **Tipo** | AFK |
| **Blocked by** | Fatia 1 |

**What to build:** `templates/planilha/Candidatos.example.csv` (fictício) + colunas da spec; guia curto de revisão/import.

**Acceptance**
- [x] Colunas mínimas da spec
- [x] Só dados fictícios (`6199999002X` / `TELEFONE_OCULTO`)
- [x] Instruções: gravar reais só em `data/exports/` (gitignored)

**Verification:** example commitável; zero PII real. **Concluída 2026-07-16.**

---

### Fatia 3 — Script Places → CSV ⚠️ **PAUSADA** (2026-07-16)

| Campo | Valor |
|-------|--------|
| **Tipo** | HITL (chave API + billing Google) |
| **Blocked by** | Fatia 2 · **orçamento / cartão** |
| **Status** | **Pausada** — representante sem condição de custo agora |

**What to build (quando retomar):** Script Python + `.env` Places; output `data/exports/`; cap 40; Brasília; sem log de telefone por default.

**Retomar quando:** houver billing Google + `autorizo retomar fatia 3`.

**Acceptance** (adiadas)
- [ ] Sem chave → erro claro
- [ ] Com chave → CSV ≤ 40 em `data/exports/`
- [ ] Dedupe `place_id`

---

### Fatia 3b — Organizador CSV zero-custo *(caminho A+B)*

| Campo | Valor |
|-------|--------|
| **Tipo** | AFK + HITL review |
| **Blocked by** | Fatia 2 |
| **Status** | **Concluída** 2026-07-16 |

**What to build:** Script **local e gratuito** que **não** chama Google. Você busca no Maps/Instagram (manual), cola ou passa um rascunho (texto/CSV simples), e o script:

- normaliza para o formato `Candidatos.example.csv`;
- preenche `fonte=Maps`, `coletado_em`, `status_revisao=Pendente`;
- gera `place_id` local estável (ex.: hash do nome+endereço) se não houver ID Google;
- grava só em `data/exports/` (gitignored);
- **não** imprime telefones no stdout por padrão.

**Não faz:** busca automática na internet, scrape, Places API.

**Artefatos:** `scripts/organizar_candidatos.py`, `scripts/README-organizar-candidatos.md`, `templates/planilha/Candidatos-entrada.example.csv`

**Acceptance**
- [x] README de uso
- [x] Saída compatível com `Candidatos-revisao.md`
- [x] Zero dependência de chave paga
- [x] Diff sem PII; dry-run 3 linhas fictícias OK

**Verification:** `python scripts/organizar_candidatos.py -i templates/planilha/Candidatos-entrada.example.csv` → export gitignored.

---

### Fatia 4 — Checklist triagem humana

| Campo | Valor |
|-------|--------|
| **Tipo** | AFK |
| **Blocked by** | Fatia 2 (independente de 3 / 3b) |

**What to build:** Checklist (markdown): feminina, já-cliente (offline), WA, multimarcas, score → promover a Leads ou descartar; **nunca WA sem triagem**.

**Acceptance**
- [x] Passos objetivos
- [x] Referência a REGRAS / opt-out / já cliente

**Verification:** checklist em `templates/planilha/checklist-triagem-candidatos.md`. **Concluída 2026-07-16.**

---

### Fatia 5 — Dry-run + validation

| Campo | Valor |
|-------|--------|
| **Tipo** | HITL |
| **Blocked by** | Fatias 0–2 + (3b **ou** 3 retomada) + 4 |

**What to build:** Você tria ≥ 3 candidatos (do organizador 3b ou Places); grill validation sem colar telefones.

**Acceptance**
- [ ] Piloto executado (zero-custo **ou** Places)
- [ ] Validation sem PII
- [ ] Decisão: continuar 3b / retomar Places / pausar

**Verification:** aceite qualitativo seu.  
**Status:** aberta 2026-07-16 — guia em `docs/grill-logs/COMO-FAZER-FATIA-5.md` · template `validation-2026-07-16-fatia5-dry-run-candidatos.md`.

---

## Ordem e HITL

```text
Fatia 0 → 1 → 2 → 3b (zero-custo) + 4 (checklist) → 5 (dry-run)
                ↘ Fatia 3 Places (PAUSADA até orçamento)
```

Cada fatia: explicar diff → você `autorizo fatia N` → executar → verificação → próxima.

**Commit/push:** só com pedido explícito; nunca `clientes-existentes.csv`, exports reais, `.env`.

## Rollback

Por fatia: reverter docs/código; apagar `data/exports/`; Places: revogar chave quando existir.

## Aprovação

- [x] Fatias 0–2
- [x] Decisão **A+B** (pausar Places; caminho 3b)
- [x] Fatia 3b + Fatia 4 (`autorizo fatia 3b e fatia 4`)
- [ ] Fatia 5 dry-run (você no campo com rascunho real) — `autorizo fatia 5` quando quiser
- [ ] `autorizo retomar fatia 3` (Places, quando houver billing)

