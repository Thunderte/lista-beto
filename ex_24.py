def anagramas(palavra1: str, palavra2: str) -> bool:
    letrasIguais = 0
    if len(palavra1) != len(palavra2):
        return False
    for letra in palavra1:
        if letra in palavra2:
            letrasIguais = (letrasIguais + 1)
        elif letra not in palavra2:
            return False
    if(letrasIguais == len(palavra1)):
        return True
    
def main():
    palavra1 = str(input("Digite a primeira palavra: \n"))
    palavra2 = str(input("Digite a segunda palavra: \n"))

    verificandoAnagrama = anagramas(palavra1, palavra2)

    if verificandoAnagrama == True:
        return print(f"\nAs palavras {palavra1} e {palavra2} são anagramas")
        
    return print(f"\nAs palavras {palavra1} e {palavra2} não são anagramas")

main()