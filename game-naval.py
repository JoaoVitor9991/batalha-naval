import random

ROWS = 10
COLS = 10

navios = {
    'P': (5, 1),
    'C': (4, 1),
    'T': (3, 2),
    'R': (2, 3)
}

def criar_tabuleiro():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def verificar_posicao(tabuleiro, linha, coluna, tamanho, orientacao):
    for i in range(tamanho):
        if orientacao == 'H' and (coluna + i >= COLS or tabuleiro[linha][coluna + i] != ' '):
            return False
        elif orientacao == 'V' and (linha + i >= ROWS or tabuleiro[linha + i][coluna] != ' '):
            return False
        elif orientacao == 'D' and (linha + i >= ROWS or coluna + i >= COLS or tabuleiro[linha + i][coluna + i] != ' '):
            return False
    return True

def colocar_navio(tabuleiro, linha, coluna, tamanho, orientacao, tipo_navio):
    for i in range(tamanho):
        if orientacao == 'H':
            tabuleiro[linha][coluna + i] = tipo_navio
        elif orientacao == 'V':
            tabuleiro[linha + i][coluna] = tipo_navio
        elif orientacao == 'D':
            tabuleiro[linha + i][coluna + i] = tipo_navio

def navios_nao_se_tocam(tabuleiro, linha, coluna, tamanho, orientacao):
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for i in range(tamanho):
        for d in direcoes:
            if orientacao == 'H' and (0 <= linha + d[0] < ROWS) and (0 <= coluna + i + d[1] < COLS):
                if tabuleiro[linha + d[0]][coluna + i + d[1]] != ' ':
                    return False
            elif orientacao == 'V' and (0 <= linha + i + d[0] < ROWS) and (0 <= coluna + d[1] < COLS):
                if tabuleiro[linha + i + d[0]][coluna + d[1]] != ' ':
                    return False
            elif orientacao == 'D' and (0 <= linha + i + d[0] < ROWS) and (0 <= coluna + i + d[1] < COLS):
                if tabuleiro[linha + i + d[0]][coluna + i + d[1]] != ' ':
                    return False
    return True

def posicionar_navios(tabuleiro):
    for tipo_navio, (tamanho, quantidade) in navios.items():
        for _ in range(quantidade):
            colocado = False
            while not colocado:
                orientacao = random.choice(['H', 'V', 'D'])
                linha = random.randint(0, ROWS - 1)
                coluna = random.randint(0, COLS - 1)
                if verificar_posicao(tabuleiro, linha, coluna, tamanho, orientacao) and navios_nao_se_tocam(tabuleiro, linha, coluna, tamanho, orientacao):
                    colocar_navio(tabuleiro, linha, coluna, tamanho, orientacao, tipo_navio)
                    colocado = True

def mostrar_tabuleiro(tabuleiro, acertos):
    for i, row in enumerate(tabuleiro):
        for j, cell in enumerate(row):
            if (i, j) in acertos:
                print(cell, end=' ')
            elif cell == 'X':
                print('X', end=' ')
            else:
                print('~', end=' ')
        print()

def jogar():
    tabuleiro = criar_tabuleiro()
    posicionar_navios(tabuleiro)
    vidas = 5
    acertos_consecutivos = 0
    acertos = set()

    while vidas > 0:
        mostrar_tabuleiro(tabuleiro, acertos)
        try:
            linha = int(input('Digite a linha do tiro (0-9): '))
            coluna = int(input('Digite a coluna do tiro (0-9): '))
            if linha < 0 or linha >= ROWS or coluna < 0 or coluna >= COLS:
                print('Entrada inválida, tente novamente.')
                continue
        except ValueError:
            print('Entrada inválida, tente novamente.')
            continue

        if tabuleiro[linha][coluna] in 'PCTR':
            tipo_navio = tabuleiro[linha][coluna]
            print(f'Você atingiu um {tipo_navio} na posição (Linha: {linha}, Coluna: {coluna})!')
            acertos_consecutivos += 1
            acertos.add((linha, coluna))  # Adiciona a posição ao conjunto de acertos
            if acertos_consecutivos == 3:
                vidas += 1
                acertos_consecutivos = 0
                print('Você ganhou uma vida!')
        else:
            print('Tiro na água.')
            vidas -= 1
            acertos_consecutivos = 0
            tabuleiro[linha][coluna] = 'X'  # Marca o tiro na água com 'X'

        if all(cell == 'X' or cell == ' ' for row in tabuleiro for cell in row):
            print('Você venceu!')
            mostrar_tabuleiro(tabuleiro, set((i, j) for i in range(ROWS) for j in range(COLS)))  # Revela todo o tabuleiro
            break

    if vidas == 0:
        print('Você perdeu.')
        mostrar_tabuleiro(tabuleiro, set((i, j) for i in range(ROWS) for j in range(COLS)))  # Revela todo o tabuleiro

if __name__ == "__main__":
    jogar()