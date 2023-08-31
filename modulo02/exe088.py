import random

jogos = int(input("Número de listas geradas: "))
numeros_por_lista = 6
for _ in range(jogos):
    lista = []
    for _ in range(numeros_por_lista):
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
        else:
            num1 = random.randint(1, 60)
            list.append(num1)
    lista.sort()
    print(lista)
