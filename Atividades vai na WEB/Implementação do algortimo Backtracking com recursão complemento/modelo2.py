import sys

# Definição do tabuleiro
tabuleiro = [
    [' ', 'X', ' ', ' '],
    [' ', 'X', ' ', 'X'],
    [' ', ' ', ' ', 'X'],
    ['*', 'X', ' ', ' ']
]

# Posições iniciais e destino
inicio = (3, 0)
destino = (0, 3)
melhor_caminho = None
menor_profundidade = sys.maxsize

direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Direita, Esquerda, Baixo, Cima

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('| ' + ' | '.join(linha) + ' |')
    print()

def movimento_valido(tabuleiro, linha, coluna):
    return 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]) and tabuleiro[linha][coluna] == ' '

def chegou_destino(linha, coluna):
    return (linha, coluna) == destino

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade, caminho):
    global melhor_caminho, menor_profundidade

    if chegou_destino(linha_atual, coluna_atual):
        if profundidade < menor_profundidade:
            menor_profundidade = profundidade
            melhor_caminho = caminho[:]
        return

    for direcao in direcoes:
        nova_linha = linha_atual + direcao[0]
        nova_coluna = coluna_atual + direcao[1]

        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            tabuleiro[nova_linha][nova_coluna] = '*'
            caminho.append((nova_linha, nova_coluna))

            proximo_movimento(tabuleiro, nova_linha, nova_coluna, profundidade + 1, caminho)

            caminho.pop()
            tabuleiro[nova_linha][nova_coluna] = ' '

def main():
    linha_inicio, coluna_inicio = inicio
    tabuleiro[linha_inicio][coluna_inicio] = '*'
    
    print("Tabuleiro inicial:")
    mostrar_tabuleiro(tabuleiro)

    proximo_movimento(tabuleiro, linha_inicio, coluna_inicio, 0, [inicio])

    if melhor_caminho:
        print("Melhor caminho encontrado:")
        for pos in melhor_caminho:
            tabuleiro[pos[0]][pos[1]] = '*'
        mostrar_tabuleiro(tabuleiro)
    else:
        print("Não há caminho possível até o destino.")

if __name__ == "__main__":
    main()
