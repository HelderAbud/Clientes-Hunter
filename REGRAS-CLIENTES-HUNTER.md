# Regras operacionais — Clientes Hunter

Documento de referência da **Task A1**. Atualizado com geo-cerca, clientes existentes e exclusão de lojas femininas.

---

## 1. Objetivo

Prospecção de **lojas masculinas multimarcas** no **DF** e **Norte de Goiás**, com contato **100% WhatsApp Business**, usando **Instagram + Google Maps** para achar e qualificar leads.

**KPI principal:** `agendamentos confirmados ÷ leads qualificados`

---

## 2. Funil padrão

1. Novo lead  
2. Contato prévio feito  
3. Agendamento de visita  
4. Visita com mostruário  
5. Pedido fechado **ou** Perdido  

---

## 3. Geo-cerca (cidades)

Lista oficial: [`data/geo-cerca-cidades.csv`](data/geo-cerca-cidades.csv) — **62 cidades**.

| Status na planilha | Significado |
|--------------------|-------------|
| **ABRIR** | Prioridade para caçar lojas **novas** (prospecção fria) |
| **OK** | Carteira já trabalhada; foco em **reativação** ou novos pontos, não prospecção massiva |

**Regra:** lead com cidade **fora** desta lista → `status_funil = Descartado` + motivo `Fora da geo-cerca`.

**Correções aplicadas** (lista enviada em imagem): `BARRO ALTO = GO`, `BRASILIA = DF`.

---

## 4. Perfil alvo (quem abordar)

### 4.1 Deve ser (lead qualificado)

- Loja de **moda masculina** ou **multimarcas com linha masculina relevante**
- Cidade dentro da geo-cerca
- Indício de **WhatsApp** (bio Insta, `wa.me`, telefone celular)
- **Multimarcas real:** mínimo **4 marcas masculinas distintas** nos últimos 12 posts (ajustável)
- **Não** consta na base de clientes existentes (ver secção 6)

### 4.2 Não abordar — lojas femininas (regra obrigatória)

**Nunca** entrar em contato de prospecção fria com lojas **exclusivamente femininas**.

Marcar `status_funil = Descartado` + motivo `Loja feminina` quando houver sinal claro:

| Onde olhar | Sinais de exclusão |
|------------|-------------------|
| Nome / fantasia | *moda feminina*, *feminina*, *mulher*, *woman*, *femme*, *miss*, *girl*, *ladies* |
| Bio Instagram | “só feminino”, “moda feminina”, “plus size feminino”, “lingerie”, “moda praia feminina” |
| Posts | **Só** modelos femininas, vestidos, lingeries; zero linha masculina |
| Google Maps | Categoria ou descrição só feminina |

**Dúvida (loja mista):** se tiver **seção masculina clara** nos posts → pode qualificar; se não der para ver masculino → `Baixa prioridade` ou descartar.

### 4.3 Outros descartes

| Motivo | Quando |
|--------|--------|
| `Ja cliente existente` | Consta em [`data/clientes-existentes.csv`](data/clientes-existentes.csv) ou bio/posts com a marca representada |
| `Fora da geo-cerca` | Cidade fora da lista |
| `Sem WhatsApp` | Sem contato viável após checagem |
| `Multimarcas fraco` | Menos de 4 marcas masculinas nos posts |
| `Infantil only` | Loja **só** infantil/kids/bebê, sem adulto masculino |

---

## 5. Clientes existentes (não importunar na prospecção fria)

Base exportada: **`Clientes_900165.pdf`** → processada em [`data/clientes-existentes.csv`](data/clientes-existentes.csv) (**178 registros**).

Antes de mandar WhatsApp para lead **novo**, conferir:

1. **Fantasia** ou razão social parecida  
2. **CNPJ** (se tiver)  
3. **Cidade** + nome da loja  

Se bater → marcar `flag_ja_cliente = sim` e **não** usar template de prospecção fria.

**Exceção:** cliente inativo ou “tempo sem compra” alto → fluxo de **reativação** (mensagem diferente, não conta no KPI de prospecção fria).

---

## 6. Canais

| Canal | Uso |
|-------|-----|
| **Instagram** | Achar loja, qualificar (bio + 12 posts), contar marcas, flags feminina/cliente existente |
| **Google Maps** | Achar loja, telefone, cruzar com Insta |
| **WhatsApp Business** | **Único** canal de contato com lojista |
| **Planilha** | CRM, funil, KPI (não substituída pelo WhatsApp) |

---

## 7. Limites e anti-spam (WhatsApp)

- **5 a 8** novas abordagens frias por dia (número Business compartilhado com carteira)
- **3 a 5 variações** de texto de primeiro contato; alternar
- Sempre **revisar em voz alta** antes de enviar
- Horário comercial: **9h–17h**
- **Nunca** lista de transmissão para prospecção fria

---

## 8. Score simples

| Score | Critério resumido |
|-------|-------------------|
| **Alto** | Cidade ABRIR + multimarcas forte + WhatsApp na bio + sem cliente existente + masculino claro |
| **Médio** | Dentro da geo-cerca, masculino ok, WhatsApp ok, alguma dúvida |
| **Baixo** | Multimarcas fraco, cidade sem prioridade, ou sinais mistos |

Só **Alto** e **Médio** vão para fila de WhatsApp no mesmo dia.

---

## 9. Colunas extras na planilha (Leads)

Além das colunas base, usar:

- `flag_loja_feminina` (sim/não)
- `flag_ja_cliente` (sim/não)
- `motivo_descarte` (texto curto)
- `status_cidade` (ABRIR / OK)

---

## 10. Segurança e privacidade (MVP)

Seguir [`SEGURANCA-LGPD.md`](SEGURANCA-LGPD.md):

- Dados de clientes (`clientes-existentes.csv`) **fora do Git**
- Separar abas Leads / Clientes / Atividades na planilha
- Mascarar telefone e CNPJ antes de usar IA
- Instagram manual com limite diário; sem scraping agressivo

---

## 11. Próximo passo

- **Agora:** [`DIA-A-DIA-CLIENTES-HUNTER.md`](DIA-A-DIA-CLIENTES-HUNTER.md) — escreva **`Iniciar Dia 6`** (templates WhatsApp)
- **Planilha:** importar [`templates/planilha/`](templates/planilha/) no Google Sheets — guia [`SETUP-GOOGLE-SHEETS.md`](templates/planilha/SETUP-GOOGLE-SHEETS.md)

---

*Fontes: lista de cidades (imagem 22/05/2026), Clientes_900165.pdf (Downloads).*
