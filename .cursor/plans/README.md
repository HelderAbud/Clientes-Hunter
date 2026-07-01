# Planos Aprovados - Clientes Hunter

Esta pasta guarda planos aprovados para tarefas relevantes do projeto. Ela existe para manter rastreio entre sessoes do Cursor e evitar que decisoes importantes fiquem apenas no chat.

## Quando Criar Plano

Crie um plano quando a tarefa:

- mudar regra de negocio, funil, score, geo-cerca, templates WhatsApp, planilha ou KPI;
- envolver dados sensiveis, LGPD, automacao, integracao externa, backend ou banco;
- precisar de mais de uma fatia de entrega;
- tiver ambiguidade suficiente para exigir aprovacao antes de editar.

Nao precisa criar plano para typo, ajuste pequeno de texto, rename localizado ou mudanca trivial sem risco.

## Nome Do Arquivo

Use:

```text
plan-YYYY-MM-DD-assunto-curto.md
```

Exemplos:

```text
plan-2026-07-01-dia-08-playbook-instagram.md
plan-2026-07-01-templates-whatsapp-posvisita.md
plan-2026-07-01-gate-dia-22-postgres.md
```

## Estrutura Minima

Cada plano deve conter:

- objetivo;
- trilha escolhida: `Simple`, `Normal`, `Complex` ou `Hotfix`;
- contrato minimo afetado;
- fatias verticais;
- criterios de aceite;
- validacao prevista;
- riscos e gates humanos;
- rollback ou caminho de reversao quando aplicavel.

## Checklist Antes De Executar

- [ ] O objetivo esta claro.
- [ ] O plano cita os documentos fonte corretos.
- [ ] Nao ha dados reais ou sensiveis no plano.
- [ ] O escopo respeita o MVP manual e o gate do Dia 22.
- [ ] As fatias sao pequenas e verificaveis.
- [ ] O usuario aprovou a execucao.

