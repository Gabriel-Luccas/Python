#COnfira se a uma palindromo
palavra = str(input("Iremos conferir se a palavra digitada é um Palíndromo: ")).strip().lower()
invertido = "".join(palavra)[::-1]
print(invertido)
if palavra == invertido:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
