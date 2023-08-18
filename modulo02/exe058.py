# Computador recebe num aleatorio de 0 a 10 e o player tenta acertar até acertar
import random

pc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ramdom = random.choice(pc)
tentativas = 0
print("Tente adivinhar o meu numero ^-^ ")
ques = int(input("Digite um numero: "))
while ques != ramdom:
    print("Vocé perdeu")
    ques = int(input("Digite um numero: "))
    tentativas += 1
print(f"Vocé ganhou,  mais teve que tentar {tentativas} vezes")
print("FIM")