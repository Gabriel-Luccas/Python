# receba 5 numeros aleatorios coloque em uma tupla e devolva 2 deles

import random

lista = []
for c in range(0, 6):
    num_aleatorio = random.randint(0, 11)
    print(num_aleatorio)
    lista.append(num_aleatorio)
t = tuple(lista)
print(f"2 numeros sorteados {random.choice(t)} e {random.choice(t)}  ")
print(f"Maior {max(lista)} e min {min(lista)}")
    