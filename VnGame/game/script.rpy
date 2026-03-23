default nome_prota = ""
define p = Character("[nome_prota]", ctc="ctc", ctc_position="nestled")
define n = Character(
    None,
    what_style="narrador_dialogo",
    window_style="narrador_window"
)
image protaF:
    "protaF.png"
    zoom 0.8
    xalign 0.2
    yalign 1
image protaM:
    "protaM.png"
    zoom 5
    xalign 0.5
    yalign 0
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
    call screen escolha_genero with fade_black
    with fade_black
    show screen frase_transicao("“O mal não é profundo nem radical. Ele é como um fungo que se espalha pela superfície, porque não tem raízes. O mal vem da incapacidade de pensar, de se colocar no lugar do outro.”— Hannah Arendt") with dissolve
    pause 8.0
    hide screen frase_transicao with dissolve
    show screen horario("…4:55 da manhã.") with dissolve
    pause 2.0
    hide screen horario with dissolve

    # Guarda a escolha
    $ genero = _return

    scene bg fundo # trocar isso por um quarto
    with fade_black # isso deixa
    

    if genero == "mulher":
        $ nome_prota = "Kiyoki Kovalenko"
        show protaF
    elif genero == "homem":
        $ nome_prota = "Kuroya Yagami"
        show protaM
    
    
    p "OI {cps=30}aparece letra por letra igual maquina{/cps}" # usar o narrador (N)
    # roteiro apenas o quarto sem ninguem aparecendo e a fala do narrador ou da protaF (nao sei =] )

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


