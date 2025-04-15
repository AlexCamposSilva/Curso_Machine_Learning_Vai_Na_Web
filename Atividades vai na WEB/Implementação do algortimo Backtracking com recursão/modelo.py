# Função para mostrar o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
    print()

# Função para verificar se o movimento é válido
def movimento_valido(tabuleiro, linha, coluna):
    return (0 <= linha < len(tabuleiro) and
            0 <= coluna < len(tabuleiro[0]) and
            tabuleiro[linha][coluna] == ' ')

# Função de Backtracking para encontrar o melhor caminho
def backtracking(tabuleiro, linha, coluna, destino):
    if (linha, coluna) == destino:
        return True  # Chegou ao destino
    
    direcoes = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # Direções: direita, esquerda, cima, baixo

    for direcao in direcoes:
        nova_linha = linha + direcao[0]
        nova_coluna = coluna + direcao[1]

        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            # Marca a posição como visitada
            tabuleiro[nova_linha][nova_coluna] = '*'
            
            if backtracking(tabuleiro, nova_linha, nova_coluna, destino):
                return True  # Caminho encontrado
            
            # Desmarca a posição caso não funcione
            tabuleiro[nova_linha][nova_coluna] = ' '
    
    return False

# Função principal
def main():
    tabuleiro = [
        [' ', ' ', ' ', 'X'],
        ['X', 'X', ' ', 'X'],
        [' ', ' ', ' ', ' '],
        ['*', 'X', 'X', ' ']
    ]

    linha_inicial, coluna_inicial = 3, 0
    destino = (0, 3)

    mostrar_tabuleiro(tabuleiro)
    
    if backtracking(tabuleiro, linha_inicial, coluna_inicial, destino):
        print("Caminho encontrado:")
        mostrar_tabuleiro(tabuleiro)
    else:
        print("Não foi possível encontrar um caminho.")

# Executa o programa
main()
