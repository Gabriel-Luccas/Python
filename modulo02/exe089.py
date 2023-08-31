# 3 listas 1 geral 1 nomes 1 notas
Geral = []
while True:
    nome = input("Nome do ALuno: ")
    nota01 = float(input("Nota 1 : "))
    nota02 = float(input("nota 2 : "))
    alunos = [nome, [nota01, nota02]]
    print(alunos)
    Geral.append(alunos[:])
    Yes_no = str(input("Deseja Continuar?[S/N]: ")).upper().strip()
    if Yes_no in "S":
        continue
    else:
        break
print("Boletim geral abaixo: ")
print("=" * 100)
for aluno in Geral:
    media = (aluno[1][0] + aluno[1][1]) / 2
    print(
        f"{aluno[0]} com as Notas de {aluno[1][0]} e {aluno[1][1]} ficou com a media de {media}"
    )
    print("-=" * 50)
