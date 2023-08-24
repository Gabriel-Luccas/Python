# Loop principal que continuará executando até que o usuário decida sair
while True:
    # Pergunta ao usuário se eles querem calcular seu IMC
    escolha = str(input("Olá! Gostaria de saber seu IMC [S/N]?")).upper().strip()[0]
    # Verifica se a escolha é inválida e solicita novamente se for
    if escolha not in "S" and escolha not in "N":
        escolha = str(input("Informação anterior inválida. Gostaria de saber seu IMC [S/N]?")).upper().strip()[0]
    # Caso o usuário escolha "S" para calcular o IMC
    elif escolha in "S":
        # Solicita ao usuário inserir sua altura e peso
        altura = float(input("Digite sua altura (em metros): "))
        peso = float(input("Digite seu peso (em kg): "))
        # Calcula o IMC usando a fórmula: peso / (altura * altura)
        imc = peso / (altura * altura)
        # Verifica em que faixa o IMC se encaixa e exibe a mensagem correspondente
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
    # Caso o usuário escolha "N" para sair
    else:
        print("Ok, obrigado pela visita! :D ")
        break  # Encerra o loop para finalizar o programa