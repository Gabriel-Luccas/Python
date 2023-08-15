soma=0
for c in range(0, 6):
    num = int(input("DIgite um numero: "))
    par = num % 2
    if par == 0:
        soma += num
print(f"A soma entre os numeros pares digitados é {soma}")
2
