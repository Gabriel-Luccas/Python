# Fatorial de um n
numero = int(input("Digite um numero: "))
fatorial = 1
fatoriais = []
resultado = 1
while fatorial != numero:
    print(fatorial , end="")
    if fatorial < numero:
        print(" X ", end="")
    else:
        print(" = ", end="")
    fatorial += 1
    fatoriais.append(fatorial)
    resultado *= fatorial  # Resultado foi recebendo os fatorial e multiplicando eles ex:resulto = 1 *1(valor no peimeiro do loop)/Resultado= 1(resultado da operação anteror *2(valor na segunda vez que o loop se repetiu)/ Resultado = 2(resultado da operação anterior) * 3(valor da terceira vez que se repetiu o loop)
print(f"fatoriais do numero: {numero}! são : {fatoriais} ")
print(f"resultado do faturamento do numero: {numero} é igual a {resultado}")
