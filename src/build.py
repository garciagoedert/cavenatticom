#!/usr/bin/env python3
"""Gera a prévia editorial de cavenatti.com em public/."""
from pathlib import Path
from html import escape
import re
import time

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public"
VER = int(time.time())
FONTES = "https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..600;1,8..60,400&display=swap"
NAV = [
    ("/fernanda/", "Mrs Master"),
    ("/master/", "Master"),
    ("/programas/", "Programas e palestras"),
    ("/imersao/", "Imersão 14/11"),
    ("/imprensa/", "Imprensa"),
    ("/contato/", "Contato"),
]


def relativizar(html, arquivo):
    """Permite abrir a prévia direto do disco, inclusive links entre páginas."""
    prefixo = "../" * arquivo.count("/") or "./"

    def troca(match):
        attr, url = match.group(1), match.group(2)
        fragmento = ""
        if "#" in url:
            url, fragmento = url.split("#", 1)
            fragmento = "#" + fragmento
        consulta = ""
        if "?" in url:
            url, consulta = url.split("?", 1)
            consulta = "?" + consulta
        if url.endswith("/"):
            url += "index.html"
        return f'{attr}="{prefixo}{url.lstrip("/")}{consulta}{fragmento}"'

    return re.sub(r'(href|src)="(/(?:[^"/][^"]*)?)"', troca, html)


def imagem(src, alt, classe="", largura=None, altura=None, carregamento="lazy"):
    dimensoes = f' width="{largura}" height="{altura}"' if largura and altura else ""
    return f'<img class="{classe}" src="{src}" alt="{escape(alt)}" loading="{carregamento}"{dimensoes}>'


def faixa(dupla=False):
    return f'<span class="ed-faixa{" ed-faixa-dupla" if dupla else ""}" aria-hidden="true"></span>'


def cta(href, texto, secundaria=False):
    classe = "ed-button ed-button-outline" if secundaria else "ed-button"
    return f'<a class="{classe}" href="{href}">{texto}<span aria-hidden="true">↗</span></a>'


def header_section(numero, rotulo, titulo, id_):
    return f'<div class="ed-section-head"><span class="ed-index">{numero}</span><div><p class="ed-eyebrow">{rotulo}</p><h2 id="{id_}">{titulo}</h2></div></div>'


def layout(path, titulo, descricao, corpo, escopo="", scripts="", estilos=""):
    cur = ' aria-current="page"'
    nav = "\n".join(f'<a href="{href}"{(cur if href == path else "")}>{label}</a>' for href, label in NAV)
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{escape(descricao)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTES}">
<link rel="stylesheet" href="/css/tokens.css?v={VER}">
<link rel="stylesheet" href="/css/componentes.css?v={VER}">
<link rel="stylesheet" href="/css/site.css?v={VER}">
<link rel="stylesheet" href="/css/moderno.css?v={VER}">
<link rel="stylesheet" href="/css/editorial.css?v={VER}">
{estilos}</head>
<body class="cv {escopo}">
<a class="pulo" href="#principal">Ir para o conteúdo</a>
<header class="topo ed-topo"><div class="in">
  <a class="wmb" href="/" aria-label="Mrs &amp; Mr Master Cavenatti, página inicial"><span class="pre">Mrs &amp; Mr Master</span><span class="wm">CAVENATTI</span></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Principal">{nav}</nav>
</div></header>
<main id="principal">{corpo}</main>
<footer class="ed-footer"><div class="in ed-footer-grid">
  <div><span class="ed-footer-brand">MRS &amp; MR MASTER<br><strong>CAVENATTI</strong></span><p>Fundadores da Kihap. Duas trajetórias, uma construção em conjunto.</p></div>
  <div><p class="ed-eyebrow">Explore</p><a href="/fernanda/">Mrs Master</a><a href="/master/">Master</a><a href="/programas/">Programas e palestras</a><a href="/imersao/">Imersão 14/11</a></div>
  <div><p class="ed-eyebrow">Converse com a equipe</p><p>Para palestras, imprensa e parcerias.</p><a class="ed-footer-contact" href="/contato/">Entrar em contato ↗</a></div>
</div></footer>
{scripts}<script src="/js/site.js?v={VER}" defer></script>
</body></html>'''


HOME = f'''
<section class="ed-home-hero" aria-labelledby="home-title">
  <div class="ed-home-intro in">
    <div class="ed-home-copy">
      <p class="ed-eyebrow">Mrs &amp; Mr Master Cavenatti · Fundadores da Kihap</p>
      {faixa(True)}
      <h1 id="home-title">Duas trajetórias.<br><em>Uma construção</em> em conjunto.</h1>
      <p class="ed-lead">Ela une o alto rendimento, a Educação Física e o mestrado em Taekwondo. Ele leva a prática marcial para o ensino, a liderança e a gestão. A disciplina atravessa a escola que fundaram e a vida que constroem em família.</p>
      <div class="ed-actions">{cta('/fernanda/', 'Conheça a Mrs Master')}{cta('/master/', 'Conheça o Master', True)}</div>
    </div>
    <div class="ed-home-portraits">
      <figure class="ed-portrait ed-portrait-fer">{imagem('/img/hero-fernanda.jpg', 'Mrs Master Cavenatti praticando Taekwondo em área externa', carregamento='eager')}<figcaption>Mrs Master <span>Atleta · educadora · cofundadora</span></figcaption></figure>
      <figure class="ed-portrait ed-portrait-mas">{imagem('/img/master_cavenatti.jpeg', 'Master Cavenatti com uniforme de Taekwondo', carregamento='eager')}<figcaption>Master <span>Mestre · educador · cofundador</span></figcaption></figure>
    </div>
  </div>
  <div class="ed-home-hero-bottom in"><span>Esporte</span><span>Educação</span><span>Família</span><span>Liderança</span></div>
