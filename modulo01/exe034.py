# Receba um valor de salario e calcule seu aumento se for superior a 1250 é um aumento de 10% se for menor ou = é de 15%


# Salario

salario = int(input("Digite seu salario "))

# Aumento

dez = salario * 0.10
aumento10 = salario + dez
quinze = salario * 0.15
aumento15 = salario + quinze

# Receber aumento

if salario >= 1250:
    print(
        f"O seu aumento de 10% que da R${dez} no salario de R${salario} fica R${aumento10}"
    )
else:
    print(
        f"O seu aumento de 15% que da R${quinze} no salario de R${salario} fica R${aumento15}"
    )
