# calcule e madia e diga reprovado 5.0, recuperação 5.0 e 6.9 , aprovado 7.0
nota1 = float(input("DIgite sua nota "))
nota2 = float(input("DIgite sua nota "))

# Media
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f"Parabens pela sua nota de {media} vocé foi arpovado")
elif media > 5.0:
    print(
        f"Boa!! com sua nota de {media} não foi reprovado mas podemos melhorala com a recuperação"
    )
else:
    print(f"Com sua nota de {media} foi reprovado T-T ")
