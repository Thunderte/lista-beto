from typing import List

def mediaNotasListaAluno(listaNotas: None) -> None:
    somaNotas: float = 0
    mediaNotas: float = 0
    notasAcimaDaMedia: None = []
    for i in range(0, len(listaNotas)):
        somaNotas = (somaNotas + listaNotas[i])
    mediaNotas = (somaNotas / len(listaNotas))
    for i in range(0, len(listaNotas)):
        if listaNotas[i] > mediaNotas:
            notasAcimaDaMedia.append(listaNotas[i])
    return print(f'A média das notas do aluno informado é {mediaNotas} e as notas acimas da média são {notasAcimaDaMedia}')

def main():
    portugues: float = float(input('Digite a nota que o aluno tirou em português: \n'))
    ingles: float = float(input('Digite a nota que o aluno tirou em inglês: \n'))
    matematica: float = float(input('Digite a nota que o aluno tirou em matemática: \n'))
    espanhol: float = float(input('Digite a nota que o aluno tirou em espanhol: \n'))

    notas: List[float] = [portugues, ingles, matematica, espanhol]
    mediaNotasListaAluno(notas)

main()