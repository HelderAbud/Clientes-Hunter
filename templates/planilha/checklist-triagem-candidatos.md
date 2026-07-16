# Checklist — triagem de candidatos → lead (Fatia 4)

Use após o organizador (3b) ou qualquer CSV em `data/exports/`.  
Contrato: [`REGRAS`](../../REGRAS-CLIENTES-HUNTER.md) · [`CONTEXT`](../../CONTEXT.md) · [`SEGURANCA-LGPD`](../../SEGURANCA-LGPD.md).

**Regra de ouro:** nenhum WhatsApp sem passar por este checklist.

---

## Por cada linha com `status_revisao = Pendente`

### 1. Geo-cerca

- [ ] Cidade está em [`data/geo-cerca-cidades.csv`](../../data/geo-cerca-cidades.csv)?
- [ ] Se não → `Descartado` + motivo `Fora da geo-cerca`

### 2. Loja feminina / perfil

- [ ] Nome, Maps ou Insta sugerem **só** moda feminina?
- [ ] Se sim → `Descartado` + `Loja feminina`
- [ ] Mista com masculino claro → pode seguir

### 3. Já cliente (offline)

- [ ] Conferir na base local `data/clientes-existentes.csv` (**não** colar no chat / Git)
- [ ] Se bater → não usar template frio; marcar `flag_ja_cliente` / fluxo reativação
- [ ] Motivo se descartar da fria: `Ja cliente existente`

### 4. WhatsApp

- [ ] Telefone celular / wa.me utilizável?
- [ ] Se não → `Descartado` + `Sem WhatsApp` (ou buscar outra fonte depois)

### 5. Multimarcas (Instagram manual)

- [ ] Abrir perfil público (se achar)
- [ ] Contar ≥ 4 marcas masculinas nos ~12 posts?
- [ ] Se fraco → `Descartado` + `Multimarcas fraco` **ou** score baixo e não entrar na fila WA

### 6. Score e promoção

- [ ] Score **Alto** ou **Médio**? (só esses vão para WA no dia)
- [ ] Atualizar candidato: `status_revisao = Qualificado`
- [ ] Copiar para aba **Leads**:
  - `fonte = Maps`
  - `status_funil = Novo lead`
  - `status_cidade` (ABRIR/OK)
  - flags e `whatsapp` / `link_wa_me`

### 7. Antes do primeiro WhatsApp

- [ ] Dentro do limite 5–8/dia
- [ ] Horário 9h–17h (nunca após 18h)
- [ ] Template revisado em voz alta (HITL)
- [ ] 1 abordagem por loja/dia

### 8. Opt-out

- [ ] Se pedirem para não contatar → `Descartado` + `Opt-out` — **nunca** reabordar

---

## Meta do bloco (lembrete operacional)

- Triagem: preferir qualidade a volume
- Foto de fachada (se fizer): celular/Drive pessoal — fora do repo

## Arquivos úteis

| Arquivo | Uso |
|---------|-----|
| [`Candidatos-revisao.md`](Candidatos-revisao.md) | Colunas e fluxo |
| [`scripts/README-organizar-candidatos.md`](../../scripts/README-organizar-candidatos.md) | Como gerar o CSV |
| [`Mensagens-WhatsApp.md`](Mensagens-WhatsApp.md) | Templates após qualificar |
