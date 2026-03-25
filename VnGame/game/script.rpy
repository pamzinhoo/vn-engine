# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define s = Character("Steve")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

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

