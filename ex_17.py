from typing import List

def ordernarListaDeNumeros(lista: List[float]) -> List[float]:
    lista.sort()
    return lista

def main():
    listaDeNumeros: List[float] = [1, 5, 3, 2, 4, -2, -8, 0, 6]
    print(ordernarListaDeNumeros(listaDeNumeros))

main()
