default nome_prota = ""
define p = Character("[nome_prota]", ctc="ctc", ctc_position="nestled", name_color="#FFFFFF")
define n = Character(
    None,
    what_style="narrador_dialogo",
    window_style="narrador_window"
)

define bibliotecaria = Character("Bibliotecária")
define recepcionista = Character("Recepcionista")
define august = Character("August")
define elizabeth = Character("Elizabeth")
define desconhecido = Character("???")

image protaF:
    "protaF.png"
    zoom 0.8
    xalign 0.2
    yalign 1

image protaM:
    "protaM.png"
    zoom 0.2
    xalign 0.2
    yalign 1.0
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

# Progresso da exploração da escola (rota Kiyoki)
default visitou_biblioteca = False
default visitou_armarios = False
default visitou_dormitorios = False

label start:
    scene black with fade_black
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
        p "{cps=30}{color=#FFFF00}Mal consigo abrir os olhos.{/color}{/cps}" #cama
        
        p "{cps=30}{color=#FFFF00}Minhas pálpebras pesam, e o cansaço parece grudado no meu corpo.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}Mas não é como se eu tivesse escolha.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}Minhas malas já estão prontas.{/color}{/cps}"
        
        p "{cps=30}{color=#FFFF00}Eu só preciso me arrumar… e ir pro aeroporto.{/color}{/cps}"
        
        scene black with fade
        pause 1.0
        scene bg fundo with fade
        
        
        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}Essa sou eu.{/color}{/cps}"# mostrar o espelho aqui, talvez?
        
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

        p "{cps=30}{color=#FFFF00}Mais especificamente em York , uma cidade da Prússia.{/color}{/cps}"
        
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
        p "{cps=30}{color=#FFFF00}O nome é Instituto Real de York .{/color}{/cps}"
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
        p "{cps=30}{color=#FFFF00}(som do ônibus freando){/color}{/cps}"
        p "{cps=30}{color=#FFFF00}…finalmente.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Que viagem exaustiva…{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}E olha que eu dormi quase o tempo todo.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Minhas costas ainda doem por causa daquela cadeira.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Mas tudo bem.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Valeu a pena.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Finalmente estou aqui.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}O Instituto Real de York {/color}{/cps}"
        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Então é isso.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}A partir daqui…{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}as coisas começam a mudar.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Eu entro na escola.{/color}{/cps}"

        p "{cps=30}{color=#FFFF00}Os portões já estão abertos e alguns alunos começam a chegar aos poucos.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Não são muitos.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Afinal, ainda é bem cedo.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Hoje não teremos aula.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Pelo menos não da forma tradicional.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}A escola nos entregou uma lista com tudo o que precisamos resolver antes do início do semestre.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Caramba.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Isso é muita coisa.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Ainda bem que cheguei cedo.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Se eu me organizar direitinho, talvez consiga terminar tudo antes do movimento aumentar.{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Agora...{/color}{/cps}"
        p "{cps=30}{color=#FFFF00}Por onde eu começo?{/color}{/cps}"

        label hub_exploracao:
            menu:
                "Escolher armários" if not visitou_armarios:
                    jump exploracao_armarios
                "Ir para a biblioteca" if not visitou_biblioteca:
                    jump exploracao_biblioteca
                "Ir para recepção dos dormitórios" if not visitou_dormitorios:
                    jump exploracao_dormitorios
                "Explorar Campus" if visitou_armarios and visitou_biblioteca and visitou_dormitorios:
                    jump exploracao_campus

    elif persistent.genero == "homem":
        $ nome_prota = "Kuroya Yagami"
        show protaM
        show screen day_locate("00", "Escola - Corredor")
        p "{cps=30}parte masculina{/cps}"
        
        p "{cps=30}a fala do personagem masculino é diferente{/cps}"
        
        p "{cps=30}ele tem que falar de forma diferente.{/cps}"
        
        p "{cps=30}de preferência na giria.{/cps}"
        
        p "{cps=30}desse naipe aí tá ligado{/cps}"

        # Escolha da rota inicial para homem
        menu:
            "Focar em Maya":
                jump rota_maya
            "Explorar a escola":
                jump rota_exploracao
            "Ir para a aula":
                jump rota_aula

    return

