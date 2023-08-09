# receba um nome e retorne somente sue primeiro e ultimo nome

nome = str(input("Digite seu nome "))
split = nome.split()
nome1 = split[0]
nome2 = split[-1]

print(f"Primeiro nome : {nome1}\nSeegundo nome: {nome2}")