default nome_prota = ""
define p = Character("[nome_prota]", ctc="ctc", ctc_position="nestled", name_color="#FFFFFF")
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
image aviso:
    "aviso.png"
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
    scene black
    pause 0.5
    scene aviso with dissolve
    pause 10.0
    scene black with dissolve
    pause 1.0
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
        
        show screen day_locate("00", "Escola - Corredor")
        p "{cps=30}{color=#FFFF00}Mal consigo abrir os olhos.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}Minhas pálpebras pesam, e o cansaço parece grudado no meu corpo.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}Mas não é como se eu tivesse escolha.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}Minhas malas já estão prontas.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}Eu só preciso me arrumar… e ir pro aeroporto.{/color}{/cps}"
        
        scene black with fade
        pause 1.0
        scene bg fundo with fade
        
        
        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}Essa sou eu.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}Descabelada. Exausta.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}Não que isso seja novidade.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}Cabelo cacheado não é exatamente… prático.{/color}{/cps}"
        
        p "{cps=30}{color=#0099cc}(suspiro){/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        
       

        p "{cps=30}{color=#FFFF00}Hoje é o dia da minha viagem de volta.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}Atualmente, eu estou no Japão. Vim passar as férias aqui pois meu padrasto é japonês.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}Eu gosto daqui.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}É um lugar… doce. Confortável.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}Mas, bem… eu não sou daqui.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}Eu nasci na Europa.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}Mais especificamente em Insterburg, uma cidade da Prússia.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}É pra lá que eu estou voltando agora.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Vinte e duas horas de viagem.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}E, quando eu chegar, ainda vou ter que pegar um ônibus.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}..!{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}Eu sou meio desajeitada.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Nem expliquei o mais importante ainda.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Hoje é meu primeiro dia no ensino médio.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Nova escola.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Nova rotina.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Novo tudo.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}O nome é Instituto Real de Insterburg.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Sim… eu sei como isso soa.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Eu sou rica.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Riquinha mimada, se você preferir.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Mas não se engane.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Por mais que eu viva cercada de luxo…{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}com a vida praticamente decidida…{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}isso nunca foi o que mais importou pra mim.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}A minha maior paixão… é a história da humanidade.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Histórias de pessoas.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Sempre que eu escuto a história de alguém…{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}meu coração pesa.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Não importa quem seja.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Eu acho que todo mundo merece ser visto.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Ser lembrado.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Mas o mundo não funciona assim e nunca funcionou{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Pelo menos... não para pessoas iguais a mim{/color}{/cps}"

        p "{cps=30}{color=#0099cc}(som do ônibus freando){/color}{/cps}"
        p "{cps=30}{color=#FFFF00}…finalmente.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Que viagem exaustiva…{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}E olha que eu dormi maior parte do tempo no avião.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Minhas costas ainda doem por causa das cadeiras do ônibus.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Mas tudo bem.{/color}{/cps}" # sprites começa aqui
        show protaF
        p "{cps=30}{color=#FFFF00}Valeu a pena.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Finalmente estou aqui.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}O Instituto Real de Insterburg.{/color}{/cps}"
        p "{cps=30}{color=#0099cc}(eu olho para aqueles enormes portões com um leve aperto na garganta){/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Então é isso.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}A partir daqui…{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Nada será o mesmo.{/color}{/cps}"
        
        p "{cps=30}{color=#0099cc}(porta fechando){/color}{/cps}"
        
    elif persistent.genero == "homem":
        $ nome_prota = "Kuroya Yagami"
        show protaM
        show screen day_locate("Escola - Corredor", "00") # esconder day locate -> hide screen day_locate
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
