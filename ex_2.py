def imparOuPar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'

def main():
    numero = int(input("Digite um número: "))
    print(f"O número {numero} é {imparOuPar(numero)}")

main()