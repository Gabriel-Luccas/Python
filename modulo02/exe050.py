# A somo entre somente os numeros pares
soma = 0
for c in range(1,7):
    num = int(input(f"DIgite um o {c} valor: "))
    if num % 2 == 0:
        soma += num
print(f"A soma entre os numeros pares digitados é {soma}")
2
