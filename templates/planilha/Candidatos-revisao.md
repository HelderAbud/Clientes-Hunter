# Candidatos Places — revisão e import (piloto)

Template: [`Candidatos.example.csv`](Candidatos.example.csv) (só dados **fictícios**).  
Contrato: [`CONTEXT.md`](../../CONTEXT.md) · [`REGRAS` §6.1](../../REGRAS-CLIENTES-HUNTER.md) · [ADR 0004](../../docs/adr/0004-coleta-assistida-google-places.md) · [`SEGURANCA-LGPD.md`](../../SEGURANCA-LGPD.md).

## Colunas

| Coluna | Obrigatório | Notas |
|--------|-------------|--------|
| `place_id` | Sim | Dedupe Google |
| `nome` | Sim | Nome fantasia / estabelecimento |
| `cidade` | Sim | Piloto: `BRASILIA` |
| `endereco` | Sim | Conferência |
| `telefone` | Desejável | Pode vir vazio ou `TELEFONE_OCULTO` em demos |
| `site` | Não | Ajuda a achar Instagram depois |
| `maps_url` | Sim | Rastreio |
| `fonte` | Sim | Sempre `Maps` neste fluxo |
| `coletado_em` | Sim | ISO datetime |
| `status_revisao` | Sim | `Pendente` / `Qualificado` / `Descartado` |
| `observacoes` | Não | Curto; sem CPF/senha |

## Onde gravar o quê

| Arquivo | Git |
|---------|-----|
| `templates/planilha/Candidatos.example.csv` | Pode versionar |
| `data/exports/candidatos-brasilia-YYYYMMDD.csv` (real) | **Nunca** — pasta gitignored |

## Fluxo humano (após o organizador 3b ou Places)

1. Gerar CSV: ver [`../../scripts/README-organizar-candidatos.md`](../../scripts/README-organizar-candidatos.md) (R$ 0) **ou** Places (pausado).
2. Abrir o CSV em `data/exports/` (local).
3. Seguir [`checklist-triagem-candidatos.md`](checklist-triagem-candidatos.md).
4. `Qualificado` → copiar para aba **Leads** (`fonte=Maps`, `status_funil=Novo lead`, score).
5. **Nunca** enviar WhatsApp direto do CSV de candidatos sem triagem.

## Import opcional no Sheets

1. Criar aba `Candidatos` (opcional) **ou** trabalhar só no Excel/CSV local.
2. Arquivo → Importar → `Candidatos.example.csv` para treinar o formato.
3. Dados reais: importar só a partir de `data/exports/` na sua máquina; planilha **privada**.

## LGPD

- Não commitar exports reais.
- Não publicar a planilha na web.
- No Cursor: máscara `TELEFONE_OCULTO` / nunca anexar o export inteiro.
