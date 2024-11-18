def contarCaracteresEmUmaPalavra(palavra) -> int:
    if not palavra:
        print("Error: você deve digitar uma palavra")
        exit()

    return len(palavra)

def main():
    palavra = input("Digite uma palavra: \n")

    print(f'Essa palavra tem {contarCaracteresEmUmaPalavra(palavra)} caracteres')

main()
