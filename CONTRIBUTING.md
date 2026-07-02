# Como colaborar — Clientes Hunter

Guia para quem entra no projeto (colaborador ou dev). Leia **nesta ordem** antes de alterar qualquer coisa.

---

## 1. Entenda o projeto em 2 minutos

| Item | Detalhe |
|------|---------|
| **O quê** | Prospecção B2B de lojas masculinas multimarcas (DF + Norte GO) |
| **Como vende** | WhatsApp → agendamento → visita com mostruário |
| **Fase atual** | MVP manual — Google Sheets + documentação (Dias 1–5 ✅) |
| **Próximo passo** | Dia 6 — templates WhatsApp (`DIA-A-DIA-CLIENTES-HUNTER.md`) |
| **KPI principal** | `agendamentos confirmados ÷ leads qualificados` |

Documentos obrigatórios:

1. [`README.md`](README.md) — visão geral
2. [`REGRAS-CLIENTES-HUNTER.md`](REGRAS-CLIENTES-HUNTER.md) — regras de negócio
3. [`SEGURANCA-LGPD.md`](SEGURANCA-LGPD.md) — **ler antes de tocar em dados**
4. [`DIA-A-DIA-CLIENTES-HUNTER.md`](DIA-A-DIA-CLIENTES-HUNTER.md) — roteiro dia a dia

---

## 2. Fluxo dos 4 especialistas (revisão antes de commit)

Use esta ordem ao revisar ou entregar trabalho. Prompts originais em `Desktop/Agentes/`.

| Ordem | Especialista | Quando usar | Foco neste projeto |
|-------|--------------|-------------|-------------------|
| 1 | **Código** | Alterar arquivos, scripts, estrutura | Organização, nomenclatura, duplicação, segurança em scripts |
| 2 | **Testes** | Antes de commit | Validar CSV, fórmulas Dashboard, checklist manual do dia |
| 3 | **Recrutador** | README, commits, apresentação | Projeto parece profissional? Outro dev entende em 20s? |
| 4 | **Analista GitHub** | Antes de push/PR | [`CHECKLIST_FINAL.md`](CHECKLIST_FINAL.md) completo |

**Regra:** não pule etapas. Código → testes → apresentação → checklist GitHub.

---

## 3. Setup local (primeira vez)

```bash
git clone <url-do-repositorio>
cd "Clientes Hunter"
```

### Dados sensíveis (cada máquina)

Estes arquivos **não vêm do Git**. O titular do projeto deve passar por canal seguro (WhatsApp, Drive privado):

| Arquivo local | Conteúdo |
|---------------|----------|
| `data/clientes-existentes.csv` | 178 clientes reais (CNPJ) |
| Planilha Google Sheets operacional | Leads reais com telefone |

Estrutura de referência (sem dados reais): [`data/clientes-existentes.example.csv`](data/clientes-existentes.example.csv)

### Planilha Google Sheets

1. Seguir [`templates/planilha/SETUP-GOOGLE-SHEETS.md`](templates/planilha/SETUP-GOOGLE-SHEETS.md)
2. Importar CSVs de [`templates/planilha/`](templates/planilha/)
3. Importar clientes existentes na aba oculta **Clientes**

### Variáveis de ambiente (futuro)

```bash
cp .env.example .env
# Preencher só quando usar Telegram/Evolution/Postgres (Fase 2+)
```

---

## 4. Como trabalhar no dia a dia

### Comando no Cursor

| Comando | Ação |
|---------|------|
| `Iniciar Dia N` | Checklist detalhado do dia N |
| `Validar Dia N` | Confirmar se o dia está pronto |
| `Status Clientes Hunter` | Ver progresso geral |

### Ritual operacional (representante)

| Horário | Ação |
|---------|------|
| Manhã (30–45 min) | Captar + qualificar leads |
| Meio-dia (30 min) | Enviar WhatsApp aprovados (máx. 5–8/dia) |
| Fim do dia (20 min) | Atualizar funil + Dashboard + Atividades |

### O que você pode ajudar agora

| Área | Tarefas |
|------|---------|
| **Documentação** | Melhorar README, corrigir typos, traduzir seções |
| **Templates** | Criar templates WhatsApp (Dia 6–7) |
| **Planilha** | Validar fórmulas Dashboard, dropdowns, CSVs |
| **Scripts** | Import CSV, normalizar telefone (Fase 3+) |
| **Código** | Postgres, API — **só após Dia 22 (gate)** |

---

## 5. Regras de commit (Conventional Commits)

```
tipo(escopo): descrição curta no imperativo
```

| Tipo | Uso |
|------|-----|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Só documentação |
| `refactor` | Refatoração sem mudar comportamento |
| `test` | Testes |
| `chore` | Config, gitignore, deps |

**Exemplos bons:**

```
docs: adiciona templates WhatsApp primeiro contato
fix: corrige fórmula taxa agendamento no Dashboard
feat: script importação leads CSV para planilha
docs(readme): atualiza progresso Dias 1-6
```

**Evitar:** `update`, `ajuste`, `alterações`, `teste`, `final`

---

## 6. Branches

| Branch | Uso |
|--------|-----|
| `main` | Estável, sempre utilizável |
| `feat/nome-curto` | Nova funcionalidade |
| `docs/nome-curto` | Só documentação |
| `fix/nome-curto` | Correção |

Fluxo: `feat/...` → PR ou merge em `main` após checklist.

---

## 7. O que NUNCA commitar

- `data/clientes-existentes.csv` (CNPJ real)
- `data/_pdf_raw.txt`, `*.pdf`
- `.env` (tokens)
- Exports de planilha com telefones reais
- Cookies/sessão Instagram

Ver [`.gitignore`](.gitignore) e [`SEGURANCA-LGPD.md`](SEGURANCA-LGPD.md).

---

## 8. Checklist rápido antes de cada PR/commit

- [ ] Li `REGRAS-CLIENTES-HUNTER.md` se mudei fluxo de negócio
- [ ] Nenhum dado sensível no diff (`git diff`)
- [ ] Passou pelo fluxo dos 4 especialistas (se alteração relevante)
- [ ] [`CHECKLIST_FINAL.md`](CHECKLIST_FINAL.md) — seções aplicáveis marcadas
- [ ] Commit message segue Conventional Commits
- [ ] README atualizado se mudou setup ou progresso

---

## 9. Dúvidas?

1. Consulte [`PLANO-CLIENTES-HUNTER.md`](PLANO-CLIENTES-HUNTER.md) — visão completa fases 0–7
2. No Cursor: `Status Clientes Hunter` ou `Iniciar Dia N`
3. Titular do projeto define prioridade entre Dias 6–22

---

*Projeto operacional — MVP manual. Backend e automação só após gate Dia 22.*
