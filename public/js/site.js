(function () {
  var menu = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  if (menu && nav) {
    menu.addEventListener('click', function () {
      var aberto = nav.classList.toggle('aberto');
      menu.setAttribute('aria-expanded', aberto ? 'true' : 'false');
    });
    nav.addEventListener('click', function (event) {
      if (event.target.closest('a')) {
        nav.classList.remove('aberto');
        menu.setAttribute('aria-expanded', 'false');
      }
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && nav.classList.contains('aberto')) {
        nav.classList.remove('aberto');
        menu.setAttribute('aria-expanded', 'false');
        menu.focus();
      }
    });
  }

  var form = document.getElementById('form-contato');
  if (!form) return;
  var assunto = new URLSearchParams(location.search).get('assunto');
  if (assunto) {
    var select = form.elements['assunto'];
    for (var i = 0; i < select.options.length; i++) {
      if (select.options[i].value === assunto) {
        select.selectedIndex = i;
        break;
      }
    }
  }
  var ok = document.getElementById('status-ok');
  var falha = document.getElementById('status-falha');
  var emailCampo = document.getElementById('campo-email');
  var emailAjuda = document.getElementById('email-ajuda');
  var emailValido = function (valor) { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(valor); };

  function erroEmail(ativo) {
    emailCampo.classList.toggle('erro', ativo);
    form.elements['email'].setAttribute('aria-invalid', ativo ? 'true' : 'false');
    emailAjuda.textContent = ativo ? 'Confira o e-mail, por exemplo nome@empresa.com.br.' : '';
  }

  form.elements['email'].addEventListener('blur', function () {
    if (this.value.trim()) erroEmail(!emailValido(this.value.trim()));
  });

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    ok.hidden = true;
    falha.hidden = true;
    var nome = form.elements['nome'].value.trim();
    var email = form.elements['email'].value.trim();
    var mensagem = form.elements['mensagem'].value.trim();
    if (!nome || !mensagem) {
      falha.textContent = 'Preencha seu nome e a mensagem.';
      falha.hidden = false;
      (!nome ? form.elements['nome'] : form.elements['mensagem']).focus();
      return;
    }
    if (!emailValido(email)) {
      erroEmail(true);
      form.elements['email'].focus();
      return;
    }
    erroEmail(false);
    var endpoint = (window.CAVENATTI && window.CAVENATTI.formEndpoint) || '';
    if (!endpoint) {
      falha.textContent = 'O envio ainda não está configurado nesta prévia.';
      falha.hidden = false;
      return;
    }
    var dados = {};
    new FormData(form).forEach(function (valor, chave) { dados[chave] = valor; });
    fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(dados) })
      .then(function (resposta) {
        if (!resposta.ok) throw new Error(resposta.status);
        ok.hidden = false;
        form.reset();
        ok.focus();
      })
      .catch(function () {
        falha.textContent = 'Não foi possível enviar agora. Tente novamente em instantes.';
        falha.hidden = false;
      });
  });
})();
