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
        "???",
    ]

    personagens_dados = {
        "Pam": {
            "foto":        "images/protaF.png",
            "nome":        "Pam",
            "descricao":   "alguma coisa aqui",
            "historia":    "historia do rdr2",
            "curiosidade": "ela é uma pessoa",
            "bloqueado":   False,
        },
        "Nao sei": {
            "foto":        "protaM.png",
            "nome":        "Prota M",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
        },
        "Maya": {
            "foto":        "foto_personagem_aqui",
            "nome":        "Maya",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
        },
        "Ethan": {
            "foto":        "foto_personagem_aqui",
            "nome":        "Ethan",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
        },
        "Diretor": {
            "foto":        "foto_personagem_aqui",
            "nome":        "Diretor",
            "descricao":   "descricao_aqui",
            "historia":    "historia_aqui",
            "curiosidade": "curiosidades_aqui",
            "bloqueado":   False,
        },
        "???": {
            "foto":        "foto_personagem_aqui",
            "nome":        "???",
            "descricao":   "— BLOQUEADO —",
            "historia":    "Desbloqueie este personagem para ler mais.",
            "curiosidade": "...",
            "bloqueado":   True,
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

## Animação de entrada do card
transform carousel_flip_in:
    zoom 0.0
    time 0.0
    
    easeout 0.35 zoom 1.0

## Animação de zoom no hover
transform card_hover_zoom:
    zoom 1.0
    on hover:
        ease 0.2 zoom 1.1
    on idle:
        ease 0.2 zoom 1.0
## ── Estilos ─────────────────────────────────────────────────────────────────
style info_label is default:
    size 18
    color "#ffaa00"
    font "fonts/fonte.ttf"

style info_text is default:
    size 15
    color "#cccccc"

## ── Tela principal - Carrossel ──────────────────────────────────────────────
screen perfil_catalogo():
    tag menu
    modal False

    # Fundo
    add "#0a0a0f"

    default personagem_selecionado = "Pam"
    default carrossel_idx = 0
    default tab = "personagens"
    default lugar_selecionado = "Escola"
    default carrossel_idx_lugares = 0
    default rota_selecionada = "Rota de Pam"
    default carrossel_idx_rotas = 0

    $ bg_personagens = "#ffaa00" if tab == "personagens" else "#2a2a2a"
    $ tc_personagens = "#000000" if tab == "personagens" else "#ffffff"
    $ bg_lugares = "#ffaa00" if tab == "lugares" else "#2a2a2a"
    $ tc_lugares = "#000000" if tab == "lugares" else "#ffffff"
    $ bg_rotas = "#ffaa00" if tab == "rotas" else "#2a2a2a"
    $ tc_rotas = "#000000" if tab == "rotas" else "#ffffff"

    # Menu lateral (estilo da imagem)
    frame:
        xpos 0
        ypos 0
        xsize 140
        yfill True
        background "#2a2a2a"

        vbox:
            xfill True
            spacing 0
            yalign 0.0

            text "MENU":
                size 16
                color "#ffffff"
                font "fonts/fonte.ttf"
                xalign 0.5

            frame:
                background "#ffaa00"
                xfill True
                ysize 3

            textbutton "PERSONAGENS":
                xfill True
                ysize 50
                background bg_personagens
                text_size 12
                text_color tc_personagens
                action SetScreenVariable("tab", "personagens")

            textbutton "LUGARES":
                xfill True
                ysize 50
                background bg_lugares
                text_size 12
                text_color tc_lugares
                action SetScreenVariable("tab", "lugares")

            textbutton "ROTAS":
                xfill True
                ysize 50
                background bg_rotas
                text_size 12
                text_color tc_rotas
                action SetScreenVariable("tab", "rotas")

    # Botão voltar
    textbutton "VOLTAR":
        xpos 60
        ypos 1030
        xysize (100, 35)
        text_size 14
        text_color "#ffffff"
        background "#00000000"
        action Return()

    # Título
    text "CATÁLOGO":
        xpos 200
        ypos 20
        size 44
        color "#ffaa00"
        font "fonts/fonte.ttf"

    # ════════════════════════════════════════════════════════════════════════════
    # CARROSSEL DE PERSONAGENS
    # ════════════════════════════════════════════════════════════════════════════

    if tab == "personagens":

        # Botão anterior
        textbutton "◄":
            xpos 30
            ypos 400
            xysize (80, 150)
            background "#2a2a2a"
            hover_background Solid("#444444")
            text_size 48
            text_color "#ffaa00"
            text_hover_color "#ffffff"
            action If(carrossel_idx > 0, 
                    SetScreenVariable("carrossel_idx", carrossel_idx - 1),
                    NullAction())

        # Frame carrossel
        frame:
            xpos 140
            ypos 150
            xsize 1700
            ysize 800
            background "#00000000"

            hbox:
                spacing 30
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

                    button:
                        at card_hover_zoom
                        action [
                            SetScreenVariable("personagem_selecionado", char_nome),
                            Function(play_page_flip)
                        ]

                        frame:
                            if is_selected:
                                background "#ffffff33"
                                xysize (380, 750)
                                padding (8, 8, 8, 8)
                                at carousel_flip_in
                            else:
                                background "#1a1a1a"
                                xysize (370, 740)
                                padding (6, 6, 6, 6)

                            vbox:
                                spacing 0
                                xfill True
                                yfill True

                                # Foto
                                frame:
                                    background "#0a0a0a"
                                    xysize (370, 690)

                                    if not bloqueado and renpy.loadable(foto):
                                        add foto:
                                            xysize (370, 690)
                                    else:
                                        text "???":

                                            size 80
                                            color "#555555"
                                            xalign 0.5
                                            yalign 0.5

                                # Nome
                                text char_nome:
                                    size 11
                                    color "#ffffff"
                                    xalign 0.5
                                    yalign 0.5

        # Botão próximo
        textbutton "►":
            xpos 1850
            ypos 400
            xysize (80, 150)
            background "#2a2a2a"
            hover_background Solid("#444444")
            text_size 48
            text_color "#ffaa00"
            text_hover_color "#ffffff"
            action If(carrossel_idx < len(personagens_lista) - max_visible,
                    SetScreenVariable("carrossel_idx", carrossel_idx + 1),
                    NullAction())

    elif tab == "lugares":

        # Botão anterior lugares
        textbutton "◄":
            xpos 30
            ypos 400
            xysize (80, 150)
            background "#2a2a2a"
            hover_background Solid("#444444")
            text_size 48
            text_color "#ffaa00"
            text_hover_color "#ffffff"
            action If(carrossel_idx_lugares > 0, 
                    SetScreenVariable("carrossel_idx_lugares", carrossel_idx_lugares - 1),
                    NullAction())

        # Frame carrossel lugares
        frame:
            xpos 140
            ypos 150
            xsize 1700
            ysize 800
            background "#00000000"

            hbox:
                spacing 30
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

                    button:
                        at card_hover_zoom
                        action [
                            SetScreenVariable("lugar_selecionado", lugar_nome),
                            Function(play_page_flip)
                        ]

                        frame:
                            if is_selected:
                                background "#ffffff33"
                                xysize (380, 750)
                                padding (8, 8, 8, 8)
                                at carousel_flip_in
                            else:
                                background "#1a1a1a"
                                xysize (370, 740)
                                padding (6, 6, 6, 6)

                            vbox:
                                spacing 0
                                xfill True
                                yfill True

                                # Foto
                                frame:
                                    background "#0a0a0a"
                                    xysize (370, 690)

                                    if not bloqueado and renpy.loadable(foto):
                                        add foto:
                                            xysize (370, 690)
                                    else:
                                        text "???":

                                            size 80
                                            color "#555555"
                                            xalign 0.5
                                            yalign 0.5

                                # Nome
                                text lugar_nome:
                                    size 11
                                    color "#ffffff"
                                    xalign 0.5
                                    yalign 0.5

        # Botão próximo lugares
        textbutton "►":
            xpos 1850
            ypos 400
            xysize (80, 150)
            background "#2a2a2a"
            hover_background Solid("#444444")
            text_size 48
            text_color "#ffaa00"
            text_hover_color "#ffffff"
            action If(carrossel_idx_lugares < len(lugares_lista) - max_visible,
                    SetScreenVariable("carrossel_idx_lugares", carrossel_idx_lugares + 1),
                    NullAction())

    elif tab == "rotas":

        # Botão anterior rotas
        textbutton "◄":
            xpos 30
            ypos 400
            xysize (80, 150)
            background "#2a2a2a"
            hover_background Solid("#444444")
            text_size 48
            text_color "#ffaa00"
            text_hover_color "#ffffff"
            action If(carrossel_idx_rotas > 0, 
                    SetScreenVariable("carrossel_idx_rotas", carrossel_idx_rotas - 1),
                    NullAction())

        # Frame carrossel rotas
        frame:
            xpos 140
            ypos 150
            xsize 1700
            ysize 800
            background "#00000000"

            hbox:
                spacing 30
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

                    button:
                        at card_hover_zoom
                        action [
                            SetScreenVariable("rota_selecionada", rota_nome),
                            Function(play_page_flip)
                        ]

                        frame:
                            if is_selected:
                                background "#ffffff33"
                                xysize (380, 750)
                                padding (8, 8, 8, 8)
                                at carousel_flip_in
                            else:
                                background "#1a1a1a"
                                xysize (370, 740)
                                padding (6, 6, 6, 6)

                            vbox:
                                spacing 0
                                xfill True
                                yfill True

                                # Foto
                                frame:
                                    background "#0a0a0a"
                                    xysize (370, 690)

                                    if not bloqueado and renpy.loadable(foto):
                                        add foto:
                                            xysize (370, 690)
                                    else:
                                        text "???":

                                            size 80
                                            color "#555555"
                                            xalign 0.5
                                            yalign 0.5

                                # Nome
                                text rota_nome:
                                    size 11
                                    color "#ffffff"
                                    xalign 0.5
                                    yalign 0.5

        # Botão próximo rotas
        textbutton "►":
            xpos 1850
            ypos 400
            xysize (80, 150)
            background "#2a2a2a"
            hover_background Solid("#444444")
            text_size 48
            text_color "#ffaa00"
            text_hover_color "#ffffff"
            action If(carrossel_idx_rotas < len(rotas_lista) - max_visible,
                    SetScreenVariable("carrossel_idx_rotas", carrossel_idx_rotas + 1),
                    NullAction())

    # ════════════════════════════════════════════════════════════════════════════
    # PAINEL DE DETALHES
    # ════════════════════════════════════════════════════════════════════════════

    if tab == "personagens":
        $ dados = personagens_dados[personagem_selecionado]
        $ nome = dados["nome"]
        $ descricao = dados["descricao"]
        $ historia = dados["historia"]
        $ curiosidade = dados["curiosidade"]
    elif tab == "lugares":
        $ dados = lugares_dados[lugar_selecionado]
        $ nome = dados["nome"]
        $ descricao = dados["descricao"]
        $ historia = dados["historia"]
        $ curiosidade = dados["curiosidade"]
    elif tab == "rotas":
        $ dados = rotas_dados[rota_selecionada]
        $ nome = dados["nome"]
        $ descricao = dados["descricao"]
        $ historia = dados["historia"]
        $ curiosidade = dados["curiosidade"]

    # Frame detalhes
    frame:
        xpos 140
        ypos 980
        xsize 1640
        ysize 70
        background "#1a1510"
        padding (15, 10, 15, 10)

        viewport:
            xfill True
            yfill True
            mousewheel True
            draggable True
            at carousel_flip_in

            vbox:
                spacing 15

                # Nome
                text nome:
                    size 32
                    color "#ffaa00"
                    font "fonts/fonte.ttf"

                # Linha
                frame:
                    background "#ffaa00"
                    xfill True
                    ysize 2

                # Conteúdo
                hbox:
                    spacing 40
                    xfill True

                    vbox:
                        xsize 600
                        spacing 10

                        text "Descrição":
                            style "info_label"

                        text descricao:
                            style "info_text"

                        text "História":
                            style "info_label"

                        text historia:
                            style "info_text"

                    vbox:
                        xsize 600
                        spacing 10

                        text "Curiosidades":
                            style "info_label"

                        text curiosidade:
                            style "info_text"

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