def area(a, b):
    area = a * b
    print(f"A área do terro é de {area}m\u00B2")


def linha():
    print("=-" * 50)


linha()
print("Calcular área do terreno")
linha()
largura = float(input("Largura(m): "))
comprimento = float(input("Comprimento(m): "))
area(largura, comprimento)
