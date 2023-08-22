# receba varios nome do produto seu valor e devolva valor total e produto mais barato
soma_total = 0
acima_100_reias = 0
while True:
    nome_produto = str(input("Nome do produto: "))
    valor_produto = float(input("Preço do produto: "))
    soma_total += valor_produto
    continue_or_not = str(input("Quer continuar[S/N]? ")).upper().strip()
    if continue_or_not in "N":
        break
    elif valor_produto > 1000:
        acima_100_reias += 1
print(f"soma total R${soma_total}\nE foram comprados {acima_100_reias} acima de R$1000")
