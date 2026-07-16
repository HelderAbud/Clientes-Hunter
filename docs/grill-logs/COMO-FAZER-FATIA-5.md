# Fatia 5 — Dry-run (você executa)

Tempo estimado: 30–60 min. Custo: R$ 0.

## Passo a passo

### 1. Buscar no Maps (Brasília)

Ache **pelo menos 3** lojas masculinas/multimarcas (nome + telefone + endereço ou link Maps).

### 2. Montar o rascunho

1. Copie `templates/planilha/Candidatos-entrada.example.csv`  
2. Salve como arquivo **local** (ex.: na Área de Trabalho ou `data/exports/rascunho-entrada.csv`)  
3. Substitua as linhas demo pelos dados reais  
4. **Não** commit esse arquivo se tiver telefone real

### 3. Organizar

Na pasta `Clientes Hunter`:

```bash
python scripts/organizar_candidatos.py -i caminho/do/seu-rascunho.csv
```

Confira: arquivo novo em `data/exports/candidatos-BRASILIA-YYYYMMDD.csv`.

### 4. Triar (≥ 3)

Abra [`checklist-triagem-candidatos.md`](../templates/planilha/checklist-triagem-candidatos.md)  
e marque Qualificado / Descartado. Quem passar → aba Leads (`fonte=Maps`).

### 5. Fechar a validação

Preencha só **números** em:

[`docs/grill-logs/validation-2026-07-16-fatia5-dry-run-candidatos.md`](../docs/grill-logs/validation-2026-07-16-fatia5-dry-run-candidatos.md)

Depois no chat diga, por exemplo:

`fatia 5 ok — 5 candidatos, 2 qualificados, 3 descartados`

(sem telefones / nomes se quiser máximo de privacidade; agregados bastam)
