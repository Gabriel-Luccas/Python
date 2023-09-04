dados_jogador = {}
gosl = []
dados_jogador["nome"] = str(input("Nome do jogador: "))
dados_jogador["partidas jogadas"] = int(input("Partidas jogadas: "))
dados_jogador["gosl"] = []
for c in range(dados_jogador["partidas jogadas"]):
    gosl_partida = int(input(f"Numero de gols na {c+1} partida: "))
    dados_jogador["gosl"].append(gosl_partida)

print("=-" * 50)

print(f"O jogador {dados_jogador['nome']}")
soma_total = sum(dados_jogador["gosl"])
print(f"Fez {dados_jogador['gosl']} e um total de {soma_total} Gols ")
print("=-" * 50)

print(
    f"O jogador {dados_jogador['nome']} jogou {dados_jogador['partidas jogadas']} partidas"
)

for partida, gols in enumerate(dados_jogador["gosl"], start=1):
    print(f"Na partida {partida} ele fez {gols} gols")
