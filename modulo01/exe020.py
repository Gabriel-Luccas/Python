#lista aleatoria 
import random
n1=input("Nome ")
n2=input("nome ")
n3=input("nome ")
n4=input("Nome ")

nomes=(n1, n2, n3, n4)
listaem=list(nomes)
random.shuffle(listaem)

print(f"A ordem de nomes sorteada vai ser esssa {listaem}")