# Crie uma função adaptavel ao tamanho do parametro que é uma msm e as linhas ("=-")  seguem esse tamanho


def texto(msm):
    print("-" * len(txt) * 2)
    print(msm)
    print("-" * len(txt) * 2)


print("O que vocé tem a dizer? ")
txt = str(input("Digite sua mensagem: "))
texto(txt)
