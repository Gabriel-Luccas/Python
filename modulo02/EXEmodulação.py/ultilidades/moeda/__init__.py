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
    print("-="*50)
    print("RESUMO DO VALOR".center(100))
    print("-="*50)
    print(f"Preço analisado:             R$ {numero:.2f}")
    print(f"Dobro do Preço:              R$ {dobro:.2f}")
    print(f"Metade do valor:             R$ {metade:.2f}")
    print(f"Aumentando {porcent}% do valor:  R$ {PlusPorcente:.2f}")
    print(f"Reduzindo {porcent}% do valor:   R$ {ReducePorcente:.2f}")