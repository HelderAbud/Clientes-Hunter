# ADR 0001 — MVP em Google Sheets antes de PostgreSQL

- **Status:** Aceito
- **Data:** 2026-06-01
- **Decisores:** representante + revisor (Cursor)
- **Relacionado a:** DIA-A-DIA Dia 22 (gate Fase 3); PLANO §5, §6, §9 (Fase 3)

## Contexto

O Clientes Hunter precisa de um CRM para registrar leads, funil e KPI. Existe a
tentação de "já fazer direito" com PostgreSQL + API desde o início. Porém:

- A operação ainda é **individual** e de **baixo volume** (5–8 abordagens/dia).
- O valor a provar primeiro é **de processo** (qualificação, geo-cerca, HITL),
  não de tecnologia.
- Custo precisa ser **R$ 0** enquanto não há retorno comprovado (ver PLANO §6).

## Decisão

Operar o MVP inteiramente em **Google Sheets** (abas `Leads`, `Atividades`,
`Clientes`, `Hashtags`, `Dashboard`), com CSVs versionados como template.
A aba `KitsFotos` foi **descontinuada** em 2026-07-15 (foto de fachada fica
no campo, fora do repo). A migração para PostgreSQL **só é avaliada no gate
do Dia 22**, com critérios objetivos (ver abaixo).

## Consequências

**Positivas**
- Custo zero; começa hoje, sem setup de infraestrutura.
- Qualquer pessoa edita/entende sem conhecimento técnico.
- Foco em validar regras de negócio antes de codar.

**Negativas / custos**
- Sem deduplicação automática nem auditoria técnica robusta.
- Risco de inconsistência manual (mitigado por dropdowns/listas fechadas).
- Migração futura exigirá mapear colunas → tabelas.

**Quando reabrir esta decisão (gatilhos do Dia 22)**
- \> 200 leads **ou** duplicatas frequentes.
- Necessidade de histórico/auditoria técnica (tabela `events`).
- Mais de 1 usuário operando.
- Import automatizado (Maps) passa a compensar economicamente.

## Alternativas consideradas

| Alternativa | Por que NÃO (agora) |
|-------------|---------------------|
| PostgreSQL + API desde o início | Custo de tempo/infra sem valor de negócio provado; overengineering para 1 usuário |
| Planilha Excel local | Sem acesso multi-dispositivo, sem fórmulas colaborativas, backup manual frágil |
| Ferramenta de CRM paga (Pipedrive etc.) | Custo recorrente; menos controle sobre regras de geo-cerca/qualificação específicas |
