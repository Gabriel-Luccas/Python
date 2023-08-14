# Receba uma idade e clasifique-a  0 a 9 mirim 10 a 14 infantil 15 a 19 junior 20 a 22 senior acima master

ano = int(input("Em que ano vocé nasceu ? "))
idade = 2023 - ano
if idade <= 9:
    print(f"com {idade} vocé é um atleta mirim")
elif idade <= 14:
    print(f"com {idade} vocé é um atleta infantil")
elif idade <= 19:
    print(f"com {idade} vocé é um atleta junior")
elif idade <= 24:
    print(f"com {idade} vocé é um atleta senior ")
elif idade > 25:
    print(f"com {idade} vocé é um atleta master")
else:
    None
