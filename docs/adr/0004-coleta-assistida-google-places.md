# ADR 0004 — Coleta assistida via Google Places (piloto Brasília) antes de scrape/Instagram/WA auto

- **Status:** Aceito · **implementação Places adiada** (2026-07-16 — orçamento)
- **Data:** 2026-07-16
- **Decisores:** representante + Cursor (Helder Complex — Gates 0–3)
- **Relacionado a:** [spec](../../.cursor/plans/spec-2026-07-16-coleta-assistida-places.md); [plan](../../.cursor/plans/plan-2026-07-16-coleta-assistida-places.md); PLANO Fase 4; ADR 0001–0003

## Emenda operacional (2026-07-16)

Billing Google Places **indisponível** no momento. Mantém-se a decisão (Places oficial quando houver custo).  
**Até lá:** caminho zero-custo = busca manual + **organizador CSV** (Fatia 3b do plano) — sem scrape, sem API paga.  
Retomar Fatia 3 Places só com autorização explícita + chave.

## Contexto

O MVP manual (Sheets + busca loja a loja) não cabe no tempo do representante. Há
pressão para “buscar na internet sozinho”. Alternativas inseguras (scraping Maps/Instagram,
bot logado, disparo em massa) violam termos, LGPD e o ADR 0002 (WA HITL).

O PLANO já previa **Fase 4 — coleta assistida** com um conector oficial. O gate do
Dia 22 / ADR 0001 tratava Postgres; aqui autorizamos **só a coleta**, sem exigir
banco ainda.

## Decisão

1. **Autorizar coleta assistida** com **Google Places API** (conector oficial).
2. **Proibir** neste corte: scrape HTML Maps, scrape/bot Instagram, cookies/sessão,
   rotação de IP, envio automático de WhatsApp / Evolution / lista de transmissão.
3. **Piloto:** cidade **Brasília (DF)**; cap **≤ 40** resultados por execução;
   **1 cidade** por run.
4. **Artefato:** script local + CSV de **candidatos** (`status_revisao = Pendente`).
   Candidato **não** é lead qualificado até triagem humana (REGRAS atuais).
5. **CRM** continua Google Sheets (ADR 0001). Postgres/API JWT **não** são
   pré-requisito deste piloto.
6. **Segredos/PII:** chave em `.env`; exports reais fora do Git (ADR 0003).
7. **WA** permanece manual HITL (ADR 0002); limites 5–8/dia e horário 9h–17h intactos.

## Consequências

**Positivas**
- Reduz tempo de caça sem abandonar qualificação humana.
- Fonte auditável (`place_id`, `fonte=Maps`, `coletado_em`).
- Caminho alinhado ao PLANO Fase 4 sem “atalho ilegal”.

**Negativas / custos**
- Custo variável da Places API (mitigado por cap e 1 cidade).
- Falsos positivos exigem triagem (feminina, shopping, sem WA).
- Contrato documental (CONTEXT/REGRAS/SEGURANCA) precisa ser atualizado na fatia 1
  de implementação (ainda não executada neste ADR).

## Alternativas consideradas

| Alternativa | Por que NÃO (agora) |
|-------------|---------------------|
| Scraping Google Maps / Instagram | Termos, bloqueio, risco LGPD/conta |
| Comprar lista fria genérica | Qualidade/geo-cerca duvidosa; ainda precisa triagem |
| Postgres + API completa antes de coletar | Overengineering; ADR 0001 ainda vale para CRM |
| WA automático junto com a coleta | Viola ADR 0002; risco de spam/ban |

## Rollback

Desativar chave API; apagar exports locais; reverter docs de contrato se o piloto
for abortado; script sem chave não opera.

## Quando reabrir

- Expandir para outras cidades ABRIR após piloto OK.
- Enriquecimento Instagram (Fase 5) — ADR separado.
- WA semi-automático — só revisitando ADR 0002.
- Postgres — gatilhos do ADR 0001 / Dia 22.
