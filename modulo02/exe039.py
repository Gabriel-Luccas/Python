# receba um ano de nacimento e calcule a idade e se ja passou de 18 none se fez 18 se inscreve no exercito  se é menor de 18 aviso
from datetime import datetime


ano = int(input("Quem ano vocé nasceu ? "))
anoAtual = datetime.now().year
idade = anoAtual - ano
atrasp= idade - 18
falta= 18 - idade

if idade < 18:
    print(f"com a idade de {idade} Esta chegando a sua fez de se alistar no exercito daqui a {falta} anos")
elif idade == 18:
    print(f"com a idadede de {idade} está na hora de vocé se alisatar no exercito")
else:
    print(f"com {idade} Ja passou {atrasp} anos do alistamento ")
