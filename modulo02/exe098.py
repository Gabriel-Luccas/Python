# função com for


def cont(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        print(f"{c} ", end="")


def linha():
    print("=-" * 40)


linha()
print("primeira contagem")
print("começa em 1 até 10 em 1 em 1 ")
cont(1, 11, 1)
print()

linha()
print("Segunda contagem")
print("Começa em 10 até 0 em 2 em 2 ")
cont(10, -2, -2)
print()


linha()
print("Contagem Personalizada")
inicio = int(input("começa em: "))
fim = int(input("termina em : "))
passo = int(input("vai de quanto em quanto: "))
if passo == 0:
    passo = 1
print(f"Começa em {inicio} até {fim} em {passo} em {passo}")
cont(inicio, fim, passo)
print()
linha()
