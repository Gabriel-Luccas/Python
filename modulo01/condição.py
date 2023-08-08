codigo_compra = int(input("digite o codigo da compra"))

if codigo_compra == 5222:
    print("comprar na promoção")
elif codigo_compra == 5333:
    print("compra a prazo no boleto")
elif codigo_compra == 5444:
    print("compra no cartão")
else:
    print("codigo não cadastrado")
