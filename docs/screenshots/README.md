# Screenshots — Clientes Hunter

Pasta para evidências visuais de portfólio. **Somente dados fictícios.**

## Arquivo esperado (Dia 2 da trilha)

| Arquivo | Conteúdo |
|---------|----------|
| `planilha-demo.png` | Aba de leads no Google Sheets (ou Excel) com linhas **demo** |

Enquanto o PNG não existir, o README e [`docs/portfolio/etapas.md`](../portfolio/etapas.md) apontam para este guia.

---

## Como capturar (checklist LGPD)

1. Abra a planilha operacional (setup: [`templates/planilha/SETUP-GOOGLE-SHEETS.md`](../../templates/planilha/SETUP-GOOGLE-SHEETS.md)).
2. Use **só** nomes inventados, ex.:
   - Loja: `Moda Norte Demo`, `Multimarcas Centro Fake`
   - Cidade: uma da geo-cerca pública (ex.: `Brasília`, `Formosa`)
   - WhatsApp / telefone: `TELEFONE_OCULTO` ou `(61) 90000-0000`
   - CNPJ: nunca na tela — se a coluna existir, use `CNPJ_OCULTO` ou deixe vazio
3. Mostre colunas úteis ao portfólio: nome fantasia, cidade, `status_funil`, score, fonte (sem PII real).
4. Capture a região da tabela (Win+Shift+S ou ferramenta do navegador).
5. Salve como **`docs/screenshots/planilha-demo.png`** (este diretório).
6. Revise o PNG: zero telefone/CNPJ/nome de cliente real.

### Proibido no screenshot

- Linhas de `data/clientes-existentes.csv`
- Números reais de WhatsApp
- CNPJ real
- Export completo da planilha de produção

---

## Depois de salvar o PNG

1. No [`README.md`](../../README.md), na seção **Funil de prospecção**, substitua a linha que aponta para este guia por:

```markdown
![Planilha demo (dados fictícios)](docs/screenshots/planilha-demo.png)
```

2. Em [`docs/portfolio/etapas.md`](../portfolio/etapas.md), Etapa 2: troque o texto “ainda não versionado” por link/imagem para `planilha-demo.png`.
3. Marque a tarefa correspondente em [`TRILHA-DIA-A-DIA.md`](../../TRILHA-DIA-A-DIA.md) (Dia 2).

**HITL:** peça revisão humana do PNG antes de commit/push.
