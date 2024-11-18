def calcularMediaAritNotas(nota1: float, nota2: float, nota3: float) -> float:
    if not nota1:
        print("Error: Digite a primeira nota")
    elif not nota2:
        print("Error: Digite a segunda nota")
    elif not nota3:
        print("Error: Digite a terceira nota")
    
    somaNotas = (nota1 + nota2 + nota3)
    mediaAritNotas = (somaNotas / 3)

    return mediaAritNotas

def main():
    nota1 = float(input("Digite a primeira nota: \n"))
    nota2 = float(input("Digite a segunda nota: \n"))
    nota3 = float(input("Digite a terceira nota: \n"))

    print(f'A média aritmética das notas é: {calcularMediaAritNotas(nota1, nota2, nota3)}')

main()

