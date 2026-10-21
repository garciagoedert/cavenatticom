# Correções do site cavenatti.com (revisão de 13/10/2026)

Leia `copy-site-cavenatti.md` antes de começar. A troca de "Fernanda" por "Mrs Master Cavenatti" é intencional: mantenha.

## Corrigir

1. **Fontes dos números.** Os dados +1.200 alunos, 30 instrutores, 10 unidades, 14 anos, 1997, 2004, Administração e UFPR vêm dos textos biográficos dos fundadores. Troque as legendas de fonte em todas as páginas por: "Fonte: textos biográficos de Mrs Master Cavenatti e Master Cavenatti, outubro de 2026." Na Home, se quiser manter kihap.com.br, cite apenas para as cidades.
2. **Link "Ler a história completa →".** Hoje aponta para a própria seção. Remova o link da Home até existir uma página `/historia`.
3. **Descrições de produto sem aspas.** Remova as aspas curvas das descrições dos cartões de produto (Home e Programas). Não são citações.
4. **Diferenciar Mrs Master e Master.** Nos cartões de fundador e nas aberturas das páginas, mantenha sempre a cor (cobre para Mrs Master, petróleo para Master) e coloque a faixa curta de 96px entre o nome e CAVENATTI, como no componente Assinaturas do design system.

## Ajustar

5. Na Home, a seção "Programas" deve ficar em fundo `--papel` (sem a classe `recuo`), para não repetir o fundo de "Nossa história".
6. Tema escuro: além do `@media (prefers-color-scheme: dark)`, repita os mesmos valores em `:root[data-theme="escuro"]`, e use `:root:not([data-theme="claro"])` no media query (já está), para que a troca manual de tema funcione nos dois sentidos.
7. Hierarquia de títulos: na Home, os nomes nos cartões de fundador devem ser `h2` (não `h3`), ou adicione um `h2` visualmente oculto "Os fundadores" na seção.
8. Rodapé: Instagram e LinkedIn com os endereços reais (@fernandacavenatti e @master_cavenatti, LinkedIn a confirmar). Enquanto não houver, esconda os links em vez de usar `href="#"`.
9. Link externo "Visitar kihap.com.br ↗": adicionar `target="_blank" rel="noopener"`.

## Não mexer

Cores, fontes, faixa, assinatura "Mrs & Mr Master Cavenatti", formulário de contato e marcações `data-pendente`.
