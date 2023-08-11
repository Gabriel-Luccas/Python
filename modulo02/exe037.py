# receba um numero inteiro qualuqer e e converta pra base 2 , 10 , 16

num = int(input("DIgite um numero inteiro : "))
print(
    "Escolha qual base de conversão: 1 para binário, 2 para octal, 3 para hexadecimal"
)
escolha = int(input("conversão: "))

# conversão base 2
bin = bin(num)[2:]
# conversão base octa
octal = oct(num)[2:]
# conversão base hexa
hexa = hex(num)[2:]
# escolha de conversão

if escolha == 1:
    print(f" o numero {num} convertio em binario fica: {bin}")
elif escolha == 2:
    print(f" o numero {num} convertio em octagonal fica: {octal}")
elif escolha == 3:
    print(f" o numero {num} convertio em hexadecimal fica: {hexa}")
else:
    print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
