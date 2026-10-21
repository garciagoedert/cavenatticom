// Página /imersao/: ingresso pré-selecionado pelos botões e envio para o checkout.
// O link do checkout fica em window.CAVENATTI.checkoutUrl (js/config.js). Vazio = inscrições ainda fechadas.
(function () {
  var sel = document.getElementById('ingresso');
  var f = document.getElementById('form-inscricao'), av = document.getElementById('aviso-form');
  if (!f || !sel) return;
  document.querySelectorAll('[data-ingresso]').forEach(function (a) {
    a.addEventListener('click', function () { sel.value = a.getAttribute('data-ingresso'); });
  });
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var nome = f.nome.value.trim(), email = f.email.value.trim();
    if (!nome || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) {
      av.className = 'im-aviso'; av.textContent = 'Preencha nome e um e-mail válido para continuar.';
      (!nome ? f.nome : f.email).focus(); return;
    }
    var url = (window.CAVENATTI && window.CAVENATTI.checkoutUrl) || '';
    if (!url) {
      av.className = 'im-retorno';
      av.textContent = 'O link de pagamento ainda não foi publicado. Assim que estiver no ar, este botão leva você direto ao checkout.';
      return;
    }
    location.href = url;
  });
})();
