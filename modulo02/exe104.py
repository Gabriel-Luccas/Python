# def função que aceita somente numeros int  e nega todos os restos de input
def leiaint():
    while True:
        numero = (input("DIgite um nemero: ")).strip()
        if numero.isnumeric():
            print(numero)
            break
        else:
            print("ERRO , só aceitamos numeros inteiros")

        


n = leiaint()
