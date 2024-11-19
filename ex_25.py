from typing import List
def filtroNumerosPares(lista: List[int]) -> List[int]:
    numerosPares = []
    for numero in range(len(lista)):
        if lista[numero] % 2 == 0 and lista[numero] != 0:
            numerosPares.append(lista[numero])

    return numerosPares

def main():
    return print(filtroNumerosPares([0, 1, 3, 5, 2, 4, 6, 8, 12, 14]))

main()