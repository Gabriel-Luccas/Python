# def função que gera im dicionario com as notas de um aluno


def nota(*notas, sit=True):
    lista = notas
    geral = {}
    geral["total de provas "] = len(lista)
    geral["maior nota"] = max(lista)
    geral["menor nota"] = min(lista)
    nota_total = sum(lista)
    geral["media"] = f"{nota_total  / len(lista):.2f}"
    media_int = nota_total / len(lista)
    if sit == True:
        if media_int > 7:
            geral["situação"] = "Aprovado"
        elif media_int >= 5:
            geral["situação"] = "Mediano"
        elif media_int < 5:
            geral["situação"] = "Reprovado"
    return geral


bia = nota(5, 10, 10, sit=True)
print(bia)
