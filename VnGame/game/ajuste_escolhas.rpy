# Ajuste automatico do tamanho da fonte nas escolhas.
#
# O fundo do botao de escolha tem 760px, mas a moldura desenhada ocupa as
# bordas: a area util no meio e de cerca de 650px. Legendas longas — que
# aparecem sobretudo depois de traduzidas, porque o mesmo texto muda de
# tamanho em cada idioma — passavam por cima da moldura.
#
# A funcao abaixo mede a legenda com as larguras reais da Montserrat e so
# reduz a fonte quando ela nao caberia. Escolhas curtas ficam no tamanho
# padrao, sem diferenca visual entre uma opcao e outra do mesmo menu.

init python:

    # Largura de cada caractere na Montserrat, medida em tamanho 100.
    LARGURAS_MONTSERRAT = {' ': 25, '!': 24.2, '"': 33.4, "'": 18.4, '(': 31.1, ')': 31.1, ',': 18.2, '-': 38, '.': 18.2, '0': 65.2, '1': 34.2, '2': 55.5, '3': 54.8, '4': 64.4, '5': 54.8, '6': 59.2, '7': 57, '8': 62.4, '9': 59.2, ':': 18.2, ';': 18.2, '?': 55.4, 'A': 68.8, 'B': 74.8, 'C': 70.1, 'D': 82.6, 'E': 66.8, 'F': 62.9, 'G': 77.4, 'H': 81.6, 'I': 28.6, 'J': 47.7, 'K': 69.3, 'L': 58, 'M': 95.6, 'N': 81.6, 'O': 83.6, 'P': 71, 'Q': 83.6, 'R': 71.6, 'S': 60.1, 'T': 54.8, 'U': 79.4, 'V': 67, 'W': 108, 'X': 62.1, 'Y': 61, 'Z': 63.9, 'a': 57.4, 'b': 67.1, 'c': 54.5, 'd': 67.1, 'e': 58.7, 'f': 31.1, 'g': 67.7, 'h': 66.8, 'i': 25, 'j': 25.5, 'k': 56.2, 'l': 25, 'm': 106.8, 'n': 66.8, 'o': 61, 'p': 67.1, 'q': 67.1, 'r': 38.3, 's': 46.3, 't': 38.8, 'u': 66.4, 'v': 50.8, 'w': 83.8, 'x': 49.8, 'y': 50.8, 'z': 49.1, '¡': 24.2, '¿': 55.4, 'á': 57.4, 'ã': 57.4, 'ç': 54.5, 'é': 58.7, 'ê': 58.7, 'í': 25, 'ñ': 66.8, 'ó': 61, '—': 100, '“': 31.2, '”': 31.2, '…': 55.6}

    # Usada para qualquer caractere fora da tabela (acentos raros, simbolos).
    LARGURA_CARACTERE_PADRAO = 56

    # Area livre dentro da moldura do botao de escolha.
    ESCOLHA_LARGURA_UTIL = 650

    def escolha_largura(legenda, tamanho):
        """Largura aproximada da legenda, em pixels, no tamanho de fonte dado."""
        import re
        limpo = re.sub(r"\{[^}]*\}", "", legenda)
        total = sum(LARGURAS_MONTSERRAT.get(c, LARGURA_CARACTERE_PADRAO) for c in limpo)
        return total * tamanho / 100.0

    def escolha_tamanho(legenda):
        """Tamanho de fonte para uma escolha: o padrao quando cabe, menor quando nao."""
        base = gui.choice_button_text_size
        largura = escolha_largura(legenda, base)
        if largura <= ESCOLHA_LARGURA_UTIL:
            return base
        return max(18, int(base * ESCOLHA_LARGURA_UTIL / largura))
