# par ou impar
import random

win_streak = 0
print("Vamos jogar Par ou Impar ")
while True:
    par_impar = str(input("Impar pu par ?[I/P] ")).upper().strip()[0]
    numero_usuario = int(input("Digite seu numero: "))
    pc = range(10)
    pc_choice = random.choice(pc)
    soma = pc_choice + numero_usuario
    print(soma)
    if par_impar in "I" and soma % 2 != 0 or par_impar in "P" and soma % 2 == 0:
        win_streak += 0
        print(f"Vocé ganhou o resultado {win_streak} seguidas")
    else:
        print(f"Vocé perdeu o resultado foi {soma}")
        break
print("FIM")
