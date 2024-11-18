def palavrasUnicasNaFrase(frase):
    palavras = frase.split()
    palavrasUnicas = []

    for palavra in palavras:
        if palavras.count(palavra) == 1:
            palavrasUnicas.append(palavra)

    return len(palavrasUnicas)

def main():
    frase = input("Digite uma frase: \n")

    print(f'A frase tem {palavrasUnicasNaFrase(frase)} palavras únicas')

main()