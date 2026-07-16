# Spec — Coleta assistida via Google Places (piloto Brasília)

| Campo | Valor |
|-------|--------|
| **Status** | **Aprovada** (Gate 2) · **Hardened v1.1** (Gate 3) · 2026-07-16 |
| **Versão** | 1.1 |
| **Trilha Helder** | Complex |
| **Skill** | `to-spec` + spec-hardening |
| **Discovery** | [discovery-2026-07-16-coleta-assistida-places.md](discovery-2026-07-16-coleta-assistida-places.md) |
| **ADR** | [docs/adr/0004-coleta-assistida-google-places.md](../../docs/adr/0004-coleta-assistida-google-places.md) |
| **Gates** | 0–3 autorizados / cumpridos |

---

## Problem

A busca manual de lojas (Instagram/Maps, uma a uma) não escala para o tempo disponível do representante. É necessário gerar, de forma **oficial e limitada**, uma lista de **candidatos** em Brasília (telefone/endereço/nome) para triagem humana e prospecção WhatsApp HITL — sem scraping e sem envio automático.

## Scope

### In scope (este corte)

1. **Contrato:** atualizar glossário e segurança para autorizar **coleta assistida** via Google Places API (conector oficial), mantendo proibido scraping / bot Insta / WA automático.
2. **Piloto:** uma execução para cidade **Brasília (DF)** (`status_cidade = ABRIR`).
3. **Artefato técnico mínimo:** script local (Python recomendado) que:
   - lê chave de `.env` (`GOOGLE_PLACES_API_KEY`);
   - consulta Places (Text Search / Nearby — detalhe na fatia de build);
   - aplica filtro de geo-cerca (só Brasília neste spike);
   - deduplica por `place_id`;
   - grava CSV de **candidatos** (não mistura direto como lead qualificado).
4. **Template CSV** versionado (só cabeçalho + 1–2 linhas fictícias) + guia curto de import/revisão.
5. **Fluxo humano:** candidato `Pendente` → triagem (feminina / já cliente / WA / multimarcas) → promove para `Leads` ou `Descartado`.
6. **ADR 0004** (Aceito no Gate 3).

### Out of scope

- Scraping Google Maps HTML, Instagram, cookies, rotação de IP.
- Envio automático de WhatsApp / Evolution API / lista de transmissão.
- Contagem automática de marcas nos posts (Fase 5).
- PostgreSQL / API JWT / painel web (fase seguinte se o piloto valer).
- Varredura de todas as 62 cidades de uma vez.
- Commit de telefones reais ou de `clientes-existentes.csv`.
- Alterar KPI principal ou limites diários de WA (5–8, 9h–17h).

## Acceptance criteria

- [ ] Existe termo **candidato** (e **coleta assistida**) em `CONTEXT.md`, alinhado a esta spec.
- [ ] `SEGURANCA-LGPD.md` e `REGRAS` (trecho canais/coleta) permitem Places API oficial e continuam proibindo scrape/bot/WA auto.
- [ ] ADR 0004 Aceito: Places sim · scrape não · WA HITL · piloto Brasília.
- [ ] Script (ou comando documentado) produz CSV de candidatos para Brasília com colunas mínimas: `place_id`, `nome`, `cidade`, `endereco`, `telefone`, `site`, `maps_url`, `fonte`, `coletado_em`, `status_revisao`.
- [ ] `fonte` = `Maps`.
- [ ] Cap de resultados no piloto: **≤ 40** linhas por execução (configurável; default 40).
- [ ] Template no repo **sem** telefone real; exports reais em pasta gitignored ou só local.
- [ ] Checklist humano documentado: nenhum WA sem triagem; cruzar já-cliente offline.
- [ ] Dry-run: executar 1x com chave local → lista revisável (aceite qualitativo do representante).

## Decisions

| # | Decisão | Origem |
|---|---------|--------|
| D1 | Fonte #1 = Google Places API (oficial) | Gate 0 |
| D2 | Cidade piloto = **Brasília** | Gate 1 |
| D3 | Candidato ≠ lead qualificado até triagem humana | Discovery |
| D4 | Stack do spike = script local + CSV (não Postgres no 1º corte) | Discovery |
| D5 | Instagram continua manual neste corte | Gate 0 |
| D6 | Antecipa Fase 4 do PLANO; não exige app Postgres completo | Complex / ADR 0004 |
| D7 | NFRs e limites fechados na seção Hardening abaixo | Gate 3 |

### Test seam (nível mais alto)

**CSV de saída do script** (colunas + `cidade` Brasília + `place_id` único + cap ≤ 40).

---

## Hardening (v1.1) — NFR / limites / rollback

### Non-functional requirements

| NFR | Requisito |
|-----|-----------|
| **Segurança** | Chave só em `.env`; nunca logar a key; exports reais fora do Git |
| **LGPD** | Minimização (campos da spec); finalidade B2B; mascarar se colar no chat |
| **Confiabilidade** | Sem chave ou falha HTTP → exit ≠ 0 e mensagem clara; não gravar CSV parcial silencioso sem flag |
| **Custo** | Default `max_results=40`; documentar alerta de billing no Cloud |
| **Operação** | 1 cidade/run no piloto; termos de busca configuráveis por argumento/env |
| **Observabilidade** | Log local: cidade, qtd resultados, `coletado_em` (sem dump de PII no stdout em modo default) |
| **Compatibilidade** | CRM continua Sheets; script é lateral ao MVP documental |

### Limites fechados (piloto)

| Limite | Valor |
|--------|--------|
| Cidades / execução | 1 (`BRASILIA`) |
| Resultados / execução | ≤ 40 |
| Execuções recomendadas / dia (piloto) | ≤ 1 |
| Promoção a lead | só humana |
| Disparo WA | só HITL manual |

### Rollback

1. Revogar/restringir chave no Google Cloud.  
2. Apagar `data/exports/` (ou pasta local gitignored) com CSV reais.  
3. Se abortar a iniciativa: reverter fatia de contrato + marcar ADR 0004 como Obsoleto.  
4. Código do script pode permanecer desabilitado (sem `.env` = no-op operacional).

### Exceções explícitas

- Não há SLA de uptime (script local).  
- Qualidade do telefone Places não é garantida = WA (aceitável; triagem humana).

---

## Risks

| Risco | Severidade | Mitigação |
|-------|------------|-----------|
| Custo / billing Places | Média | Cap ≤ 40; 1 cidade; alertas Cloud |
| Falsos positivos | Alta | Fila `Pendente` + HITL |
| Telefone ≠ WhatsApp | Média | Motivo `Sem WhatsApp` |
| Vazamento PII no Git | Alta | `.gitignore` + ADR 0003 |
| Drift “MVP sem API” | Média | ADR 0004 + CONTEXT |
| Termos Google | Alta | Só API oficial |

## Verification

1. Diff de contrato sem PII.  
2. Script + `.env` local → CSV inspecionado.  
3. Zero WA / zero Instagram no pipeline.  
4. ≥ 3 candidatos triados (Qualificado ou Descartado).  
5. Grill/validation após piloto.

## Próximos gates

| Gate | Conteúdo | Autorização |
|------|----------|-------------|
| **4** | `to-issues` → plano com fatias | `autorizo gate 4` |
| **5** | Executar fatia N | `autorizo fatia N` |

---

## Aprovação

- [x] Gate 2: `aprovo spec` (2026-07-16)
- [x] Gate 3: hardening + ADR 0004 Aceito (2026-07-16)
- [ ] Gate 4: plano de fatias
- [ ] Implementação: só com autorização por fatia
