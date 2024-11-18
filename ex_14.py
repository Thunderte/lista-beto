def verificaPalindromo(palavra: str) -> str:
    palavraAntiga = palavra
    palavraInvertida = palavra[::-1]

    if palavraAntiga == palavraInvertida:
        return f'A palavra {palavraAntiga} é um palíndromo'

    return f'A palavra {palavraAntiga} não é um palíndromo'

def main() -> None:
    palavra = str(input('Digite uma palavra para saber se é um palíndromo: \n'))

    return print(verificaPalindromo(palavra))

main()