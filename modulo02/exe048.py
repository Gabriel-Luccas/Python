# soma entre os multiplos de 3

soma = 0

for c in range(1, 501, 2 ):
    if c % 3 == 0:
        soma = soma + c
print("A soma dos múltiplos de 3 é:", soma)