</section>

<section class="ed-founders ed-section in" aria-labelledby="fundadores-title">
  {header_section('01', 'Os fundadores', 'Duas vozes. Autoridades próprias.', 'fundadores-title')}
  <div class="ed-founder-grid">
    <article class="ed-founder ed-founder-fer">
      <div class="ed-founder-image">{imagem('/img/fernanda-medalha.jpg', 'Mrs Master Cavenatti com a filha e uma medalha de Taekwondo')}</div>
      <div class="ed-founder-body"><p class="ed-eyebrow">Mrs Master Cavenatti</p><h3>Conhecimento para ocupar o próprio espaço.</h3><p>10x campeã mundial de Taekwondo, tem formação em Educação Física e Fisiologia do Exercício, além de mestrado na modalidade. Cofundadora da Kihap, une experiência no esporte, conhecimento acadêmico e visão empreendedora.</p><a class="ed-text-link" href="/fernanda/">Conheça sua trajetória ↗</a></div>
    </article>
    <article class="ed-founder ed-founder-mas">
      <div class="ed-founder-image">{imagem('/img/master-em-aula.jpg', 'Master Cavenatti conduzindo uma aula de Taekwondo')}</div>
      <div class="ed-founder-body"><p class="ed-eyebrow">Master Cavenatti</p><h3>Disciplina que se torna prática.</h3><p>4x campeão mundial de Taekwondo, pratica a modalidade desde 1994 e construiu sua trajetória como mestre, educador e empreendedor. Cofundador da Kihap, conecta ensino, gestão e desenvolvimento de pessoas.</p><a class="ed-text-link" href="/master/">Conheça sua trajetória ↗</a></div>
    </article>
  </div>
</section>

<section class="ed-thesis ed-section" aria-labelledby="thesis-title"><div class="in ed-thesis-grid">
  <div><p class="ed-eyebrow">O que une os dois</p>{faixa(True)}<h2 id="thesis-title">Disciplina é o que dá continuidade ao que importa.</h2></div>
  <div class="ed-thesis-lines">
    <div><span>01 / Esporte</span><p>Treinar, aprender e voltar à prática.</p></div>
    <div><span>02 / Educação</span><p>Olhar para cada pessoa e acompanhar sua evolução.</p></div>
    <div><span>03 / Vida real</span><p>Construir uma empresa e estar presente na vida em família.</p></div>
  </div>
</div></section>

<section class="ed-family ed-section in" aria-labelledby="family-title">
  <div class="ed-family-photo">{imagem('/img/familia-estudio.jpg', 'Mrs Master e Master Cavenatti com Benício e Serena')}</div>
  <div class="ed-family-copy"><p class="ed-eyebrow">Além do tatame</p>{faixa(True)}<h2 id="family-title">Uma família também se constrói todos os dias.</h2><p>Mrs Master e Master dividem a vida, a criação dos filhos e a construção da Kihap. Aqui, disciplina não é uma imagem de perfeição: é a disposição de cuidar, assumir compromissos e continuar juntos.</p></div>
</section>

<section class="ed-kihap ed-section" aria-labelledby="kihap-title"><div class="in">
  <div class="ed-kihap-top"><div><p class="ed-eyebrow">O projeto que construíram</p>{faixa(True)}<h2 id="kihap-title">A Kihap é esse trabalho em movimento.</h2></div><p>Uma comunidade de desenvolvimento físico, mental e emocional. Nas escolas, as experiências dos dois se encontram no ensino, na formação de instrutores e na relação com as famílias.</p></div>
  <div class="ed-stats"><div><strong>+1.200</strong><span>alunos</span></div><div><strong>+30</strong><span>instrutores</span></div><div><strong>10</strong><span>unidades</span></div><div><strong>3</strong><span>cidades</span></div></div>
  <a class="ed-text-link" href="https://kihap.com.br" target="_blank" rel="noopener noreferrer">Conheça a Kihap ↗</a>
</div><div class="ed-kihap-image">{imagem('/img/kihap-comunidade.jpg', 'Comunidade Kihap reunida em um evento de artes marciais')}</div></section>

