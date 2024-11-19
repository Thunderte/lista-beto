def soma(numero1: float, numero2: float) -> float:
    return (numero1 + numero2)

def subtracao(numero1: float, numero2: float) -> float:
    return (numero1 - numero2)

def divisao(numero1: float, numero2: float) -> float:
    return (numero1 / numero2)

def multiplicacao(numero1: float, numero2: float) -> float:
    return (numero1 * numero2)

def main():
    print('-------------------- CALCULADORA -------------------- \n')
    print('Seja bem-vindo a calculadora, temos alguns sistemas de calculos, você deve escolher um entre:\n')
    print(' 1 - SOMA \n 2 - SUBTRAÇÃO \n 3 - DIVISÃO \n 4 - MULTIPLICAÇÃO \n')
    operacao = int(input("Qual operação você deseja fazer? \n"))

    if operacao == 1:
        numero1 = float(input("Digite o valor do primeiro número: \n"))
        numero2 = float(input("Digite o valor do segundo número: \n"))

        som = soma(numero1, numero2)

        return print(f"O resultado da soma é {som}")
    elif operacao == 2:
        numero1 = float(input("Digite o valor do primeiro número: \n"))
        numero2 = float(input("Digite o valor do segundo número: \n"))

        sub = subtracao(numero1, numero2)

        return print(f"O resultado da subtração é {sub}")
    elif operacao == 3:
        numero1 = float(input("Digite o valor do primeiro número: \n"))
        numero2 = float(input("Digite o valor do segundo número: \n"))

        div = divisao(numero1, numero2)

        return print(f"O resultado da subtração é {div}")
    elif operacao == 4:
        numero1 = float(input("Digite o valor do primeiro número: \n"))
        numero2 = float(input("Digite o valor do segundo número: \n"))

        multi = multiplicacao(numero1, numero2)

        return print(f"O resultado da multiplicação é {multi}")
    else:
        return print("\n Error: Operação desconhecida")
main()
