import random

jogos = int(input("Número de listas geradas: "))
numeros_por_lista = 6
for _ in range(jogos):
    lista = []
    for _ in range(numeros_por_lista):
        lista.append(random.randint(1, 10))
    print(lista)