# Labels para rotas alternativas

label rota_pam:
    p "Escolhi focar em Pam."
    # Adicione o conteúdo da rota de Pam aqui
    return

label rota_maya:
    p "Escolhi focar em Maya."
    # Adicione o conteúdo da rota de Maya aqui
    return

label rota_exploracao:
    p "Decidi explorar a escola primeiro."
    # Adicione exploração aqui
    return

label rota_aula:
    p "Vou direto para a aula."
    # Adicione conteúdo da aula aqui
    return

label exploracao_biblioteca:
    $ visitou_biblioteca = True

    p "{cps=30}{color=#FFFF00}Assim que entro na biblioteca, fico parada por alguns segundos.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Ela é enorme.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Enorme não.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Gigantesca.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Meus olhos percorrem as estantes e parecem não encontrar um fim.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}É linda.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Simplesmente linda.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu definitivamente vou passar muitas horas aqui.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Bibliotecas sempre foram meu lugar favorito em qualquer escola.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Olha o tamanho dessas estantes...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Três andares inteiros de livros.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Três andares de pura magia.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Espera.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Estou me distraindo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}O cronograma.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Foi pra isso que eu vim.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Me aproximo do balcão principal, onde uma bibliotecária me recebe com um sorriso gentil.{/color}{/cps}"

    p "{cps=30}{color=#FFFF00}Olá.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu vim confirmar meu cronograma de aulas.{/color}{/cps}"
    bibliotecaria "Bom dia, minha jovem."
    bibliotecaria "Claro, vou lhe explicar como o sistema da escola funciona."
    bibliotecaria "Todos os alunos frequentam as aulas normais durante a manhã."
    bibliotecaria "A diferença está no período da tarde."
    bibliotecaria "Aqui, acreditamos que cada aluno deve dedicar parte do seu tempo a uma área de interesse específica."
    bibliotecaria "Por isso oferecemos três opções."
    bibliotecaria "A primeira é o período integral."
    bibliotecaria "Você terá aulas nos dois turnos."
    bibliotecaria "É a opção mais exigente, mas costuma ser escolhida por alunos que desejam seguir carreiras acadêmicas mais competitivas."
    bibliotecaria "A segunda é a trilha de informática."
    bibliotecaria "Todas as tardes são dedicadas à educação digital, programação e ciência da computação."
    bibliotecaria "E por último temos o programa de clubes."
    bibliotecaria "Nesse modelo, você participa de um dos clubes da escola às segundas, quartas e sextas."
    bibliotecaria "Já nas terças e quintas, o período é reservado para atividades físicas."
    bibliotecaria "Então..."
    bibliotecaria "Qual dessas opções mais combina com você?"

