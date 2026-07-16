# CONTEXT — Vocabulário de domínio do Clientes Hunter

> Fonte única de verdade dos **termos de domínio**. Antes de cada Dia/Task (ver
> [`DIA-A-DIA-CLIENTES-HUNTER.md`](DIA-A-DIA-CLIENTES-HUNTER.md)), o grill
> (ver [`docs/grill-logs/`](docs/grill-logs/)) confirma estes termos. Quando um
> termo novo surgir ou mudar de significado, **atualize aqui primeiro** e cite no log do grill.
>
> Regras completas vivem em [`REGRAS-CLIENTES-HUNTER.md`](REGRAS-CLIENTES-HUNTER.md);
> privacidade em [`SEGURANCA-LGPD.md`](SEGURANCA-LGPD.md). Este arquivo é o **dicionário curto**.

---

## Por que este arquivo existe

O Clientes Hunter tem regras sutis (geo-cerca, "multimarcas real", "já cliente",
loja feminina). Sem um vocabulário único, mensagens, prompts de IA e futuros
campos de planilha/banco nascem com nomes divergentes. Este arquivo evita isso:
**um termo, uma definição, em um lugar.**

---

## Glossário canônico

| Termo | Significa (definição acordada) | Não confundir com |
|-------|-------------------------------|-------------------|
| **Lead** | Registro de uma loja **já triada** (ou em triagem) na planilha de prospecção fria | **Candidato** (pré-triagem); Cliente existente |
| **Candidato** | Loja sugerida pela **coleta assistida** (ex.: Places), ainda **não** qualificada; `status_revisao` = Pendente/Qualificado/Descartado | Lead qualificado; linha pronta para WhatsApp |
| **Lead qualificado** | Loja masculina/multimarcas, dentro da geo-cerca, com indício de WhatsApp, **≥4 marcas masculinas**, **não** cliente existente | Qualquer loja encontrada (candidato ou lead bruto) |
| **Coleta assistida** | Busca limitada via **Google Places API** (oficial) gerando CSV de candidatos; triagem e WA continuam humanos ([ADR 0004](docs/adr/0004-coleta-assistida-google-places.md)) | Scraping HTML; bot Instagram; envio automático de WA |
| **`status_revisao`** | Estado do candidato: `Pendente` / `Qualificado` / `Descartado` (antes de virar lead no funil) | `status_funil` (só após promoção a lead) |
| **Geo-cerca** | Lista **fechada** de 62 cidades (DF + Norte GO) em [`data/geo-cerca-cidades.csv`](data/geo-cerca-cidades.csv) onde a prospecção é válida | Raio em km / mapa de calor |
| **`status_cidade` = ABRIR** | Cidade priorizada para caçar lojas **novas** (prospecção fria) | OK |
| **`status_cidade` = OK** | Carteira já trabalhada; foco em **reativação**, não prospecção massiva | ABRIR |
| **Multimarcas real** | **≥ 4 marcas masculinas distintas** nos últimos 12 posts do Instagram (ajustável) | "Diz ser multimarcas" na bio sem prova |
| **Loja feminina** | Loja **exclusivamente** feminina → **descarte obrigatório** na prospecção fria | Loja mista com seção masculina clara (pode qualificar) |
| **Já cliente / cliente existente** | Consta em [`data/clientes-existentes.csv`](data/clientes-existentes.csv) (178 registros, fora do Git) ou bio/posts mostram que já vende a marca representada | Lead novo |
| **Reativação** | Contato com cliente existente inativo — mensagem diferente, **não conta** no KPI de prospecção fria | Prospecção fria |
| **Score** | Prioridade do lead: **Alto / Médio / Baixo**. Só Alto e Médio entram na fila de WhatsApp do dia | Status do funil |
| **Funil (`status_funil`)** | Estado do lead no processo (7 valores, lista fechada — ver abaixo) | Score |
| **Descartado** | Lead removido da prospecção; sempre acompanhado de `motivo_descarte` | Perdido (chegou ao funil e não fechou) |
| **`motivo_descarte`** | Texto curto padronizado: `Loja feminina`, `Fora da geo-cerca`, `Sem WhatsApp`, `Multimarcas fraco`, `Infantil only`, `Ja cliente existente`, `Opt-out` | Observação livre |
| **Abordagem fria** | Primeiro contato WhatsApp com lead novo (limite **5–8/dia**) | Reativação / follow-up |
| **HITL (aprovação humana)** | Toda mensagem é **sugerida** pela IA/template e **enviada manualmente** após você revisar | Envio automático |
| **Disparo** | Envio efetivo da mensagem (no MVP, **sempre manual**) | Automação Evolution (fase futura) |
| **Opt-out** | Loja pediu para **não ser contatada** → `Descartado` + motivo `Opt-out`, nunca reabordar | Lead "Perdido" |
| **Foto de fachada** | Evidência visual da loja capturada pelo representante no campo (celular/Drive pessoal); **fora do repo e sem aba obrigatória na planilha** | Kit de fotos / aba `KitsFotos` (descontinuados no MVP) |
| **Fonte** | De onde o lead veio: `Instagram` / `Maps` / `Guia` / `Indicação` (`Maps` inclui Places API) | Canal de contato (sempre WhatsApp) |
| **MVP** | Sheets + CSV + Cursor + WhatsApp HITL; **coleta assistida Places** autorizada (piloto Brasília, ADR 0004); CRM continua sem Postgres | App Postgres completo; Evolution; scrape |

