# receba varios numros e para quando for digitado 999
numeros_digitados = 0
numero = 0
soma = []
while numero != 999:
    numero = int(input("Digite um numero: "))
    if numero != 999:
        soma.append(numero)
        numeros_digitados += 1
soma_total = sum(soma)
print(numeros_digitados)
print(soma)
print(soma_total)
