# Entrega do site Cavenatti para publicação

**Versão:** 20/10/2026  
**Prévia para aprovação:** https://cavenatti-previa-de-aprovacao-26f96.goskip.app/  
**Projeto da prévia no Skip:** Cavenatti Prévia de Aprovação (ID 67920)

## O que está no pacote

- `public/`: site estático completo. Esta é a pasta que deve ser enviada para a hospedagem; `public/index.html` é a página inicial.
- `src/`: arquivos de origem que geram as sete páginas HTML, incluindo a página da Imersão. Guarde-os para futuras alterações de texto e estrutura.
- `checar-pendencias.py`: verificador de campos ainda não prontos para publicação definitiva.
- Arquivos `.md` na raiz: orientações do projeto, conteúdo editorial, perguntas para os fundadores e registro das pendências. Os arquivos `copy-site-cavenatti.md` e `prompt-correcoes-v1.md` são registros de versões anteriores; use `proposta-copy-v2.md` e a prévia atual como referência para aprovação.

O site usa HTML, CSS e JavaScript, sem instalação de bibliotecas. As fotos necessárias estão dentro de `public/`, inclusive a versão editada da foto do Master na Imersão (`public/imersao/master-falando-sem-ata.png`). A prévia no Skip foi adaptada para aquele serviço; **para outra hospedagem, use a pasta `public/` deste ZIP**.

## Antes da publicação definitiva

1. Obter aprovação dos fundadores para textos, fotos, valores, data, programação e informações biográficas. As respostas ainda necessárias estão em `perguntas-fundadores.md` e `REVISAO-PREVIA.md`.
2. Configurar o destino real do formulário de contato. A página envia um `POST` JSON; o endereço de recebimento é `formEndpoint` em `public/js/config.js`. Providenciar um serviço que receba esses dados, confirme o envio e encaminhe a mensagem à equipe.
3. Configurar a inscrição e o pagamento da Imersão. Hoje `checkoutUrl` em `public/js/config.js` está vazio. O fluxo atual redireciona para um único endereço e **não transmite ao checkout** o nome, e-mail, WhatsApp, tipo de ingresso ou cupom selecionados no formulário. A equipe responsável deve integrar esses dados e confirmar os valores de Individual (R$ 297) e Dupla (R$ 499), descontos, capacidade e regras de compra antes de ativar inscrições.
4. Atualizar as marcações `data-pendente` nos formulários depois que as integrações estiverem funcionando. Executar `python3 checar-pendencias.py` na raiz do pacote. A publicação definitiva deve prosseguir quando o verificador indicar `Sem pendências.` e os dois fluxos tiverem sido testados de ponta a ponta.

**Estado desta entrega:** o site está pronto para revisão visual e editorial. Os formulários de contato e pagamento ainda não funcionam; a prévia publicada no Skip avisa isso aos visitantes. A pasta `public/` do pacote não inclui esse aviso específico da prévia; a equipe de publicação deve inserir um aviso visível caso coloque a versão incompleta em um domínio acessível ao público.

## Como hospedar

Em qualquer serviço de hospedagem estática, configure `public/` como a pasta de publicação. É necessário preservar a estrutura de pastas para que funcionem as rotas `/fernanda/`, `/master/`, `/programas/`, `/imprensa/`, `/contato/` e `/imersao/`. Configure o domínio e HTTPS no serviço escolhido.

Para conferir antes da publicação, na raiz do pacote:

```sh
cd public
python3 -m http.server 8765
```

Abra `http://localhost:8765/` no navegador. Teste também as páginas internas, imagens, menu em celular e desktop, formulário de contato e checkout após a integração.

## Como atualizar o site

Os textos e a estrutura das páginas estão em `src/build.py` e `src/imersao_corpo.html`. Depois de editá-los, execute `python3 src/build.py` na raiz do pacote para regenerar o HTML em `public/`. **Esse comando também redefine `public/js/config.js` com endereços vazios**; se as integrações forem configuradas diretamente nesse arquivo, é preciso reaplicá-las após cada geração. Para uma manutenção permanente, atualize também a linha que escreve `config.js` em `src/build.py` ou injete a configuração no processo de publicação.

As imagens, CSS e JavaScript de interação ficam em `public/`. A pasta `public/` já contém as páginas geradas; não é necessário executar o gerador para apenas hospedar esta entrega.
