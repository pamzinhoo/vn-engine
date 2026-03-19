define e = Character("Eileen") 
image bg fundo = "fundo.png"
label start:
    scene bg fundo
    
    show eillen happy
    e "OI"
    call screen escolha_menu
    if _return == "legal":
        e "Obrigado!"
    else:
        s "Seu programador favorito!"
    
    hide steve
    show lula at truecenter
    e "Olha o bolsonaro apareceu"
    hide lula
    show bolsonaro at truecenter
    b "Ta ok?"
    b "Olha quem vem la!"
    hide bolsonaro
    show lula at truecenter
    
    l "Isso é o que você pode fazer!"
    
    return

screen escolha_menu:
    modal True
    frame:
        xalign 0.5 yalign 0.9  # ← MEIO HORIZONTAL + EMBAIXO
        vbox:
            spacing 20
            textbutton "Legal!" action Return("legal")
            textbutton "Quem é você?" action Return("quem")

    
