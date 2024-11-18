def inverteString(palavra):
    if not palavra:
        print("Error: você deve digitar uma palavra")
        exit()

    return palavra[::-1]

def main():
    palavra = input("Digite uma palavra: \n")

    print(f'A palavra invertida é: {inverteString(palavra)}')

main()