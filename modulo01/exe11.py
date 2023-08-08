#um produto e mostre seu preço com 5% de desconto

product=float(input("qual o valor do produto "))
discount=float(5/100*product)
discontvalor=float(product-discount)

print(f"o valor normal do produto é {product} , mas com 5% de disconto que tira {discount} do valor do produto isso deixa ele com um valor de {discontvalor} ")