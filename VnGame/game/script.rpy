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
image espelho:
    "espelho.png"
    xalign 0.5
    yalign 0.5
    zoom 1.0
    xysize (1920, 1080)

image ctc:
    alpha 1.0
    "seta.png"
    0.75
    alpha 0.0
    0.75
    repeat

# Variável para guardar o gênero escolhido
default persistent.genero = ""
default persistent.prota_data = None

label start:
    call screen escolha_genero with fade_black
    with fade_black
    show screen frase_transicao("“O mal não é profundo nem radical. Ele é como um fungo que se espalha pela superfície, porque não tem raízes. O mal vem da incapacidade de pensar, de se colocar no lugar do outro.”— Hannah Arendt") with dissolve
    pause 6.0
    hide screen frase_transicao with dissolve
    show screen frase_transicao("Dia 0") with dissolve
    pause 1.0
    hide screen frase_transicao with dissolve
    pause 1.0
    show screen horario("…4:55 da manhã.") with dissolve
    pause 2.0
    hide screen horario with dissolve

    show screen botao_perfil

    # Guarda a escolha
    $ persistent.genero = _return
    if persistent.genero == "mulher":
        $ prota_data = protaF_data
    elif persistent.genero == "homem":
        $ prota_data = protaM_data
    $ persistent.prota_data = prota_data

    scene bg fundo 
    with fade_black # isso deixa
    

    if persistent.genero == "mulher":
        $ nome_prota = "Kiyoki Kovalenko"
        
        
        p "{cps=30}Mal consigo abrir os olhos.{/cps}"
        
        p "{cps=30}Minhas pálpebras pesam, e o cansaço parece grudado no meu corpo.{/cps}"
        
        p "{cps=30}Mas não é como se eu tivesse escolha.{/cps}"
        
        p "{cps=30}Minhas malas já estão prontas.{/cps}"
        
        p "{cps=30}Eu só preciso me arrumar… e ir pro aeroporto.{/cps}"
        
        scene black with fade
        pause 1.0
        scene bg fundo with fade
        
        
        p "{cps=30} ... {/cps}"

        p "{cps=30}Essa sou eu.{/cps}"
        
        p "{cps=30}Descabelada. Exausta.{/cps}"
        
        p "{cps=30}Não que isso seja novidade.{/cps}"
        
        p "{cps=30}Cabelo cacheado não é exatamente… prático.{/cps}"
        
        p "{cps=30} ... {/cps}"
        
       

        p "{cps=30}Hoje é o dia da minha viagem de volta.{/cps}"

        p "{cps=30}Atualmente, eu estou no Japão. Vim passar as férias aqui — meu padrasto é japonês.{/cps}"

        p "{cps=30}Eu gosto daqui.{/cps}"

        p "{cps=30}É um lugar… doce. Confortável.{/cps}"

        p "{cps=30}Mas, bem… eu não sou daqui.{/cps}"

        p "{cps=30}Eu nasci na Europa.{/cps}"

        p "{cps=30}Mais especificamente em Insterburg, uma cidade da Prússia.{/cps}"
        
        p "{cps=30}É pra lá que eu estou voltando agora.{/cps}"
        
        p "{cps=30} ... {/cps}"
        p "{cps=30}Vinte e duas horas de viagem.{/cps}"
        p "{cps=30}E, quando eu chegar, ainda vou ter que pegar um ônibus.{/cps}"
        p "{cps=30}..!{/cps}"

        p "{cps=30}Eu sou meio desajeitada.{/cps}"
        p "{cps=30}Nem expliquei o mais importante ainda.{/cps}"

        p "{cps=30} ... {/cps}"
        p "{cps=30}Hoje é meu primeiro dia no ensino médio.{/cps}"
        p "{cps=30}Nova escola.{/cps}"
        p "{cps=30}Nova rotina.{/cps}"
        p "{cps=30}Novo tudo.{/cps}"

        p "{cps=30} ... {/cps}"
        p "{cps=30}O nome é Instituto Real de Insterburg.{/cps}"
        p "{cps=30}Sim… eu sei como isso soa.{/cps}"
        p "{cps=30}Eu sou rica.{/cps}"
        p "{cps=30}Riquinha mimada, se você preferir.{/cps}"

        p "{cps=30} ... {/cps}"
        p "{cps=30}Mas não se engane.{/cps}"
        p "{cps=30}Por mais que eu viva cercada de luxo…{/cps}"
        p "{cps=30}Com a vida praticamente decidida…{/cps}"
        p "{cps=30}isso nunca foi o que mais importou pra mim.{/cps}"

        p "{cps=30} ... {/cps}"
        p "{cps=30}A minha maior paixão… é a história da humanidade.{/cps}"
        p "{cps=30}Histórias de pessoas.{/cps}"
        p "{cps=30}De verdade.{/cps}"

        p "{cps=30} ... {/cps}"
        p "{cps=30}Sempre que eu escuto a história de alguém…{/cps}"
        p "{cps=30}meu coração pesa.{/cps}"
        p "{cps=30}Não importa quem seja.{/cps}"

        p "{cps=30} ... {/cps}"
        p "{cps=30}Eu acho que todo mundo merece ser visto.{/cps}"
        p "{cps=30}Ser lembrado.{/cps}"

        p "{cps=30} ... {/cps}"
        p "{cps=30}Mas o mundo não funciona assim.{/cps}"
        p "{cps=30}Nunca funcionou.{/cps}"
        p "{cps=30}Principalmente… pra quem não é como eu.{/cps}"

        p "{cps=30} (som do ônibus freando){/cps}"
        p "{cps=30}…finalmente.{/cps}"
        p "{cps=30}Que viagem exaustiva…{/cps}"
        p "{cps=30}E olha que eu dormi maior parte do tempo no avião.{/cps}"
        p "{cps=30}Minhas costas ainda doem por causa das cadeiras do ônibus.{/cps}"
        
        p "{cps=30}...{/cps}"
        p "{cps=30}Mas tudo bem.{/cps}" # sprites começa aqui
        show protaF
        p "{cps=30}Valeu a pena.{/cps}"

        p "{cps=30}...{/cps}"
        p "{cps=30}Finalmente estou aqui.{/cps}"
        p "{cps=30}O Instituto Real de Insterburg.{/cps}"
        p "{cps=30}(eu olho para aqueles enormes portões com um leve aperto na garganta){/cps}"
        p "{cps=30}Então é isso.{/cps}"
        p "{cps=30}A partir daqui…{/cps}"
        p "{cps=30}Nada será o mesmo.{/cps}"
        
    elif persistent.genero == "homem":
        $ nome_prota = "Kuroya Yagami"
        show protaM
        
        p "{cps=30}parte masculina{/cps}"
        
        p "{cps=30}a fala do personagem masculino é diferente{/cps}"
        
        p "{cps=30}ele tem que falar de forma diferente.{/cps}"
        
        p "{cps=30}de preferência na giria.{/cps}"
        
        p "{cps=30}desse naipe aí tá ligado{/cps}"

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
