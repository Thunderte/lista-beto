def numerosPrimosEmUmIntervalo(inicio, fim):
    primos = []
    for numero in range(inicio, fim + 1):
        if numero > 1:
            for i in range(2, numero):
                if numero % i == 0:
                    break
            else:
                primos.append(numero)
    return primos

def main():
    inicio = int(input("Digite o início do intervalo: \n"))
    fim = int(input("Digite o fim do intervalo: \n"))

    print(f'Os números primos no intervalo de {inicio} a {fim} são: {numerosPrimosEmUmIntervalo(inicio, fim)}')

main()