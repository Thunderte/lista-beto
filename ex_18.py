def somaDiagonaisMatrizQuadrada(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i] + matriz[i][len(matriz) - i - 1]
    return soma

def main():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(somaDiagonaisMatrizQuadrada(matriz))

main()