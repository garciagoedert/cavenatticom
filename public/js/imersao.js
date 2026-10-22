// Página /imersao/: ingresso pré-selecionado pelos botões e envio para a planilha + checkout do Mercado Pago.
(function () {
  var sel = document.getElementById('ingresso');
  var f = document.getElementById('form-inscricao'), av = document.getElementById('aviso-form');
  if (!f || !sel) return;

  var btn = f.querySelector('button[type="submit"]');

  document.querySelectorAll('[data-ingresso]').forEach(function (a) {
    a.addEventListener('click', function () {
      sel.value = a.getAttribute('data-ingresso');
    });
  });

  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var nome = f.nome.value.trim(), email = f.email.value.trim();
    if (!nome || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) {
      av.className = 'im-aviso';
      av.textContent = 'Preencha nome e um e-mail válido para continuar.';
      (!nome ? f.nome : f.email).focus();
      return;
    }

    var cfg = window.CAVENATTI || {};
    var sheetUrl = cfg.sheetUrl || 'https://script.google.com/macros/s/AKfycbwW3OEpez3uDEOmf8JTnFCY3gmnf1pU-lE8gzdONZ4mgY9aErepgbz-Y5ar2LxCyNpeRA/exec';
    var checkout = (f.ingresso.value === 'dupla')
      ? (cfg.checkoutDupla || 'https://mpago.li/1LnY6BS')
      : (cfg.checkoutIndividual || 'https://mpago.li/1Rs26z1');

    var payload = {
      nome: nome,
      email: email,
      whatsapp: (f.whatsapp ? f.whatsapp.value.trim() : ''),
      ingresso: (f.ingresso ? f.ingresso.value : 'individual'),
      cupom: (f.cupom ? f.cupom.value.trim() : '')
    };

    if (btn) {
      btn.disabled = true;
      btn.textContent = 'Redirecionando para o pagamento...';
    }
    av.className = 'im-retorno';
    av.textContent = 'Gravando sua inscrição e abrindo o checkout do Mercado Pago...';

    var redirected = false;
    function irParaCheckout() {
      if (!redirected) {
        redirected = true;
        window.location.href = checkout;
      }
    }

    try {
      fetch(sheetUrl, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'text/plain;charset=utf-8' },
        body: JSON.stringify(payload)
      }).then(function () {
        irParaCheckout();
      }).catch(function () {
        irParaCheckout();
      });
    } catch (err) {
      irParaCheckout();
    }

    // Fallback de segurança para garantir o redirecionamento
    setTimeout(irParaCheckout, 1600);
  });
})();
