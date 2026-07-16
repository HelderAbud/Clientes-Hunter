# Grill logs — Clientes Hunter

Registro curto da **conversa de alinhamento** ("grill") feita **antes** de
executar um Dia/Task do [`DIA-A-DIA-CLIENTES-HUNTER.md`](../../DIA-A-DIA-CLIENTES-HUNTER.md).
Adaptado do padrão do projeto Loja Sistema para a realidade **operacional**
(planilha + WhatsApp manual), não de código.

## O que é o grill (versão Clientes Hunter)

Antes de tocar na planilha, nos templates ou nas regras, você (ou o Cursor)
questiona cada decisão do dia:

- "Isso bate com as [`REGRAS`](../../REGRAS-CLIENTES-HUNTER.md) e o [`CONTEXT`](../../CONTEXT.md)?"
- "Que termo de domínio usar? (geo-cerca, multimarcas real, já cliente...)"
- "Como vou saber que ficou **Pronto**?" (critério objetivo)
- "Tem dado sensível? Preciso mascarar para a IA?" (ver [`SEGURANCA-LGPD`](../../SEGURANCA-LGPD.md))

O agente faz **uma pergunta de cada vez** até alinhar. No fim, gera o log.

## Quando fazer (e quando pular)

| Situação | Grill? |
|----------|--------|
| Dia que muda regra de negócio, planilha ou cria template (ex.: Dia 6, Dia 8, Dia 20) | **Sim** |
| Decisão difícil de reverter | **Sim** + abrir [ADR](../adr/) |
| Ajuste trivial (corrigir typo, link) | Não — direto |

## Como usar

1. Copie [`TEMPLATE.md`](TEMPLATE.md).
2. Salve como `AAAA-MM-DD-dia-NN-tema.md` (ex.: `2026-06-02-dia-06-templates-whatsapp.md`).
3. Preencha durante a conversa de alinhamento.
4. Só comece a executar o Dia com o campo **"Aprovado para executar"** marcado.

## Prompt para iniciar (cole no Cursor)

```
Grill antes do Dia N do Clientes Hunter.

Ponto de partida: DIA-A-DIA-CLIENTES-HUNTER.md (Dia N)
Apoio: REGRAS, SEGURANCA-LGPD, CONTEXT.md

Antes de eu executar:
1. Leia o Dia N e os docs de apoio
2. Confirme os termos de domínio em CONTEXT.md
3. Faça perguntas UMA DE CADA VEZ até alinharmos
4. Para cada resposta, diga sua recomendação
5. Se surgir decisão difícil de reverter, proponha um ADR em docs/adr/
6. Ao final, preencha o log em docs/grill-logs/ no formato do TEMPLATE.md
```

## Índice de logs

| Data | Dia/Task | Tema | Arquivo |
|------|----------|------|---------|
| 2026-06-01 | Dia 6 / A3.1 | Templates WhatsApp + etiquetas | [2026-06-01-dia-06-templates-whatsapp.md](2026-06-01-dia-06-templates-whatsapp.md) |
| 2026-06-01 | Dia 7 / A3.2 | Confirmação + pós-visita + kits *(superseded)* | [2026-06-01-dia-07-confirmacao-posvisita-kits.md](2026-06-01-dia-07-confirmacao-posvisita-kits.md) |
| 2026-06-02 | Dia 8 / A4 | Playbook Instagram (hashtags + roteiro) | [2026-06-02-dia-08-playbook-instagram.md](2026-06-02-dia-08-playbook-instagram.md) |
| 2026-07-15 | Dia 7 / contrato | Descontinuar kits + fechar Task A3 | [2026-07-15-descontinuar-kits-fotos.md](2026-07-15-descontinuar-kits-fotos.md) |
| 2026-07-16 | Complex / Gate 3 | Coleta assistida Places — hardening + ADR 0004 | [2026-07-16-gate3-coleta-assistida-places.md](2026-07-16-gate3-coleta-assistida-places.md) |
| 2026-07-16 | Complex / Gate 4 | Plano fatias + análise LGPD/Git | ver `.cursor/plans/plan-2026-07-16-coleta-assistida-places.md` |
| 2026-07-16 | Complex / Fatia 1 | Contrato candidato + coleta assistida | [2026-07-16-fatia1-contrato-coleta-assistida.md](2026-07-16-fatia1-contrato-coleta-assistida.md) |
| 2026-07-16 | Complex / A+B | Pausar Places pago; caminho 3b zero-custo | [2026-07-16-pausar-places-caminho-zero-custo.md](2026-07-16-pausar-places-caminho-zero-custo.md) |
| 2026-07-16 | Complex / 3b+4 | Organizador CSV + checklist triagem | [2026-07-16-fatia3b-4-organizador-checklist.md](2026-07-16-fatia3b-4-organizador-checklist.md) |
| 2026-07-16 | Complex / Fatia 5 | Dry-run (HITL) — em andamento | [COMO-FAZER-FATIA-5.md](COMO-FAZER-FATIA-5.md) · [validation-…](validation-2026-07-16-fatia5-dry-run-candidatos.md) |
