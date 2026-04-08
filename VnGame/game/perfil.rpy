################################################################################
## Janela de Perfil do Personagem
################################################################################

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
            right_bar Frame("gui/bar/right.png", 6, 6)
            thumb Frame("gui/bar/thumb.png", 6, 6)
            thumb_shadow Frame("gui/bar/thumb_shadow.png", 6, 6)


screen perfil_janela():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1050
        ysize 680
        background None
        padding (15, 15, 15, 15)

        vbox:
            spacing 12

            # Título principal
            text "PERFIL DO PERSONAGEM" style "perfil_titulo"
            
            $ prota_data = persistent.prota_data
            $ g = persistent.genero
            
            if prota_data is not None:
                # Conteúdo principal em hbox
                hbox:
                    spacing 20
                    
                    # Coluna esquerda - Imagem
                    vbox:
                        spacing 8
                        if g == "mulher":
                            add "protaF.png" xysize (240, 380) xalign 0.5 yalign 0.0
                        elif g == "homem":
                            add "protaM.png" xysize (240, 380) xalign 0.5 yalign 0.0
                        else:
                            text "Imagem indisponível" size 20 color "#ffffff" xalign 0.5
                    
                    # Coluna direita - Dados organisados em seções com scrollbar
                    viewport:
                        xsize 770
                        ysize 545
                        
                        
                        vbox:
                            spacing 10
                            
                            # Seção 1: Informações Básicas
                            frame:
                                background Solid("#16213e80")
                                padding (10, 8)
                                xsize 750
                                
                                vbox:
                                    spacing 6
                                    text "Informações Básicas" style "perfil_secao_titulo"
                                    hbox:
                                        spacing 15
                                        vbox:
                                            spacing 4
                                            text "Nome:" style "perfil_label"
                                            text "Apelido:" style "perfil_label"
                                            text "Gênero:" style "perfil_label"
                                            text "Sexualidade:" style "perfil_label"
                                            text "Ocupação:" style "perfil_label"
                                            text "Espécie:" style "perfil_label"
                                        vbox:
                                            spacing 4
                                            text "[prota_data['nome']]" style "perfil_valor"
                                            text "[prota_data['apelido']]" style "perfil_valor"
                                            text "[prota_data['genero']]" style "perfil_valor"
                                            text "[prota_data['sexualidade']]" style "perfil_valor"
                                            text "[prota_data['ocupacao']]" style "perfil_valor"
                                            text "[prota_data['especie']]" style "perfil_valor"
                            
                            # Seção 2: Anatomia
                            frame:
                                background Solid("#16213e80")
                                padding (10, 8)
                                xsize 750
                                
                                vbox:
                                    spacing 6
                                    text "Anatomia" style "perfil_secao_titulo"
                                    hbox:
                                        spacing 15
                                        vbox:
                                            spacing 4
                                            text "Altura:" style "perfil_label"
                                            text "Peso:" style "perfil_label"
                                            text "Raça:" style "perfil_label"
                                            text "Tipo Sanguíneo:" style "perfil_label"
                                        vbox:
                                            spacing 4
                                            text "[prota_data['anatomia']['altura']]" style "perfil_valor"
                                            text "[prota_data['anatomia']['peso']]" style "perfil_valor"
                                            text "[prota_data['anatomia']['raca']]" style "perfil_valor"
                                            text "[prota_data['anatomia']['tipo_sangue']]" style "perfil_valor"
                            
                            # Seção 3: Personalidade (com barras visuais)
                            frame:
                                background Solid("#16213e80")
                                padding (10, 8)
                                xsize 750
                                
                                vbox:
                                    spacing 8
                                    text "Personalidade" style "perfil_secao_titulo"
                                    
                                    use barra_atributo("Gentileza", prota_data['personalidade']['kind'])
                                    use barra_atributo("Inteligência", prota_data['personalidade']['smart'])
                                    use barra_atributo("Seriedade", prota_data['personalidade']['serious'])
                                    use barra_atributo("Humor", prota_data['personalidade']['funny'])
                                    use barra_atributo("Saúde", prota_data['personalidade']['healthy'])
                            
                            # Seção 4: Cores e Notas
                            frame:
                                background Solid("#16213e80")
                                padding (10, 8)
                                xsize 750
                                
                                vbox:
                                    spacing 4
                                    text "Notas" style "perfil_secao_titulo"
                                    text "[prota_data['notas']]" style "perfil_valor" color "#CCCC99"
                                    text "Cores: [', '.join(prota_data['cores_principais'])]" style "perfil_label" size 18
                                    text "Favoritas: [', '.join(prota_data['cores_favoritas'])]" style "perfil_label" size 18

            else:
                text "Nenhum personagem selecionado ainda." size 24 color "#FFCCCC" xalign 0.5
            
            # Botão de fechar
            hbox:
                xalign 0.5
                spacing 10
                textbutton "Fechar" action Hide("perfil_janela"):
                    background Solid("#FF000080")
                    hover_background Solid("#FF0000CC")
                    padding (12, 8)

