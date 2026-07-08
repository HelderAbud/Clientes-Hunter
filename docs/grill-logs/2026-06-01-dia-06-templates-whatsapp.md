# Grill — Dia 06 / Task A3.1 (Templates WhatsApp + etiquetas)

- **Data:** 2026-06-01
- **Participantes:** representante + Cursor
- **Referência:** DIA-A-DIA-CLIENTES-HUNTER.md → Dia 6
- **Docs lidos:** REGRAS (§4 perfil, §7 anti-spam), SEGURANCA-LGPD (§4, §6), CONTEXT.md

## Escopo desta sessão

Criar a biblioteca comercial de primeiro contato: etiquetas de WhatsApp por
estágio do funil e 3 templates de primeiro contato (variações anti-spam) com
placeholders. Validar o fluxo planilha → texto → `link_wa_me` em dry run.

## O que NÃO vou mudar (limite de escopo)

- Não envio nenhuma mensagem real (só dry run).
- Não crio templates de confirmação/pós-visita (isso é Dia 7 / Task A3.2).
- Não altero regras de geo-cerca, score ou funil.

## Perguntas respondidas

| # | Pergunta | Resposta acordada | Recomendação do revisor |
|---|----------|-------------------|-------------------------|
| 1 | Prefixo das etiquetas WA? | **Sem prefixo** (Novo, Contato, Agenda, Visita, Fechado, Perdido, Não abordar) | Eu sugeri `CH-`; representante preferiu sem prefixo (mais limpo no celular) |
| 2 | Tom do primeiro contato? | **Caloroso e regional, conciso** | Concordo — representante local gera confiança B2B |
| 3 | Citar a marca representada no 1º contato? | **Sim** — criar placeholder `{marca}` e identificar-se como representante | Concordo — transparência reforça base legal LGPD (interesse legítimo + identificação) |
| 4 | Onde salvar a biblioteca? | **Só na aba `KitsFotos` da planilha** — nada no repositório | Aceito; templates entregues no chat para colar na planilha |

## Termos atualizados em CONTEXT.md

- [x] Nenhum termo novo (placeholders usam termos já definidos: loja, cidade, marca, região)

## ADRs

- [x] Nenhum — decisão facilmente reversível (texto de template), sem trade-off difícil

## Checklist pré-execução

- [x] Li o Dia 6 e os docs de apoio
- [x] Termos batem com `CONTEXT.md`
- [x] Sei o critério **"Pronto quando"**: escolher template + abrir WA em < 2 min
- [x] Sei como validar: dry run em 1 lead teste, sem enviar
- [x] Dados sensíveis: templates só com placeholders; nenhum telefone/CNPJ real; nada sensível no repositório

## Placeholders padronizados

`{loja}` · `{cidade}` · `{regiao}` · `{seu_nome}` · `{marca}`

## Riscos / dúvidas remanescentes

- Confirmar na operação se 3 variações bastam para o limite de 5–8/dia (pode subir para 5 no Dia 7 se repetir muito).
- Garantir alternância manual das variações (anti-spam) — sem automação no MVP.

## Aprovado para executar?

- [x] **Sim** — alinhado via grill em 2026-06-01
- [ ] Não — pendências: ___
