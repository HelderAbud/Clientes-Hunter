# ADRs — Architecture Decision Records (Clientes Hunter)

Registros curtos de **decisões difíceis de reverter**. Adaptado do padrão usado
no projeto Loja Sistema.

## Quando criar um ADR (as 3 condições juntas)

Crie um ADR **somente** se **todas** forem verdadeiras:

1. **Difícil de reverter** depois (custo, dados, hábito operacional).
2. Um futuro leitor vai perguntar **"por que assim?"**.
3. Houve **alternativa real** (a escolha não foi óbvia).

Decisões triviais (renomear coluna, ajustar texto de template) **não** viram ADR —
vão no log do grill ou direto no commit.

## Formato

Use [`TEMPLATE.md`](TEMPLATE.md). Nome do arquivo: `NNNN-slug-curto.md`
(numeração sequencial, 4 dígitos).

## Status possíveis

`Proposto` → `Aceito` → (pode virar) `Substituído por NNNN` ou `Obsoleto`.

## Índice

| # | Decisão | Status |
|---|---------|--------|
| [0001](0001-mvp-em-sheets-antes-de-postgres.md) | MVP em Google Sheets antes de PostgreSQL | Aceito |
| [0002](0002-whatsapp-manual-hitl-antes-de-evolution.md) | WhatsApp manual com aprovação humana antes da Evolution API | Aceito |
| [0003](0003-retencao-e-mascaramento-lgpd.md) | Retenção 12 meses + dados sensíveis fora do Git + mascaramento para IA | Aceito |
