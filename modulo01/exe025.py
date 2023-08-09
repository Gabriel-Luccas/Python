#receba um nome e me diga sim ou não se começa com SANTO

name=input("Diga me o nome de sua cidade ")
snmae= name.strip().split()
sim="Santos" in snmae[0]

print(f"sua cidade {sim} tem Santos no começo do nome")