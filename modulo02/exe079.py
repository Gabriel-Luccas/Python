# receba valores até o usario não quiser mais , não aceite valores repetidos , devolva os valores em ordem crecente

lista_valores = []
print("Lista de Valores (Não aceitamos valores repetidos)")
valor = int(input("Adicionar valor a lista: "))
lista_valores.append(valor)
while True:
    opção = str(input("Deseja adicionar outro valor [N/S]: ")).upper().strip()
    if opção in "S":
        valor = int(input("Adicionar outro valor a lista: "))
        lista_valores.append(valor)
    elif opção in "N":
        print("OK iremos exibir a lista criada")
        break
    else:
        print("Valor invalido recomeçar")
        break
li = sorted(lista_valores)
print(f"Valore digitados {lista_valores}")
print(f"Ordem crecente {li}")
