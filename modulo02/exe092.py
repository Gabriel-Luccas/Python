dados_pessoa = {}
dados_pessoa["nome"] = str(input("Nome: "))
dados_pessoa["Ano de nascimento: "] = int(input("Ano de nascimento:"))
dados_pessoa["CdT"] = int(input("Carteira de trabalho ( 0 não tem): "))
if dados_pessoa["CdT"] != 0:
    dados_pessoa["ano contratação"] = int(input("Ano de contratação: "))
    aposentadoria = 2023 - dados_pessoa["ano contratação"]
    dados_pessoa["salario"] = float(input("Salario: "))
    aposentadoria = 2023 - dados_pessoa["ano contratação"]
elif dados_pessoa["CdT"] == 0:
    print("Sem carteira")
else:
    print("invalido")
print("=-" * 100)
idade = 2023 - dados_pessoa["Ano de nascimento: "]
print(f"{dados_pessoa['nome']} tem {idade} anos ")
if dados_pessoa["CdT"] != 0:
    print(
        f"com a carteira de trabalho: {dados_pessoa['CdT']} contratado em {dados_pessoa['ano contratação']}"
    )
    print(
        f"{dados_pessoa['nome']} vai seaposentar em {dados_pessoa['ano contratação']+ 35} com {idade + 35}"
    )
else:
    print("Sem carteira de trabalho")
