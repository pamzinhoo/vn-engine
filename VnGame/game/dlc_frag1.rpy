# dlc_frag1.rpy
# =============
#
# Fragmento I -- "Génesis". Conteudo da primeira carta de DLC (ver
# dlc_fragmentos em script.rpy e a screen dlc_carta_meio_conteudo).
#
# Fica em arquivo proprio, e nao no script.rpy, porque a intencao e' que
# fragmentos possam migrar pra pasta cifrada que o launcher descriptografa
# em tempo de execucao (ver dlc_loader.rpy). Um fragmento por arquivo torna
# essa mudanca um "mover arquivo", sem cirurgia no roteiro principal.

# Elenco exclusivo deste fragmento. bibliotecaria e august ja existem no
# script.rpy e sao reaproveitados como estao.
define zatsko = Character("Zatsko", what_slow_cps=30, ctc="ctc", ctc_position="nestled")
define edgar = Character("Edgar", what_slow_cps=30, ctc="ctc", ctc_position="nestled")
define flora = Character("Flora", what_slow_cps=30, ctc="ctc", ctc_position="nestled")
define enfermeira = Character(_("Enfermeira"), what_slow_cps=30, ctc="ctc", ctc_position="nestled")


# ============================================================================
# DLC #1 -- "I Génesis" (Fragmento I)
#
# Roteiro do fragmento mostrado na carta do meio da selecao de rota (ver
# dlc_fragmentos e screen dlc_carta_meio_conteudo). POV do Zatsko, fora da
# linha do tempo das duas rotas principais -- por isso nao toca em nenhuma
# variavel de progresso e volta pra selecao ao terminar.
#
# Sem "scene"/"show" de fundo de proposito: o documento do roteiro nao traz
# indicacao de cenario e a DLC ainda nao tem arte alem da carta, entao a cena
# roda em tela preta. Quando os cenarios chegarem, e' so intercalar aqui.
# ============================================================================
label dlc_frag1_genesis:
    scene black with dissolve
    show screen horario(_("04:30 da manhã.")) with dissolve
    pause 2.0
    hide screen horario with dissolve

    n "..."
    n "O despertador toca."
    zatsko "Hmm..."
    n "Olho em volta."
    n "Só vejo o Edgar dormindo na cama ao lado."
    n "Ugh..."
    n "Cadê..."
    n "Cadê o August?"
    n "?!"
    n "Me levanto rapidamente."
    n "Merda!"
    n "Ele dormiu no quarto de alguma funcionária de novo!"
    n "Esse lazarento ainda vai ser demitido!"
    n "Me visto rapidamente e saio correndo."
    n "Procurando pela escola onde ele deve estar."
    n "Procuro nos dormitórios das funcionárias."
    n "TOC TOC"
    bibliotecaria "Uh? Zatsko? Tem ideia de que horas são?"
    zatsko "M-Me perdoe, senhora Odette..."
    zatsko "Por acaso o August está aí dentro?"
    bibliotecaria "August?"
    n "Ela olha para trás."
    bibliotecaria "Ele não está aqui, mas..."
    bibliotecaria "Agora que você mencionou, também não vejo a Flor."
    zatsko "A senhora Flora?"
    bibliotecaria "Ela mesma. Por quê?"
    zatsko "Ah, eles devem só..."
    zatsko "Ter começado o serviço mais cedo, haha."
    zatsko "Obrigado, senhorita Odette."
    zatsko "Desculpe perturbar seu sono."
    bibliotecaria "Tudo bem, meu lindo. Irei voltar a dormir. Bom serviço, viu?"
    n "Ela fecha a porta."
    n "..."
    n "EU VOU MATAR ESSES DOIS!"
    n "Já tenho até ideia de onde eles estão."
    n "..."
    n "Abro a porta gentilmente."
    zatsko "Ah, sabia..."
    zatsko "No armário do zelador. Que bonito, hein?"
    zatsko "Se o Rentaro pega vocês dormindo no armário dele, ele faz vocês de esfregão."
    august "Bocejo"
    august "Zatsko, meu lindão! Bom dia!"
    august "Olha, seu cabelo está mais brilhoso hoje..."
    zatsko "Me poupe. Levantem e vamos ao trabalho!"
    zatsko "Os alunos chegam hoje."
    august "HOJE?! Ugh..."
    august "Mas relaxa, eu dormi de uniforme limpo pra acordar sem pressa."
    zatsko "Ugh, que nojo..."
    august "Ah, vai. Cinco horinhas de sono não sujam roupa nenhuma..."
    n "THUD"
    zatsko "Não suja roupa, mas mata um."
    flora "Ugh, me desculpe, Zatsko..."
    flora "Eu nem percebi quando isso aconteceu..."
    flora "Esse loiro sabe como mexer comigo."
    zatsko "Tudo bem, senhorita."
    zatsko "De qualquer forma, não posso dar ordens a você..."
    zatsko "Você é quem é a superiora aqui."
    flora "Ugh..."
    flora "Eu não estou me sentindo bem..."
    flora "Não sei se consigo trabalhar hoje."
    zatsko "O que está sentindo?"
    zatsko "Se estiver muito cansada, podemos te chamar quando os alunos chegarem."
    flora "Não, eu realmente estou passando mal..."
    zatsko "Venha, eu vou te levar para a enfermaria..."
    n "Pego meu walkie-talkie."
    zatsko "Edgar, já acordou?"
    edgar "Já, sim, ué."
    edgar "Tá achando que eu sou o August e acordo meio-dia?"
    zatsko "Pois é..."
    zatsko "No armário do zelador, caído no chão."
    zatsko "Deixo isso pra você."
    edgar "Pode deixar."
    n "Com isso, levo a superiora para a enfermaria."
    n "Ela realmente estava muito mal."
    n "Sua pele estava gelada..."
    n "E horas se passaram desde que eu estava na frente da enfermaria."
    n "Os alunos já estavam na escola."
    n "Depois de cinco horas esperando..."
    n "Finalmente tenho um retorno."
    enfermeira "Zatsko, pode entrar."
    zatsko "Obrigado."
    n "..."
    zatsko "E então? O que houve?"
    enfermeira "Ela está descansando agora."
    enfermeira "A partir de amanhã, ela terá que deixar o trabalho pesado para vocês..."
    zatsko "Ela está bem? Está machucada?!"
    zatsko "Por quanto tempo ela vai precisar desse descanso?"
    enfermeira "Por 9 meses!"
    zatsko "O que...?"
    zatsko "Ela está tão machucada assim?"
    enfermeira "Parabéns, papai!"
    zatsko "O QUÊ?!"
    zatsko "Eu... Eu não sou o..."
    n "Eu repenso antes de responder."
    n "..."
    zatsko "O-Obrigado, haha..."
    zatsko "Será que o diretor vai ficar bravo?"
    enfermeira "Você sabe melhor do que ninguém que ele admira muito a maternidade."
    enfermeira "Não se preocupe. Ela e o bebê estarão em boas mãos."
    n "..."
    n "…"

    scene black with dissolve

    # Fim do fragmento: volta pro menu principal. full_restart limpa a pilha
    # de call e o estado da sessao -- o jogador nao estava numa partida, so
    # assistiu a DLC a partir da tela de selecao de rota, entao nao ha
    # progresso pra preservar. O "return" abaixo nunca chega a rodar
    # (full_restart levanta excecao); fica so pra fechar o label direito.
    $ renpy.full_restart()
    return
