# receba valor da casa , salrio e em quantos anos ele vai pagar


# SAlARIO E VALOR CASA
salario = float(input("Digite seu salario: "))
Valor_casa = float(input("Valor da casa: "))
Anos = int(input("Em qauntos anos vocé planeja pagar ? "))

# P = valor casa/ Meses totais de anos = valor da prestação
Meses = Anos * 12
prestação = Valor_casa / Meses


# Condição de 30%(0.30) se a prestação execer ele não recebe o emprestimo
trinta = salario * 0.30

if prestação >= trinta:
    print(" Emprestimo negado, Infelizmente a sua prestação ultrapassou 30 porcemto do salario e com isso não poderemos continuar com o emprestimo ")
else:
    print(
        f" Emprestimo Concebido como o valor de sua prestação de R${prestação:.2F} não ultrapassou 30% do seu salario R${trinta:.2F} iremos fazer esse emprestimo \nCom o salario de R${salario} em {Anos} anos esperos que voce compre a casa   "
    )
