# cavenatti.com (prévia editorial)

HTML, CSS e JS puros. As páginas são geradas por `src/build.py` (sem dependências, Python 3).

```
python3 src/build.py            # regenera public/
python3 checar-pendencias.py    # lista trechos ainda não aprovados; sai com erro se houver
cd public && python3 -m http.server 8765   # pré-visualizar em http://localhost:8765
```

- `public/css/tokens.css`: tokens do design system (claro e escuro). `componentes.css`: bundle.css do design system. `site.css`: layout.
- Conteúdo e copy da prévia ficam em `src/build.py`. Direção editorial atual: `proposta-copy-v2.md`; a antiga `copy-site-cavenatti.md` permanece como registro da primeira versão.
- A nova camada visual está em `public/css/editorial.css`, sobre os tokens e componentes originais. A página da Imersão mantém seu estilo próprio.
- Formulário: defina `formEndpoint` no gerador `src/build.py` antes de publicar (POST JSON com nome, email, empresa, assunto, cidade, data, mensagem). A prévia não simula envio.
- O roteiro para apresentar a prévia aos fundadores, as pendências de conteúdo e as fotos a solicitar estão em `REVISAO-PREVIA.md`. As perguntas prontas para envio estão em `perguntas-fundadores.md`. Formulários sem destino configurado levam `data-pendente`. Só publicar com `checar-pendencias.py` limpo.
- A Home e a página de Programas divulgam Imersão, Introdução à Mente Faixa Preta (online, com os dois) e Academy. Os dois últimos encaminham interessados ao contato enquanto preço, ementa e acesso são confirmados.
- Imersão 14/11 (`/imersao/`): corpo em `src/imersao_corpo.html`, identidade Cavenatti v2, linha Faixa Preta, em `public/css/imersao.css` (classes `im-*`, sobre os tokens de `tokens.css`), script em `public/js/imersao.js`. O botão de inscrição usa `checkoutUrl` em `public/js/config.js`; enquanto estiver vazio, a página avisa que o pagamento ainda não foi publicado e o formulário fica marcado como pendente.
