#peça um salario e me mostre com 15% de aumento

salario=float(input("digite seu salario "))
valor15=float(15/100*salario)
soma=float(valor15+salario)

print(f"seu salario atual é de {salario} com um aumento de 15% seria {soma}")