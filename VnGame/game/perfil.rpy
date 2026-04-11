################################################################################
## Janela de Perfil do Personagem
################################################################################
init:
    transform slide_fade_in:
        alpha 0.0
        xoffset 200
        ease 0.4 alpha 1.0 xoffset 0

    transform fade_bg:
        alpha 0.0
        ease 0.3 alpha 0.6



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


screen perfil_janela():
    modal True
    zorder 200

    # 🔥 Fundo escuro (overlay estilo AAA)
    add Solid("#000000") at fade_bg

    # 🔥 Container principal com animação
    frame:
        at slide_fade_in
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 700
        background Frame("gui/frame.png", 20, 20)
        padding (20, 20)

        vbox:
            spacing 15

            # 🔥 Header moderno
            hbox:
                xfill True

                text "PERFIL DO PERSONAGEM":
                    style "perfil_titulo"

                textbutton "✕":
                    action Hide("perfil_janela")
                    style "botao_fechar"
                    background None

            $ prota_data = getattr(persistent, "prota_data", None)

            if prota_data:

                hbox:
                    spacing 25

                    # 🔥 Lado esquerdo (avatar futuramente)
                    frame:
                        xsize 260
                        ysize 500
                        background Solid("#111a")

                        vbox:
                            xalign 0.5
                            yalign 0.5

                            text "Avatar":
                                xalign 0.5

                    # 🔥 Lado direito (conteúdo)
                    viewport:
                        xsize 750
                        ysize 560
                        scrollbars "vertical"
                        mousewheel True

                        vbox:
                            spacing 15

    # 🔥 Informações Básicas
                            frame:
                                background Solid("#1e2a3acc")
                                padding (15, 12)

                                vbox:
                                    spacing 6
                                    text "Informações Básicas" style "perfil_secao_titulo"

                                    text "Nome: [prota_data['nome']]"
                                    text "Apelido: [prota_data['apelido']]"
                                    text "Gênero: [prota_data['genero']]"
                                    text "Sexualidade: [prota_data['sexualidade']]"
                                    text "Ocupação: [prota_data['ocupacao']]"
                                    text "Espécie: [prota_data['especie']]"

    # 🔥 Personalidade
                            frame:
                                background Solid("#1e2a3acc")
                                padding (15, 12)

                                vbox:
                                    spacing 10
                                    text "Personalidade" style "perfil_secao_titulo"

                                    use barra_atributo("Gentileza", prota_data['personalidade']['kind'])
                                    use barra_atributo("Inteligência", prota_data['personalidade']['smart'])
                                    use barra_atributo("Seriedade", prota_data['personalidade']['serious'])
                                    use barra_atributo("Humor", prota_data['personalidade']['funny'])
                                    use barra_atributo("Saúde", prota_data['personalidade']['healthy'])

    # 🔥 Anatomia (CORRIGIDO)
                            frame:
                                background Solid("#1e2a3acc")
                                padding (15, 12)

                                vbox:
                                    spacing 8
                                    text "Anatomia" style "perfil_secao_titulo"

                            
                                    
                                    text "Altura:" style "perfil_label"
                                    text "[prota_data['anatomia']['altura']]" style "perfil_valor"

                            
                                    
                                    text "Peso:" style "perfil_label"
                                    text "[prota_data['anatomia']['peso']]" style "perfil_valor"

                            
                                    
                                    text "Raça:" style "perfil_label"
                                    text "[prota_data['anatomia']['raca']]" style "perfil_valor"

                            
                                    
                                    text "Tipo Sanguíneo:" style "perfil_label"
                                    text "[prota_data['anatomia']['tipo_sangue']]" style "perfil_valor"

    # 🔥 Extras
                            frame:
                                background Solid("#1e2a3acc")
                                padding (15, 12)

                                vbox:
                                    spacing 6
                                    text "Notas" style "perfil_secao_titulo"
            else:
                text "Nenhum personagem selecionado." xalign 0.5
            
            # Botão de fechar
            #hbox:
                #xalign 0.5
                #spacing 10
                #textbutton "Fechar" action Hide("perfil_janela"):
                    #background Solid("#FF000080")
                    #hover_background Solid("#FF0000CC")
                    #padding (12, 8)