label escolha_periodo:
    menu:
        "Aulas acadêmicas em período Integral":
            p "{cps=30}{color=#FFFF00}Seria interessante mas muito exaustivo...{/color}{/cps}"
            jump escolha_periodo
        "Aulas de informática":
            p "{cps=30}{color=#FFFF00}Eu não me dou muito bem com a tecnologia...{/color}{/cps}"
            jump escolha_periodo
        "Clubes e atividades Físicas":
            p "{cps=30}{color=#FFFF00}Acho que os clubes são interessantes.{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}E as atividades físicas devem ajudar a manter minha saúde em dia.{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}Parece a escolha perfeita para mim.{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}Eu gostaria de participar dos clubes e atividades físicas!{/color}{/cps}"
            bibliotecaria "Uma ótima escolha, minha jovem."
            bibliotecaria "Atualmente a escola oferece quatro clubes."
            bibliotecaria "Temos o Clube de Literatura, que acontece aqui na biblioteca."
            bibliotecaria "O Clube de Debate, próximo à sala do grêmio."
            bibliotecaria "O Clube de Jornalismo e..."
            p "{cps=30}{color=#FFFF00}CLUBE DE JORNALISMO?!{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}Eu gritei.{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}Sem querer.{/color}{/cps}"
            bibliotecaria "Haha."
            bibliotecaria "Acho que já sei qual será a sua escolha."
            p "{cps=30}{color=#FFFF00}H-Haha...{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}Me desculpe.{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}Eu sinto meu rosto esquentar.{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}Que vergonha.{/color}{/cps}"
            bibliotecaria "Não se preocupe."
            bibliotecaria "Fico feliz em ver alguém tão animada."
            bibliotecaria "Aqui está seu cronograma impresso."
            bibliotecaria "Mas você também poderá consultá-lo pelo aplicativo da escola."
            bibliotecaria "E o Clube de Jornalismo fica neste mesmo corredor."
            bibliotecaria "Tenho certeza de que você encontrará facilmente."
            p "{cps=30}{color=#FFFF00}Muito obrigada!{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}Tenha um ótimo dia!{/color}{/cps}"

            p "{cps=30}{color=#FFFF00}Certo.{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}Uma tarefa concluída.{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}Agora...{/color}{/cps}"
            p "{cps=30}{color=#FFFF00}O que devo fazer?{/color}{/cps}"

    jump hub_exploracao

