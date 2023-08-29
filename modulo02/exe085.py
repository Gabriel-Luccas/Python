# uma lista com2 lostas dentro uma para pares e outra para impars
lista_numeros = []
pares = []
impares = []
for contador in range(8):
    numero = int(input("Numero: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
lista_numeros.append(pares)
lista_numeros.append(impares)
print(f"os numeros pares são {lista_numeros[0]}")
print(f"os numeros impares são {lista_numeros[1]}")
