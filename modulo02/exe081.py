# receba varis valores , devolva quantos foram digitados , em ordem decrecente e se tem o valor "5" ou não na lista
valores = []
valor = int(input("Numero: "))
valores.append(valor)
quantidade_valores = 1
while True:
    opcao = str(input("Quer continuar [S/N]?:  ")).upper().strip()
    if opcao in "S":
        valor = int(input("Proximo Numero: "))
        quantidade_valores += 1
        valores.append(valor)
    else:
        break
valores.sort(reverse=True)
print(f"A ordem de valores decrecentes fica : {valores}")
print(f"A quantidade de valores digitados foram {quantidade_valores}")
if 5 in valores:
    print(f"o Valor 5 foi digitado na lista e esta na posição {valores.index(5)}")
else:
    print("o valor 5 não foi digitado na lista")
