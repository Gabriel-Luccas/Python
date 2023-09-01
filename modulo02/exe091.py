import random

lista_jogadores = []

for cont in range(1,5):
  numero_dado={}
  numero_dado["Jogador"]=f"jogador{cont:02d}"
  numero_dado["dado"]= random.randint(1,6)
  lista_jogadores.append(numero_dado)
print(lista_jogadores)
# Crie uma lista de posições a partir das médias dos jogadores
