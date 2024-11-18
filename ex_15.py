import random

def jogoAdvinhacao(nivelDeJogo: int):
    numeroInicial: int = 1
    numeroLimite: int = 100
    numeroDeTentativas = 0

    numeroSorteado = random.randint(1, 100) 

    if numeroSorteado and numeroSorteado >= numeroInicial and numeroSorteado <= numeroLimite:
        if nivelDeJogo == 1:
            for i in range(0, 10):
               numeroDeTentativas = numeroDeTentativas + 1
               tentativa: int = int(input(f'Você tem 10 tentativas\nTentativa {numeroDeTentativas} \n Digite um número de 0 a 100 e eu digo se você acertou: \n'))

               if tentativa == numeroSorteado:
                return f'Parabéns, você acertou o número sorteado que é {numeroSorteado} na {numeroDeTentativas} tentativa no modo de dificuldade fácil\nObrigado por jogar'

        elif nivelDeJogo == 2:
              for i in range(0, 5):
               numeroDeTentativas = numeroDeTentativas + 1
               tentativa: int = int(input(f'Você tem 5 tentativas\nTentativa {numeroDeTentativas} \n Digite um número de 0 a 100 e eu digo se você acertou: \n'))

               if tentativa == numeroSorteado:
                return f'Parabéns, você acertou o número sorteado que é {numeroSorteado} na {numeroDeTentativas} tentativa no modo de dificuldade médio\nObrigado por jogar'

        elif nivelDeJogo == 3:
              for i in range(0, 3):
               numeroDeTentativas = numeroDeTentativas + 1
               tentativa: int = int(input(f'Você tem 3 tentativas\nTentativa {numeroDeTentativas} \n Digite um número de 0 a 100 e eu digo se você acertou: \n'))

               if tentativa == numeroSorteado:
                return f'Parabéns, você acertou o número sorteado que é {numeroSorteado} na {numeroDeTentativas} tentativa no modo de dificuldade médio\nObrigado por jogar'

        return f'Você perdeu o jogo, reinicie e tente novamente'


def main() -> None:
    print('--------------------------- JOGO DA ADVINHAÇÃO ---------------------------')
    print('\n')
    print('Bem vindo ao jogo da advinhação, o jogo funcina da seguinte forma, eu vou sortear um numero de 1 a 100 e você tem que tentar advinhar')
    print('\n')
    print('--------------------------- DIFICULDADE ---------------------------')
    print('Para começar escolha uma dificuldade\n Temos a\n 1 - FÁCIL\n 2 - MÉDIO\n 3 - DIFICIL')
    dificuldade = int(input())
    print('\n')

    if dificuldade != 1 and dificuldade != 2 and dificuldade != 3:
        print('Error: Selecione um nivel de dificuldade de 1 a 3')
        return exit

    return print(jogoAdvinhacao(dificuldade))

main()

