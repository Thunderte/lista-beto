def verificadorDeMaioridade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

def main():
    idade = int(input("Digite a sua idade: \n"))

    print(verificadorDeMaioridade(idade))

main()