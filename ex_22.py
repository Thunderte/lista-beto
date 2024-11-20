def vogaisEConsoantes(frase: str) -> str:
    vogais = "aeiouáéíóúâêôãõàAEIOUÁÉÍÓÚÂÊÔÃÕÀ"
    consoantes = "bcçdfghjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ"
    quantidadeVogais = 0
    quantidadeConsoantes = 0

    for letra in frase:
        if letra in vogais:
            quantidadeVogais = (quantidadeVogais + 1)
        elif letra in consoantes:
            quantidadeConsoantes = (quantidadeConsoantes + 1)
    return f"A frase informada contém {quantidadeVogais} vogais e {quantidadeConsoantes} consoantes"





print(vogaisEConsoantes("testando para ver se está funcionando"))