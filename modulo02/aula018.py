#Lista composta 
pessoas=[["gabriel",20], ["Erika",29], ["Sabet",39]]
print(pessoas[2][0])
galera=list()
dados=[]
for contador in range(4):
  dados.append(str(input("Nome: ")))
  dados.append(str(input("Idade: ")))
  galera.append(dados[:])
  dados.clear()
print(galera)