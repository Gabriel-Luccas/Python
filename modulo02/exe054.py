# peça a idade de 7 pessoas e infrme quantas são maiores de 18

maior_18 = 0
menor_18 = 0
for c in range(0, 7):
    ano = int(input("Em que ano vocé nasceu? "))
    idade = 2023 - ano
    if idade >= 18:
        print("Vocé é maior de 18")
        maior_18 += 1
    else:
        print("Vocé é menor de 18")
        menor_18 += 1
print(f"Nos temos {maior_18} maiores de idade e {menor_18} menores de idade")
