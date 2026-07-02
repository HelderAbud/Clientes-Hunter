# Dashboard — fórmulas (aba Dashboard)

Assume aba **Leads** com dados a partir da linha 2. Ajuste intervalo se necessário.

| Célula | Rótulo | Fórmula (PT-BR Google Sheets) |
|--------|--------|----------------------------------|
| A1 | Métrica | |
| B1 | Valor | |
| A2 | Total leads | `=CONT.SE(Leads!A:A;">0")-1` ou `=CONT.VALORES(Leads!A2:A)` |
| A3 | Leads qualificados (alto+medio) | `=CONT.SE(Leads!M:M;"alto")+CONT.SE(Leads!M:M;"medio")` |
| A4 | Agendamentos | `=CONT.SE(Leads!N:N;"Agendamento de visita")+CONT.SE(Leads!N:N;"Visita com mostruario")` |
| A5 | Taxa agendamento | `=SE(B3=0;0;B4/B3)` |
| A6 | Descartados | `=CONT.SE(Leads!N:N;"Descartado")` |
| A7 | Novo lead (fila) | `=CONT.SE(Leads!N:N;"Novo lead")` |

**Nota:** coluna M = `score`, coluna N = `status_funil` na estrutura padrão de [`Leads.csv`](Leads.csv).

Formato B5 como percentagem.
