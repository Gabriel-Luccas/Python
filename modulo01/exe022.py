# crie um prgrama que leai o nome e devolvva em maisculo minusculo letras ao todo sem espaçoes e quantas letras tem o primeiro nome

fullname = input("Nome Completo ")
upper = fullname.upper()
low = fullname.lower()
strip = fullname.replace(" ", "")
lentotal = len(strip)
nomes = fullname.split()
name1 = len(nomes[0]) 

print(
    f" seu nome completo é {fullname} e maiusculo fica {upper} e em minusculo fica {low} tendo um total de {lentotal} letras contando somente o primeiro nome {name1}"
)
