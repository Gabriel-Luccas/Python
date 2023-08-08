# receba um numero de 0 1 9999 e leias as suas unidades ex 1892 1 milhar 8 centenas 9 dezenas e 2 unidades

num = input("Digite um numero ")
mi = num[0:1]
cen= num[1:2]
dez= num[2:3]
uni= num[3:4]
print(f"seu numero {num}, tem  {mi} milhares,{cen} centenas, {dez} dezenas, {uni} unidades.")


