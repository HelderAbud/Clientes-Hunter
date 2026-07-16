# Setup — Google Sheets Clientes Hunter

Planilha operacional v1 (Tasks A2 / Dias 3–5). Importe os CSV desta pasta ou copie cabeçalhos manualmente.

## 1. Criar planilha

1. [Google Sheets](https://sheets.google.com) → **Nova planilha em branco**
2. Renomear: **Clientes Hunter — Operacional**
3. Pasta Drive **privada**; compartilhar só se necessário
4. Guardar link numa nota local (não commitar link com dados reais)

## 2. Dia 3 — Aba Leads

1. Renomear aba `Sheet1` → **`Leads`**
2. **Arquivo → Importar** → upload [`Leads.csv`](Leads.csv) **ou** [`Leads-10-teste.csv`](Leads-10-teste.csv) (Dia 5)
3. **Exibir → Congelar → 1 linha**
4. Criar aba auxiliar **`Listas`** (oculta depois) com colunas de validação — ver [`listas-validacao.csv`](listas-validacao.csv)
5. Criar aba **`Cidades`** — importar coluna `cidade` de [`../../data/geo-cerca-cidades.csv`](../../data/geo-cerca-cidades.csv)

### Validação de dados (Google Sheets)

Selecionar colunas em `Leads` → **Dados → Validação de dados**:

| Coluna | Critério | Valores |
|--------|----------|---------|
| `cidade` | Lista de intervalo | `Cidades!A2:A63` |
| `fonte` | Lista | Instagram, Maps, Guia, Indicação |
| `flag_multimarcas` | Lista | sim, nao |
| `flag_loja_feminina` | Lista | sim, nao |
| `flag_ja_cliente` | Lista | sim, nao |
| `score` | Lista | alto, medio, baixo |
| `status_funil` | Lista | Novo lead, Contato previo feito, Agendamento de visita, Visita com mostruario, Pedido fechado, Perdido, Descartado |
| `status_cidade` | Lista | ABRIR, OK |

### Fórmula sugerida `link_wa_me` (coluna G)

Se `whatsapp` estiver só com dígitos na coluna F (linha 2):

```
=SE(F2="";"";"https://wa.me/55"&F2)
```

## 3. Dia 4 — Demais abas

| Aba | Importar |
|-----|----------|
| **Atividades** | [`Atividades.csv`](Atividades.csv) |
| **Clientes** | [`../../data/clientes-existentes.csv`](../../data/clientes-existentes.csv) — **ocultar aba** |
| **Hashtags** | [`Hashtags.csv`](Hashtags.csv) |
| **Candidatos** (opcional) | Só para treinar: [`Candidatos.example.csv`](Candidatos.example.csv) — guia [`Candidatos-revisao.md`](Candidatos-revisao.md). CSV **reais** ficam em `data/exports/` (fora do Git), não versionar |
| **Dashboard** | Criar manualmente — fórmulas em [`Dashboard-formulas.md`](Dashboard-formulas.md) |

## 4. Permissões

- Aba **Clientes**: clic direito → **Ocultar folha** (ou proteger)
- Não publicar planilha na web

## 5. Próximo

Após importar: **Dia 5** — validar 10 leads em [`Leads-10-teste.csv`](Leads-10-teste.csv).
