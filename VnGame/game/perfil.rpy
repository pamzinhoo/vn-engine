################################################################################
## Janela de Perfil do Personagem
################################################################################

init -1:

    transform book_entrance:
        alpha 0.0
        yoffset 50
        pause 0.0
        ease 0.5:
            alpha 1.0 
            yoffset 0
       

    transform slide_fade_in:
        alpha 0.0
        xoffset 200
        ease 0.4 alpha 1.0 xoffset 0

    transform fade_bg:
        alpha 0.0
        ease 0.3 alpha 0.6

    transform page_flip_in:
        xtile 0.0
        xzoom 0.1
        alpha 0.3
        ease 0.6 xtile 1.0 xzoom 1.0 alpha 1.0

    transform page_sway:
        rotate 0.0
        linear 1.5 rotate -0.5
        linear 1.5 rotate 0.5
        linear 1.5 rotate 0.0
        repeat


screen botao_perfil():
    frame:
        textbutton "{b}{i}Perfil{/i}{/b}":
            xalign 0.5
            yalign 0.5
            action Show("perfil_janela")
            style "perfil_button"
        xalign 0.98
        yalign 0.02
        xsize 130
        ysize 50
        background Solid("#00000080")


screen barra_atributo(nome, valor):
    vbox:
        spacing 2
        hbox:
            spacing 5
            text nome style "perfil_atributo_nome" xsize 100
            text "[valor]/100" style "perfil_atributo_valor" xsize 50 xalign 1.0
        
        bar:
            xsize 220
            ysize 12
            value valor
            range 100
            left_bar Frame("gui/bar/left.png", 6, 6)
            right_bar Frame("gui/bar/right.png", 12, 6)
            thumb Frame("gui/bar/thumb.png", 6, 6)
            thumb_shadow Frame("gui/bar/thumb_shadow.png", 6, 6)


screen barra_atributo_livro(nome, valor):
    vbox:
        spacing 3
        hbox:
            spacing 5
            text nome:
                style "livro_atributo_nome"
                xsize 100
            text "[valor]/100":
                style "livro_atributo_valor"
                xsize 80
                xalign 1.0
        
        bar:
            xsize 520
            ysize 10
            value valor
            range 100
            left_bar Frame("gui/bar/left.png", 6, 6)
            right_bar Frame("gui/bar/right.png", 12, 6)
            thumb Frame("gui/bar/thumb.png", 6, 6)
            thumb_shadow Frame("gui/bar/thumb_shadow.png", 6, 6)


