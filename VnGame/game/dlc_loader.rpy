# dlc_loader.rpy
# ================
#
# ESSENCIAL ENTENDER O PAPEL DESTE ARQUIVO:
# O jogo Ren'Py NAO descriptografa nada. NAO guarda chave nenhuma. NAO fala
# com o Discord. NAO decide quem tem DLC. Toda essa responsabilidade fica
# no LAUNCHER (fora do Ren'Py) e no BACKEND.
#
# Por que? Porque codigo .rpy e compilado para .rpyc, que e trivialmente
# decompilavel (unrpyc e publico). Qualquer verificacao de "if tem_dlc:"
# escrita aqui pode ser encontrada e apagada por um usuario com um pouco de
# conhecimento. Colocar a decisao de autorizacao aqui seria exatamente o
# erro que este projeto quer evitar.
#
# O QUE ESTE ARQUIVO REALMENTE FAZ:
# Le uma variavel de ambiente que o LAUNCHER configura ANTES de iniciar o
# processo do Ren'Py, contendo o(s) caminho(s) de pastas temporarias onde
# o launcher ja descriptografou (em disco, numa pasta de sessao efemera)
# o conteudo das DLCs que aquele usuario JA FOI AUTORIZADO A TER, checado
# no backend poucos segundos antes.
#
# O Ren'Py so "enxerga" o conteudo que fisicamente existe nessas pastas.
# Se o usuario nao foi autorizado, o launcher nunca descriptografa nada,
# a pasta nunca existe, e o Ren'Py simplesmente nao tem os arquivos da
# DLC para carregar -- nao existe "flag" para forcar True, porque nao ha
# flag nenhuma: ou o arquivo esta la, decifrado, ou nao esta.

init -999 python:
    import os

    # LIMERENCE_DLC_PATHS: lista de diretorios separados por os.pathsep,
    # definida pelo launcher no ambiente do processo filho (Ren'Py) antes
    # de inicia-lo. Cada diretorio contem o conteudo JA DESCRIPTOGRAFADO
    # de uma DLC autorizada (script .rpyc, imagens, audio daquela DLC).
    _dlc_paths_raw = os.environ.get("LIMERENCE_DLC_PATHS", "")

    _loaded_dlcs = []

    if _dlc_paths_raw:
        for _path in _dlc_paths_raw.split(os.pathsep):
            _path = _path.strip()
            if not _path:
                continue
            if not os.path.isdir(_path):
                # Pasta anunciada pelo launcher mas nao existe de verdade:
                # ignora silenciosamente. Isso NAO e uma falha de seguranca
                # -- e so o caso normal de "launcher disse que ia preparar
                # mas por algum motivo (erro de rede, etc) nao preparou".
                continue

            # Isto e o unico "gancho" real: adiciona a pasta decifrada ao
            # searchpath do Ren'Py, para que os arquivos .rpyc/imagens/audio
            # dentro dela sejam carregados como se fizessem parte do jogo.
            renpy.config.searchpath.append(_path)
            _loaded_dlcs.append(os.path.basename(_path))

    # Disponibiliza para o resto do jogo saber quais DLCs foram carregadas
    # NESTA sessao -- util so para UI ("Capitulo Extra disponivel!"), nunca
    # para decidir autorizacao (autorizacao ja aconteceu antes, no backend
    # + launcher; a esta altura so estamos refletindo o que ja foi decidido).
    store.limerence_loaded_dlcs = _loaded_dlcs


# Label opcional de diagnostico -- ajuda a debugar em desenvolvimento.
# Chame com `call show_loaded_dlcs` de um script de debug se precisar.
label show_loaded_dlcs:
    python:
        _msg = "DLCs carregadas nesta sessao: %r" % (limerence_loaded_dlcs,)
    "[_msg]"
    return