<section class="ed-offers ed-section in" aria-labelledby="offers-title">
  {header_section('02', 'Para empresas e eventos', 'Experiências com quem vive o que ensina.', 'offers-title')}
  <p class="ed-section-intro">Convide cada fundador ou converse sobre uma participação dos dois. Os temas e formatos são definidos de acordo com o público e o objetivo do encontro.</p>
  <div class="ed-offer-list">
    <article><span class="ed-offer-mark ed-fer-mark">01</span><div><p class="ed-eyebrow">Com a Mrs Master</p><h3>Esporte, movimento e liderança</h3><p>Uma conversa a construir a partir da experiência dela no alto rendimento, no estudo e no empreendedorismo.</p></div><a href="/contato/?assunto=Palestra%20com%20a%20Mrs%20Master" aria-label="Conversar sobre participação da Mrs Master">Conversar ↗</a></article>
    <article><span class="ed-offer-mark ed-mas-mark">02</span><div><p class="ed-eyebrow">Com o Master</p><h3>Disciplina e constância na vida real</h3><p>Palestras e encontros sobre clareza, ação e continuidade para pessoas, lideranças e equipes.</p></div><a href="/contato/?assunto=Palestra%20com%20o%20Master" aria-label="Conversar sobre palestra com o Master">Conversar ↗</a></article>
    <article><span class="ed-offer-mark ed-duo-mark">03</span><div><p class="ed-eyebrow">Com os dois</p><h3>Uma construção compartilhada</h3><p>Consulte uma participação conjunta sobre a trajetória dos fundadores e a experiência de construir a Kihap.</p></div><a href="/contato/?assunto=Participa%C3%A7%C3%A3o%20dos%20dois" aria-label="Conversar sobre participação dos dois">Conversar ↗</a></article>
  </div>
  <div class="ed-actions">{cta('/programas/', 'Ver programas e palestras')}</div>
</section>

<section class="ed-event ed-section" aria-labelledby="event-title"><div class="in ed-event-grid">
  <div class="ed-event-image">{imagem('/imersao/master-palestra.jpg', 'Master Cavenatti apresentando uma ideia diante de uma plateia')}</div>
  <div class="ed-event-copy"><p class="ed-eyebrow">14 de novembro de 2026 · Brasília · por Master Cavenatti</p><h2 id="event-title">Imersão da Mentalidade Faixa Preta</h2><p>Do tatame para a vida. Um dia presencial para trabalhar a distância entre saber o que importa e conseguir colocar em prática.</p>{cta('/imersao/', 'Conheça a Imersão')}</div>
</div></section>

<section class="ed-products ed-section in" aria-labelledby="home-products-title">
  {header_section('03', 'Para continuar aprendendo', 'A jornada também acontece em outros formatos.', 'home-products-title')}
  <div class="ed-product-grid">
    <article><p class="ed-eyebrow">Online · com os dois</p><h3>Introdução à Mente Faixa Preta</h3><p>Um curso online conduzido por Mrs Master e Master Cavenatti. Consulte as informações de acesso e conteúdo.</p><a class="ed-text-link" href="/contato/?assunto=Introdu%C3%A7%C3%A3o%20%C3%A0%20Mente%20Faixa%20Preta">Saiba mais ↗</a></article>
    <article><p class="ed-eyebrow">Programa</p><h3>Academy</h3><p>Conheça o Academy e converse com a equipe sobre a proposta e as possibilidades de participação.</p><a class="ed-text-link" href="/contato/?assunto=Academy">Conhecer o Academy ↗</a></article>
  </div>
</section>

