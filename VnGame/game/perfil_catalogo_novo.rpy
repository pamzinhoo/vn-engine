################################################################################
## Catálogo de Personagens — Estilo Diário/Livro BONITO
## Layout: 1920x1080 | Ren'Py 8.x
################################################################################

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

## ── Estilos ──────────────────────────────────────────────────────────────────
style diario_bg is default:
    background "#0a0a0f"

style diario_livro_outer is frame:
    background "#000000"
    xsize 1200
    ysize 740
    xalign 0.5
    yalign 0.5
    padding (4, 4, 4, 4)

style diario_livro_inner is frame:
    background "#1a1510"
    xfill True
    yfill True
    padding (0, 0, 0, 0)

style diario_pagina_esq is frame:
    background "#f0e8d8"
    xsize 530
    yfill True
    padding (20, 30, 20, 30)

style diario_pagina_dir is frame:
    background "#ede5d4"
    xsize 640
    yfill True
    padding (30, 30, 30, 30)

style diario_nome_text is default:
    font "fonts/fonte.ttf"
    size 38
    color "#1a1005"
    xalign 0.0
    yalign 0.0

style diario_label_text is default:
    font "fonts/fonte.ttf"
    size 17
    color "#8b3a2a"
    xalign 0.0

style diario_corpo_text is default:
    size 20
    color "#2d2010"
    xalign 0.0
    layout "subtitle"

style diario_divisor is frame:
    background "#8b3a2a"
    xfill True
    ysize 2

style diario_char_button is button:
    xsize 160
    ysize 44
    background "#00000000"
    hover_background Solid("#8b3a2a55")
    selected_background Solid("#8b3a2a99")
    padding (12, 6, 12, 6)

style diario_char_button_text is button_text:
    size 22
    color "#aaaaaa"
    hover_color "#ffffff"
    selected_color "#ffffff"
    insensitive_color "#555555"
    xalign 0.0

style diario_indicador is frame:
    background "#8b3a2a"
    xsize 10
    ysize 10

style diario_voltar_button is button:
    xsize 120
    ysize 44
    background "#00000000"
    hover_background Solid("#ffffff22")
    padding (10, 6, 10, 6)

style diario_voltar_button_text is button_text:
    size 24
    color "#aaaaaa"
    hover_color "#ffffff"

