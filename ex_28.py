def verificadorDeSudoku(quadro):
    # Função para verificar se uma lista contém números únicos de 1 a 9 (sem duplicatas)
    def verificadorDeGrupo(grupo):
        numeros = [num for num in grupo if num != '.']  # Ignorar células vazias ('.')
        return len(numeros) == len(set(numeros))  # Verifica se todos os números são únicos
    
    for row in quadro:
        if not verificadorDeGrupo(row):
            return False

    for col in range(9):
        if not verificadorDeGrupo([quadro[row][col] for row in range(9)]):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [
                quadro[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            ]
            if not verificadorDeGrupo(box):
                return False

    return True


def main():
    # Exemplo de tabuleiro de Sudoku
    exemploQuadro = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]

    if verificadorDeSudoku(exemploQuadro):
        print("O tabuleiro de Sudoku é válido!")
    else:
        print("O tabuleiro de Sudoku NÃO é válido!")

main()