<section class="ed-close ed-section in"><p class="ed-eyebrow">Seu evento, sua equipe, seu projeto</p><h2>Vamos conversar sobre o que faz sentido para o seu público.</h2>{cta('/contato/', 'Fale com a equipe')}</section>
'''


def timeline(items):
    return '<ol class="ed-timeline">' + ''.join(f'<li><span>{escape(mark)}</span><p>{text}</p></li>' for mark, text in items) + '</ol>'


def formations(items):
    return '<div class="ed-formations">' + ''.join(f'<div><span>{num:02d}</span><p>{text}</p></div>' for num, text in enumerate(items, 1)) + '</div>'


# Os comentários permanecem na fonte até chegarem as informações dos fundadores.
# [títulos, eventos, datas e fotos das palestras realizadas pela Mrs Master]
# [títulos, eventos, datas e fotos confirmadas das palestras do Master]
# [livros, capas das edições e comentários pessoais da Mrs Master]
# [livros, capas das edições e comentários pessoais do Master]
# [hobbies e episódio de família aprovado por cada fundador]
# [instituição, nome oficial, período e titulação do mestrado em Taekwondo]

# Cada livro exige: capa da edição escolhida, título, autor e comentário
# pessoal aprovado. Os arrays vazios não geram blocos na prévia.
LIVROS = {"fernanda": [], "master": []}
# Histórico de palestras: título, evento, data, local e registro aprovado.
PALESTRAS = {"fernanda": [], "master": []}

FORMACOES_COMPARTILHADAS = [
    "Millionaire Mind Intensive · T. Harv Eker.",
    "Mission to Million · T. Harv Eker.",
    "Train the Trainer · T. Harv Eker.",
    "Método CIS · Paulo Vieira.",
    "Método Origem.",
]


def livros_section(chave):
    if not LIVROS[chave]:
        return ""
    cards = "".join(
        f'<article class="ed-book"><img src="{escape(item["capa"])}" alt="Capa de {escape(item["titulo"])}" loading="lazy"><div><h3>{escape(item["titulo"])}</h3><p class="ed-book-author">{escape(item["autor"])}</p><p>{escape(item["comentario"])}</p></div></article>'
        for item in LIVROS[chave]
    )
    return f'<section class="ed-section ed-books in" id="livros" aria-labelledby="books-title">{header_section("05", "Indicações de livros", "Leituras que acompanham a trajetória.", "books-title")}<div class="ed-books-grid">{cards}</div></section>'


def palestras_realizadas(chave):
    if not PALESTRAS[chave]:
        return ""
    items = "".join(
        f'<li><strong>{escape(item["titulo"])}</strong><span>{escape(item["evento"])} · {escape(item["data"])}</span></li>'
        for item in PALESTRAS[chave]
    )
    return f'<div class="ed-talk-history"><h3>Palestras realizadas</h3><ul>{items}</ul></div>'

FUNDADORES = {
    "fernanda": {
        "nome": "Mrs Master Cavenatti", "titulo": "Mrs Master", "classe": "ed-fer", "cor": "Cobre",
        "sobretitulo": "Esporte · educação · liderança", "hero_img": "/img/hero-fernanda.jpg",
        "hero_alt": "Mrs Master Cavenatti praticando Taekwondo em área externa",
        "linha": "Atleta, educadora e cofundadora. Uma trajetória de conquistas construída com conhecimento e autonomia.",
        "hero_texto": "Dez vezes campeã mundial de Taekwondo, fez mestrado na modalidade e reúne alto rendimento, estudo e empreendedorismo. Na Kihap, participa da construção de uma escola que forma pessoas.",
        "sobre_titulo": "Quem ela é, além dos títulos.",
        "sobre": "Mrs Master Cavenatti começou no Taekwondo aos 14 anos. A experiência como atleta levou-a à Educação Física, à Fisiologia do Exercício e ao mestrado na modalidade. Sempre gostou de dançar e praticou jazz por muitos anos, inclusive na vida adulta. Hoje também é atleta de corrida: começou com poucos quilômetros e foi ampliando seus limites dia após dia. Cofundou a Kihap com o Master e é mãe de Benício e Serena. Família, movimento e trabalho fazem parte da mesma vida, sem que um papel defina todos os outros.",
        "sobre_foto": "/img/fernanda-medalha.jpg", "sobre_alt": "Mrs Master Cavenatti com a filha e uma medalha de Taekwondo",
        "traj_titulo": "Prática, estudo e decisões próprias.",
        "traj_intro": "O Taekwondo começou na adolescência e tornou-se uma carreira de alto rendimento. O jazz acompanhou sua vida por muitos anos. Mais tarde, a corrida trouxe outro modo de experimentar a evolução: começar com poucos quilômetros e seguir, um dia de cada vez. O estudo e o empreendedorismo levaram essa experiência à construção da Kihap.",
        "traj": [("14 anos", "Início no Taekwondo."), ("UFPR", "Graduação em Educação Física e especialização em Fisiologia do Exercício."), ("10×", "Campeã mundial de Taekwondo."), ("Kihap", "Cofundação de uma escola de artes marciais e desenvolvimento de pessoas."), ("Hoje", "Atleta de corrida, depois de começar com poucos quilômetros e ampliar seus limites dia após dia.")],
        "form_titulo": "Conhecimento que acompanha a prática.",
        "form": ["Graduação em Educação Física · Universidade Federal do Paraná.", "Especialização em Fisiologia do Exercício · Universidade Federal do Paraná.", "Mestrado em Taekwondo.", "Curso de Neurociências · Prof. Pedro Calabrez.", *FORMACOES_COMPARTILHADAS],
        "palestra_titulo": "Uma trajetória para abrir conversas.",
        "palestra_texto": "A experiência da Mrs Master reúne esporte de alto rendimento, conhecimento do corpo, empreendedorismo e liderança feminina. Temas e formatos de participação são construídos com ela para o contexto de cada evento.",
        "palestra_cta": "Converse sobre uma participação", "assunto": "Palestra%20com%20a%20Mrs%20Master",
        "galeria": [("/img/fernanda-corrida-familia.jpg", "Mrs Master correndo ao lado da família"), ("/img/fernanda-detalhe.jpg", "Detalhe da faixa preta da Mrs Master Cavenatti")],
    },
    "master": {
        "nome": "Master Cavenatti", "titulo": "Master", "classe": "ed-mas", "cor": "Petróleo",
        "sobretitulo": "Artes marciais · educação · liderança", "hero_img": "/img/master_cavenatti.jpeg",
        "hero_alt": "Master Cavenatti com uniforme de Taekwondo",
        "linha": "Mestre, educador e cofundador. Uma trajetória de liderança construída com disciplina e constância.",
        "hero_texto": "Participou por dez anos da equipe do Brasil em torneios internacionais de Taekwondo. Reconhecido Mestre nos EUA em 2018, conquistou o segundo mestrado nos EUA em 2024. Em programas e palestras, leva a disciplina do treinamento para a vida real.",
        "sobre_titulo": "Quem ele é, além do tatame.",
        "sobre": "Master Cavenatti é cofundador da Kihap, mestre de Taekwondo e formado em Administração. Durante dez anos, integrou a equipe do Brasil em torneios internacionais. Sua atuação reúne ensino, gestão e desenvolvimento de pessoas. Divide a vida com a Mrs Master e é pai de Benício e Serena. A jornada no triatlo também faz parte de sua história; família, esporte e trabalho exigem escolhas sustentadas com constância.",
        "sobre_foto": "/img/master-treino.jpg", "sobre_alt": "Master Cavenatti acompanhando uma atividade de Taekwondo com o filho",
        "traj_titulo": "Da prática marcial à formação de pessoas.",
        "traj_intro": "O percurso começou no Taekwondo, passou por uma década na equipe do Brasil em torneios internacionais e ganhou escala no ensino e na gestão da Kihap. O triatlo ampliou sua experiência com treino, resistência e constância.",
        "traj": [("1994", "Início no Taekwondo."), ("1997", "Faixa preta 1º Dan."), ("2004", "Certificação como instrutor."), ("10 anos", "Na equipe do Brasil em torneios internacionais."), ("2018", "Reconhecido Mestre nos Estados Unidos."), ("2024", "Segundo mestrado nos Estados Unidos."), ("Hoje", "Cofundador da Kihap, com atuação no ensino e na liderança.")],
        "form_titulo": "Formação que se transforma em ensino.",
        "form": ["Graduação em Administração.", "Certificação como instrutor de Taekwondo · 2004.", "Reconhecimento como Mestre nos EUA · 2018.", "Segundo mestrado nos EUA · 2024.", *FORMACOES_COMPARTILHADAS],
        "palestra_titulo": "Disciplina que encontra a vida real.",
        "palestra_texto": "Nas palestras, o Master conecta artes marciais e empreendedorismo a escolhas que exigem clareza, método e continuidade. O conteúdo parte do desafio do público e busca aplicação na vida e no trabalho.",
        "palestra_cta": "Solicite uma proposta de palestra", "assunto": "Palestra%20com%20o%20Master",
        "galeria": [("/img/master-triathlon-bike-mar.jpg", "Master Cavenatti pedalando durante uma prova de triatlo"), ("/imersao/master-palestra.jpg", "Master Cavenatti falando em um encontro de formação")],
    },
}


def founder_page(d):
    chave = "fernanda" if d["classe"] == "ed-fer" else "master"
    livros = livros_section(chave)
    voz = '''<section class="ed-master-voice ed-section" aria-labelledby="voice-title"><div class="in"><p class="ed-eyebrow">Nas palavras do Master</p><blockquote id="voice-title">“Aprendi cedo que faixa preta não é um ponto de chegada, é o hábito de voltar ao treino todos os dias. É isso que ensino: não se trata de fazer mais, e sim de fazer com constância aquilo que você já sabe que importa.”</blockquote><p>Master Cavenatti</p></div></section>''' if chave == "master" else ""
    triatlo = '''<section class="ed-triathlon ed-section in" aria-labelledby="triathlon-title">
  {header_section('03', 'Além do tatame', 'A jornada do triatlo.', 'triathlon-title')}
  <p class="ed-section-intro">O triatlo faz parte da trajetória esportiva do Master. As imagens de treino e de prova mostram outra expressão da disciplina que ele leva ao ensino: voltar à prática e seguir até o fim.</p>
  <div class="ed-triathlon-grid">
    <figure><img src="/img/master-triathlon-bike.jpg" alt="Master Cavenatti pedalando em uma prova de triatlo" loading="lazy"><figcaption>O percurso</figcaption></figure>
    <figure><img src="/img/master-triathlon-chegada-inteira.jpg" alt="Master Cavenatti cruzando a linha de chegada do Ironman Cozumel" loading="lazy"><figcaption>A chegada · Cozumel, 2023</figcaption></figure>
    <figure><img src="/img/master-triathlon-chegada.jpg" alt="Master Cavenatti após uma prova de triatlo" loading="lazy"><figcaption>Depois da prova</figcaption></figure>
  </div>
