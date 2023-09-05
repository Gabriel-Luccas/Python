# função gera 5 num ramdom e função somapar
import random

numeros_sorteados = []


def linha():
    print("-" * 50)


def sorteio():
    global numeros_sorteados
    while len(numeros_sorteados) < 5:
        numeros_sorteados.append(random.randint(1, 100))


soma_par = []


def somapar(lista):
    global soma_par
    pos = 0
    for numero in lista:
        if numero % 2 == 0:
            soma_par.append(numero)


linha()
sorteio()
print("Números sorteados:")
print(numeros_sorteados)

linha()
somapar(numeros_sorteados)
print("Números pares da lista:")
print(soma_par)
soma_pares = sum(soma_par)
print(f"A soma dos numeros pares é de {soma_pares}")
linha()
