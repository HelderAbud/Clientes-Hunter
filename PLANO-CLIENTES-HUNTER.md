# Clientes Hunter — Plano do projeto (guia para júnior)

Este documento reúne a **ideia**, o **passo a passo**, **melhorias** e um **plano sequencial concreto** para implementar o sistema aos poucos. Leia na ordem; cada fase só começa quando a anterior estiver “ok”. O **checklist simples com explicações** está na [secção 10](#10-checklist-passo-a-passo-simples).

> **Roteiro dia a dia (modo plano):** use [`DIA-A-DIA-CLIENTES-HUNTER.md`](DIA-A-DIA-CLIENTES-HUNTER.md) — 30 dias com checklist um a um. Comando: `Iniciar Dia N`. **Progresso:** Dias 1–5 ✅ (Task A2); próximo Dia 6.

---

## 1. O que é o Clientes Hunter?

**Clientes Hunter** é um sistema de **captação e prospecção** para quem representa **marcas comerciais** no **Distrito Federal** e no **Norte de Goiás**, focado em **lojas masculinas multimarcas**.

Ele deve:

1. **Achar** lojas novas (ou ainda não trabalhadas) nas cidades da sua área.
2. **Qualificar** se faz sentido abordar (multimarcas de verdade, não concorrente direto indevido, etc.).
3. **Priorizar** quem tem **WhatsApp** e bom sinal de conversão.
4. **Preparar** mensagem de primeiro contato **personalizada** (você aprova antes de enviar).
5. **Acompanhar** o funil em um **Kanban**: Novo → Contato prévio → Agendamento de visita → Visita com mostruário → Pedido fechado (ou perdido).

**Nome do projeto:** Clientes Hunter  
**Usuário principal:** o representante (uso individual / equipe pequena).

---

## 1.1 Objetivo, escopo e KPI principal

**Objetivo oficial do programa:** facilitar a identificação de lojas potenciais na internet e no Instagram, organizar o contato prévio por mensagem e aumentar a taxa de agendamentos presenciais, onde a venda é realizada com apresentação do mostruário em loja.

### Escopo operacional (o que o sistema faz)

1. **Encontrar** lojas com perfil multimarcas masculino (DF + Norte GO).
2. **Qualificar** se vale abordagem comercial.
3. **Preparar o contato prévio** por WhatsApp com mensagem personalizada e poucas fotos estratégicas.
4. **Converter o interesse em agendamento** de visita presencial.
5. **Registrar o funil completo** até visita realizada e resultado da venda.

### KPI principal

- **Taxa de agendamento por lead qualificado** = `agendamentos confirmados / leads qualificados`.

### KPIs de apoio

- **Taxa de comparecimento na visita** = `visitas realizadas / agendamentos confirmados`.
- **Taxa de fechamento pós-visita** = `pedidos fechados / visitas realizadas`.
- **Tempo médio até agendamento** = dias entre primeiro contato e confirmação de visita.

---

## 2. Glossário (leia uma vez)

| Termo | Significado |
|--------|-------------|
| **Lead** | Um registro de uma loja candidata à prospecção. |
| **Fonte** | O lugar de onde o dado veio (Google Maps, Instagram, site guia, etc.). |
| **Enriquecimento** | Passo que adiciona informação (posts do Insta, marcas mencionadas, telefone, etc.). |
| **Score** | Nota de prioridade (ex.: “Ouro” = cidade pequena + poucas marcas + WhatsApp). |
| **Geo-cerca** | Lista de **cidades** onde você atua; fora disso o sistema **não** deve priorizar lead. |
| **Disparo** | Envio da mensagem (no início **manual**; depois pode ser automatizado com cuidado). |
| **MVP** | Versão mínima que já te economiza tempo no dia a dia. |

---

## 3. Ideia central do produto (visão)

### 3.1 Captação (várias fontes)

O sistema pode **varrer** periodicamente (ex.: 1x por dia):

1. **Google Maps** — buscas do tipo *loja masculina multimarcas* por cidade da geo-cerca. Coletar nome, telefone, site, link do Maps.
2. **Instagram** — hashtags e perfis públicos (#lojamasculina, #modamasculinadf, etc.) e perfis que mencionam a marca representada. Coletar @, bio, link de WhatsApp se existir.
3. **Sites guia** — cadastros públicos (ex.: guias locais). Coletar nome, cidade, contato.

**Melhoria contínua:** começar com **1 fonte bem feita** (Maps ou planilha manual) antes de abrir todas.

### 3.2 Enriquecimento e regras

Para cada loja:

- Ver **últimos posts** (ex.: 12) no Instagram **público** quando fizer sentido.
- **Potencial alto** se não aparecer marca marca concorrente direta nos critérios que vocês definirem.
- **CNPJ / situação** — opcional; busca externa pode ser manual no início.
- **Telefone** — priorizar número com indício de **WhatsApp** (link `wa.me`, “WhatsApp” na bio, etc.).
- **Score** — combinar: cidade (tamanho), diversidade de marcas, presença de WhatsApp, ausência de sinal “já é cliente existente”.

### 3.3 Canal WhatsApp (diferencial)

- Primeiro contato por **WhatsApp**, não e-mail.
- Mensagem **modelo** com placeholders: nome da loja, sua cidade, seu nome, região.
- **Você aprova** antes de enviar (obrigatório no MVP ético e anti-bloqueio).

### 3.4 Kanban de prospecção

Estados sugeridos:

1. **Novo lead**
2. **Contato prévio feito**
3. **Agendamento de visita**
4. **Visita com mostruário**
5. **Pedido fechado** ou **Perdido**

**Melhoria:** registrar **data** e **nota curta** ao mudar de coluna (o que foi dito, objeção).

---

## 4. Regras de negócio importantes

### 4.1 Geo-cerca (só DF + Norte GO)

Manter uma **lista fechada de cidades** (ex.: Brasília, Formosa, Planaltina, Águas Lindas, Luziânia, Anápolis, Uruaçu, Porangatu, Niquelândia — **ajustar com o representante**).  
**Melhoria:** campo `cidade` normalizado (sem typo) para filtrar bem.

### 4.2 “Marca já vende”

Se bio ou posts indicam **fortemente** que a loja **já trabalha a marca**, marcar como **cliente existente / não importunar** para prospecção fria.

### 4.3 “Multimarcas real”

Muitas lojas dizem multimarcas mas têm poucas marcas. Regra exemplo (ajustável): **menos de 4 marcas distintas** mencionadas nos posts → **descartar** ou **baixa prioridade**.

### 4.4 Anti-spam (WhatsApp)

- **Várias variações** de texto (ex.: 5 modelos), alternar.
- **Atraso** entre envios (ex.: 90–180 s) se houver automação.
- **Limite diário** de novas abordagens (ex.: 10 aprovadas por dia).

---

## 5. Arquitetura em ideias (sem obrigar stack agora)

Pense em **camadas** (facilita para júnior dividir tarefas):

| Camada | Função |
|--------|--------|
| **Coleta** | Conectores: Maps, guias, Instagram (público). Saída: dados brutos + fonte + data. |
| **Normalização** | Unificar nomes, telefone, @; **deduplicar** leads. |
| **Enriquecimento** | Jobs que preenchem score, marcas, flags. |
| **Política** | Regras: geo-cerca, multimarcas, anti-spam, aprovação humana. |
| **Armazenamento** | Planilha (MVP barato) ou **PostgreSQL** (app). |
| **Interface** | Planilha + Telegram; depois painel ou Retool; depois app próprio se quiser. |
| **Canal** | WhatsApp manual (`wa.me`) → opcional **Evolution API** (automação, custo de VPS). |

**Melhoria:** separar **“script pesado”** de **“API web”** para não travar requisições.

---

## 6. Estratégia de custo acessível (prioridade do projeto)

Ordem recomendada do **mais barato** ao **menos barato**:

1. **Manual + Google Sheets** — R$ 0 (além do que você já paga de internet/celular).
2. **Scripts no seu PC** exportando CSV → Sheets — R$ 0.
3. **n8n self-hosted** no PC (avisos no Telegram) — R$ 0; VPS só se precisar 24h.
4. **PostgreSQL em Docker local** — R$ 0.
5. **Evolution + VPS** — só quando o ganho de tempo pagar o ~R$ 30–120/mês + chip dedicado.

**Evitar no início:** APIs pagas de mapas em alto volume, n8n Cloud, banco gerenciado, WhatsApp Cloud API (até haver necessidade e orçamento).

---

## 7. Pré-requisitos (contas e serviços)

| Item | Para quê | Notas |
|------|----------|--------|
| **WhatsApp (ideal Business)** | Falar com lojistas | MVP: envio **manual** com texto gerado. |
| **Telegram + bot (BotFather)** | Alertas “lead novo / mensagem pronta” | Token e `chat_id` são segredos. |
| **Google Sheets** | MVP da base de leads | R$ 0. |
| **Instagram (seu perfil)** | Credibilidade | Opcional para o sistema rodar; útil para conversão. |
| **Site** | Não obrigatório no MVP | Painel interno pode ser depois; política de privacidade pode ser página simples se necessário. |

---

## 8. Riscos e responsabilidade (ler antes de automatizar)

- **Termos de uso** de Google/Instagram sobre coleta automatizada.
- **LGPD:** tratar dados com finalidade clara; não guardar o que não precisa; definir tempo de retenção.
- **Bloqueio no WhatsApp** se parecer spam — por isso **aprovação humana**, variações e limites.

---

## 9. Plano sequencial concreto (para o júnior executar em ordem)

Cada fase tem **objetivo**, **tarefas** e **critério de pronto**. Não pule o “pronto”.

### 9.1 Base de execução vertical com IA (tasks em ordem)

Use esta secao como **roteiro oficial de execucao diaria**. A ideia e entregar em fatias verticais: cada task fecha um ciclo ponta a ponta com valor real.

#### Estrutura padrao de cada task vertical

1. **Entrada** (dados minimos): loja, cidade, Instagram, WhatsApp, fonte.
2. **IA sugere**: prioridade, mensagem inicial e proximo passo.
3. **Humano aprova e executa**: envio, agendamento, visita.
4. **Registro**: status, data, nota curta e proximo follow-up.
5. **Metrica**: resultado objetivo da task.

#### Ordem oficial de implementacao (A -> C)

##### Fase A - Fundacao operacional (sem codigo pesado)

**Task A1 - Contrato minimo do processo**

- [x] Confirmar objetivo oficial do Clientes Hunter.
- [x] Confirmar funil padrao: Novo lead -> Contato previo feito -> Agendamento de visita -> Visita com mostruario -> Pedido fechado/Perdido.
- [x] Definir lead qualificado (criterios claros).
- [x] Definir limite diario de abordagens.
- [x] Definir KPI principal: taxa de agendamento por lead qualificado.

**Pronto quando:** qualquer pessoa entende o processo em 1 pagina e executa sem duvida.

**Task A2 - Base de leads (planilha operacional v1)**

- [x] Criar abas: `Leads`, `Atividades`, `KitsFotos`, `Dashboard`.
- [x] Criar colunas minimas em `Leads`: id_lead, loja, cidade, instagram, whatsapp, fonte, score, status_funil, data_ultimo_contato, proximo_passo, data_proximo_passo, observacoes (+ flags e colunas extras — ver [`templates/planilha/`](templates/planilha/)).
- [x] Criar lista fechada para `status_funil` (sem digitacao livre).
- [x] Cadastrar 10 leads de teste e validar consistencia.

**Pronto quando:** 10 leads cadastrados sem erro de status, cidade ou contato.

**Task A3 - Biblioteca comercial (mensagens + kits de fotos)**

- [ ] Criar 3 templates de primeiro contato.
- [ ] Criar 2 templates de confirmacao de agendamento.
- [ ] Criar 2 templates de pos-visita.
- [ ] Definir 3 kits de fotos (nome do kit, perfil de loja indicado, link da pasta).

**Pronto quando:** em menos de 2 minutos voce escolhe mensagem e kit para qualquer lead.

##### Fase B - Primeira fatia vertical real (campo)

**Task B1 - Slice 1: Lead -> Contato previo -> Agendamento**

- [ ] Captar 20 leads reais (internet + Instagram).
- [ ] Qualificar e priorizar em score simples (alto/medio/baixo).
- [ ] Gerar mensagem com apoio da IA.
- [ ] Revisar manualmente e enviar.
- [ ] Registrar respostas no funil e medir resultado.

**Pronto quando:** 20 leads processados com historico completo e taxa de agendamento calculada.

**Task B2 - Slice 2: Agendamento -> Visita -> Resultado**

- [ ] Confirmar agenda de visitas.
- [ ] Executar visita com roteiro de mostruario.
- [ ] Registrar resultado da visita no mesmo dia.
- [ ] Definir proximo passo e data de follow-up.

**Pronto quando:** toda visita realizada tem resultado registrado e proximo passo definido.

##### Fase C - IA assistente de conversao (com HITL)

**Task C1 - IA para qualificacao e mensagem inicial**

- [ ] Criar prompt padrao para classificacao do lead.
- [ ] Configurar saida da IA: prioridade + justificativa + mensagem sugerida.
- [ ] Manter aprovacao humana obrigatoria antes do envio.

**Pronto quando:** o tempo medio de analise por lead cai pelo menos 30%.

**Task C2 - IA para follow-up inteligente**

- [ ] Criar prompt de follow-up com base no historico da loja.
- [ ] Gerar variacoes de follow-up por status de funil.
- [ ] Medir recuperacao de leads mornos.

**Pronto quando:** aumento perceptivel da taxa de resposta em leads mornos.

#### Passo a passo de execucao com minha ajuda (operacao guiada)

1. Voce me chama com: **"Iniciar Task A1"** (ou A2, B1, etc.).
2. Eu devolvo checklist detalhado e instrucoes praticas da task.
3. Voce executa e me envia o resultado real.
4. Eu valido se esta **pronto** ou se precisa ajuste.
5. So avancamos para a proxima task quando a atual fechar o criterio de pronto.

#### Rotina diaria recomendada (ritmo simples)

- **Manha (30-45 min):** captar leads, qualificar e preparar mensagens.
- **Meio do dia (30 min):** enviar contatos aprovados e confirmar agendamentos.
- **Fim do dia (20 min):** atualizar funil, registrar metricas e definir proximo passo.

---

### Fase 0 — Alinhamento (1–3 dias, sem código obrigatório)

**Objetivo:** decisões escritas que evitam refazer trabalho.

**Tarefas:**

1. Fechar **lista de cidades** da geo-cerca e **cidades excluídas** (ex.: não priorizar certas áreas).
2. Escrever **critério multimarcas** (número mínimo de marcas, como contar).
3. Escrever **como detectar “já vende a marca”** (palavras, hashtags, fotos — nível de confiança).
4. Definir **limite diário** de novas abordagens e **modelos de mensagem** (3–5 variações).
5. Criar a **planilha modelo** com colunas: nome, cidade, telefone, @Instagram, link WhatsApp, fonte, score, estágio Kanban, notas, data último contato.

**Pronto quando:** planilha existe + documento de regras tem 1 página que qualquer pessoa da equipe entende.

---

### Fase 1 — MVP manual (primeira semana útil)

**Objetivo:** ganhar tempo **sem** automação arriscada.

**Tarefas:**

1. Rodar buscas **manualmente** no Maps por cidade (termos combinados).
2. Preencher a planilha; normalizar telefone (DDD, 55).
3. Gerar link WhatsApp: `https://wa.me/55XXXXXXXXXXX` (sem caracteres extras no número).
4. Colar **mensagem personalizada** e enviar **manualmente**.
5. Mover coluna **estágio** conforme o Kanban.

**Pronto quando:** em 1 dia você consegue processar uma lista de ~10 leads novos com mensagens consistentes e sem duplicar erros grosseiros.

**Melhoria:** gravar um **vídeo curto** ou checklist “como preencher uma linha” para não depender de você.

---

### Fase 2 — Telegram + n8n (opcional, ainda custo baixo)

**Objetivo:** notificação automática “tem lead novo / texto pronto”.

**Tarefas:**

1. Criar bot no BotFather; guardar token com segurança.
2. Obter `chat_id` do destino (você ou grupo).
3. Instalar **n8n** localmente (Docker) ou em VPS **só se** precisar 24h.
4. Fluxo: ao inserir linha na planilha (ou webhook), enviar mensagem no Telegram com resumo + texto sugerido.

**Pronto quando:** ao adicionar uma linha de teste, o Telegram avisa em até 1 minuto.

**Melhoria:** botão ou comando no Telegram “copiar texto” (se implementarem depois).

---

### Fase 3 — Banco PostgreSQL + pequena API ou scripts (app de verdade)

**Objetivo:** histórico confiável, deduplicação, auditoria.

**Tarefas:**

1. Subir Postgres em Docker **local**.
2. Desenhar tabelas mínimas: `leads`, `events` (mudança de estágio), `sources`.
3. Escrever script ou API para: inserir lead, atualizar estágio, listar “top 10 do dia”.
4. Testar **deduplicação** (mesmo telefone ou mesmo @).

**Pronto quando:** você consegue explicar “de onde veio cada lead” só olhando o banco.

**Melhoria:** migrações versionadas (Flyway/Liquibase se for Java; Alembic se for Python) — escolher **uma** stack na Fase 3 e manter.

---

### Fase 4 — Coleta assistida (Maps / guias)

**Objetivo:** menos cópia manual, ainda respeitando limites.

**Tarefas:**

1. Um **único** conector bem testado (ex.: export do Maps por cidade).
2. Import para planilha ou Postgres.
3. Log de erros e “linhas rejeitadas” (cidade fora da geo-cerca).

**Pronto quando:** uma execução diária gera lista revisável em menos tempo que o manual puro.

**Melhoria:** fila de “precisa revisão humana” para leads com score baixo de confiança.

---

### Fase 5 — Instagram público (enriquecimento)

**Objetivo:** validar “multimarcas real” e “já vende a marca”.

**Tarefas:**

1. Ler só o **mínimo** necessário (bio + N posts).
2. Contar @ de marcas com **lista allowlist** atualizável.
3. Marcar flags no banco/planilha.

**Pronto quando:** amostra de 30 lojas mostra que a regra **reduz** falso positivo.

**Melhoria:** não usar login de Instagram no robô se não for indispensável.

---

### Fase 6 — WhatsApp semi-automático (Evolution API)

**Objetivo:** após **aprovação**, enviar por API com delay e variações.

**Tarefas:**

1. Número **dedicado**; VPS estável; Evolution instalado; HTTPS.
2. Fluxo: só envia se status = `aprovado_pelo_representante`.
3. Métricas: quantos enviados, quantos responderam (manual).

**Pronto quando:** em um dia de teste, **nenhuma** mensagem sai sem aprovação e os delays foram respeitados.

**Melhoria:** pausa global se WhatsApp sinalizar problema de sessão.

---

### Fase 7 — Painel (Retool, Bubble ou front próprio)

**Objetivo:** Kanban visual e fila “10 do dia”.

**Tarefas:**

1. Tela de lista com filtros (cidade, score, estágio).
2. Drag-and-drop ou botões de estágio.
3. Tela de aprovação de mensagem.

**Pronto quando:** você não precisa abrir SQL para operar o dia.

---

## 10. Checklist passo a passo (simples)

**Como usar:** marca cada caixa `- [ ]` como `- [x]` quando concluir. **Não avance para a fase seguinte** até a atual estar fechada — assim evitas retrabalho e dados bagunçados.

**Lembra-te da ideia:** o Clientes Hunter ajuda a **encontrar lojas**, **filtrar** as que valem a pena na tua área, **falar por WhatsApp** com mensagem boa (tu aprovando no início) e **acompanhar** no Kanban até fechar ou perder.

---

### Fase 0 — Decidir as regras (antes de automatizar qualquer coisa)

- [x] **Fechar a lista de cidades** onde trabalhas (DF + Norte GO) e anotar cidades que **não** queres priorizar.  
  *Por quê:* isto é a “cerca” do projeto; lead fora da lista vira ruído.

- [x] **Escrever em papel/planilha o critério “multimarcas de verdade”** (ex.: mínimo de marcas diferentes).  
  *Por quê:* sem regra clara, não dá para qualificar nem ensinar o sistema depois.

- [x] **Definir como reconhecer “já vende a marca”** (palavras na bio, posts, etc.).  
  *Por quê:* evita importunar cliente que já é teu.

- [ ] **Definir limite diário** de novas abordagens e **3 a 5 textos** de primeiro contacto (variações).  
  *Por quê:* protege a tua conta de WhatsApp e mantém a abordagem humana. *(Limite definido em REGRAS; textos na Task A3.)*

- [x] **Criar a planilha modelo** com colunas: nome, cidade, telefone, @Instagram, link WhatsApp, fonte, score, estágio Kanban, notas, data último contacto.  
  *Por quê:* é a base mínima para o MVP manual e tudo o que vier depois. *(Templates: [`templates/planilha/`](templates/planilha/) — importar no Google Sheets.)*

- [x] **Teste de “outra pessoa entende”:** alguém lê as regras numa página e percebe sem ti ao lado.  
  *Por quê:* se só tu entendes, o projeto não escala nem sobrevive às férias.

**Fase 0 pronta quando:** planilha existe + regras escritas e compreensíveis. *(Planilha: templates prontos; falta limite+textos A3 para fechar 100%.)*

---

### Fase 1 — Trabalhar à mão (primeiro ganho de tempo, risco baixo)

- [ ] **Buscar lojas** (ex.: Google Maps) **cidade a cidade**, só dentro da tua lista.  
  *Por quê:* treinas o olho e validas termos de busca antes de scripts.

- [ ] **Preencher a planilha** com nome, contacto, fonte e cidade **sem gralhas** na cidade.  
  *Por quê:* filtros e relatórios só funcionam com dados limpos.

- [ ] **Normalizar telefone** (DDD, código 55) e gerar link `https://wa.me/55...` sem caracteres a mais.  
  *Por quê:* um dígito errado = mensagem para o sítio errado.

- [ ] **Escrever mensagem personalizada** por loja, **ler em voz alta**, enviar **tu manualmente**.  
  *Por quê:* no MVP, tu és o controlo de qualidade e de ética.

- [ ] **Mover o estágio no Kanban** (coluna) e anotar **data + nota curta** quando houver mudança.  
  *Por quê:* daqui a uma semana não te lembras do que foi dito.

**Fase 1 pronta quando:** num dia consegues tratar ~10 leads novos de forma consistente, sem duplicar erros grosseiros.

---

### Fase 2 — Telegram / n8n (opcional — só avisos)

- [ ] **Criar bot no Telegram** e guardar token com cuidado (não commits públicos).  
  *Por quê:* o bot manda alertas para ti, não substitui o WhatsApp da loja.

- [ ] **Ligar um fluxo simples:** “entrou lead novo / há texto sugerido” → mensagem no Telegram.  
  *Por quê:* não perdes oportunidades quando estás noutra tarefa.

**Fase 2 pronta quando:** um teste (linha nova na planilha ou evento de teste) gera aviso em pouco tempo.

---

### Fase 3 — Base de dados (histórico sério)

- [ ] **PostgreSQL a correr** (ex.: Docker no teu PC).  
  *Por quê:* planilha cresce; base dá histórico, consultas e deduplicação.

- [ ] **Tabelas mínimas:** leads, eventos de mudança de estágio, origens.  
  *Por quê:* sabes *quando* e *porquê* cada lead mudou de coluna.

- [ ] **Testar duplicados:** mesmo telefone ou mesmo @ não devem criar dois “mundos”.  
  *Por quê:* duplicar contactos irrita lojistas e estraga métricas.

**Fase 3 pronta quando:** consegues explicar “de onde veio cada lead” só olhando para a base.

---

### Fase 4 — Importar do Maps / guias (menos copiar-colar)

- [ ] **Um único método de importação** bem testado (export + CSV ou script pequeno).  
  *Por quê:* vários métodos ao mesmo tempo = confusão e bugs.

- [ ] **Registar erros e linhas rejeitadas** (ex.: cidade fora da geo-cerca).  
  *Por quê:* sabes o que falhou em vez de dados silenciosamente errados.

**Fase 4 pronta quando:** uma “corrida” diária poupa tempo claro vs. fazer tudo à mão.

---

### Fase 5 — Instagram público (enriquecer)

- [ ] **Ler só o necessário:** bio + poucos posts por perfil.  
  *Por quê:* menos dados = menos risco e menos complexidade.

- [ ] **Contar marcas com lista que podes atualizar** (allowlist).  
  *Por quê:* a regra “multimarcas” fica objetiva.

- [ ] **Validar com ~30 lojas reais** se a regra reduz contactos maus.  
  *Por quê:* métrica simples antes de automatizar em massa.

**Fase 5 pronta quando:** vês menos “falsos bons” leads na fila.

---

### Fase 6 — WhatsApp semi-automático (só com maturidade)

- [ ] **Número dedicado**, aprovação humana **obrigatória**, atrasos entre envios e limite diário.  
  *Por quê:* sem isto, risco de bloqueio e de parecer spam.

- [ ] **Nenhuma mensagem sai** sem estado tipo “aprovado pelo representante”.  
  *Por quê:* controlo explícito; em dúvida, não envia.

**Fase 6 pronta quando:** dia de teste sem envios acidentais e com delays respeitados.

---

### Fase 7 — Painel (Kanban visível)

- [ ] **Ecrã com lista/filtros** (cidade, score, estágio) e forma fácil de mudar estágio.  
  *Por quê:* o dia a dia não pode depender de SQL.

- [ ] **Sítio para rever e aprovar texto** antes de contactar (se ainda aplicável).  
  *Por quê:* mantém o princípio do MVP ético.

**Fase 7 pronta quando:** operas o funil inteiro sem abrir a base “na mão”.

---

### Visão de uma linha (todas as fases)

| Fase | Entregável mínimo |
|------|-------------------|
| 0 | Regras + planilha modelo |
| 1 | Fluxo manual ponta a ponta |
| 2 | Telegram avisa evento novo |
| 3 | Postgres com leads + eventos |
| 4 | Import Maps/guias com log |
| 5 | Enriquecimento Instagram |
| 6 | Evolution com aprovação + delay |
| 7 | Painel Kanban |

---

## 11. Como usar este plano no Cursor (Superpowers / padrão dos projetos)

1. Para cada fase, abra **Plan Mode** e peça: “implementar só Fase X do PLANO-CLIENTES-HUNTER.md”.
2. Salve planos aprovados em `.cursor/plans/` (ex.: `ogoichi-hunter-fase-3-postgres.md`).
3. Mudanças sensíveis (dados pessoais, automação WhatsApp, scraping): **aprovação humana** antes de expandir escopo.

---

## 12. Ideias de melhoria futura (backlog)

- Mapa heatmap por cidade (onde ainda falta loja).
- Importar **lista de marcas concorrentes** para filtro automático.
- Biblioteca de **kits de fotos** versionados por coleção (Verão 26, etc.).
- Modo **“reenviar follow-up”** com template separado (com aprovação).
- Export CSV para o CRM interno, se existir padrão interno.

---

## 13. Resumo para o júnior (o que fazer amanhã)

1. Ler **Fase 0** e **Fase 1** com calma.  
2. Montar a **planilha** e **testar 5 lojas reais** manualmente.  
3. Só então pedir ajuda para automatizar **uma** coisa (ex.: Telegram ou import CSV).  
4. **Não** começar por Evolution API se o manual ainda não estiver confortável — o risco e o custo não compensam.

---

*Documento vivo: ao fechar cada fase, atualize este arquivo com datas, decisões e o que mudou nas regras de negócio.*
