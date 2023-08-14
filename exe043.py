# Receba o valor de um produto e em tal condiçoes tera o pagamento alterado: dinheiro ou cheque = 10% desconto / a vista cartão 5% desconto /2x cartão preço normal / 3x ou mais 10% juros

print(
    "opção 1 : dinheiro ou cheque\nopção 2 : cartão a vista\nopção 3 : até 2x no cartão\nopção 4 : 3x ou mais no cartão "
)
opção = int(input("Qual opção de pagamento: "))
valor = float(input("Qual o valor do produto : "))
# dinheir ou chque
desconto_dinheiro = valor - (valor * 0.10)
# cartão a vista
vista = valor - (valor * 0.05)
# valor sem auteração até 2x car~tão
normal = valor
# Juros
juros = valor * 0.20
montaine = valor + juros
if opção == 4:
    parcela = int(input(f"Em quantas parcelas vai pagar: "))
    valor_parcela = montaine / parcela
    print(
        f"Nesta opção o valor do produto tera 20% de juros ficando R${montaine} de R${normal} e foi pago em {parcela} parcelas cada uma sendo R${valor_parcela:.2F}"
    )
elif opção == 1:
    print(
        f"Nesta opção o valor do produto tera 10% de desconto ficando R${desconto_dinheiro} de R${normal}"
    )
elif opção == 2:
    print(
        f"Nesta opção o valor do produto tera 5% de desconto ficando R${vista} de R${normal}"
    )
elif opção == 3:
    print(f"Nesta opção o valor do produto sera padrão ficando R${normal}")
else:
    print("opção invalida tente novamente")
