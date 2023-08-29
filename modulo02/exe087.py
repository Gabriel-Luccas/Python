# matrix aprimorada
par = []
valor00 = int(input("Digite o valor para [0,0]: "))
valor01 = int(input("Digite o valor para [0,1]: "))
valor02 = int(input("Digite o valor para [0,2]: "))

valor10 = int(input("Digite o valor para [1,0]: "))
valor11 = int(input("Digite o valor para [1,1]: "))
valor12 = int(input("Digite o valor para [1,2]: "))

valor20 = int(input("Digite o valor para [2,0]: "))
valor21 = int(input("Digite o valor para [2,1]: "))
valor22 = int(input("Digite o valor para [2,2]: "))

numeros_digitados = [
    valor00,
    valor01,
    valor02,
    valor10,
    valor11,
    valor12,
    valor20,
    valor21,
    valor22,
]
for item in numeros_digitados:
    if item % 2 == 0:
        par.append(item)
    else:
        None

numero1 = [valor00, valor01, valor02]
numero2 = [valor10, valor11, valor12]
numero3 = [valor20, valor21, valor22]
lista = [[numero1], [numero2], [numero3]]
soma_par = sum(par)
soma_terceira_coluna = valor02 + valor12 + valor22
maxi = max(valor10, valor11, valor12)
for item in lista:
    print(item)
print(f"A soma dos items pares da matrix = {soma_par}")
print(f"A soma dos valores da terceira coluna da matrix é = {soma_terceira_coluna}")
print(f"o maior valor da segunda linha da matrix é {maxi}")
