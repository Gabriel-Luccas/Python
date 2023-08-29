# Receba o nome e peso de varias pessoas , retorne qauntidades de pessoas cadastradas o menor e maior peso
nome_das_pessoas = []
pesos = []
numero_de_pessoas_cadastradas = 0
while True:
    nome_das_pessoas.append(str(input("Nome: ")))
    pesos.append(int(input("Peso: ")))
    numero_de_pessoas_cadastradas += 1
    yes_or_no = str(input("Deseja continuar?[S/N]: ")).upper().strip()
    if yes_or_no in "S":
        continue
    else:
        break
maior_peso = max(pesos)
menor_peso = min(pesos)


indice_maior_peso = pesos.index(maior_peso)
indece_menor_peso = pesos.index(menor_peso)
nome_menor_peso = nome_das_pessoas[indece_menor_peso]
nome_maior_peso = nome_das_pessoas[indice_maior_peso]

print(f"O maior peso é de {maior_peso} e pertence a {nome_maior_peso}")
print(f"O menor peso é {menor_peso} e pertence a {nome_menor_peso}")
print(f"Total de cadastros : {numero_de_pessoas_cadastradas}")
