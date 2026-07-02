<<<<<<< HEAD
# Clientes-Hunter
Clientes Hunter: sistema de captação e prospecção comercial para representantes de moda masculina no DF e Norte de Goiás. Encontra lojas multimarcas no Instagram e Google Maps, qualifica leads por score e geo-cerca, organiza contato WhatsApp com aprovação humana e acompanha o funil Kanban. MVP operacional em Google Sheets.
=======
# Clientes Hunter

Sistema de captação e prospecção comercial para representantes de moda masculina no **DF** e **Norte de Goiás**. Encontra lojas multimarcas no Instagram e Google Maps, qualifica leads por score e geo-cerca, organiza contato WhatsApp com aprovação humana e acompanha o funil Kanban até visita com mostruário. **MVP operacional em Google Sheets.**

[![Progresso](https://img.shields.io/badge/progresso-Dias%201--5%20✅-brightgreen)](#progresso)
[![Fase](https://img.shields.io/badge/fase-MVP%20manual-blue)](#stack-atual)
[![LGPD](https://img.shields.io/badge/LGPD-documentado-orange)](SEGURANCA-LGPD.md)

---

## O que resolve

Representantes comerciais perdem tempo com leads ruins (loja feminina, fora da área, cliente existente, multimarcas falso). O Clientes Hunter **filtra**, **prioriza** e **organiza** o caminho até o agendamento de visita presencial — onde a venda acontece com mostruário.

**KPI principal:** `agendamentos confirmados ÷ leads qualificados`

---

## Stack atual (MVP)

| Camada | Tecnologia |
|--------|------------|
| CRM | Google Sheets |
| Dados | CSV + templates versionados |
| Captação | Instagram + Google Maps (manual) |
| Contato | WhatsApp Business (manual, HITL) |
| IA | Cursor — sugere, humano aprova |
| Docs | Markdown |
| Futuro | PostgreSQL, n8n, Evolution API (pós Dia 22) |

---

## Progresso

| Bloco | Status |
|-------|--------|
| Dias 1–2 — Regras + LGPD | ✅ |
| Dias 3–5 — Planilha operacional v1 | ✅ |
| Dia 6 — Templates WhatsApp | ✅ |
| Dias 7–9 — Biblioteca + Instagram | ⬜ **próximo** |
| Dias 10–15 — Campo real (20 leads) | ⬜ |
| Dias 16–22 — Visitas + IA + gate backend | ⬜ |

Detalhe: [`DIA-A-DIA-CLIENTES-HUNTER.md`](DIA-A-DIA-CLIENTES-HUNTER.md)

---

## Estrutura do repositório

```
Clientes Hunter/
├── README.md                 ← você está aqui
├── CONTRIBUTING.md           ← guia para colaboradores
├── CHECKLIST_FINAL.md        ← auditoria pré-push (4 especialistas)
├── PLANO-CLIENTES-HUNTER.md  ← visão completa fases 0–7
├── REGRAS-CLIENTES-HUNTER.md ← regras de negócio
├── DIA-A-DIA-CLIENTES-HUNTER.md
├── SEGURANCA-LGPD.md
├── .env.example
├── data/
│   ├── geo-cerca-cidades.csv      ← 62 cidades (público)
│   └── clientes-existentes.example.csv
└── templates/planilha/            ← importar no Google Sheets
```

---

## Começar rápido

### Colaborador (dev)

1. Clone o repositório
2. Leia [`CONTRIBUTING.md`](CONTRIBUTING.md) — **obrigatório**
3. Leia [`SEGURANCA-LGPD.md`](SEGURANCA-LGPD.md) — dados sensíveis
4. Importe planilha: [`templates/planilha/SETUP-GOOGLE-SHEETS.md`](templates/planilha/SETUP-GOOGLE-SHEETS.md)
5. Peça ao titular o `data/clientes-existentes.csv` real (fora do Git)
6. No Cursor: `Iniciar Dia 6`

### Representante (operação)

| Comando Cursor | Ação |
|----------------|------|
| `Iniciar Dia N` | Checklist do dia |
| `Validar Dia N` | Confirmar se está pronto |
| `Status Clientes Hunter` | Ver progresso |

---

## Funil de prospecção

```
Novo lead → Contato prévio → Agendamento → Visita → Fechado / Perdido
                                              ↓
                                         Descartado
```

Regras completas: [`REGRAS-CLIENTES-HUNTER.md`](REGRAS-CLIENTES-HUNTER.md)

---

## Segurança

- **Nunca commitar:** CNPJ/telefones reais, PDFs de clientes, `.env`
- **Mascarar** dados antes de usar IA
- **5–8** abordagens WhatsApp frias por dia
- Ver [`.gitignore`](.gitignore) e [`SEGURANCA-LGPD.md`](SEGURANCA-LGPD.md)

---

## Documentação

| Documento | Conteúdo |
|-----------|----------|
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Como colaborar + fluxo 4 especialistas |
| [`CHECKLIST_FINAL.md`](CHECKLIST_FINAL.md) | Auditoria pré-envio |
| [`PLANO-CLIENTES-HUNTER.md`](PLANO-CLIENTES-HUNTER.md) | Plano completo (fases 0–7) |
| [`REGRAS-CLIENTES-HUNTER.md`](REGRAS-CLIENTES-HUNTER.md) | Qualificação, geo-cerca, limites |
| [`DIA-A-DIA-CLIENTES-HUNTER.md`](DIA-A-DIA-CLIENTES-HUNTER.md) | Roteiro 30 dias |
| [`SEGURANCA-LGPD.md`](SEGURANCA-LGPD.md) | Privacidade e IA |
| [`templates/planilha/`](templates/planilha/) | CSVs para Google Sheets |

---

## Roadmap técnico

1. **Agora** — Planilha + templates + campo manual
2. **Fase 2** — Telegram/n8n (alertas)
3. **Fase 3** — PostgreSQL + API (após gate Dia 22)
4. **Fase 4–5** — Import Maps + enriquecimento Instagram
5. **Fase 6–7** — WhatsApp semi-auto + painel Kanban

---

## Licença

Uso interno / operacional. Definir licença pública se o projeto for open source.
>>>>>>> docs/pr1-inventory
