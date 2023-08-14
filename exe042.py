# Altura e Peso
altura = float(input("Digite sua altura (em metros): "))
peso = float(input("Digite seu peso (em kg): "))

# IMC
imc = peso / (altura * altura)
if imc < 18.5:
    print("Abaixo do ideal: magreza")
elif imc < 25:
    print("Peso ideal: CONTINUE ASSIM ;D")
elif imc < 30:
    print("Acima do ideal: sobrepeso")
elif imc < 40:
    print("Muito acima do peso: obesidade")
else:
    print("Peso excessivo: obesidade mórbida")
