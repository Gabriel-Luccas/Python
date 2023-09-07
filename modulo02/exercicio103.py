# def ficha jogador e gol


def ficha(jogador="", gols=0):
    dados_jogador = {}
    dados_jogador["jogador"] = jogador
    if jogador in "":
        dados_jogador["jogador"] = "<desconhecido>"
    dados_jogador["gols"] = gols
    if gols == "":
        dados_jogador["gols"] = 0
    return dados_jogador


jogador = str(input("Nome do jogador: "))
gols =(input("Gols : "))
dados_jogador = ficha(jogador, gols)
print(dados_jogador)

