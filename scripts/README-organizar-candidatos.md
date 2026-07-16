# Organizador de candidatos (Fatia 3b) — R$ 0

Script: [`organizar_candidatos.py`](organizar_candidatos.py)  
**Não usa** Google Places / API paga. Você busca no Maps (manual); o script só **formata**.

## Pré-requisito

- Python 3.10+ (só biblioteca padrão)

## 1. Montar o rascunho

Copie [`../templates/planilha/Candidatos-entrada.example.csv`](../templates/planilha/Candidatos-entrada.example.csv)  
ou crie um CSV com cabeçalho:

```text
nome,cidade,endereco,telefone,site,maps_url,observacoes
```

Preencha com lojas que você achou no Maps (dados reais **só na sua máquina**).

Aliases aceitos: `loja`→nome, `whatsapp`→telefone, `link_maps`→maps_url, etc.

## 2. Rodar

Na raiz do repo `Clientes Hunter`:

```bash
python scripts/organizar_candidatos.py -i templates/planilha/Candidatos-entrada.example.csv
```

Saída padrão:

`data/exports/candidatos-BRASILIA-YYYYMMDD.csv` (**gitignored**)

Opções úteis:

```bash
python scripts/organizar_candidatos.py -i meu-rascunho.csv --cidade BRASILIA --max 40
python scripts/organizar_candidatos.py -i meu-rascunho.csv -o data/exports/candidatos-brasilia.csv --verbose
```

`--verbose` mostra só os **últimos 4 dígitos** do telefone no terminal (não o número completo).

## 3. Triar

Siga [`../templates/planilha/checklist-triagem-candidatos.md`](../templates/planilha/checklist-triagem-candidatos.md)  
e [`../templates/planilha/Candidatos-revisao.md`](../templates/planilha/Candidatos-revisao.md).

## LGPD

- Não commit/push de `data/exports/*.csv` reais
- Não cole o CSV no Cursor sem máscara
- `place_id` local = `LOCAL_<hash>` (não é ID Google)

## Quando tiver dinheiro para Places

Retomar Fatia 3 do plano (`autorizo retomar fatia 3`) — ADR 0004.
