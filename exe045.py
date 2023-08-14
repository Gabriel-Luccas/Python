# faça um jogo de jokenpo

import random

print("VAMOS JOGAR JOKENPO")
print("Digite : 1 para pedra\nDigite : 2 para papel\nDigite : 3 para tesoura")
player = int(input("Escolha entre padra, papel ou tesoura "))
pedra = 1
papel = 2
tesoura = 3
opcões = [pedra, papel, tesoura]
pc = random.choice(opcões)
if pc == player:
    print("EMPATE")
elif pc == 1 and player == 2:
    print("VOCÉ GANHOU SEU ADVERSARIO ESCOLHERU PEDRA E VOCÈ PAPEL")
elif pc == 1 and player == 3:
    print("VOCÉ PERDEU SEU ADVERSARIO ESCOLHERU PEDRA E VOCÈ TESOURA")
elif pc == 2 and player == 3:
    print("VOCÉ GANHOU SEU ADVERSARIO ESCOLHERU PAPEL E VOCÈ TESOURA")
elif pc == 2 and player == 1:
    print("VOCÉ PERDEU SEU ADVERSARIO ESCOLHERU PAPEL E VOCÈ PEDRA")
elif pc == 3 and player == 1:
    print("VOCÉ GANHOU SEU ADVERSARIO ESCOLHERU TESOURA E VOCÈ PEDRA")
elif pc == 3 and player == 2:
    print("VOCÉ PERDEU SEU ADVERSARIO ESCOLHERU TESOURA E VOCÈ PAPEL")
else:
    None
