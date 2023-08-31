# Dicionarios 
Pessoas={'nome':'Gabrel','idade':'20','altura':'1.83'}
print(Pessoas)
print(Pessoas.values())
print(Pessoas.keys())
print(Pessoas.items())
print(Pessoas['idade'])


Pessoas=[]
dados={}
for c in range(2):
  dados["nome"]=str(input("Nome: "))
  dados["Idade"]=str(input("Idade: "))
  Pessoas.append(dados.copy())
for d in Pessoas:
  for keys, values in dados.items():
    print(f" {keys} e {values}") 
