# receba varios numeros coloqueos em uma lista e depois crei duas lisats com base na lista existente so que somente seus numeros impares e pares
lista_valores = []
while True:
    valor = int(input("Digite o valor: "))
    lista_valores.append(valor)
    yes_or_no = str(input("Quer continuar?[S/n]: ")).upper().strip()
    if yes_or_no in "S":
        continue
    else:
        break
par = []
impar = []
for v in lista_valores:
    if v % 2 == 0:
        par.append(v)
    elif v % 2 != 0:
        impar.append(v)
print(f"a lista de valores digitados= {lista_valores}")
print(f"a lista contem esses valores pares = {par}")
print(f"a lista contem esses valores impares = {impar}")
