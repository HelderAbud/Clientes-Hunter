# Dados — Clientes Hunter

| Arquivo | Conteúdo | Git |
|---------|----------|-----|
| [`geo-cerca-cidades.csv`](geo-cerca-cidades.csv) | 62 cidades (DF + Norte GO) | Pode commitar |
| [`clientes-existentes.example.csv`](clientes-existentes.example.csv) | Estrutura sem CNPJ real | Pode commitar |
| [`clientes-existentes.csv`](clientes-existentes.csv) | 178 clientes (PDF) | **Não commitar** — ver `.gitignore` |
| [`_pdf_raw.txt`](_pdf_raw.txt) | Texto bruto do PDF | **Não commitar** |

**Segurança:** ver [`../SEGURANCA-LGPD.md`](../SEGURANCA-LGPD.md).

**PDF original (local, fora do repo):**  
`C:\Users\Pessoal\Downloads\Clientes_900165.pdf`

**Atualizar clientes:** exportar novo PDF e rodar parser (pedir ajuda no Cursor). Não enviar CSV completo para IA — mascarar CNPJ/telefone.

**Backups:** use `data/backups/` (pasta ignorada pelo Git) para exports mensais da planilha.
