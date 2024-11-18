def contadorDeCaracteresFrase(frase: str) -> dict:
    dicionarioCaracteres = {}
    for i in range(0, len(frase)):
        if frase[i] in dicionarioCaracteres:
            dicionarioCaracteres[frase[i]] = dicionarioCaracteres[frase[i]] + 1
        else:
            dicionarioCaracteres[frase[i]] = 1
    return dicionarioCaracteres


def main() -> None:
    frase = input('Digite uma frase: \n')
    print(contadorDeCaracteresFrase(frase))

main()
