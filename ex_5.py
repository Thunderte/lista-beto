def tabuada(numero: int) -> None:
    for i in range(1, 10 + 1):
        numeroTabuada = (i * numero)
        print(f'{i} x {numero} = {numeroTabuada}')

def main():
    numero = int(input("Digite um número: \n"))

    tabuada(numero)

main()

