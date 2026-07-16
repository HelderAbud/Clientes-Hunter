# Discovery — Coleta assistida (Google Places)

| Campo | Valor |
|-------|--------|
| **Status** | Gate 1 concluído · cidade piloto **Brasília** · Gate 2 spec em andamento |
| **Data** | 2026-07-16 |
| **Trilha Helder** | Complex |
| **Skill** | `context-discovery` (antes de `to-spec`) |
| **Gate 0** | Autorizado — busca automática; WA continua HITL; fonte #1 Places API |

---

## 1. Problema (confirmado)

Busca manual loja a loja (Instagram/Maps) consome tempo demais. O representante precisa de uma **lista candidata** por cidade da geo-cerca (nome + telefone + endereço), para **triar e contactar** no WhatsApp Business com aprovação humana.

## 2. O que o repo já diz (Path A)

| Fonte | Achado |
|-------|--------|
| `CONTEXT.md` | MVP = Sheets + CSV + WA manual; backend só pós-Dia 22 |
| `SEGURANCA-LGPD.md` | Proibido no MVP: bot Insta, scraping em massa, rotação IP, DM fria em massa |
| `PLANO` Fase 4 | Coleta assistida: **um** conector (Maps/guias) → import → log de rejeitados |
| `PLANO` Fase 5–6 | Instagram enriquecimento e WA via API = **depois**, não no primeiro corte |
| `ADR 0001` | Sheets antes de Postgres; gate Dia 22 |
| Geo-cerca | 62 cidades; status `ABRIR` / `OK` |

**Implicação:** autorizar coleta Places = **antecipar Fase 4** e **atualizar contrato** (SEGURANCA/CONTEXT/REGRAS/TRILHA) no Gate de spec/ADR — ainda sem scraping Instagram.

## 3. Modelo alvo (MVP coleta)

```text
Input:  1 cidade ABRIR + termos de busca (ex.: "loja de roupa masculina")
        + Google Places API (oficial)
Process: filtrar geo-cerca → dedupe por place_id → excluir já-cliente (offline)
Output: CSV/aba "Candidatos" (revisão humana)
Humano: 5 min/loja → qualifica ou descarta → Leads → WA HITL
```

**Não automatizar neste MVP:** envio WhatsApp, DM Instagram, login em redes, scrape de posts para contar marcas.

## 4. Campos mínimos a coletar (Places)

| Campo | Obrigatório? | Uso |
|-------|--------------|-----|
| `place_id` | Sim | Dedupe / auditoria |
| `nome` (fantasia) | Sim | Lead |
| `cidade` | Sim | Geo-cerca |
| `endereco` | Sim | Conferência |
| `telefone` | Desejável | WA (comercial) |
| `site` | Opcional | Achar Insta depois (manual) |
| `maps_url` | Sim | Rastreio |
| `fonte` | Sim | valor fixo `Maps` (Places) |
| `coletado_em` | Sim | LGPD / auditoria |
| `status_revisao` | Sim | `Pendente` / `Qualificado` / `Descartado` |

Instagram **não** vem da Places API de forma confiável → enriquecimento manual ou Fase 5 depois.

## 5. Limites operacionais sugeridos (spike)

| Limite | Recomendação | Motivo |
|--------|--------------|--------|
| Cidades por execução | **1** | Custo + revisão humana |
| Resultados por busca | **≤ 20–40** (cap no spike) | Evitar dump massivo |
| Execuções / dia | **1** no piloto | LGPD + anti-spam de processo |
| Após import | Só score Alto/Médio → fila WA | Contrato atual |
| WA | Continua 5–8/dia, HITL | Sem mudança |

## 6. Segurança / LGPD (pré-requisitos da spec)

- Chave API só em `.env` / secret local — **nunca** no Git.
- Telefones reais: não commitar CSV de produção; template com dados fictícios no repo.
- Finalidade: prospecção B2B comercial na geo-cerca.
- Opt-out e “já cliente” continuam regras humanas antes do envio.
- IA: se usar Cursor com export, mascarar `TELEFONE_OCULTO`.

## 7. Stack sugerida para o spike (ainda não escolhida na spec)

| Opção | Prós | Contras |
|-------|------|---------|
| **A — Script Python local** + CSV → Sheets | Rápido, barato, fatia fina | Sem UI |
| **B — Postgres + API** (Fase 3 completa) | Histórico sério | Mais lento para o 1º valor |
| **C — Só Google Sheets + Apps Script** | Zero backend | Limites e manutenção no Sheets |

**Recomendação discovery:** começar com **A** (script + CSV), import manual/planilha; Postgres só se o piloto provar valor.

## 8. Conflitos de glossário a resolver na spec

| Termo hoje | Tensão | Proposta |
|------------|--------|----------|
| MVP “sem API” | Places precisa de API Google | Novo termo: **coleta assistida** (autorizada pós-gate) |
| “Sem scraping” | Places API ≠ scraping | Manter proibição de scrape; permitir **conector oficial Places** |
| Lead vs candidato | Import bruto ainda não é lead qualificado | Introduzir **candidato** (pré-triagem) vs **lead** |

## 9. Riscos

| Risco | Mitigação |
|-------|-----------|
| Custo Places estoura | Cap por cidade + billing alert no Cloud |
| Muitos falsos (loja feminina, shopping genérico) | Fila `Pendente` + triagem humana obrigatória |
| Telefone fixo ≠ WhatsApp | Humano valida; motivo `Sem WhatsApp` |
| Termos Google | Só API oficial; sem HTML scrape |
| Pular qualificação | Spec: import **nunca** dispara WA |

## 10. Critério de pronto do discovery (Gate 1)

- [x] Problema e fonte #1 alinhados (Gate 0)
- [x] Modelo alvo e fora de escopo escritos
- [x] Campos mínimos e limites sugeridos
- [x] Opções de stack com recomendação
- [x] **Cidade piloto** confirmada: **Brasília (DF)** — 2026-07-16
- [ ] Orçamento/custo Cloud aceito em princípio (tratar na spec / Gate 3)

## 11. Próximo gate

**Gate 2 — `to-spec`:** escrever `spec-2026-07-16-coleta-assistida-places.md` com acceptance criteria testáveis.  
Só após: confirmação da cidade piloto + `autorizo gate 2`.

---

## Pergunta única (context-discovery) — respondida

**Cidade piloto:** Brasília (DF) — confirmado 2026-07-16.

**Gate 2:** spec em [`spec-2026-07-16-coleta-assistida-places.md`](spec-2026-07-16-coleta-assistida-places.md).

