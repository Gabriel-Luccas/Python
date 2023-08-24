# receba 4 numberos int coloca em tupla e devolva  se nove foi digitado e qual posição o primeor 3 apareceu e quantos num par

num1 = int(input("Digite numero: "))
num2 = int(input("Digite numero: "))
num3 = int(input("Digite numero: "))
num4 = int(input("Digite numero: "))
t = (num1, num2, num3, num4)
nove = t.count(9)
tres = t.index(3)
posição_correta = tres + 1
par = 0
if num1 % 2 == 0:
    par += 1
if num2 % 2 == 0:
    par += 1
if num3 % 2 == 0:
    par += 1
if num4 % 2 == 0:
    par += 1
print(
    f"foram digitados {t} o nove foi digitado {nove} vezes o 3 está na posilçao {posição_correta} e tem {par} numeros pares"
)
