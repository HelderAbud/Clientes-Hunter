# CHECKLIST FINAL — PRÉ-ENVIO DO PROJETO

> Auditoria antes de push, PR ou apresentação. Adaptado ao **Clientes Hunter** (MVP documental + planilha).
> Use o fluxo dos 4 especialistas: Código → Testes → Recrutador → este checklist.

**Progresso atual:** Dias 1–5 ✅ · Próximo: Dia 6 (templates WhatsApp)

---

## 1. Revisão de conteúdo e arquivos

- [x] Documentação principal presente (README, PLANO, REGRAS, DIA-A-DIA, SEGURANCA)
- [x] Templates CSV sem telefones reais (fictícios 6199999000X)
- [x] Arquivo exemplo de clientes (`clientes-existentes.example.csv`) sem CNPJ real
- [ ] Remover rascunhos locais (`Novo Documento de Texto.md.txt` — não versionar)
- [ ] Sem PDFs de clientes no repositório
- [ ] Nomenclatura consistente (Clientes Hunter, status_funil, geo-cerca)
- [ ] Links internos entre docs funcionam
- [ ] Progresso em `DIA-A-DIA-CLIENTES-HUNTER.md` atualizado

---

## 2. Arquitetura e organização

- [x] Estrutura de pastas clara (`data/`, `templates/planilha/`)
- [x] Separação Leads / Clientes / Atividades (conceito + abas planilha)
- [x] `.gitignore` protege dados sensíveis
- [x] `.env.example` com placeholders (sem secrets)
- [ ] `CONTRIBUTING.md` lido por colaboradores
- [ ] Roadmap futuro documentado (Fases 3–7 no PLANO)
- [ ] Decisão Dia 22 (planilha vs Postgres) registrada quando chegar

---

## 3. Dados e planilha

- [x] Geo-cerca: 62 cidades em `data/geo-cerca-cidades.csv`
- [x] Colunas Leads documentadas (SETUP-GOOGLE-SHEETS.md)
- [x] Dropdowns fechados (status_funil, score, fonte, cidade)
- [x] 10 leads teste validados (`Leads-10-teste.csv`)
- [ ] Planilha Google importada e link guardado localmente (não no Git)
- [ ] Dashboard fórmulas testadas na planilha real
- [ ] Aba Clientes oculta/protegida na planilha
- [ ] Backup mensal em `data/backups/` (pasta ignorada)

---

## 4. Segurança e LGPD

- [x] `clientes-existentes.csv` no `.gitignore`
- [x] Regras LGPD documentadas (`SEGURANCA-LGPD.md`)
- [x] Mascaramento para IA (TELEFONE_OCULTO, CNPJ_OCULTO)
- [x] Limite WhatsApp 5–8 abordagens/dia definido
- [x] Sem scraping agressivo Instagram no MVP
- [ ] Colaborador recebeu CSV real por canal seguro (fora do Git)
- [ ] Opt-out documentado (motivo `Opt-out` no funil)
- [ ] Retenção 12 meses leads Perdido — política acordada

---

## 5. Operação e qualidade (testes manuais)

- [x] Funil padrão definido (7 estados incl. Descartado)
- [x] Critérios lead qualificado escritos
- [x] Regra loja feminina = Descartado
- [x] Regra ja_cliente = não prospecção fria
- [ ] Templates WhatsApp criados (Dia 6–7)
- [ ] Dry run: planilha → mensagem → link_wa_me < 2 min
- [ ] Playbook Instagram 5 min/perfil (Dia 8)
- [ ] Campo B1: 20 leads reais processados (Dia 10–15)
- [ ] KPI taxa agendamento calculado no Dashboard

---

## 6. GitHub profissional

- [x] README com descrição, stack, estrutura, progresso
- [x] CONTRIBUTING.md para colaboradores
- [x] Commit inicial com Conventional Commits
- [ ] Histórico limpo (sem commits genéricos)
- [ ] Descrição do repositório GitHub (~350 caracteres)
- [ ] Topics/tags: `prospeccao`, `crm`, `whatsapp`, `google-sheets`
- [ ] Screenshots planilha/Dashboard (quando tiver dados reais mascarados)
- [ ] LICENSE definida (se aplicável)

---

## 7. Colaboração (irmão / dev)

- [ ] Clone + leitura README + CONTRIBUTING concluídos
- [ ] Setup planilha feito seguindo SETUP-GOOGLE-SHEETS.md
- [ ] CSV clientes reais recebido offline
- [ ] Primeira tarefa atribuída (ex.: Dia 6 templates)
- [ ] Fluxo 4 especialistas entendido

---

## 8. Deploy e produção (futuro — pós Dia 22)

- [ ] Decisão go/no-go Postgres documentada
- [ ] Docker Compose app + Postgres
- [ ] HTTPS em produção
- [ ] JWT + rate limiting (multi-usuário)
- [ ] Backup criptografado
- [ ] Health check + logs sem PII

---

## 9. Apresentação (portfólio / recrutador)

- [x] Problema que resolve descrito (prospecção territorial B2B)
- [x] Diferencial: geo-cerca + score + HITL WhatsApp + LGPD desde MVP
- [x] Stack atual: Google Sheets, CSV, Cursor, docs Markdown
- [x] Roadmap técnico: Telegram → Postgres → Evolution → painel
- [ ] Desafios: anti-spam WA, não importunar clientes, qualificação multimarcas
- [ ] Métricas reais pós B1 (taxa agendamento)
- [ ] Demo GIF ou prints (planilha mascarada)

---

## 10. Plano pós-entrega

| Prioridade | Item |
|------------|------|
| P0 | Dias 6–9 — biblioteca comercial + playbook Insta |
| P1 | Dias 10–15 — campo real 20 leads + KPI |
| P2 | Dias 16–18 — visitas B2 |
| P3 | Dias 19–21 — IA assistente HITL |
| P4 | Dia 22 — gate Postgres |
| Backlog | n8n Telegram, import Maps, Evolution API, painel Kanban |

---

## Assinatura de release (preencher antes de push importante)

| Campo | Valor |
|-------|-------|
| Data | |
| Responsável | |
| Dia concluído | |
| Especialista Código | [ ] OK |
| Especialista Testes | [ ] OK |
| Recrutador (README/commits) | [ ] OK |
| Analista GitHub (este checklist) | [ ] OK |

---

*Checklist vivo — marque `[x]` conforme avança. Revisar ao fechar cada bloco do DIA-A-DIA.*