label exploracao_armarios:
    $ visitou_armarios = True

    p "{cps=30}{color=#FFFF00}Agora preciso escolher meus armários.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Tanto o do corredor quanto o do banheiro.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Acho melhor resolver isso antes da maioria dos alunos chegar.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Assim posso escolher um lugar bom sem precisar disputar espaço.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Começo a andar pelos corredores observando as fileiras de armários.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Hum...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Seria conveniente escolher um que fique mais ou menos na mesma distância de todas as salas.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Mas um armário próximo ao clube também evitaria atrasos.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Ugh.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}São opções demais.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Enquanto penso nisso, continuo caminhando distraidamente.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}THUMP{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Ai!{/color}{/cps}"
    desconhecido "Ei, garota!"
    desconhecido "Tome mais cuidado!"
    p "{cps=30}{color=#FFFF00}Acabei esbarrando em alguém.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Me perdoe, senhor!{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu estava distraída.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Ele estende a mão e me ajuda a levantar.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Seu uniforme chama minha atenção.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}É diferente dos outros funcionários da escola.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Tem algo quase militar nele.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Será que ele é um dos seguranças?{/color}{/cps}"
    august "August Pinochet, ao seu dispor."
    august "E tente prestar mais atenção por onde anda."
    august "Os corredores podem ser mais perigosos do que parecem."
    p "{cps=30}{color=#FFFF00}Me desculpe.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Não vai acontecer de novo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Você é um dos seguranças da escola?{/color}{/cps}"
    desconhecido "August!"
    desconhecido "Preciso da sua ajuda!"
    desconhecido "Rápido!"
    p "{cps=30}{color=#FFFF00}Um homem aparece correndo no corredor.{/color}{/cps}"
    august "(suspira)"
    august "Enfim."
    august "Tome mais cuidado, jovem."
    august "Agora, se me der licença, tenho trabalho a fazer."
    p "{cps=30}{color=#FFFF00}Ele se afasta junto do outro funcionário.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Estranho.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Aquele zelador parecia realmente preocupado.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Mas talvez eu esteja pensando demais.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Enfim.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Tenho armários para escolher.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Meus olhos percorrem o corredor mais uma vez.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Hum...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Aquele ao lado da biblioteca parece uma boa opção.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Caminho até ele.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Escolho o armário do meio.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Mas, no instante em que estendo a mão...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Alguém segura meu braço.{/color}{/cps}"
    desconhecido "Esse armário precisa ser meu."
    p "{cps=30}{color=#FFFF00}Eu me viro, assustada.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Desculpe... quem é você?{/color}{/cps}"
    desconhecido "A-ah!"
    desconhecido "Me perdoe pela grosseria."
    elizabeth "Meu nome é Elizabeth Montenegro."
    elizabeth "E eu realmente preciso desse armário."
    p "{cps=30}{color=#FFFF00}Posso perguntar o motivo?{/color}{/cps}"
    elizabeth "Bem..."
    elizabeth "Se você souber guardar segredo, acho que sim."
    p "{cps=30}{color=#FFFF00}Não vejo problema.{/color}{/cps}"
    elizabeth "O dono do armário 013 parece ser um antigo amigo de infância meu."
    elizabeth "Então eu gostaria de ficar com o 014."
    elizabeth "Faz sentido, não?"
    p "{cps=30}{color=#FFFF00}Ah...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Nesse caso, tudo bem.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu procuro outro.{/color}{/cps}"
    elizabeth "Haha."
    elizabeth "Muito obrigada pela compreensão, querida."
    p "{cps=30}{color=#FFFF00}Ela sorri.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Um sorriso educado.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Perfeito até demais.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Não foi nada.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu me afasto procurando outro armário.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Que garota estranha.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Ela foi gentil.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Educada.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Mas...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Não sei.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Tem alguma coisa nela que me deixa desconfortável.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Talvez seja a forma como fala.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Talvez seja aquele sorriso.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Ou talvez eu esteja apenas imaginando coisas.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Que feio, Kiyoki.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Você acabou de conhecê-la.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Não deveria sair julgando os outros assim.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Encontro outro armário vazio e finalmente decido ficar com ele.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Bem.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Acho que esse será meu companheiro pelos próximos anos.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Abro a porta e começo a guardar algumas coisas.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Nada demais.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Livros.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Cadernos.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Estojo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Notebook.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Tablet.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Só o necessário para as aulas.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Depois de organizar tudo, dou uma olhada para o armário.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Está muito sem graça.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Acabo colocando algumas pequenas decorações.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Um chaveiro.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Alguns enfeites discretos.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Coisas simples.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu gosto de deixar minhas coisas com um pouco da minha personalidade.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Mas sem exageros.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Sempre preferi algo mais minimalista.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Pronto.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Agora só falta escolher um armário no banheiro.{/color}{/cps}"

    p "{cps=30}{color=#FFFF00}Ai...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Sinceramente, achei uma péssima ideia a escola ter casas de banho coletivas em vez de banheiros nos dormitórios.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Pelo menos existem chuveiros individuais para quem prefere privacidade.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Tudo bem.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Nem sempre podemos ficar na nossa zona de conforto.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Vamos lá.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Me aproximo do bloco de banho feminino.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}O lugar é enorme.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Muito maior do que eu esperava.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Espera.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Ninguém escolheu um armário ainda?{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu realmente cheguei cedo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Hum...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Acho que vou ficar com o armário 041.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Ele fica próximo dos chuveiros.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}E...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}041 é meu número da sorte.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Era um número que aparecia em um desenho que eu assistia quando criança.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Desde então, acabei me apegando a ele.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Abro o armário.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Que legal.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}A escola oferece dois roupões.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Um rosa e um branco.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Que fofo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Organizo minhas toalhas e produtos de higiene cuidadosamente.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Tudo em seu devido lugar.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Esse eu não vou decorar.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}O calor e a umidade provavelmente estragariam qualquer adesivo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Além disso...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Não acho que armários de banheiro sejam exatamente o tipo de coisa que se decora.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Huh?{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Paro por um instante.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Alguém está cantando.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}A melodia ecoa pelos corredores do banheiro.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu conheço essa música.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Tenho quase certeza disso.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Por alguns segundos, penso em procurar de onde ela vem.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Mas...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Talvez seja melhor não incomodar.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}As garotas daqui ainda são completas desconhecidas para mim.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}E eu não quero parecer uma esquisita no meu primeiro dia.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Então.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Uma tarefa concluída.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}O que devo fazer agora?{/color}{/cps}"

    jump hub_exploracao


