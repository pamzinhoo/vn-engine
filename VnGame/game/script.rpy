default nome_prota = ""
define p = Character("[nome_prota]", ctc="ctc", ctc_position="nestled")
image protaF:
    "protaF.png"
    zoom 0.2
image protaM:
    "protaM.png"
image bg fundo = "fundo.png"
image ctc:
    alpha 1.0
    "seta.png"
    0.75
    alpha 0.0
    0.75
    repeat

# Variável para guardar o gênero escolhido
default genero = ""

label start:
    # Tela de escolha ANTES do fade
    call screen escolha_genero

    # Guarda a escolha
    $ genero = _return

    scene bg fundo
    with fade_black
    

    if genero == "mulher":
        $ nome_prota = "Kiyoki Kovalenko"
        show protaF
    elif genero == "homem":
        $ nome_prota = "Menino"
        show protaM
    
    
    p "OI {cps=30}aparece letra por letra igual maquina{/cps}"
    call screen escolha_menu

    if _return == "legal":
        p "Obrigado!"
    elif _return == "quem":
        p "{cps=30}Seu {glitch=50}programador{/glitch} favorito!{/cps}"

    return

# Tela de escolha de gênero
screen escolha_genero:
    modal True

    # Fundo escuro por trás
    add "#000000"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        text "Quem você é?" xalign 0.5 size 40 color "#ffffff"

        hbox:
            spacing 50
            xalign 0.5

            # Botão Mulher (com foto)
            vbox:
                spacing 10
                xalign 0.5
                add "protaF.png" zoom 0.2  # ajuste o zoom conforme o tamanho da sua foto
                textbutton "Mulher" action Return("mulher") xalign 0.5

            # Botão Homem (sem foto por enquanto)
            vbox:
                spacing 10
                xalign 0.5
                # Placeholder até ter a foto do homem
                add "protaM.png"   # retângulo cinza no lugar da foto
                textbutton "Homem" action Return("homem") xalign 0.5

screen escolha_menu:
    modal True
    frame:
        xalign 0.5 yalign 0.9
        vbox:
            spacing 20
            textbutton "Legal!" action Return("legal")
            textbutton "Quem é você?" action Return("quem")