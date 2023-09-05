# Criei a função max()

maior_lista = 0


def linha():
    print("=" * 50)


def maior(*numeros):
    global maior_lista
    for num in numeros:
        if num > maior_lista:
            maior_lista = num


lista_numeros = []
valores_informados = len(lista_numeros)
while True:
    Yes_no = str(input("Adicionar Numeros a lista[S/N]: ")).upper()
    if Yes_no in "S":
        add_number = int(input("Adicionar numero: "))
        lista_numeros.append(add_number)
    else:
        break

valores_informados = len(lista_numeros)
maior(*lista_numeros)
linha()
print(f"O maior valor informado dos {valores_informados} valores  foi de {maior_lista}")
linha()
