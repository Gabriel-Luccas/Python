# receba 2 valores e mostre um menu de 5 opçoes soma , sub , mult , div e so ira sair do menu ao usar o 5
print("celcular operações entre")
numero1 = float(input("DIgite o primeiro numero: "))
numero2 = float(input("DIgite o segundo numero: "))
menu = 0
while menu != 5:
    print("Digite 1 Soma")
    print("Digite 2 Subtração")
    print("Digite 3 Multiplicação")
    print("Digite 4 DIvisão")
    print("Digite 5 Sair")
    menu = int(input("EScolha entre as opçoes a cima: "))
    if menu == 1:
        print(f"A Soma entre {numero1} e {numero2} é igual a {numero1 + numero2}")
    elif menu == 2:
        print(f"A Subtração entre {numero1} e {numero2} é igual a {numero1 - numero2}")
    elif menu == 3:
        print(
            f"A multiplicação entre {numero1} e {numero2} é igual a {numero1 * numero2}"
        )
    elif menu == 4:
        print(f"A divisão entre {numero1} e {numero2} é igual a {numero1 / numero2}")
    elif menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5:
        print("opção invalida")
print("Obrigado")
