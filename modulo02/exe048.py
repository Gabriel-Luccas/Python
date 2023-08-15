soma = 0

for c in range(0, 500):
    resto = c % 3
    if resto == 0:
        soma = +c
print("A soma dos múltiplos de 3 é:", soma)