palavra = str(input("Iremos conferir se a palavra digitada é um Palíndromo: ")).strip().lower()
invertido = palavra[::-1]
if palavra == invertido:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
