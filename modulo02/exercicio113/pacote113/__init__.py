# funçoes criadas para o exercicio 113

def leiaint(numero):
    while True:
        try:
            numero = int(input("Digite um numero inteiro: "))
        except:
            print("ERRO:somente numeros inteiros")
        else:
            return numero



def leiareal(numero):
    while True:
        try:
            numero = float(input("Digite um numero real: "))
        except:
            print("ERRO:somente numeros reais")
        else:
            return numero


