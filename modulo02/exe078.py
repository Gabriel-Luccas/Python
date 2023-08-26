# receba 5 valores e coloque en uma lista devolva os valores e sua posciçaõ na lista
numeros=[]
for v in range(0, 5):
    numero = int(input("Numero: "))
    numeros.append(numero)
maior_valor = max(numeros)
menor_valor = min(numeros)

print(
    f"valores da lista {numeros} o maior valor da lista é = {maior_valor} na posição {numeros.index(maior_valor)} e o menor = {menor_valor} na posição {numeros.index(menor_valor)}"
)
