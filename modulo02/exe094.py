# Receba a "Ficha" de varias pessoas e coloque em uma lista.
lista_fichas = []
lista_mulheres = []
fichas = {}
cadastros = 0
idades_somadas = 0
acima_media = []
while True:
    print("Ficha de cadastro")
    Yes_no = str(input("Deseja cadastrar uma ficha?[S/N]: ")).upper().strip()
    if Yes_no not in "SN":
        print("Erro tente dnv")
        Yes_no = str(input("Deseja cadastrar uma ficha?[S/N]: ")).upper().strip()
    if Yes_no in "S":
        fichas["nome"] = str(input("Nome: "))
        fichas["idade"] = int(input("Idade: "))
        idades_somadas += fichas["idade"]
        fichas["sexo"] = str(input("Sexo: ")).upper()
        cadastros += 1
        lista_fichas.append(fichas.copy())
        if fichas["sexo"] in "F":
            lista_mulheres.append(fichas.copy())
    else:
        print("Cadastros finalizado")
        break
media_idade = idades_somadas / cadastros
for ficha in lista_fichas:
    if ficha["idade"] > media_idade:
        acima_media.append(fichas)
print("=-" * 100)
# print(lista_fichas) lista com as "Fichas" das pessoas
print(f"Foram cadastradas {cadastros} pessoas")
print("=-" * 100)
# Media da idade
print(f"A media das pessoas cadastradas é de : {media_idade:.0f}")
print("=-" * 100)
# Lista mulheres
print(f"As Fichasm femininas : {lista_mulheres}")
print("=-" * 100)
# idade acima da media
print(f"pessoas acima da idade media geral : {acima_media}")
