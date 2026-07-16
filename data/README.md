# Dados — Clientes Hunter

| Arquivo | Conteúdo | Git |
|---------|----------|-----|
| [`geo-cerca-cidades.csv`](geo-cerca-cidades.csv) | 62 cidades (DF + Norte GO) | Pode commitar |
| [`clientes-existentes.example.csv`](clientes-existentes.example.csv) | Estrutura sem CNPJ real | Pode commitar |
| [`clientes-existentes.csv`](clientes-existentes.csv) | 178 clientes (PDF) | **Não commitar** — ver `.gitignore` |
| [`_pdf_raw.txt`](_pdf_raw.txt) | Texto bruto do PDF | **Não commitar** |
| [`exports/`](exports/) | CSV reais (Places, backups de leads) | **Não commitar** (só `exports/README.md`) |

**Segurança:** ver [`../SEGURANCA-LGPD.md`](../SEGURANCA-LGPD.md).

**PDF original:** manter **fora do repositório** (pasta local privada do titular — ex.: Downloads). Nome típico: `Clientes_900165.pdf`.

**Atualizar clientes:** exportar novo PDF e rodar parser (pedir ajuda no Cursor). Não enviar CSV completo para IA — mascarar CNPJ/telefone.

**Backups:** use `data/backups/` (pasta ignorada pelo Git) para exports mensais da planilha.
