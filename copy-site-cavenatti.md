# Copy do site cavenatti.com

**Arquivo histórico da primeira versão.** Para a prévia atual, consulte `proposta-copy-v2.md`, `prompt-implementacao-copy-v2.md` e `src/build.py`.

Versão 1 · 13/10/2026 · preparada por Mariana (e.feito) para o desenvolvimento do site com o Claude Code.

## Contexto para o desenvolvimento

- **Site:** cavenatti.com, site de Mrs & Mr Master Cavenatti (Mrs Master Cavenatti e Master Cavenatti), fundadores da Kihap. É um site de autoridade, palestras, imprensa e parcerias, e também a vitrine dos produtos dos dois. Não é site de matrícula; isso fica no kihap.com.br.
- **Design system (fonte da verdade visual):** https://claude.ai/artifact/3NgnJvSeSAxHoPkbKgrpiY. Leia primeiro o README e o tokens.json de lá.
- **Resumo dos tokens:**
  - Papel `#F4F3F0` · Papel elevado `#FFFFFF` · Tinta `#1A1918` · Tinta suave `#57534E` · Linha `#D9D6D0`
  - Fernanda (cobre) `#A0451F`, tinta clara `#F5E1D6`
  - Master (petróleo) `#1F4A5A`, tinta clara `#D8E6EA`
  - Elo Kihap: ouro `#DEA129` (nunca como texto sobre fundo claro; para texto use `#7E5A12`), grafite `#303030`
  - Mente Faixa Preta: fundo `#0F0F0F` com faixa ouro (exclusivo desse produto)
  - Tema escuro: ver tokens.json do design system
- **Tipografia (Google Fonts):** Archivo (títulos, nomes, rótulos, botões, números; títulos grandes em peso 800 com `font-stretch: 115%`) e Source Serif 4 (textos longos e citações).
- **Faixa:** barra de 8px, cantos retos, na cor do fundador. Dupla (metade cobre, metade petróleo) para o que é dos dois.
- **Cantos retos** em cartões e imagens; 2px só em botões e campos. Cartões sem sombra, borda de 1px.
- **Assinaturas (não alterar):**
  - Marca principal: **Mrs & Mr Master Cavenatti** (MRS & MR MASTER em caixa alta espaçada acima de CAVENATTI)
  - Fernanda: **Mrs Master Cavenatti** (o primeiro nome não aparece no site; decisão de 13/10/2026)
  - Master: **Master Cavenatti**
  - Produtos: "por Mrs Master Cavenatti", "por Master Cavenatti" ou "por Mrs & Mr Master Cavenatti"
- **Componentes do design system usados abaixo:** Assinaturas, Faixa, Botão, Cabeçalho de seção, Citação, Provas, Cartão de fundador, Cartão de produto, Contato, Home.
- **Regras de texto:** português do Brasil; sem emoji; sem travessão no meio da frase; todo número com fonte; trechos marcados [confirmar] não vão ao ar sem validação.

## Mapa do site

1. `/` Home
2. `/fernanda` Mrs Master Cavenatti
3. `/master` Master Cavenatti
4. `/historia` Nossa história (pode começar como seção da Home)
5. `/programas` e uma página por produto (Mente Faixa Preta, Palestras, Mentoria, Evento 14/11)
6. `/imprensa` Kit de imprensa com bios curtas
7. `/contato` Formulário único (assunto: palestra, imprensa, parceria, mentoria, outro)

---

## 1. Home

**Topo (Assinaturas):** MRS & MR MASTER / CAVENATTI
**Navegação:** Mrs Master · Master · Programas · Palestras · Imprensa · Contato

**Abertura**
- Sobretítulo: FUNDADORES DA KIHAP
- Título: Duas trajetórias, uma mesma disciplina.
- Subtítulo: Ela chegou ao tatame aos 14 anos e fez da ciência do movimento a base da sua formação. Ele começou em 1994 e transformou o Taekwondo em empresa, método e missão. Juntos, construíram uma escola com mais de 1.200 alunos.