</section>''' if chave == "master" else ""
    form_num = '04' if chave == 'master' else '03'
    talk_num = '05' if chave == 'master' else '04'
    return f'''
<section class="ed-person-hero {d['classe']}" aria-labelledby="person-title">
  <div class="ed-person-hero-copy"><p class="ed-eyebrow">{d['sobretitulo']}</p>{faixa()}<h1 id="person-title">{d['titulo']}<small>CAVENATTI</small></h1><p class="ed-person-line">{d['linha']}</p><p>{d['hero_texto']}</p>{cta('/contato/?assunto=' + d['assunto'], 'Convide ' + ('a Mrs Master' if d['classe']=='ed-fer' else 'o Master'))}</div>
  <div class="ed-person-hero-image">{imagem(d['hero_img'], d['hero_alt'], carregamento='eager')}</div>
</section>
<nav class="ed-chapter-nav" aria-label="Nesta página"><div class="in"><a href="#sobre">Sobre</a><a href="#trajetoria">Trajetória</a>{'<a href="#triathlon-title">Triatlo</a>' if chave == 'master' else ''}<a href="#formacoes">Formações</a><a href="#palestras">Palestras</a><a href="#contato-pessoa">Contato</a></div></nav>
<section class="ed-section ed-person-about in" id="sobre" aria-labelledby="about-title">
  {header_section('01', 'Sobre', d['sobre_titulo'], 'about-title')}
  <div class="ed-person-about-grid"><p class="ed-person-about-text">{d['sobre']}</p><figure>{imagem(d['sobre_foto'], d['sobre_alt'])}<figcaption>Esporte e família fazem parte de uma trajetória mais ampla.</figcaption></figure></div>
