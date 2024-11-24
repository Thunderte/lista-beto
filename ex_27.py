import re

def main():
    texto = input("Digite um texto: ").lower()

    palavrasRegex = re.findall(r'\b\w+\b', texto)

    contador = {}
    for palavra in palavrasRegex:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1

    palavrasOrdenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    for palavra, freq in palavrasOrdenadas[:5]:
        if freq == 1:
            print(f"{palavra}: {freq} vez")
        elif freq > 1:
            print(f"{palavra}: {freq} vezes")

main()