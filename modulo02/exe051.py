num = int(input("Digite um número: "))
fim = int(input("Digite o fim da PA: "))

soma = 0  # Variável para armazenar a soma dos números na PA

for c in range(num, fim + 1):
    soma += c  # Adiciona cada número à soma
    print(c, end=" ")  # Imprime o número da PA
    if c != fim:  # Verifica se é o último número para não imprimir a vírgula
        print(",", end=" ")

print("\nA soma dos números na PA é:", soma)