</section>
{voz}
<section class="ed-section ed-person-timeline" id="trajetoria" aria-labelledby="traj-title"><div class="in">
  {header_section('02', 'Trajetória', d['traj_titulo'], 'traj-title')}
  <div class="ed-two-col"><p class="ed-section-intro">{d['traj_intro']}</p>{timeline(d['traj'])}</div>
</div></section>
{triatlo}
<section class="ed-section ed-person-form in" id="formacoes" aria-labelledby="form-title">
  {header_section(form_num, 'Formações', d['form_titulo'], 'form-title')}
  {formations(d['form'])}
</section>
<section class="ed-section ed-person-talks" id="palestras" aria-labelledby="talk-title"><div class="in ed-talk-grid">
  <div>{header_section(talk_num, 'Palestras', d['palestra_titulo'], 'talk-title')}<p class="ed-section-intro">{d['palestra_texto']}</p>{palestras_realizadas(chave)}{cta('/contato/?assunto=' + d['assunto'], d['palestra_cta'])}</div>
  <div class="ed-talk-image">{imagem(d['galeria'][1][0], d['galeria'][1][1])}</div>
</div></section>
{livros}
<section class="ed-section ed-person-gallery in" aria-label="Em imagens"><div class="ed-gallery">{''.join('<figure>'+imagem(src, alt)+'</figure>' for src,alt in d['galeria'])}</div></section>
<section class="ed-close ed-section in" id="contato-pessoa"><p class="ed-eyebrow">Contato</p><h2>Leve essa experiência para o seu público.</h2>{cta('/contato/?assunto=' + d['assunto'], 'Fale com a equipe')}</section>
'''

PROGRAMAS = f'''
<section class="ed-page-intro in"><p class="ed-eyebrow">Empresas · eventos · comunidades</p>{faixa(True)}<h1>Experiências com quem vive o que ensina.</h1><p>Mrs Master e Master Cavenatti levam repertórios diferentes para encontros que pedem reflexão e aplicação. Conheça as frentes de atuação e converse sobre o formato adequado ao seu público.</p></section>
<section class="ed-section ed-program-paths in" aria-labelledby="prog-title">{header_section('01', 'Escolha por quem conduz', 'Três caminhos para começar a conversa.', 'prog-title')}
  <div class="ed-offer-list">
    <article><span class="ed-offer-mark ed-fer-mark">01</span><div><p class="ed-eyebrow">Com a Mrs Master</p><h3>Esporte, movimento e liderança</h3><p>Uma participação a desenhar com ela, a partir do alto rendimento, do conhecimento do corpo e da experiência como cofundadora.</p><span class="ed-offer-meta">Público e formato definidos em conversa</span></div><a href="/contato/?assunto=Palestra%20com%20a%20Mrs%20Master">Consultar ↗</a></article>
    <article><span class="ed-offer-mark ed-mas-mark">02</span><div><p class="ed-eyebrow">Com o Master</p><h3>Disciplina aplicada à vida real</h3><p>Palestras e encontros para transformar intenção em constância, com exemplos do esporte, da liderança e do cotidiano.</p><span class="ed-offer-meta">Para equipes, lideranças e eventos</span></div><a href="/contato/?assunto=Palestra%20com%20o%20Master">Consultar ↗</a></article>
    <article><span class="ed-offer-mark ed-duo-mark">03</span><div><p class="ed-eyebrow">Com os dois</p><h3>Uma construção em conjunto</h3><p>Consulte uma participação conjunta sobre a trajetória dos fundadores e a experiência de construir a Kihap.</p><span class="ed-offer-meta">Para empresas e eventos</span></div><a href="/contato/?assunto=Participa%C3%A7%C3%A3o%20dos%20dois">Consultar ↗</a></article>
  </div>
