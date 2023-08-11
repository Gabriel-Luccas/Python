num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num = [num1, num2]
max_valor = max(num)

if num1 == num2:
    print(f"Os valores {num1} e {num2} são iguais")
elif max_valor == num1:
    print(f"O maior valor é o {num1}")
elif max_valor == num2:
    print(f"O maior valor é o {num2}")
else:
    print("Informação inválida. Por favor, tente novamente.")

