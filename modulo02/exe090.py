lsita_alunos = []
dados_aluno = {}
while True:
    dados_aluno["Nome"] = str(input("Nome do alumo: "))
    dados_aluno["Nota01"] = int(input("Nota prova 1 do aluno: "))
    dados_aluno["Nota02"] = int(input("Nota prova 2 do aluno: "))
    media = (dados_aluno["Nota01"] + dados_aluno["Nota02"]) / 2
    dados_aluno["Media"] = media
    dados_aluno["Estado"] = ""
    if media >= 7:
        dados_aluno["Estado"] = "Aprovado"
    else:
        dados_aluno["Estado"] = "Reprovado"
    lsita_alunos.append(dados_aluno.copy())
    Yes_No = str(input("Quer adicionar outro aluno?[S/N]: ")).upper().strip()
    if Yes_No in "S":
        continue
    else:
        break
print("=" * 100)
print("BOLETIM")
for aluno in lsita_alunos:
    nome = aluno["Nome"]
    media = aluno["Media"]
    estado = aluno["Estado"]
    print(f"nome: {nome} media: {media} estado: {estado}")
print("=-" * 50)