## ── Tela principal ───────────────────────────────────────────────────────────
screen perfil_catalogo():
    tag menu
    modal False

    add "#0a0a0f"

    add Solid("#1a0f0522"):
        ysize 300
        yalign 0.0

    fixed:
        xsize 1920
        ysize 1080

        ## MENU LATERAL ESQUERDO
        frame:
            xpos 0
            ypos 0
            xsize 420
            yfill True
            background "#00000000"

            vbox:
                style_prefix "navigation"
                xpos gui.navigation_xpos
                yalign 0.5
                spacing gui.navigation_spacing

                if main_menu:
                    textbutton _("Início") action Start()

                textbutton _("Carga") action ShowMenu("load")
                textbutton _("Perfil") action ShowMenu("perfil_catalogo")
                textbutton _("Sobre") action ShowMenu("about")

                if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                    textbutton _("Ajuda") action ShowMenu("help")

                if renpy.variant("pc"):
                    textbutton _("Sair") action Quit(confirm=not main_menu)

        ## Botão Voltar
        textbutton _("Voltar"):
            style "return_button"
            action Return()

        ## Título "Diário"
        text _("Diário"):
            xpos 470
            ypos 60
            size 52
            color "#c8b89a"
            font "fonts/fonte.ttf"

        ## LISTA DE PERSONAGENS
        default personagem_selecionado = "Pam"

        frame:
            xpos 430
            ypos 160
            xsize 200
            ysize 740
            background "#00000000"

            vbox:
                spacing 4
                yalign 0.0

                for nome_char in personagens_lista:
                    $ dados = personagens_dados[nome_char]
                    $ bloqueado = dados["bloqueado"]

                    hbox:
                        spacing 8
                        yalign 0.5

                        if nome_char == personagem_selecionado:
                            frame:
                                style "diario_indicador"
                                yalign 0.5
                        else:
                            frame:
                                background "#00000000"
                                xsize 10
                                ysize 10
                                yalign 0.5

                        textbutton nome_char:
                            style "diario_char_button"
                            selected (nome_char == personagem_selecionado)
                            action SetScreenVariable("personagem_selecionado", nome_char)

        ## LIVRO (centralizado no Y)
        frame:
            xpos 630
            yalign 0.5
            xsize 1206
            ysize 748
            background "#000000cc"
            padding (0, 0, 0, 0)

        frame:
            xpos 626
            yalign 0.5
            xsize 1200
            ysize 740
            background "#1a1510"
            padding (3, 3, 3, 3)

            hbox:
                spacing 0

                ## ── PÁGINA ESQUERDA (FOTO LIMPA) ────────────────────────────────
                frame:
                    style "diario_pagina_esq"

                    frame:
                        background "#e8dcc8"
                        xfill True
                        yfill True
                        padding (0, 0, 0, 0)

                    $ foto_path = personagens_dados[personagem_selecionado]["foto"]
                    $ eh_bloqueado = personagens_dados[personagem_selecionado]["bloqueado"]

                    if not eh_bloqueado and renpy.loadable(foto_path):
                        add foto_path:
                            xysize (380, 480)
                            xalign 0.5
                            yalign 0.48
                    else:
                        frame:
                            xsize 380
                            ysize 480
                            xalign 0.5
                            yalign 0.48
                            background "#2a2018"
                            padding (10, 10, 10, 10)

                            text "[foto_path]":
                                size 14
                                color "#887755"
                                xalign 0.5
                                yalign 0.5
                                layout "subtitle"

                ## Lombada central
                frame:
                    background "#0a0806"
                    xsize 8
                    yfill True

                ## ── PÁGINA DIREITA (TEXTO COM CANTOS "L") ───────────────────────
                frame:
                    style "diario_pagina_dir"

                    frame:
                        background "#e8dcc0"
                        xfill True
                        yfill True
                        padding (0, 0, 0, 0)

                    frame:
                        background "#d4c8b0"
                        xpos 0
                        ypos 0
                        xsize 55
                        ysize 55

                    frame:
                        background "#d4c8b0"
                        xpos 0
                        ypos 0
                        xsize 28
                        ysize 28

                    frame:
                        background "#d4c8b0"
                        xalign 1.0
                        yalign 1.0
                        xsize 55
                        ysize 55

                    frame:
                        background "#d4c8b0"
                        xalign 1.0
                        yalign 1.0
                        xsize 28
                        ysize 28

                    frame:
                        background "#00000012"
                        xfill True
                        ysize 35
                        yalign 0.0

                    frame:
                        background "#00000012"
                        xfill True
                        ysize 35
                        yalign 1.0

                    $ d = personagens_dados[personagem_selecionado]

                    viewport:
                        xfill True
                        yfill True
                        mousewheel True
                        draggable True

                        vbox:
                            spacing 18

                            text d["nome"]:
                                style "diario_nome_text"

                            frame:
                                style "diario_divisor"

                            null height 6

                            text _("Descrição"):
                                style "diario_label_text"
                            text d["descricao"]:
                                style "diario_corpo_text"

                            null height 4

                            text _("História"):
                                style "diario_label_text"
                            text d["historia"]:
                                style "diario_corpo_text"

                            null height 4

                            text _("Curiosidades"):
                                style "diario_label_text"
                            text d["curiosidade"]:
                                style "diario_corpo_text"

                            null height 20

                            text "1 / 1":
                                size 18
                                color "#8b3a2a"
                                xalign 1.0

################################################################################
## FIM - CÓDIGO COMPLETO E BONITO!
################################################################################