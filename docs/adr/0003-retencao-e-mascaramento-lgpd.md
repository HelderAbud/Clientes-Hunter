# ADR 0003 — Retenção 12 meses, dados sensíveis fora do Git e mascaramento para IA

- **Status:** Aceito
- **Data:** 2026-06-01
- **Decisores:** representante + revisor (Cursor)
- **Relacionado a:** SEGURANCA-LGPD (todo); REGRAS §10; `.gitignore`; CHECKLIST §4

## Contexto

O projeto trata dados de terceiros (lojistas): nome fantasia, telefone/WhatsApp
comercial e, na base de clientes existentes, **CNPJ**. Isso obriga decisões de
LGPD que são **difíceis de reverter** depois que dados vazam:

- O que pode/não pode ir para o Git (repositório pode virar público/portfolio).
- Por quanto tempo guardar leads que não evoluíram.
- O que pode ser enviado para uma IA (Cursor) durante a operação.

## Decisão

1. **Fora do Git, sempre:** `data/clientes-existentes.csv`, `data/_pdf_raw.txt`,
   qualquer `*.pdf` de clientes, exports com telefones, `.env`, cookies/sessão.
   Garantido por [`.gitignore`](../../.gitignore).
2. **Minimização:** leads guardam só o necessário para prospecção B2B (sem CPF,
   sem endereço residencial, sem dado financeiro).
3. **Retenção:** leads `Perdido` são arquivados/apagados após **12 meses**
   (ajustável). Pedido de não-contato → `Descartado` + motivo `Opt-out`, nunca reabordar.
4. **Mascaramento para IA:** antes de colar no chat, telefone → `TELEFONE_OCULTO`,
   CNPJ → `CNPJ_OCULTO`; nunca enviar CSV/PDF inteiro nem tokens/cookies.

## Consequências

**Positivas**
- Repositório seguro para virar portfolio público sem vazar PII.
- Base legal clara (interesse legítimo B2B + transparência no 1º contato).
- Reduz superfície de risco ao usar IA na operação diária.

**Negativas / custos**
- Operador precisa lembrar de mascarar (mitigado por checklist em SEGURANCA §9).
- Dados reais ficam fora do versionamento → backup local manual em `data/backups/` (ignorado).

**Quando reabrir esta decisão**
- Migração para banco (Fase 3): revisar criptografia em repouso, `sanitizeForAI()` no código, tabela de auditoria.
- Operação multiusuário: revisar controle de acesso e contrato de tratamento de dados.

## Alternativas consideradas

| Alternativa | Por que NÃO |
|-------------|-------------|
| Versionar tudo (inclusive CSV real) | Vazamento de CNPJ/telefones; reprova auditoria; risco se repo for público |
| Sem política de retenção | Acúmulo de PII sem finalidade fere minimização da LGPD |
| Enviar dados crus para IA | Exposição desnecessária de dados pessoais a terceiros |
