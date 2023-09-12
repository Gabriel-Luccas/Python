from ultilidades.moeda import double, half, PlusPorcent, ReducePorcent, verificar_numero, resume

def obter_numero_valido():
    while True:
        entrada = input("Digite um valor: R$ ")
        valido, numero = verificar_numero(entrada)
        if valido:
            return numero
        else:
            print("Entrada inválida. Digite um número válido.")

numero = obter_numero_valido()
porcent = float(input("Digite uma Porcentagem: "))

dobro = double(numero)
metade = half(numero)
PlusPorcente = PlusPorcent(numero, porcent)
ReducePorcente = ReducePorcent(numero, porcent)

resume(numero, porcent, dobro, metade, PlusPorcente, ReducePorcente)
