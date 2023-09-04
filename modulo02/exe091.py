import random

lista_jogadores = []

for cont in range(1, 5):
    numero_dado = {}
    numero_dado["Jogador"] = f"jogador{cont:02d}"
    numero_dado["dado"] = random.randint(1, 6)
    lista_jogadores.append(numero_dado.copy())
print(lista_jogadores)
# Crie uma lista de posições a partir das médias dos jogadores
lista_jogadores = sorted(lista_jogadores, key=lambda x: x["dado"], reverse=True)
for jogador in lista_jogadores:
    jogador_nome = jogador["Jogador"]
    jogador_dado = jogador["dado"]
    print(f"{jogador_nome} tirou {jogador_dado} no dado.")
