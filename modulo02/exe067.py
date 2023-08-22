while True:
    Tabuada_do = int(input("Tabuado do: "))
    vezes = 1
    if Tabuada_do < 0:
        break
    for c in range(1, 11):
        print(f"{Tabuada_do} x {vezes} = {Tabuada_do*vezes}")
        vezes += 1
print("FIM")
