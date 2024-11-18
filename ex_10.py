def calcularAreaDeUmRetangulo(base, altura):
    return (base * altura) / 2

def main():
    base = int(input("Digite a base do retângulo: \n"))
    altura = int(input("Digite a altura do retângulo: \n"))

    print(f'A área do retângulo é: {calcularAreaDeUmRetangulo(base, altura)}')

main()