</section>
<section class="ed-event ed-section" aria-labelledby="program-event-title"><div class="in ed-event-grid"><div class="ed-event-image">{imagem('/imersao/master-palestra.jpg', 'Master Cavenatti apresentando uma ideia diante de uma plateia')}</div><div class="ed-event-copy"><p class="ed-eyebrow">Evento presencial · 14 de novembro de 2026 · Brasília</p><h2 id="program-event-title">Imersão da Mentalidade Faixa Preta</h2><p>Um dia prático com Master Cavenatti. A página da Imersão traz a proposta, a programação e as informações de inscrição criadas para essa experiência.</p>{cta('/imersao/', 'Ver página completa da Imersão')}</div></div></section>
<section class="ed-products ed-section in" aria-labelledby="products-title">
  {header_section('02', 'Programas', 'Escolha como aprofundar essa jornada.', 'products-title')}
  <div class="ed-product-grid">
    <article><p class="ed-eyebrow">Presencial · Master Cavenatti</p><h3>Imersão da Mentalidade Faixa Preta</h3><p>14 de novembro de 2026, em Brasília. Um dia dedicado a transformar intenção em prática.</p><a class="ed-text-link" href="/imersao/">Programação e ingressos ↗</a></article>
    <article><p class="ed-eyebrow">Curso online · com os dois</p><h3>Introdução à Mente Faixa Preta</h3><p>Mrs Master e Master Cavenatti conduzem este curso online. Converse com a equipe para conhecer conteúdo e acesso.</p><a class="ed-text-link" href="/contato/?assunto=Introdu%C3%A7%C3%A3o%20%C3%A0%20Mente%20Faixa%20Preta">Solicitar informações ↗</a></article>
    <article><p class="ed-eyebrow">Programa</p><h3>Academy</h3><p>O Academy também faz parte das experiências Cavenatti. Consulte a proposta e as condições de participação.</p><a class="ed-text-link" href="/contato/?assunto=Academy">Solicitar informações ↗</a></article>
  </div>
</section>
<section class="ed-close ed-section in"><p class="ed-eyebrow">Contratação</p><h2>Conte o desafio do seu público. Vamos conversar sobre a participação adequada.</h2>{cta('/contato/', 'Solicite uma proposta')}</section>
'''

IMPRENSA = f'''
<section class="ed-page-intro in"><p class="ed-eyebrow">Imprensa</p>{faixa(True)}<h1>Duas trajetórias para conhecer e contar.</h1><p>Biografias breves de Mrs Master e Master Cavenatti para veículos, organizadores e parceiros.</p></section>
<section class="ed-section in ed-press-grid" aria-label="Biografias">
  <article class="ed-press-bio ed-fer"><p class="ed-eyebrow">Mrs Master Cavenatti</p><h2>Atleta, educadora e cofundadora.</h2><p>Dez vezes campeã mundial de Taekwondo, começou na modalidade aos 14 anos. É formada em Educação Física, especialista em Fisiologia do Exercício pela UFPR e fez mestrado em Taekwondo. Sua atuação reúne esporte, educação e empreendedorismo na construção da Kihap.</p><a class="ed-text-link" href="/fernanda/">Conheça sua trajetória ↗</a></article>
  <article class="ed-press-bio ed-mas"><p class="ed-eyebrow">Master Cavenatti</p><h2>Mestre, educador e cofundador.</h2><p>Pratica Taekwondo desde 1994 e integrou por dez anos a equipe do Brasil em torneios internacionais. Reconhecido Mestre nos EUA em 2018, recebeu seu segundo mestrado no país em 2024. É formado em Administração e cofundou a Kihap.</p><a class="ed-text-link" href="/master/">Conheça sua trajetória ↗</a></article>
