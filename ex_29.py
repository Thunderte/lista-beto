def deletarDuplicados(lista):
    return list(set(sublista) for sublista in lista)


def main():
    listaAninhada = [[1, 2, 3, 3], [4, 6, 5, 6], [7, 8, 7, 9]]

    return print(f'Sublista sem valores duplicados: {deletarDuplicados(listaAninhada)}')

main()