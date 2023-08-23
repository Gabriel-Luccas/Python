# receba um n de 0 a 20 e devolta ele el extensso
extenso = (
    "zero",
    "um",
    "dois",
    "tres",
    "Quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
)
while True:
    numero = int(input("Digite um numero de 0 a 10: "))
    if numero < 0 or numero > 10:
        numero = int(input("Numero invalido Tente Novamente: "))
    valor = extenso[numero]
    print(f"em extenso fica: {valor}")
    break
