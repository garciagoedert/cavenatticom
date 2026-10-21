# Prompt para o Codex — reformulação editorial do site Cavenatti

Trabalhe no projeto `/Users/marianapaul/Desktop/Claude/Cavenatti/site`. O site atual foi feito com Claude, mas os arquivos de origem, estilos, design system e imagens estão nesta pasta e no diretório `Fotos` do projeto. Leia primeiro `README.md`, `copy-site-cavenatti.md`, `proposta-copy-v2.md`, `src/build.py`, `src/imersao_corpo.html`, os estilos em `public/css/` e o inventário de imagens. Analise o resultado atual antes de alterar. A proposta de copy é a base editorial; refine frases quando necessário para melhorar a leitura, preservando os fatos e as pendências.

## Objetivo

Reformule **design e copy** para apresentar Mrs Master Cavenatti e Master Cavenatti como fundadores da Kihap, com duas marcas pessoais fortes e peso equivalente. O site deve funcionar como portfólio de autoridade e porta de entrada para empresas, organizadores de eventos, imprensa e parceiros contratarem cada fundador ou os dois. A Kihap é a prova concreta da atuação conjunta, mas este site não é uma página de matrícula.

O conceito visual é **um site editorial sobre duas pessoas em ação**. Preserve a identidade já construída — assinaturas, tipografia, cobre da Mrs Master, petróleo do Master, elo visual com a Kihap e a faixa como elemento de marca — e redesenhe a hierarquia, a sequência e o ritmo das páginas. Busque impacto por fotografia real, composição, escala tipográfica e espaço; evite uma sucessão uniforme de cartões, efeitos gratuitos e aparência de template corporativo.

## Narrativa

- **Disciplina** é o fio que liga esporte, educação, liderança, empresa e vida em família. Mostre o que ela permite construir e sustentar. Não a reduza a rigidez, produtividade ou uma frase motivacional genérica.
- **Família** é uma dimensão compartilhada da história dos dois. Dê protagonismo igual a ambos como pais e parceiros; use um episódio real quando for fornecido em `[história familiar aprovada pelos fundadores]`. Até lá, escreva com sobriedade, sem idealizar a rotina nem usar os filhos como prova comercial.
- **Mrs Master:** destaque autonomia, dez títulos mundiais de Taekwondo, formação, mestrado em Taekwondo, liderança e atuação como cofundadora. A maternidade integra a história dela, mas não substitui sua autoridade. Não invente uma causa, palestra ou programa voltado a mulheres.
- **Master:** destaque ensino, gestão, liderança e disciplina aplicada à vida real. Sua página deve ter o mesmo nível de profundidade e a mesma estrutura da página dela.
- Remova as frases “ela, mais coração / ele, mais razão” e “ela, mais reservada / ele, mais expansivo”. Substitua impressões de personalidade por contribuições, decisões e histórias concretas.

## Direção visual por área

1. **Home:** mantenha uma abertura forte para a dupla, mas teste uma combinação de fotos que mostre mais do que dois chutes. Apresente os dois como fundadores na primeira tela e deixe visíveis os caminhos para as páginas individuais. Organize a sequência como: abertura; duas autoridades; contribuição de cada um e construção conjunta; disciplina na prática; dimensão familiar; Kihap e números; ofertas para públicos externos; contato. Use a faixa da marca como fio visual discreto que passa do cobre ao petróleo e se encontra nas seções conjuntas.
2. **Páginas individuais:** mesma arquitetura e peso visual: Abertura, Sobre (incluindo família e hobbies), Trajetória, Formações acadêmicas e cursos, Palestras ministradas, Indicações de livros e Contato. A fotografia e os exemplos devem tornar cada página própria. Evite que toda a trajetória vire uma grade de cartões iguais. Use uma linha editorial ou capítulos com marcos, imagens e respiro.
3. **Fotos:** examine primeiro `Fotos/` e `site/public/img/`. Use retratos, cenas de ensino, atuação empresarial, esporte e família conforme a história de cada seção. Fotos de família devem ter contexto e autorização. Se alguma imagem indispensável não existir, continue com a melhor foto disponível e entregue uma lista de produção com **página, seção, enquadramento, orientação, uso pretendido e prioridade**. Não invente nem gere rostos dos fundadores.
4. **Livros:** apresente como pequena biblioteca editorial, com capa da edição escolhida, título, autor e comentário pessoal aprovado. Sem carrossel obrigatório nem card vazio.
5. **Programas e palestras:** separe “Com a Mrs Master”, “Com o Master” e “Com os dois”. Cada oferta deve mostrar autoria, tema, público, formato e chamada de contato; quando faltar algo, marque no material de revisão. Diferencie palestras já ministradas de temas propostos. Evite depender de hover para revelar conteúdo essencial, especialmente no celular.
6. **Imersão de 14/11/2026:** é uma oferta do Master. O conteúdo atual da página foi criado principalmente por ele. Preserve proposta, voz, estrutura central e informações já publicadas; ajuste somente integração visual, navegação, autoria e inconsistências claras. Dê destaque de campanha ao evento sem transformá-lo em item permanente do menu principal. “Introdução à Mente Faixa Preta” é outro item até confirmação de autoria e formato.
7. **Navegação e contato:** simplifique o menu principal, deixe evidente como contratar Mrs Master, Master ou os dois e retire links que prometem conteúdo inexistente. Reveja o formulário para registrar quem o visitante quer convidar.

## Fatos confirmados e lacunas

A cliente confirmou que os números atuais do site estão corretos, que a Mrs Master foi **dez vezes campeã mundial de Taekwondo** e que **fez mestrado em Taekwondo**. Preserve os números de modo consistente em todas as páginas. Não associe automaticamente o mestrado a Jacksonville. Use marcadores específicos em colchetes no material de revisão: `[instituição do mestrado]`, `[nome oficial do curso]`, `[período]`, `[titulação/conclusão]`, `[hobby que deseja compartilhar]`, `[título da palestra ministrada]`, `[capa da edição escolhida]`, `[comentário pessoal sobre o livro]` etc. Não invente datas, cursos, palestras, livros, depoimentos ou falas em primeira pessoa. Não publique colchetes nem componentes vazios; preserve a estrutura no código e oculte da prévia pública o que depender de resposta. Use `data-pendente` onde a checagem do projeto exigir.

## Execução e entrega

Edite a fonte dos textos em `src/build.py` e os arquivos de origem correspondentes; regenere `public/`. Preserve o design system como base, mas altere layouts e componentes quando a nova narrativa pedir. Faça a implementação completa possível com o material disponível, sem parar para solicitar fotos ou respostas; registre as pendências no fim.

Confira desktop e celular, incluindo legibilidade, contraste, foco por teclado, navegação, imagens, formulários e informações essenciais sem hover. Rode a checagem de pendências do projeto. Entregue: (a) prévia local das páginas; (b) resumo do que mudou na narrativa e no design; (c) lista exata das respostas pendentes, por página; (d) lista priorizada de novas fotos, apenas se forem realmente necessárias. Não publique nem faça deploy.
