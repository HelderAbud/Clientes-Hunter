# Grill — Dia 08 / Task A4 (Playbook Instagram)

- **Data:** 2026-06-02
- **Participantes:** representante + Cursor
- **Referência:** DIA-A-DIA-CLIENTES-HUNTER.md → Dia 8
- **Docs lidos:** REGRAS (§4 perfil, §6 canais, §8 score), SEGURANCA-LGPD (§5 Instagram), CONTEXT.md, geo-cerca-cidades.csv

## Escopo desta sessão

Criar a lista de hashtags (gerais + por cidade), o roteiro de triagem de 5 min
por perfil e alinhar a bio do Instagram do representante.

## O que NÃO vou mudar (limite de escopo)

- Não faço scraping nem login automatizado (só leitura manual de perfis públicos).
- Não envio DM — contato é só por WhatsApp.

## Perguntas respondidas

| # | Pergunta | Decisão acordada |
|---|----------|------------------|
| 1 | Quais cidades priorizar? | **Todas** as 51 cidades ABRIR |
| 2 | Estilo das hashtags? | **Gerais + por cidade** |
| 3 | Onde guardar o roteiro de 5 min? | **Só na planilha** (aba Hashtags como nota) |

## Entregue

- `templates/planilha/Hashtags.csv` regenerado: 10 hashtags gerais (`GERAL`) +
  51 hashtags por cidade ABRIR (geradas a partir de `geo-cerca-cidades.csv`).
- Roteiro de 5 min e bio do Instagram entregues no chat para colar na planilha.

## Termos atualizados em CONTEXT.md

- [x] Nenhum termo novo

## ADRs

- [x] Nenhum

## Riscos / dúvidas remanescentes

- Cidades ABRIR muito pequenas (ex.: Trombas, Mutunópolis, Mimoso de Goiás) têm
  pouca atividade no Instagram → nelas, **priorizar Google Maps** em vez de hashtag.
- Hashtag por cidade pode vir vazia; é normal — cruzar com hashtags gerais + localização.

## Aprovado para executar?

- [x] **Sim** — hashtags geradas; roteiro/bio para colar na planilha; triagem-teste de 5 perfis fica com o representante
