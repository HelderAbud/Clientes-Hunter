# Segurança e LGPD — Clientes Hunter (MVP)

Práticas aplicáveis **agora**, sem backend. Complementa [`REGRAS-CLIENTES-HUNTER.md`](REGRAS-CLIENTES-HUNTER.md).

Referência de intenção: [`Novo Documento de Texto.md.txt`](Novo%20Documento%20de%20Texto.md.txt) — itens de JWT, Redis, scraping agressivo etc. ficam para **fases futuras** (app/banco).

---

## 1. O que nunca commitar no Git

| Item | Motivo |
|------|--------|
| `data/clientes-existentes.csv` | CNPJ e dados comerciais da carteira |
| `data/_pdf_raw.txt` | Extração bruta do PDF de clientes |
| `*.pdf` de clientes / exports | Mesmo conteúdo sensível |
| `.env` | Tokens (Telegram, Evolution, APIs) |
| Backups de planilha com telefones | Dados pessoais/comerciais |
| Cookies/sessão Instagram | Risco de hijack de conta |

**Pode commitar:** `geo-cerca-cidades.csv`, regras, templates **sem** dados reais, `.env.example`.

---

## 2. Separação de dados (planilha / arquivos)

Mesmo no MVP manual, manter **3 blocos separados**:

| Bloco | Conteúdo | Quem acessa |
|-------|----------|-------------|
| **Leads** | Prospecção: loja, cidade, @, WhatsApp, score, funil | Você (operação diária) |
| **Clientes** | Base de clientes (PDF/CSV importado) | Só você; aba/arquivo restrito |
| **Atividades** | Log: data, ação, resposta (sem CPF/endereço) | Você |

**Regra:** lead novo **não** precisa de CNPJ do lojista. CNPJ fica só na base de clientes existentes.

---

## 3. Minimização (LGPD)

Armazenar **apenas** o necessário para prospecção B2B:

- **Sim:** nome fantasia, cidade, @ Instagram, telefone/WhatsApp comercial, notas de abordagem.
- **Não** em leads: CPF de pessoa física, endereço residencial, histórico financeiro detalhado.
- **Apagar/arquivar** leads `Perdido` após **12 meses** (ajustável).
- Se loja pedir **não contatar**: marcar `Descartado` + motivo `Opt-out` e não reabordar.

**Base legal (resumo):** interesse legítimo em prospecção comercial B2B + transparência no primeiro contato (identificar-se como representante comercial).

---

## 4. Uso de IA (Cursor e similares)

### Antes de colar no chat

- [ ] Substituir telefone: `(61) 99999-9999` → `TELEFONE_OCULTO`
- [ ] Substituir CNPJ → `CNPJ_OCULTO`
- [ ] **Não** enviar CSV/PDF inteiro de clientes
- [ ] Enviar só: nome da loja, cidade, trecho da bio, score, dúvida comercial
- [ ] **Não** colar cookies, tokens ou senhas de Instagram/WhatsApp

### Exemplo seguro

```
Loja: LOJA_EXEMPLO_042 | Cidade: Formosa-GO
Bio: multimarcas masculina, wa.me na bio
Marcas nos posts: A, B, C, D (4 distintas)
Dúvida: mensagem de primeiro contato WhatsApp
```

---

## 5. Instagram e web (manual)

- Só **perfis públicos**; leitura manual (bio + ~12 posts).
- **Limite:** 8–12 perfis triados por dia.
- **Proibido no MVP:** bot logado, scraping em massa, rotação de IP, DM frio em massa.
- Respeitar pedido de exclusão se loja responder no WhatsApp.

---

## 6. WhatsApp

- Envio **manual** com aprovação sua.
- **5–8** abordagens frias novas por dia (número Business compartilhado).
- **No máximo 1 abordagem por loja por dia**; follow-up só em outro dia.
- Horário comercial (9h–17h); **nunca após as 18h**.
- Sem lista de transmissão para prospecção fria.

---

## 7. Backups locais

- Planilha Google: pasta **privada**; compartilhar só se necessário.
- Export mensal opcional em pasta local (`data/backups/`) — pasta no `.gitignore`.
- PDF original: manter fora do repositório (ex.: `Downloads`).

---

## 8. Logs e observações

Não registrar em `observacoes` ou chats:

- Senhas, tokens, cookies
- CPF
- Dados bancários

---

## 9. Checklist rápido (antes de cada sessão)

- [ ] Dados sensíveis fora do Git?
- [ ] IA recebe só o mínimo mascarado?
- [ ] Lead checado contra `clientes-existentes` antes de WhatsApp frio?
- [ ] Loja feminina / fora geo-cerca descartada?
- [ ] Limite diário de abordagens respeitado?

---

## 10. O que fica para fases futuras (não implementar agora)

Só quando houver **API + banco + multi-usuário**:

- JWT, bcrypt/argon2, CSRF, rate limiting em API
- Criptografia AES-256 em banco
- Redis, filas, Docker produção
- Scraping Instagram automatizado
- Evolution API WhatsApp
- Auditoria técnica (`events` table), Sentry, 2FA admin
- Função `sanitizeForAI()` no código

---

*Documento operacional — MVP manual. Revisar ao migrar para Postgres/app.*
