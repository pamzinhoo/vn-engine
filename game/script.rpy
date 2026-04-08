# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Arlyson", color="#ff00cc")
image player normal = "jair.webp"
define p = Character("Player", color="#0000ff")


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

    e "venho do Ceara, tenho 18 anos e sou estudante de engenharia de software na UFC. Sou apaixonada por tecnologia, música e viagens. Adoro explorar novos lugares e conhecer pessoas interessantes. Estou animada para compartilhar minhas experiências e aprender com os outros aqui!"

    e ""

    e "Espero que possamos nos divertir juntos e criar memórias incríveis! Vamos embarcar nessa jornada emocionante e descobrir o que o futuro nos reserva!"
    
    hide eileen  # Esconde o personagem anterior
    show player normal at truecenter  # Mostra o novo personagem
    p "Olá, Arlyson! É um prazer conhecê-la. Parece que temos muito em comum, especialmente o amor por tecnologia e viagens. Estou ansioso para compartilhar experiências e aprender com você também. Vamos aproveitar ao máximo essa jornada emocionante juntos!"

    p "salve"
    # This ends the game.

    return