---

## Funil padrão (`status_funil` — lista fechada)

```
Novo lead → Contato prévio feito → Agendamento de visita → Visita com mostruário → Pedido fechado
                                                                                   ↘ Perdido
(qualquer ponto)                                                                   → Descartado
```

Valores aceitos (sem digitação livre): `Novo lead`, `Contato prévio feito`,
`Agendamento de visita`, `Visita com mostruário`, `Pedido fechado`, `Perdido`, `Descartado`.

---

## KPIs (nomes oficiais)

| KPI | Fórmula | Observação |
|-----|---------|------------|
| **Taxa de agendamento** (principal) | `agendamentos confirmados ÷ leads qualificados` | Só prospecção fria; reativação não entra |
| Taxa de comparecimento | `visitas realizadas ÷ agendamentos confirmados` | Apoio |
| Taxa de fechamento pós-visita | `pedidos fechados ÷ visitas realizadas` | Apoio |
| Tempo médio até agendamento | dias entre 1º contato e confirmação | Apoio |

---

## Limites operacionais (resumo — detalhe em REGRAS)

- **5–8** abordagens frias novas por dia (número Business compartilhado).
- **3–5 variações** de texto de primeiro contato; alternar.
- **No máximo 1 abordagem por loja/dia**; follow-up só em outro dia.
- Horário **9h–17h** (preferencial; **nunca após as 18h**); nunca lista de transmissão para fria.
- Instagram: só perfis públicos, **8–12 perfis triados/dia**, leitura manual.
- Coleta Places (quando ativa): **1 cidade/run**, cap **≤ 40** candidatos; exports só em `data/exports/` (fora do Git).

---

## Termos reservados para fases futuras (não usar como se já existissem)

`PostgreSQL`, `tabela events`, `deduplicação automática`, `Evolution API`,
`n8n`, `JWT`, `sanitizeForAI()`, `painel Kanban`, scraping Instagram automatizado.
Só entram no vocabulário ativo **após decisão registrada** (Dia 22 / ADR).

**Já autorizados por ADR (não são “futuro vazio”):**
- Coleta assistida Google Places — [ADR 0004](docs/adr/0004-coleta-assistida-google-places.md) (piloto; script local + CSV).
- WhatsApp continua HITL — [ADR 0002](docs/adr/0002-whatsapp-manual-hitl-antes-de-evolution.md).

---

*Documento vivo. Ao fechar um Dia/Task que mude uma regra de negócio, atualize o termo aqui e registre no grill log correspondente.*
*Última atualização relevante: 2026-07-16 — candidato + coleta assistida (Fatia 1).*