label exploracao_dormitorios:
    $ visitou_dormitorios = True

    show screen day_locate("00", "Recepção - Dormitórios")

    p "{cps=30}{color=#FFFF00}Ok.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Agora preciso resolver a questão dos dormitórios.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Provavelmente é a tarefa mais importante da lista.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Afinal...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}É onde vou dormir pelos próximos anos.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Caminho até a área indicada no mapa da escola.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Estranho.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Parece tão pequeno.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}É apenas uma recepção com duas portas.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Será que estou no lugar certo?{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Bem...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Só existe uma forma de descobrir.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Me aproximo do balcão.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Olá.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Vim fazer meu cadastro para o dormitório.{/color}{/cps}"
    recepcionista "Bom dia, flor do dia!"
    recepcionista "Antes de qualquer coisa, preciso que leia as regras e assine aqui embaixo."
    p "{cps=30}{color=#FFFF00}(Barulho de papel){/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Caramba.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}São muitas regras.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Meus olhos percorrem rapidamente as páginas.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Uma delas chama minha atenção.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Dormitórios mistos.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Outra.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Monitoramento por câmeras nas áreas comuns.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Confesso que isso me deixa um pouco desconfortável.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Mas considerando que os dormitórios não são separados por gênero...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Acho que faz sentido.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Ainda bem que existem áreas privadas para troca de roupa e higiene pessoal.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Posso fazer uma pergunta?{/color}{/cps}"
    recepcionista "Claro, querida."
    p "{cps=30}{color=#FFFF00}Por que os dormitórios são mistos?{/color}{/cps}"
    recepcionista "Ah."
    recepcionista "Essa pergunta aparece bastante."
    recepcionista "Antigamente os dormitórios eram separados."
    recepcionista "Mas a escola enfrentava muitos problemas de convivência."
    recepcionista "Bullying."
    recepcionista "Exclusão social."
    recepcionista "E até alunos que se sentiam isolados dos próprios amigos."
    recepcionista "Depois de muitos estudos e testes, decidimos mudar o sistema."
    recepcionista "Hoje os dormitórios são mistos, mas seguimos regras bem rígidas de segurança e privacidade."
    p "{cps=30}{color=#FFFF00}E funcionou?{/color}{/cps}"
    recepcionista "Melhor do que imaginávamos."
    recepcionista "A maioria dos alunos prefere o modelo atual."
    p "{cps=30}{color=#FFFF00}Interessante...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Bem, aqui está minha assinatura.{/color}{/cps}"
    recepcionista "Perfeito."
    recepcionista "Agora só preciso de um documento com foto."
    p "{cps=30}{color=#FFFF00}Claro.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Aqui está minha identidade.{/color}{/cps}"
    recepcionista "Kiyoki Kovalenko..."
    recepcionista "Só um instante."
    p "{cps=30}{color=#FFFF00}TEC TEC TEC{/color}{/cps}"
    recepcionista "Certo."
    recepcionista "Você ficará no dormitório B14."
    recepcionista "Prédio B, segundo andar."
    p "{cps=30}{color=#FFFF00}Prédio B!{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Espera.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Prédio B?{/color}{/cps}"
    recepcionista "Aqui está seu cartão de acesso."
    recepcionista "Seja bem-vinda."
    p "{cps=30}{color=#FFFF00}Muito obrigada!{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Pego o cartão e sigo até uma das portas atrás da recepção.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Ainda não entendo onde exatamente está esse tal Prédio B.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Mas imagino que vou descobrir em alguns segundos.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Aproximo a mão da maçaneta.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}E abro a porta.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}O quê?!{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Merda...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu acabo gritando alto demais sem perceber.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Quando saio pela porta...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu congelo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}O que eu achava ser apenas uma recepção pequena...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Na verdade é a entrada de um campus inteiro.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Prédios.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Muitos prédios.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Cinco blocos enormes, cada um com três andares.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Áreas de lazer.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Um mercado 24 horas.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Um parque interno.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Isso aqui não é uma escola.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}É uma cidade.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Caramba...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Isso é muito maior do que eu imaginava.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}E muito mais incrível também.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Certo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Sem tempo pra ficar parada.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Preciso encontrar o meu bloco.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Entro no Bloco B e pego o elevador.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Tudo aqui é moderno, mas tem um ar estranho de elegância antiga.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Quase como se fosse uma realeza disfarçada de escola.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Segundo andar.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Corredor.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Encontro a porta.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Meu dormitório.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Aproximo o cartão de acesso.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}BIP{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}A trava se destranca.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Respiro fundo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}E então...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu entro.{/color}{/cps}"

    show screen day_locate("00", "Dormitório B14")

    p "{cps=30}{color=#FFFF00}Uau!{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}É maior até do que o meu quarto!{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}É lindo!{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Parece que meu colega de quarto ainda não chegou.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Isso significa que eu posso escolher qual lado quero ficar.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Hehe.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Vou ficar com o lado esquerdo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Quando o sol nasce, a luz entra primeiro por esse lado.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu gosto de acordar sentindo os raios de sol no rosto.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Certo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Hora de decorar.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Começo arrumando minha cama.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Coloco meu cobertor favorito.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Algumas almofadas fofas.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}E logo acima da cabeceira penduro vários pôsteres.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eles não poderiam faltar.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Na mesa de estudos coloco tantas coisas que nem consigo listar tudo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Livros.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}iPad.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Notebook.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Porta-lápis.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Meu pegboard.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Tudo aquilo que costumo usar nos meus estudos.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}No guarda-roupa organizo minhas roupas como faço em casa.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Mas nas portas...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Ah, nas portas eu me divirto.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Coloco vários adesivos.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Também instalo alguns ganchos para pendurar minhas bolsas e minha mochila.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}E para finalizar...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Um tapete lindo ao lado da cama.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Caramba.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Ficou lindo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Guardo minha mala sobre o guarda-roupa e dou alguns passos para trás.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Observando tudo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Eu gosto de decorar os lugares onde vivo.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Gosto de deixar partes de mim espalhadas pelo ambiente.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Minha personalidade.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Meus gostos.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Minhas memórias.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}As pessoas podem olhar para esse quarto e perceber que eu estive aqui.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Mesmo quando eu não estiver.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}...{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}Acho que são essas pequenas coisas que fazem eu ser quem sou.{/color}{/cps}"
    p "{cps=30}{color=#FFFF00}O que devo fazer agora?{/color}{/cps}"

    jump hub_exploracao


label exploracao_campus:
    p "{cps=30}{color=#FFFF00}Hora de explorar o campus.{/color}{/cps}"
    # Adicione o conteúdo da exploração do campus aqui
    return


# Tela de escolha de gênero
transform hover_glow:
    on hover:
        linear 0.15 zoom 1.02
    on idle:
        linear 0.15 zoom 1.0

screen escolha_genero:
    modal True

    $ fundo_selecao = "images/fundo_selecao_en.png" if _preferences.language == "english" else "images/fundo_selecao_pt.png"
    add fundo_selecao xpos 0 ypos 0 xysize (1920, 1080)

    button:
        xpos 0 ypos 0 xysize (1920, 1080)
        action Return("homem")
        focus_mask True
        at hover_glow
        background None
        add "images/Kuroya_select.png" xysize (1920, 1080)

    button:
        xpos 0 ypos 0 xysize (1920, 1080)
        action Return("mulher")
        focus_mask True
        at hover_glow
        background None
        add "images/Kyioki_select.png" xysize (1920, 1080)
