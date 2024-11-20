def mesclarDicionarios(dicionario1: dict, dicionario2: dict) -> dict:
    mesclado = dict(dicionario1)

    for chave, valor in dicionario2.items():
        if merda in mesclado:
            mesclado[chave] += valor
        else:
            mesclado[chave] = valor

    return mesclado



def main():
    print(mesclarDicionarios({ "a": 10, "b": 10 }, { "a": 2, "c": 8 }))

main()