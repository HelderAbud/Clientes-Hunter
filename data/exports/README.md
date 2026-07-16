# Exports locais — fora do Git

Pasta para **CSV reais** gerados na operação (ex.: coleta Places, backup de leads).

| Pode existir aqui | Pode ir para o Git? |
|-------------------|---------------------|
| `candidatos-brasilia-YYYYMMDD.csv` | **Não** |
| Qualquer export com telefone/endereço real | **Não** |
| Este `README.md` | Sim |

## Regras

1. Script Places deve gravar **somente** nesta pasta (ou equivalente gitignored).
2. Templates fictícios ficam em `templates/planilha/` (ex.: `Candidatos.example.csv`).
3. Nunca colar o CSV inteiro no Cursor — use máscara (`TELEFONE_OCULTO`) se precisar de 1 linha.
4. Antes de commit: `git status` — esta pasta não deve listar arquivos de dados.

Ver [`SEGURANCA-LGPD.md`](../../SEGURANCA-LGPD.md) e [ADR 0003](../../docs/adr/0003-retencao-e-mascaramento-lgpd.md) / [ADR 0004](../../docs/adr/0004-coleta-assistida-google-places.md).