**Entrada Fernanda (Cartão de fundador, cor cobre, à esquerda)**
- Sobretítulo: FORMAÇÃO · CIÊNCIA DO MOVIMENTO
- Assinatura: Mrs Master / CAVENATTI
- Linha: 10x campeã mundial · Educação Física e Fisiologia do Exercício (UFPR) · cofundadora da Kihap
- Link: Conhecer a trajetória →

**Entrada Master (Cartão de fundador, cor petróleo, à direita)**
- Sobretítulo: DISCIPLINA APLICADA
- Assinatura: Master / CAVENATTI
- Linha: Taekwondo desde 1994 · Mestre desde 2018 · triatleta amador · fundador da Kihap
- Link: Conhecer a trajetória →

**Nossa história (faixa dupla)**
- Sobretítulo: NOSSA HISTÓRIA
- Título: Duas formações, uma prática.
- Texto: Uma formação em Educação Física e Fisiologia do Exercício. Outra em Administração. Uma faixa preta conquistada na adolescência, outra em 1997. O que une as duas trajetórias é a mesma convicção: disciplina não é rigidez, é o que permite a cada pessoa evoluir na própria realidade. Dessa convicção nasceu a Kihap.
- Link: Ler a história completa →

**Provas (Kihap, em cor tinta)**
- +1.200 · alunos
- +30 · instrutores
- 10 · unidades
- 3 · cidades (Brasília, Florianópolis e Dourados)

**Prateleira de programas (Cartão de produto)**
- Título: Programas, palestras e mentorias
- Mente Faixa Preta · PROGRAMA PRINCIPAL · por Master Cavenatti · "Clareza, planejamento e ação para transformar o que você já sabe em constância." · Ver o programa →
- Palestras · PARA EMPRESAS · por Master Cavenatti · "A disciplina que sustenta o sucesso, para lideranças e equipes." · Ver temas →
- Evento · 14 NOV 2026 · por Master Cavenatti · "[tema a definir]" · Quero participar →
- Produto de Mrs Master Cavenatti · A DEFINIR · por Mrs Master Cavenatti · "[a definir]" (cartão tracejado, sem link)

**Bloco Kihap (faixa ouro)**
- Sobretítulo: FUNDADORES DA KIHAP
- Título: A escola que construímos.
- Texto: Uma comunidade de desenvolvimento físico, mental e emocional, com 6 unidades em Brasília, 3 em Florianópolis e 1 em Dourados. Lá, a disciplina positiva e o comprometimento ajudam cada aluno a evoluir na própria realidade.
- Link: Visitar kihap.com.br ↗

**Imprensa · Palestras · Parcerias (fundo grafite Kihap)**
- Imprensa: Biografias, fotos em alta resolução e números para veículos e organizadores. · Baixar kit de imprensa →
- Palestras: Disciplina, constância e alta performance para empresas e eventos. · Consultar agenda →
- Parcerias: Projetos institucionais e colaborações com os fundadores. · Falar com a equipe →

**Rodapé:** MRS & MR MASTER CAVENATTI · Fundadores da Kihap · Instagram · LinkedIn

---

## 2. Página Mrs Master Cavenatti (`/fernanda`, cor cobre)

**Abertura**
- Sobretítulo: FORMAÇÃO · CIÊNCIA DO MOVIMENTO
- Assinatura: Mrs Master / CAVENATTI
- Texto em primeira pessoa [proposta, validar com Mrs Master Cavenatti]: Comecei no Taekwondo aos 14 anos. Na universidade, fui buscar no corpo humano as respostas que o tatame me fazia perguntar. Hoje, o que aprendi nas duas pontas, a prática e a ciência, está na formação de cada aluno e instrutor da Kihap.

**Trajetória (linha do tempo)**
- 14 anos: início no Taekwondo
- Faixa preta: [confirmar Dan e ano]
- UFPR: graduação em Educação Física
- UFPR: especialização em Fisiologia do Exercício
- 10 títulos mundiais
- Kihap: sócia e cofundadora

**Provas:** 10x · campeã mundial | [Dan] · faixa preta [confirmar] | UFPR · Educação Física e Fisiologia do Exercício

**Texto de apoio**
Mrs Master Cavenatti une alto rendimento e conhecimento científico. Dez vezes campeã mundial, formada em Educação Física e especialista em Fisiologia do Exercício pela Universidade Federal do Paraná, é sócia e cofundadora da Kihap. Mãe do Benício e da Serena, leva para a escola a mesma convicção que guiou sua carreira: com disciplina positiva e comprometimento, cada pessoa evolui dentro da própria realidade.

