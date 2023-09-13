def half(n):
    half = n / 2
    return half


def double(n):
    double = n * 2
    return double


def PlusPorcent(n, Porcent):
    Por = n * (1 + Porcent / 100)
    return Por


def ReducePorcent(n, Porcent):
    Red = n * (1 - Porcent / 100)
    return Red


def verificar_numero(valor):
    try:
        numero = float(valor)
        return True, numero
    except ValueError:
        return False, None


def resume(numero, porcent, dobro, metade, PlusPorcente, ReducePorcente):
    print("-=" * 50)
    print("RESUMO DO VALOR".center(100))
    print("-=" * 50)
    print(f"Preço analisado:             R$ {numero:.2f}")
    print(f"Dobro do Preço:              R$ {dobro:.2f}")
    print(f"Metade do valor:             R$ {metade:.2f}")
    print(f"Aumentando {porcent}% do valor:  R$ {PlusPorcente:.2f}")
    print(f"Reduzindo {porcent}% do valor:   R$ {ReducePorcente:.2f}")


def obter_numero_valido():
    while True:
        entrada = input("Digite um valor: R$ ")
        valido, numero = verificar_numero(entrada)
        if valido:
            return numero
        else:
            print("Entrada inválida. Digite um número válido.")


def obter_porcentagem_valido():
    while True:
        entrada = input("Digite um valor pra Porcemtagem%:  ")
        valido, numero = verificar_numero(entrada)
        if valido:
            return numero
        else:
            print("Entrada inválida. Digite um número válido.")
