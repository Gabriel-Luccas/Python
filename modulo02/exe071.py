valor_desejado = int(input("Digite o valor desejado: "))

# Lista com os valores das cédulas disponíveis em ordem decrescente
cedulas_disponiveis = [100, 50, 20, 10, 5, 2, 1]
print(f"Para ter {valor_desejado} são:")
for cedula in cedulas_disponiveis:
    quantidade = valor_desejado // cedula
    valor_desejado %= cedula
    if quantidade > 0:
        print(f"{quantidade} cédula(s) de {cedula}")