</section>
<section class="ed-close ed-section in"><p class="ed-eyebrow">Imprensa e parcerias</p><h2>Precisa de informações, fotos ou uma entrevista?</h2>{cta('/contato/?assunto=Imprensa', 'Fale com a equipe')}</section>
'''

CONTATO = '''
<section class="ed-page-intro in"><p class="ed-eyebrow">Contato</p><span class="ed-faixa ed-faixa-dupla" aria-hidden="true"></span><h1>Vamos construir o encontro certo para o seu público.</h1><p>Conte seu objetivo, público, data e formato. A equipe conversa com você sobre a participação da Mrs Master, do Master ou dos dois.</p></section>
<section class="ed-contact ed-section in"><div class="ed-contact-aside"><p class="ed-eyebrow">Por onde começar</p><h2>Uma conversa pode tomar muitas formas.</h2><p>Palestra, participação em evento, imprensa, parceria ou formação. Descreva o que você imagina e a equipe retorna com as possibilidades.</p></div>
<form class="form" id="form-contato" novalidate data-pendente title="Pendente: configurar o canal de envio do formulário">
  <div class="cv-campo"><label for="nome">Nome</label><input id="nome" name="nome" autocomplete="name" required></div>
  <div class="cv-campo" id="campo-email"><label for="email">E-mail</label><input id="email" name="email" type="email" autocomplete="email" required aria-describedby="email-ajuda"><span class="ajuda" id="email-ajuda" aria-live="polite"></span></div>
  <div class="cv-campo"><label for="empresa">Empresa ou organização</label><input id="empresa" name="empresa" autocomplete="organization"></div>
  <div class="cv-campo"><label for="assunto">Assunto</label><select id="assunto" name="assunto"><option value="" selected>Escolha um assunto</option><option>Palestra com a Mrs Master</option><option>Palestra com o Master</option><option>Participação dos dois</option><option>Imersão da Mentalidade Faixa Preta</option><option>Introdução à Mente Faixa Preta</option><option>Academy</option><option>Programa ou formação</option><option>Imprensa</option><option>Parceria</option><option>Outro</option></select></div>
  <div class="cv-campo"><label for="cidade">Cidade do evento</label><input id="cidade" name="cidade" autocomplete="address-level2"></div>
  <div class="cv-campo"><label for="data">Data prevista</label><input id="data" name="data" placeholder="dd/mm/aaaa" inputmode="numeric"></div>
  <div class="cv-campo tudo"><label for="mensagem">Conte um pouco sobre o público e o objetivo</label><textarea id="mensagem" name="mensagem" required></textarea></div>
  <div class="acoes tudo"><button class="cv-btn primario" type="submit">Enviar mensagem</button></div>
  <p class="status ok tudo" id="status-ok" role="status" tabindex="-1" hidden>Mensagem enviada. A equipe entrará em contato.</p>
  <p class="status falha tudo" id="status-falha" role="alert" hidden></p>
</form></section>
'''

PAGES = [
    dict(path="/", file="index.html", escopo="home ed-site", titulo="Mrs &amp; Mr Master Cavenatti · Fundadores da Kihap", descricao="As trajetórias de Mrs Master e Master Cavenatti, fundadores da Kihap. Programas, palestras e parcerias.", corpo=HOME),
    dict(path="/fernanda/", file="fernanda/index.html", escopo="ed-site ed-person ed-fer", titulo="Mrs Master Cavenatti · Cofundadora da Kihap", descricao="Dez vezes campeã mundial de Taekwondo, educadora e cofundadora da Kihap.", corpo=founder_page(FUNDADORES["fernanda"])),
    dict(path="/master/", file="master/index.html", escopo="ed-site ed-person ed-mas", titulo="Master Cavenatti · Cofundador da Kihap", descricao="Mestre de Taekwondo, educador e cofundador da Kihap.", corpo=founder_page(FUNDADORES["master"])),
    dict(path="/programas/", file="programas/index.html", escopo="ed-site ed-programs", titulo="Programas e palestras · Cavenatti", descricao="Programas, palestras e participações de Mrs Master e Master Cavenatti para empresas e eventos.", corpo=PROGRAMAS),
    dict(path="/imprensa/", file="imprensa/index.html", escopo="ed-site", titulo="Imprensa · Cavenatti", descricao="Biografias de Mrs Master e Master Cavenatti para veículos, organizadores e parceiros.", corpo=IMPRENSA),
    dict(path="/contato/", file="contato/index.html", escopo="ed-site", titulo="Contato · Cavenatti", descricao="Converse sobre palestras, eventos, imprensa e parcerias com Mrs Master e Master Cavenatti.", corpo=CONTATO, scripts='<script src="/js/config.js"></script>\n'),
    dict(path="/imersao/", file="imersao/index.html", escopo="imersao", titulo="Imersão da Mentalidade Faixa Preta · Master Cavenatti", descricao="Imersão presencial com Master Cavenatti em 14 de novembro de 2026, em Brasília. Disciplina do tatame para a vida. 80 vagas.", corpo=(ROOT / "src" / "imersao_corpo.html").read_text(encoding="utf-8"), estilos='<link rel="stylesheet" href="/css/imersao.css">\n', scripts='<script src="/js/config.js"></script>\n<script src="/js/imersao.js" defer></script>\n'),
]

for page in PAGES:
    target = OUT / page["file"]
    target.parent.mkdir(parents=True, exist_ok=True)
    html = layout(page["path"], page["titulo"], page["descricao"], page["corpo"], page.get("escopo", ""), page.get("scripts", ""), page.get("estilos", ""))
    target.write_text(relativizar(html, page["file"]), encoding="utf-8")

# A prévia nunca simula um envio real. O checkout da Imersão permanece pendente.
(OUT / "js").mkdir(exist_ok=True)
(OUT / "js" / "config.js").write_text("window.CAVENATTI = { formEndpoint: '', prototipo: false, checkoutUrl: '' };\n", encoding="utf-8")
# A página de podcast sem conteúdo aprovado deixa de ser gerada.
podcast = OUT / "kihapcast" / "index.html"
if podcast.exists():
    podcast.unlink()
print(f"{len(PAGES)} páginas geradas em {OUT}")
