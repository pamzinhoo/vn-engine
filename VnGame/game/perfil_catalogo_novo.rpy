################################################################################
## Catálogo de Personagens — Estilo Carrossel (Inventory)
## Layout: 1920x1080 | Ren'Py 8.x
################################################################################

## ── Som e Funções ───────────────────────────────────────────────────────────
init python:
    # Som de página
    PAGE_FLIP_SOUND = None
    
    def play_page_flip():
        if PAGE_FLIP_SOUND and renpy.loadable(PAGE_FLIP_SOUND):
            renpy.sound.play(PAGE_FLIP_SOUND, channel="sound")

## ── Dados dos personagens ────────────────────────────────────────────────────
init python:
    personagens_lista = [
        "Pam",
        "Nao sei",
        "Maya",
        "Ethan",
        "Diretor",
        "Abby",
        "Kain",
        "Madelin",
        "Miguel",
        "Arlyson",
        "Aurore",
        "Kuroya",
        "Lauane",
        "Lucien",
        "August",
        "Edgar",
        "Zatsko",
        "???",
    ]

    personagens_dados = {
        "Pam": {
            "foto":        "images/kyioki_capa.png",
            "info_pt":     "images/kyioki_info_portugues.png",
            "info_en":     "images/kyioki_info_ingles.png",
            "info_es":     "images/kyioki_info_espanhol.png",
            "nome":        "Pam",
            "descricao":   "alguma coisa aqui",
            "historia":    "historia do rdr2",
            "curiosidade": "ela é uma pessoa",
            "bloqueado":   False,
            "genero":      "mulher",
            "sexualidade": "Bissexual",
            "ocupacao":    "Estudante",
            "especie":     "Humana",
            "personalidade": {
                "Gentileza":    80,
                "Inteligência": 85,
                "Seriedade":    70,
                "Humor":        60,
                "Saúde":        75,
            },
            "anatomia": {
                "altura":      "1.65m",
                "peso":        "55kg",
                "raca":        "Branca/Europeia",
                "tipo_sangue": "A+",
            },
        },
        "Nao sei": {
            "foto":        "protaM.png",
            "nome":        "Prota M",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "homem",
            "sexualidade": "Heterossexual",
            "ocupacao":    "Estudante",
            "especie":     "Humana",
            "personalidade": {
                "Gentileza":    70,
                "Inteligência": 90,
                "Seriedade":    80,
                "Humor":        50,
                "Saúde":        80,
            },
            "anatomia": {
                "altura":      "1.75m",
                "peso":        "70kg",
                "raca":        "Asiática/Japonesa",
                "tipo_sangue": "O-",
            },
        },
        "Maya": {
            "foto":        "foto_personagem_aqui",
            "nome":        "Maya",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Ethan": {
            "foto":        "foto_personagem_aqui",
            "nome":        "Ethan",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Diretor": {
            "foto":        "foto_personagem_aqui",
            "nome":        "Diretor",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Abby": {
            "foto":        "images/abby_capa.png",
            "info_pt":     "images/abby_info_portugues.png",
            "info_en":     "images/abby_info_ingles.png",
            "info_es":     "images/abby_info_espanhol.png",
            "nome":        "Abby",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Kain": {
            "foto":        "images/kain_capa.png",
            "info_pt":     "images/kain_info_portugues.png",
            "info_en":     "images/kain_info_ingles.png",
            "info_es":     "images/kain_info_espanhol.png",
            "nome":        "Kain",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Madelin": {
            "foto":        "images/madelin_capa.png",
            "info_pt":     "images/madelin_info_portugues.png",
            "info_en":     "images/madelin_info_ingles.png",
            "info_es":     "images/madelin_info_espanhol.png",
            "nome":        "Madelin",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Miguel": {
            "foto":        "images/miguel_capa.png",
            "info_pt":     "images/miguel_info_portugues.png",
            "info_en":     "images/miguel_info_ingles.png",
            "info_es":     "images/miguel_info_espanhol.png",
            "nome":        "Miguel",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Arlyson": {
            "foto":        "images/arlyson_capa.png",
            "info_pt":     "images/arlyson_info_portugues.png",
            "info_en":     "images/arlyson_info_ingles.png",
            "info_es":     "images/arlyson_info_espanhol.png",
            "nome":        "Arlyson",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Aurore": {
            "foto":        "images/aurore_capa.png",
            "info_pt":     "images/aurore_info_portugues.png",
            "info_en":     "images/aurore_info_ingles.png",
            "info_es":     "images/aurore_info_espanhol.png",
            "nome":        "Aurore",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Kuroya": {
            "foto":        "images/kuroya_capa.png",
            "info_pt":     "images/kuroya_info_portugues.png",
            "info_en":     "images/kuroya_info_ingles.png",
            "info_es":     "images/kuroya_info_espanhol.png",
            "nome":        "Kuroya",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Lauane": {
            "foto":        "images/lauane_capa.png",
            "info_pt":     "images/lauane_info_portugues.png",
            "info_en":     "images/lauane_info_ingles.png",
            "info_es":     "images/lauane_info_espanhol.png",
            "nome":        "Lauane",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Lucien": {
            "foto":        "images/lucien_capa.png",
            "info_pt":     "images/lucien_info_portugues.png",
            "info_en":     "images/lucien_info_ingles.png",
            "info_es":     "images/lucien_info_espanhol.png",
            "nome":        "Lucien",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "August": {
            "foto":        "images/august_capa.png",
            "info_pt":     "images/august_info_portugues.png",
            "info_en":     "images/august_info_ingles.png",
            "info_es":     "images/august_info_espanhol.png",
            "nome":        "August",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Edgar": {
            "foto":        "images/edgar_capa.png",
            "info_pt":     "images/edgar_info_portugues.png",
            "info_en":     "images/edgar_info_ingles.png",
            "info_es":     "images/edgar_info_espanhol.png",
            "nome":        "Edgar",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "Zatsko": {
            "foto":        "images/zatsko_capa.png",
            "info_pt":     "images/zatsko_info_portugues.png",
            "info_en":     "images/zatsko_info_ingles.png",
            "info_es":     "images/zatsko_info_espanhol.png",
            "nome":        "Zatsko",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
            "genero":      "genero_aqui",
            "sexualidade": "sexualidade_aqui",
            "ocupacao":    "ocupacao_aqui",
            "especie":     "especie_aqui",
            "personalidade": {
                "Gentileza":    50,
                "Inteligência": 50,
                "Seriedade":    50,
                "Humor":        50,
                "Saúde":        50,
            },
            "anatomia": {
                "altura":      "altura_aqui",
                "peso":        "peso_aqui",
                "raca":        "raca_aqui",
                "tipo_sangue": "tipo_sangue_aqui",
            },
        },
        "???": {
            "foto":        "foto_personagem_aqui",
            "nome":        "???",
            "descricao":   "— BLOQUEADO —",
            "historia":    "Desbloqueie este personagem para ler mais.",
            "curiosidade": "...",
            "bloqueado":   True,
            "genero":      "???",
            "sexualidade": "???",
            "ocupacao":    "???",
            "especie":     "???",
            "personalidade": {
                "Gentileza":    0,
                "Inteligência": 0,
                "Seriedade":    0,
                "Humor":        0,
                "Saúde":        0,
            },
            "anatomia": {
                "altura":      "???",
                "peso":        "???",
                "raca":        "???",
                "tipo_sangue": "???",
            },
        },
    }

    lugares_lista = [
        "Escola",
        "Parque",
        "Casa",
        "Biblioteca",
        "Cafeteria",
    ]

    lugares_dados = {
        "Escola": {
            "foto":        "images/escola.png",
            "nome":        "Escola",
            "descricao":   "O local onde os estudantes passam a maior parte do tempo.",
            "historia":    "Uma escola típica com salas de aula e pátios.",
            "curiosidade": "Fundada em 1990.",
            "bloqueado":   False,
        },
        "Parque": {
            "foto":        "images/parque.png",
            "nome":        "Parque",
            "descricao":   "Um lugar relaxante para passear.",
            "historia":    "Um parque público com árvores e bancos.",
            "curiosidade": "Tem um lago no centro.",
            "bloqueado":   False,
        },
        "Casa": {
            "foto":        "images/casa.png",
            "nome":        "Casa",
            "descricao":   "O lar dos personagens.",
            "historia":    "Uma casa confortável na cidade.",
            "curiosidade": "Tem um jardim pequeno.",
            "bloqueado":   False,
        },
        "Biblioteca": {
            "foto":        "images/biblioteca.png",
            "nome":        "Biblioteca",
            "descricao":   "Um lugar para estudo e leitura.",
            "historia":    "Biblioteca da escola com muitos livros.",
            "curiosidade": "Tem seções especiais para estudantes.",
            "bloqueado":   False,
        },
        "Cafeteria": {
            "foto":        "images/cafeteria.png",
            "nome":        "Cafeteria",
            "descricao":   "Onde os estudantes comem.",
            "historia":    "Cafeteria da escola com comida variada.",
            "curiosidade": "Serve lanches saudáveis.",
            "bloqueado":   False,
        },
    }

    rotas_lista = [
        "Rota de Pam",
        "Rota de Maya",
        "Rota de Ethan",
        "Rota do Diretor",
        "Rota Neutra",
    ]

    rotas_dados = {
        "Rota de Pam": {
            "foto":        "images/protaF.png",
            "nome":        "Rota de Pam",
            "descricao":   "Foco na relação com Pam, a protagonista feminina.",
            "historia":    "Explore a história de Pam e suas interações.",
            "curiosidade": "Uma rota romântica e emocional.",
            "bloqueado":   False,
        },
        "Rota de Maya": {
            "foto":        "foto_personagem_aqui",
            "nome":        "Rota de Maya",
            "descricao":   "Aventure-se na rota de Maya.",
            "historia":    "Descubra os segredos de Maya.",
            "curiosidade": "Uma rota misteriosa.",
            "bloqueado":   False,
        },
        "Rota de Ethan": {
            "foto":        "foto_personagem_aqui",
            "nome":        "Rota de Ethan",
            "descricao":   "Siga a rota de Ethan.",
            "historia":    "Acompanhe as aventuras de Ethan.",
            "curiosidade": "Uma rota de ação.",
            "bloqueado":   False,
        },
        "Rota do Diretor": {
            "foto":        "foto_personagem_aqui",
            "nome":        "Rota do Diretor",
            "descricao":   "Investigue a rota do Diretor.",
            "historia":    "Revele os planos do Diretor.",
            "curiosidade": "Uma rota conspiratória.",
            "bloqueado":   False,
        },
        "Rota Neutra": {
            "foto":        "foto_personagem_aqui",
            "nome":        "Rota Neutra",
            "descricao":   "Uma rota sem foco romântico.",
            "historia":    "Explore o mundo sem compromissos.",
            "curiosidade": "Para jogadores casuais.",
            "bloqueado":   False,
        },
    }

## ── Transformações/Animações ────────────────────────────────────────────────

## Animação de zoom no hover — sutil de propósito (era 1.1, chamava atenção
## demais num grid com vários cards lado a lado).
transform card_hover_zoom:
    zoom 1.0
    on hover:
        ease 0.2 zoom 1.04
    on idle:
        ease 0.2 zoom 1.0
## ── Estilos ─────────────────────────────────────────────────────────────────
style info_label is default:
    size 18
    color "#00AAE2"
    font "fonts/fonte.ttf"

style info_text is default:
    size 15
    color "#cccccc"

## ── Tela principal - Carrossel ──────────────────────────────────────────────
screen perfil_catalogo():
    tag menu
    modal False

    # Fundo
    add "images/background_catalogo.png" xpos 0 ypos 0 xysize (1920, 1080)

    default personagem_selecionado = "Pam"
    default carrossel_idx = 0
    default tab = "personagens"
    default lugar_selecionado = "Escola"
    default carrossel_idx_lugares = 0
    default rota_selecionada = "Rota de Pam"
    default carrossel_idx_rotas = 0

    $ tc_personagens = "#00AAE2" if tab == "personagens" else "#000000"
    $ tc_lugares = "#00AAE2" if tab == "lugares" else "#000000"
    $ tc_rotas = "#00AAE2" if tab == "rotas" else "#000000"

    # Abas sobre as faixas brancas da lateral
    textbutton _("PERSONAGENS"):
        xpos 20
        ypos 254
        xsize 330
        ysize 70
        background None
        text_style "load_nav_text"
        text_size 30
        text_color tc_personagens
        at button_hover_scale
        action SetScreenVariable("tab", "personagens")

    textbutton _("LUGARES"):
        xpos 20
        ypos 359
        xsize 330
        ysize 70
        background None
        text_style "load_nav_text"
        text_size 30
        text_color tc_lugares
        at button_hover_scale
        action SetScreenVariable("tab", "lugares")

    textbutton _("ROTAS"):
        xpos 20
        ypos 465
        xsize 330
        ysize 70
        background None
        text_style "load_nav_text"
        text_size 30
        text_color tc_rotas
        at button_hover_scale
        action SetScreenVariable("tab", "rotas")

    # Botão voltar sobre a faixa branca de baixo
    textbutton _("VOLTAR"):
        xpos 20
        ypos 1000
        xsize 330
        ysize 70
        background None
        text_style "load_nav_text"
        text_size 30
        at button_hover_scale
        action Return()

    # Título centralizado sobre a página
    text _("CATÁLOGO"):
        xpos 1200
        xanchor 0.5
        ypos 30
        size 50
        color "#ffffff"
        font "fonts/fonte.ttf"

    # ════════════════════════════════════════════════════════════════════════════
    # CARROSSEL DE PERSONAGENS
    # ════════════════════════════════════════════════════════════════════════════

    if tab == "personagens":

        $ max_visible = 3

        # Botão anterior
        textbutton "◄":
            text_font "DejaVuSans.ttf"
            xpos 490
            ypos 475
            xysize (80, 150)
            background None
            text_size 48
            text_color "#ffffff"
            text_hover_color "#00AAE2"
            action SetScreenVariable("carrossel_idx",
                    len(personagens_lista) - max_visible if carrossel_idx <= 0 else carrossel_idx - 1)

        # Frame carrossel
        frame:
            xpos 590
            ypos 150
            xsize 1220
            ysize 800
            background "#00000000"

            hbox:
                spacing 0
                xalign 0.5
                yalign 0.5

                $ max_visible = 3
                $ start_idx = carrossel_idx
                $ end_idx = min(len(personagens_lista), start_idx + max_visible)

                for i in range(start_idx, end_idx):
                    $ char_nome = personagens_lista[i]
                    $ char_data = personagens_dados[char_nome]
                    $ is_selected = (char_nome == personagem_selecionado)
                    $ foto = char_data["foto"]
                    $ bloqueado = char_data["bloqueado"]

                    $ cw = 360
                    $ ch = round(cw * 1500 / 994)
                    $ px = round(cw * 158 / 994)
                    $ py = round(ch * 234 / 1500)
                    $ pw = round(cw * 682 / 994)
                    $ ph = round(ch * 1085 / 1500)

                    button:
                        at card_hover_zoom
                        action [SetScreenVariable("personagem_selecionado", char_nome), Show("detalhes_perfil", data=char_data)]

                        frame:
                            if is_selected:
                                background None
                                xysize (400, 660)
                                padding (12, 12, 12, 12)
                            else:
                                background None
                                xysize (380, 640)
                                padding (10, 10, 10, 10)
                                xalign 0.0
                            yalign 0.5

                            vbox:
                                spacing 10
                                xalign 0.5

                                # Foto emoldurada por gui/card.png (994x1500)
                                fixed:
                                    xsize cw
                                    ysize ch

                                    add "gui/card.png":
                                        xysize (cw, ch)

                                    if not bloqueado and renpy.loadable(foto):
                                        add foto:
                                            xpos px
                                            ypos py
                                            xsize pw
                                            ysize ph
                                            fit "cover"
                                    else:
                                        frame:
                                            background Solid("#0a0a0a")
                                            xpos px
                                            ypos py
                                            xsize pw
                                            ysize ph

                                            text "???":
                                                size 60
                                                color "#666666"
                                                xalign 0.5
                                                yalign 0.5

                                # Nome
                                text _(char_nome):
                                    size 18
                                    color "#ffffff"
                                    xalign 0.5

        # Botão próximo
        textbutton "►":
            text_font "DejaVuSans.ttf"
            xpos 1830
            ypos 475
            xysize (80, 150)
            background None
            text_size 48
            text_color "#ffffff"
            text_hover_color "#00AAE2"
            action SetScreenVariable("carrossel_idx",
                    0 if carrossel_idx >= len(personagens_lista) - max_visible else carrossel_idx + 1)

    elif tab == "lugares":

        $ max_visible = 3

        # Botão anterior lugares
        textbutton "◄":
            text_font "DejaVuSans.ttf"
            xpos 490
            ypos 475
            xysize (80, 150)
            background None
            text_size 48
            text_color "#ffffff"
            text_hover_color "#00AAE2"
            action SetScreenVariable("carrossel_idx_lugares",
                    max(0, len(lugares_lista) - max_visible) if carrossel_idx_lugares <= 0 else carrossel_idx_lugares - 1)

        # Frame carrossel lugares
        frame:
            xpos 590
            ypos 150
            xsize 1220
            ysize 800
            background "#00000000"

            hbox:
                spacing 0
                xalign 0.5
                yalign 0.5

                $ max_visible = 3
                $ start_idx = carrossel_idx_lugares
                $ end_idx = min(len(lugares_lista), start_idx + max_visible)

                for i in range(start_idx, end_idx):
                    $ lugar_nome = lugares_lista[i]
                    $ lugar_data = lugares_dados[lugar_nome]
                    $ is_selected = (lugar_nome == lugar_selecionado)
                    $ foto = lugar_data["foto"]
                    $ bloqueado = lugar_data["bloqueado"]

                    $ cw = 360
                    $ ch = round(cw * 1500 / 994)
                    $ px = round(cw * 158 / 994)
                    $ py = round(ch * 234 / 1500)
                    $ pw = round(cw * 682 / 994)
                    $ ph = round(ch * 1085 / 1500)

                    button:
                        at card_hover_zoom
                        action [SetScreenVariable("lugar_selecionado", lugar_nome), Show("detalhes_perfil", data=lugar_data)]

                        frame:
                            if is_selected:
                                background None
                                xysize (400, 660)
                                padding (12, 12, 12, 12)
                            else:
                                background None
                                xysize (380, 640)
                                padding (10, 10, 10, 10)
                                xalign 0.0
                            yalign 0.5

                            vbox:
                                spacing 10
                                xalign 0.5

                                # Foto emoldurada por gui/card.png (994x1500)
                                fixed:
                                    xsize cw
                                    ysize ch

                                    add "gui/card.png":
                                        xysize (cw, ch)

                                    if not bloqueado and renpy.loadable(foto):
                                        add foto:
                                            xpos px
                                            ypos py
                                            xsize pw
                                            ysize ph
                                            fit "cover"
                                    else:
                                        frame:
                                            background Solid("#0a0a0a")
                                            xpos px
                                            ypos py
                                            xsize pw
                                            ysize ph

                                            text "???":
                                                size 60
                                                color "#666666"
                                                xalign 0.5
                                                yalign 0.5

                                # Nome
                                text _(lugar_nome):
                                    size 18
                                    color "#ffffff"
                                    xalign 0.5

        # Botão próximo lugares
        textbutton "►":
            text_font "DejaVuSans.ttf"
            xpos 1830
            ypos 475
            xysize (80, 150)
            background None
            text_size 48
            text_color "#ffffff"
            text_hover_color "#00AAE2"
            action SetScreenVariable("carrossel_idx_lugares",
                    0 if carrossel_idx_lugares >= len(lugares_lista) - max_visible else carrossel_idx_lugares + 1)

    elif tab == "rotas":

        $ max_visible = 3

        # Botão anterior rotas
        textbutton "◄":
            text_font "DejaVuSans.ttf"
            xpos 490
            ypos 475
            xysize (80, 150)
            background None
            text_size 48
            text_color "#ffffff"
            text_hover_color "#00AAE2"
            action SetScreenVariable("carrossel_idx_rotas",
                    max(0, len(rotas_lista) - max_visible) if carrossel_idx_rotas <= 0 else carrossel_idx_rotas - 1)

        # Frame carrossel rotas
        frame:
            xpos 590
            ypos 150
            xsize 1220
            ysize 800
            background "#00000000"

            hbox:
                spacing 0
                xalign 0.5
                yalign 0.5

                $ max_visible = 3
                $ start_idx = carrossel_idx_rotas
                $ end_idx = min(len(rotas_lista), start_idx + max_visible)

                for i in range(start_idx, end_idx):
                    $ rota_nome = rotas_lista[i]
                    $ rota_data = rotas_dados[rota_nome]
                    $ is_selected = (rota_nome == rota_selecionada)
                    $ foto = rota_data["foto"]
                    $ bloqueado = rota_data["bloqueado"]

                    $ cw = 360
                    $ ch = round(cw * 1500 / 994)
                    $ px = round(cw * 158 / 994)
                    $ py = round(ch * 234 / 1500)
                    $ pw = round(cw * 682 / 994)
                    $ ph = round(ch * 1085 / 1500)

                    button:
                        at card_hover_zoom
                        action [SetScreenVariable("rota_selecionada", rota_nome), Show("detalhes_perfil", data=rota_data)]

                        frame:
                            if is_selected:
                                background None
                                xysize (400, 660)
                                padding (12, 12, 12, 12)
                            else:
                                background None
                                xysize (380, 640)
                                padding (10, 10, 10, 10)
                                xalign 0.0
                            yalign 0.5

                            vbox:
                                spacing 10
                                xalign 0.5

                                # Foto emoldurada por gui/card.png (994x1500)
                                fixed:
                                    xsize cw
                                    ysize ch

                                    add "gui/card.png":
                                        xysize (cw, ch)

                                    if not bloqueado and renpy.loadable(foto):
                                        add foto:
                                            xpos px
                                            ypos py
                                            xsize pw
                                            ysize ph
                                            fit "cover"
                                    else:
                                        frame:
                                            background Solid("#0a0a0a")
                                            xpos px
                                            ypos py
                                            xsize pw
                                            ysize ph

                                            text "???":
                                                size 60
                                                color "#666666"
                                                xalign 0.5
                                                yalign 0.5

                                # Nome
                                text _(rota_nome):
                                    size 18
                                    color "#ffffff"
                                    xalign 0.5

        # Botão próximo rotas
        textbutton "►":
            text_font "DejaVuSans.ttf"
            xpos 1830
            ypos 475
            xysize (80, 150)
            background None
            text_size 48
            text_color "#ffffff"
            text_hover_color "#00AAE2"
            action SetScreenVariable("carrossel_idx_rotas",
                    0 if carrossel_idx_rotas >= len(rotas_lista) - max_visible else carrossel_idx_rotas + 1)

    # ════════════════════════════════════════════════════════════════════════════
    # PAINEL DE DETALHES REMOVIDO - AGORA EM TELA SEPARADA
    # ════════════════════════════════════════════════════════════════════════════

################################################################################
## CATÁLOGO COM CARROSSEL HORIZONTAL
################################################################################
##
## ✨ RECURSOS:
##   ✓ 5 cartas visíveis no carrossel
##   ✓ Navegação com setas (◄ ►)
##   ✓ Animação suave ao trocar
##   ✓ Som integrável
##   ✓ Painel de detalhes scrollável
##
## 🔊 SOM (OPCIONAL):
##   Adicione em: game/audio/page_flip.ogg
##   Altere linha 11: PAGE_FLIP_SOUND = "audio/page_flip.ogg"
##
################################################################################
## Foto do Pam carrega perfeitamente | Cantos "L" elegantes
################################################################################

## ── Barra de atributo da ficha ──────────────────────────────────────────────
screen barra_atributo_ficha(nome, valor):
    vbox:
        spacing 3
        hbox:
            spacing 5
            text _(nome):
                style "livro_atributo_nome"
                xsize 140
            text (str(valor) + "/100"):
                style "livro_atributo_valor"
                xsize 80
                xalign 1.0

        bar:
            xsize 440
            ysize 10
            value valor
            range 100
            left_bar Frame("gui/bar/left.png", 6, 6)
            right_bar Frame("gui/bar/right.png", 12, 6)
            ## thumb/thumb_shadow removidos: gui/bar/ só tem bottom/left/
            ## right/top.png. Os arquivos gui/bar/thumb.png e thumb_shadow.png
            ## nunca existiram (confirmado com renpy.loadable), e o Ren'Py
            ## levanta exceção ao renderizar a barra — ou seja, abrir a ficha
            ## de um personagem quebrava. Sem thumb a barra desenha normal,
            ## usando só left_bar/right_bar.


## ── Tela de Detalhes ────────────────────────────────────────────────────────
screen detalhes_perfil(data):
    modal True
    zorder 150

    add Solid("#000000aa")

    $ tem_info_imagem = "info_pt" in data
    $ tem_info_texto = "descricao" in data

    frame:
        xpos 675
        ypos 60
        xsize 570
        ysize 960
        background Frame("gui/frame.png", 20, 20)
        padding (24, 24, 24, 24)

        vbox:
            spacing 20
            xfill True
            yfill True

            # Cabeçalho em estilo livro
            frame:
                background Solid("#000000")
                xfill True
                ysize 80
                padding (8, 0)

                text "📖 " + _(data["nome"]):
                    style "perfil_livro_titulo"
                    xalign 0.0
                    yalign 0.5

                textbutton "X":
                    style "botao_fechar_livro"
                    text_color "#c8b89a"
                    xalign 1.0
                    yalign 0.5
                    action Hide("detalhes_perfil")

            frame:
                background Solid("#8b5a2b")
                xfill True
                ysize 3

            # Ficha de informações do personagem. A capa (data["foto"]) só
            # aparece como miniatura no carrossel — aqui dentro do "diário"
            # sempre mostra a ficha (ilustrada, se houver, senão em texto).
            fixed:
                xsize 522
                yfill True
                xalign 0.5

                if tem_info_imagem:
                    $ lang = _preferences.language
                    if lang == "english":
                        $ info_foto = data.get("info_en", data["info_pt"])
                    elif lang == "spanish":
                        $ info_foto = data.get("info_es", data["info_pt"])
                    else:
                        $ info_foto = data["info_pt"]

                    add info_foto:
                        xysize (522, 787)
                        fit "contain"

                elif tem_info_texto:
                    frame:
                        xysize (522, 787)
                        background Solid("#111111")
                        padding (16, 12)

                        viewport:
                            xfill True
                            yfill True
                            mousewheel True
                            draggable True
                            scrollbars "vertical"

                            vbox:
                                xsize 476
                                spacing 14

                                text _("Descrição"):
                                    style "perfil_secao_titulo"

                                text _(data["descricao"]):
                                    style "perfil_label"

                                if "historia" in data:
                                    text _("História"):
                                        style "perfil_secao_titulo"

                                    text _(data["historia"]):
                                        style "perfil_label"

                                if "curiosidade" in data:
                                    text _("Curiosidades"):
                                        style "perfil_secao_titulo"

                                    text _(data["curiosidade"]):
                                        style "perfil_label"

                                if "genero" in data:
                                    text _("INFORMAÇÕES"):
                                        style "livro_secao_titulo"

                                    text _("Gênero: ") + _(data.get("genero", "?")):
                                        style "livro_info_texto"

                                    text _("Sexualidade: ") + _(data.get("sexualidade", "?")):
                                        style "livro_info_texto"

                                    text _("Ocupação: ") + _(data.get("ocupacao", "?")):
                                        style "livro_info_texto"

                                    text _("Espécie: ") + _(data.get("especie", "?")):
                                        style "livro_info_texto"

                                if "personalidade" in data:
                                    text _("PERSONALIDADE"):
                                        style "livro_secao_titulo"

                                    for atributo, valor in data["personalidade"].items():
                                        use barra_atributo_ficha(atributo, valor)

                                if "anatomia" in data:
                                    text _("ANATOMIA"):
                                        style "livro_secao_titulo"

                                    text _("Altura: ") + _(data["anatomia"].get("altura", "?")):
                                        style "livro_info_texto"

                                    text _("Peso: ") + _(data["anatomia"].get("peso", "?")):
                                        style "livro_info_texto"

                                    text _("Raça: ") + _(data["anatomia"].get("raca", "?")):
                                        style "livro_info_texto"

                                    text _("Tipo Sanguíneo: ") + _(data["anatomia"].get("tipo_sangue", "?")):
                                        style "livro_info_texto"

                else:
                    add "gui/card.png":
                        xysize (522, 787)

                    if not data["bloqueado"] and renpy.loadable(data["foto"]):
                        add data["foto"]:
                            xpos 83
                            ypos 123
                            xsize 358
                            ysize 570
                            fit "cover"
                    else:
                        frame:
                            background Solid("#0a0a0a")
                            xpos 83
                            ypos 123
                            xsize 358
                            ysize 570

                            text "???":
                                size 90
                                color "#666666"
                                xalign 0.5
                                yalign 0.5