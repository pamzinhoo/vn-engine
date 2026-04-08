style narrador_window:
    background None          # sem textbox
    xpos 0
    ypos 0
    xfill True
    yfill True
    padding (80, 40)

style narrador_dialogo:
    color "#ffffff"
    size 32
    italic True
    text_align 0.5           # centralizado
    xalign 0.5
    yalign 0.5

style perfil_button is button:
    xsize 130
    ysize 50
    background Solid("#00000080")
    hover_background Solid("#000000AA")
    
style perfil_button_text is button_text:
    color "#ffffff"
    bold True
    italic True
    size 20
    xalign 0.5
    yalign 0.5

# Estilos para a janela de perfil
style perfil_titulo:
    color "#00CCFF"
    size 32
    bold True
    xalign 0.5

style perfil_secao_titulo:
    color "#66FFFF"
    size 24
    bold True
    xalign 0.0

style perfil_label:
    color "#AAAAAA"
    size 20
    xalign 0.0

style perfil_valor:
    color "#FFFFFF"
    size 20
    xalign 0.0

style perfil_atributo_nome:
    color "#CCCCCC"
    size 18
    xalign 0.0

style perfil_atributo_valor:
    color "#00FFFF"
    size 18
    bold True
    xalign 1.0
