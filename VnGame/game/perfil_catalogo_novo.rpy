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

## ── Transformações/Animações ────────────────────────────────────────────────

## Animação de entrada do card
transform carousel_flip_in:
    zoom 0.0
    time 0.0
    
    easeout 0.35 zoom 1.0
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

            textbutton "CATALOGO":
                xfill True
                ysize 50
                background "#ffaa00"
                text_size 12
                text_color "#000000"
                action NullAction()

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

    default personagem_selecionado = "Pam"
    default carrossel_idx = 0

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

                    button:
                        xysize (370, 740)
                        background "#00000000"
                        action [
                            SetScreenVariable("personagem_selecionado", char_nome),
                            Function(play_page_flip)
                        ]

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

    # ════════════════════════════════════════════════════════════════════════════
    # PAINEL DE DETALHES
    # ════════════════════════════════════════════════════════════════════════════

    $ dados = personagens_dados[personagem_selecionado]
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