def calcularFatorial(numero: int) -> str:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial = (fatorial * i)

    return f'O Fatorial de {numero}! é {fatorial}'


def main() -> None:
    numero = int(input(f'Digite um número para saber o fatorial: \n'))

    return print(calcularFatorial(numero))

main()

