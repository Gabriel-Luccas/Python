# def função help()


def linha():
    print("=" * 100)
    print("Sistema de ajuda Python")


def linha02():
    print("=" * 100)


def ajuda():
    while True:
        linha()
        a = input("Biblioteca ou função  : ")
        if a in "FIM":
            break
        linha02()
        print(f"Acesssando manual de {a}")
        help(a)
        linha02


ajuda()
