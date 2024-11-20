def removerElementosDuplicados(lista):
    novaLista = []
    for i in range(len(lista)):
        if lista[i] not in novaLista:
            novaLista.append(lista[i])
    return novaLista

def main():
    print(removerElementosDuplicados([1, 2, 3, 5, 6, 9, 2 , 3, 4]))

main()
