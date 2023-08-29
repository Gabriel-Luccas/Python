# matrix
valor00 = str(input("Digite o valor para [0,0]: "))
valor01 = str(input("Digite o valor para [0,1]: "))
valor02 = str(input("Digite o valor para [0,2]: "))

valor10 = str(input("Digite o valor para [1,0]: "))
valor11 = str(input("Digite o valor para [1,1]: "))
valor12 = str(input("Digite o valor para [1,2]: "))

valor20 = str(input("Digite o valor para [2,0]: "))
valor21 = str(input("Digite o valor para [2,1]: "))
valor22 = str(input("Digite o valor para [2,2]: "))


numero1 = [valor00, valor01, valor02]
numero2 = [valor10, valor11, valor12]
numero3 = [valor20, valor21, valor22]
lista = [[numero1], [numero2], [numero3]]
for item in lista:
    print(item)
