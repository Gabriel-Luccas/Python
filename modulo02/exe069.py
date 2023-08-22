# receba cadastros e devolva dados especificos
maior_18 = 0
homens = 0
mulher_20 = 0
while True:
    sexo_pessoa = str(input("Informe seu sexo[F/M]: ")).upper().strip()
    if sexo_pessoa not in "FM":
        print("Informação invalida tente de novo")
        continue
    elif sexo_pessoa in "M":
        homens += 1
    idade_pessoa = int(input("Informe sua idade: "))
    if idade_pessoa >= 18:
        maior_18 += 1
    elif sexo_pessoa in "F" and idade_pessoa <= 20:
        mulher_20 += 1
    continue_or_Not = str(input("Quer continuar[S/N]? ")).upper().strip()
    if continue_or_Not in "N":
        break
print(
    f"Total de pessoas com +18 = {maior_18}\nTodal de homens = {homens}\nTotal de Mulheres com menos de 20 = {mulher_20}"
)
