# ADR 0002 — WhatsApp manual com aprovação humana antes da Evolution API

- **Status:** Aceito
- **Data:** 2026-06-01
- **Decisores:** representante + revisor (Cursor)
- **Relacionado a:** REGRAS §7 (anti-spam); SEGURANCA-LGPD §6; PLANO Fase 6; CONTEXT (HITL)

## Contexto

O canal de contato é **100% WhatsApp Business**. Existe a opção de automatizar
envios com a **Evolution API** (fase futura). Porém:

- O número Business é **compartilhado com a carteira** existente — bloqueio
  significaria perder o canal principal de trabalho.
- Envio em massa frio tem **alto risco de spam/bloqueio** e fere boas práticas.
- Automação exige **VPS estável + chip dedicado** (custo ~R$ 30–120/mês) que só
  se justifica com volume comprovado.

## Decisão

No MVP, **toda** mensagem é **sugerida** (template ou IA) e **enviada
manualmente** pelo representante após revisão (HITL — *human in the loop*).
Nenhum disparo automático. Limites: **5–8 abordagens frias/dia**, **3–5
variações** de texto, horário **9h–17h**, sem lista de transmissão para fria.
A Evolution API só entra após maturidade operacional e decisão explícita.

## Consequências

**Positivas**
- Protege o número Business contra bloqueio.
- Mantém controle ético e de qualidade em cada mensagem.
- Custo zero de infraestrutura.

**Negativas / custos**
- Não escala além da capacidade manual diária.
- Depende da disciplina do operador (mitigado por etiquetas WA + checklist).

**Quando reabrir esta decisão**
- Volume de leads qualificados excede a capacidade manual de forma consistente.
- Houver **número dedicado** + orçamento para VPS + HTTPS.
- Regra inquebrável mesmo automatizado: só envia se `status = aprovado_pelo_representante`.

## Alternativas consideradas

| Alternativa | Por que NÃO (agora) |
|-------------|---------------------|
| Evolution API desde já | Risco de bloqueio do número compartilhado + custo de VPS sem volume que justifique |
| WhatsApp Cloud API (oficial Meta) | Custo, burocracia de aprovação de templates, overkill para o estágio |
| Lista de transmissão | Cara de spam, alto risco de denúncia/bloqueio em prospecção fria |
