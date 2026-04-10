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


## Estilos para o Catálogo de Personagens
style perfil_catalogo_title:
    color "#00CCFF"
    size 48
    bold True
    xalign 0.0
    yalign 0.0

style perfil_catalogo_sidebar:
    background Solid("#0f0f1e")
    xsize 160
    yfill True
    padding (15, 20, 15, 20)

style perfil_catalogo_menu_item:
    background None
    hover_background None
    padding (8, 6, 8, 6)
    xalign 0.0
    xsize 140

style perfil_catalogo_menu_item_text:
    color "#AAAAAA"
    size 14
    xalign 0.0

style perfil_catalogo_menu_item_active:
    background None
    padding (8, 6, 8, 6)
    xalign 0.0
    xsize 140

style perfil_catalogo_menu_item_active_text:
    color "#FFFFFF"
    size 14
    bold True
    xalign 0.0


## Estilos simples e compactos para menu do catálogo
style perfil_catalogo_simple_button is button:
    background None
    hover_background None
    padding (0, 0, 0, 0)
    xalign 0.0

style perfil_catalogo_simple_text is button_text:
    color "#AAAAAA"
    size 16
    xalign 0.0

style perfil_catalogo_simple_text_active is button_text:
    color "#FFFFFF"
    size 16
    bold True
    xalign 0.0

style perfil_catalogo_menu_separator:
    top_margin 20
    xalign 0.0
    xsize 2
    ysize 100
    background Solid("#00CCFF")

style perfil_catalogo_card:
    background None
    padding (0, 0, 0, 0)
    xsize 380
    ysize 140

style perfil_catalogo_card_button is button:
    background Solid("#00CCFF")
    hover_background Solid("#00FFFF")
    padding (2, 2, 2, 2)
    xsize 380
    ysize 140

style perfil_catalogo_card_container:
    background Solid("#16213e")
    xsize 376
    ysize 136
    padding (0, 0, 0, 0)

style perfil_catalogo_card_name:
    xsize 152  # 40% of 380
    ysize 136
    xalign 0.5
    yalign 0.5
    background Solid("#1a1a2e")

style perfil_catalogo_card_name_text:
    color "#FFFFFF"
    size 18
    bold True
    xalign 0.5
    yalign 0.5

style perfil_catalogo_card_photo:
    xsize 228  # 60% of 380
    ysize 136
    xalign 0.5
    yalign 0.5
    background Solid("#16213e")

style perfil_catalogo_card_photo_text:
    color "#888888"
    size 16
    italic True
    xalign 0.5
    yalign 0.5

style perfil_catalogo_grid:
    spacing 20

style perfil_catalogo_close_button is button:
    background Solid("#1a1a2e")
    hover_background Solid("#4a4a6e")
    padding (8, 8)
    xsize 40
    ysize 40

style perfil_catalogo_close_button_text:
    color "#00CCFF"
    size 24
    bold True
    xalign 0.5
    yalign 0.5

style perfil_catalogo_back_button is button:
    background Solid("#1a1a2e")
    hover_background Solid("#4a4a6e")
    padding (8, 8)
    xalign 0.0

style perfil_catalogo_back_button_text:
    color "#00CCFF"
    size 16
    xalign 0.0
    yalign 0.5
