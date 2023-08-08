#conte quantos  "a" aparece na frase e me reorne a posição do primeiro e ultimo a 

frase=input("DIgite uma frase ")
cont=frase.count("a")
primeiro_a = frase.find("a")
ultimo_a = frase.rfind("a")
print(f"{frase} ela tem {cont} letras a a primeira aparece em {primeiro_a} e a ultima em {ultimo_a}")