screen perfil_janela():
    modal True
    zorder 200

    # Fundo escuro com overlay
    add Solid("#000000") at fade_bg

    # 📖 Moldura exterior do livro com sombra
    frame:
        at book_entrance
        xalign 0.5
        yalign 0.5
        xsize 1280
        ysize 760
        background Frame("gui/frame.png", 20, 20)
        padding (30, 30)

        vbox:
            xfill True
            yfill True
            spacing 0

            # 🎨 CAPA DO LIVRO - Estilo Diário
            frame:
                xfill True
                ysize 80
                background Solid("#2d1f15")
                padding (20, 15)

                hbox:
                    xfill True
                    spacing 20

                    text "📖 PERFIL":
                        style "perfil_livro_titulo"

                    null width 50

                    textbutton "✕":
                        action Hide("perfil_janela")
                        style "botao_fechar_livro"
                        background None

            # 🔖 Divisor decorativo
            frame:
                xfill True
                ysize 3
                background Solid("#8b5a2b")

            $ prota_data = getattr(persistent, "prota_data", None)

            if prota_data:
                # 📖 LIVRO ABERTO COM DUAS PÁGINAS
                hbox:
                    xfill True
                    yfill True
                    spacing 1

                    # 📄 PÁGINA ESQUERDA (Foto/Avatar)
                    frame:
                        xsize 580
                        yfill True
                        background Solid("#f0e8d8")
                        padding (25, 25)

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 15

                            # Nome do personagem
                            text "[prota_data['nome']]":
                                style "livro_nome_text"
                                text_align 0.5
                                xalign 0.5

                            # Espaço para avatar (placeholder)
                            frame:
                                xsize 480
                                ysize 280
                                background Solid("#d4c5b0")
                                padding (20, 20)

                                text _("Avatar do\nPersonagem"):
                                    style "livro_placeholder"
                                    xalign 0.5
                                    yalign 0.5

                            # Informações básicas na página esquerda
                            frame:
                                xfill True
                                background Solid("#e8dcc8")
                                padding (12, 10)

                                vbox:
                                    spacing 2
                                    text _("Apelido:"):
                                        style "livro_label_texto"
                                    text "[prota_data['apelido']]":
                                        style "livro_valor_texto"

                    # 📄 PÁGINA DIREITA (Conteúdo)
                    frame:
                        xsize 580
                        yfill True
                        background Solid("#ede5d4")
                        padding (25, 25)

                        viewport:
                            xfill True
                            yfill True
                            scrollbars "vertical"
                            mousewheel True

                            vbox:
                                xfill True
                                spacing 12

                                # Seção: Informações Básicas
                                frame:
                                    xfill True
                                    background Solid("#dcd4c4")
                                    padding (12, 10)

                                    vbox:
                                        spacing 6
                                        xfill True

                                        text _("INFORMAÇÕES"):
                                            style "livro_secao_titulo"

                                        frame:
                                            xfill True
                                            ysize 1
                                            background Solid("#8b5a2b")

                                        text _("Gênero: ") + "[prota_data['genero']]":
                                            style "livro_info_texto"

                                        text _("Sexualidade: ") + "[prota_data['sexualidade']]":
                                            style "livro_info_texto"

                                        text _("Ocupação: ") + "[prota_data['ocupacao']]":
                                            style "livro_info_texto"

                                        text _("Espécie: ") + "[prota_data['especie']]":
                                            style "livro_info_texto"

                                # Seção: Personalidade
                                frame:
                                    xfill True
                                    background Solid("#dcd4c4")
                                    padding (12, 10)

                                    vbox:
                                        spacing 8
                                        xfill True

                                        text _("PERSONALIDADE"):
                                            style "livro_secao_titulo"

                                        frame:
                                            xfill True
                                            ysize 1
                                            background Solid("#8b5a2b")

                                        use barra_atributo_livro("Gentileza", prota_data['personalidade']['kind'])
                                        use barra_atributo_livro("Inteligência", prota_data['personalidade']['smart'])
                                        use barra_atributo_livro("Seriedade", prota_data['personalidade']['serious'])
                                        use barra_atributo_livro("Humor", prota_data['personalidade']['funny'])
                                        use barra_atributo_livro("Saúde", prota_data['personalidade']['healthy'])

                                # Seção: Anatomia
                                frame:
                                    xfill True
                                    background Solid("#dcd4c4")
                                    padding (12, 10)

                                    vbox:
                                        spacing 6
                                        xfill True

                                        text _("ANATOMIA"):
                                            style "livro_secao_titulo"

                                        frame:
                                            xfill True
                                            ysize 1
                                            background Solid("#8b5a2b")

                                        text _("Altura: ") + "[prota_data['anatomia']['altura']]":
                                            style "livro_info_texto"

                                        text _("Peso: ") + "[prota_data['anatomia']['peso']]":
                                            style "livro_info_texto"

                                        text _("Raça: ") + "[prota_data['anatomia']['raca']]":
                                            style "livro_info_texto"

                                        text _("Tipo Sanguíneo: ") + "[prota_data['anatomia']['tipo_sangue']]":
                                            style "livro_info_texto"

                                # Seção: Notas
                                frame:
                                    xfill True
                                    background Solid("#dcd4c4")
                                    padding (12, 10)

                                    vbox:
                                        spacing 6
                                        xfill True

                                        text _("NOTAS"):
                                            style "livro_secao_titulo"

                                        frame:
                                            xfill True
                                            ysize 1
                                            background Solid("#8b5a2b")

                                        text "[prota_data['notas']]":
                                            style "livro_info_texto"
            else:
                text _("Nenhum personagem selecionado."):
                    xalign 0.5
                    yalign 0.5

