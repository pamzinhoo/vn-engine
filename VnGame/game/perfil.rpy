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
        textbutton "{b}{i}Diário{/i}{/b}":
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

                    text "📖 DIÁRIO":
                        style "perfil_livro_titulo"
                        yalign 0.5

                    null:
                        xfill True

                    textbutton "✕":
                        action Hide("perfil_janela")
                        style "botao_fechar_livro"
                        background None
                        xalign 1.0
                        yalign 0.5

            # 🔖 Divisor decorativo
            frame:
                xfill True
                ysize 3
                background Solid("#8b5a2b")

            $ prota_data = getattr(persistent, "prota_data", None)
            $ pagina_diario = prota_data.get("diario_img") if prota_data else None

            # 📄 PÁGINA DO DIÁRIO (apenas imagem, desenhada à mão)
            frame:
                xfill True
                yfill True
                background Solid("#f0e8d8")
                padding (15, 15)

                if pagina_diario and renpy.loadable(pagina_diario):
                    add pagina_diario:
                        fit "contain"
                        xysize (1190, 585)
                        xalign 0.5
                        yalign 0.5
                else:
                    text _("Nenhuma página do diário ainda."):
                        style "livro_placeholder"
                        xalign 0.5
                        yalign 0.5