**Chamada (Botão acento cobre):** Convidar Mrs Master Cavenatti para um evento →

---

## 3. Página Master Cavenatti (`/master`, cor petróleo)

**Abertura**
- Sobretítulo: DISCIPLINA APLICADA
- Assinatura: Master / CAVENATTI
- Texto em primeira pessoa [proposta, validar com Master]: Comecei no Taekwondo em 1994. Aprendi cedo que faixa preta não é um ponto de chegada, é o hábito de voltar ao treino todos os dias. É isso que ensino: não se trata de fazer mais, e sim de fazer com constância aquilo que você já sabe que importa.

**Trajetória (linha do tempo)**
- 1994: início no Taekwondo
- 1997: faixa preta 1º Dan
- 2004: instrutor certificado
- Foz do Iguaçu (PR): primeiras escolas próprias [confirmar ano]
- 2018: reconhecido como Mestre
- Hoje: fundador e líder da Kihap, com mais de 1.200 alunos e 30 instrutores

**Provas:** 1994 · início no Taekwondo | 2018 · reconhecido como Mestre | +1.200 · alunos na Kihap | Triatleta amador

**Texto de apoio**
Master Cavenatti é formado em Administração e empreendedor desde as primeiras escolas, em Foz do Iguaçu. Uniu a gestão à prática marcial e construiu a Kihap, hoje com 10 unidades em três cidades. Casado com Mrs Master Cavenatti e pai do Benício e da Serena, leva para empresários e líderes o que o tatame e o triatlo lhe ensinaram: disciplina não é peso, é o que sustenta a vida que você quer viver.

**Chamada (Botão acento petróleo):** Levar a palestra para minha empresa →

---

## 4. Bios curtas para imprensa (até 60 palavras)

**Mrs Master Cavenatti:** Sócia e cofundadora da Kihap, dez vezes campeã mundial de Taekwondo. Começou nas artes marciais aos 14 anos, é formada em Educação Física e especialista em Fisiologia do Exercício pela UFPR. Mãe do Benício e da Serena.

**Master Cavenatti:** Fundador da Kihap, escola de artes marciais com mais de 1.200 alunos e 10 unidades. Pratica Taekwondo desde 1994, foi reconhecido como Mestre em 2018, é formado em Administração e é triatleta amador. Pai do Benício e da Serena.

---

## 5. Contato (componente Contato)

- Campos: Nome · E-mail · Assunto (Palestra para minha empresa, Imprensa, Parceria, Mentoria, Outro) · Data prevista do evento (opcional) · Mensagem
- Botão: Enviar mensagem
- Abaixo do botão: Respondemos em até [prazo a definir com a equipe].
- Erro de e-mail: "Falta o domínio no e-mail, por exemplo nome@empresa.com.br."
- Confirmação: "Mensagem enviada. Nossa equipe responde em até [prazo]."

---

## Pendências antes de publicar

1. Alunos: os textos dizem +1.200, o Instagram do Master dizia +1.100 ativos e o kihap.com.br diz +1.000 formados. Usado +1.200; definir se são ativos ou formados.
2. Dan e ano da faixa preta de Fernanda (o Instagram dela diz 6º Dan; o texto base não menciona).
3. Títulos do Master: o Instagram cita "4x campeão mundial" e "Ironman"; o texto base cita só "triatleta amador". Ficaram de fora até confirmação.
4. Foz do Iguaçu: ano das escolas.
5. Ano de fundação da Kihap (diagnóstico anterior cita 2012; não usado).
6. Os dois parágrafos em primeira pessoa são propostas e precisam de aprovação.
7. Tema e nome do evento de 14/11 e os produtos de Fernanda.

## Fontes

- Textos biográficos de Mrs Master Cavenatti e Master Cavenatti enviados por Mariana em 13/10/2026
- Instagram @fernandacavenatti e @master_cavenatti (setembro de 2026)
- kihap.com.br
- Resumo de atuação do Master Cavenatti (Master Cavenatti - Resumo Atuação.docx)
