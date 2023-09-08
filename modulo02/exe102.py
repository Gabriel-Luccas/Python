# def função fatorial opcioanl show True or False para ver a conta


def fatorial(numero, show=True):
    """_summary_

    Args:
        numero (int): numero digitado pelo usuario em input 
        show (bool, optional): opção opicional se estiver em True mostra o print da conta se em False  não mostra

    Returns:
        fatoriamento = int 
    """

    fatoriamento = 1
    for c in range(1, numero + 1):
        fatoriamento *= c
        if show:
            if c == 1:
                print(f"{numero}! =", end=" ")
            print(c, end=" x " if c < numero else " = ")
    return fatoriamento

numero = int(input("Digite um número: "))
resultado = fatorial(numero)
print(resultado)
