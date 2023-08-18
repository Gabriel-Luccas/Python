#Receba um n / quer continuar sim ou ? / no final mostre a media entre os n digitados e o seu max e min 
numeros= [] 
opção=0
numeros_digitados=0

while opção != 2: # loop para o "Numeros" e quebra ao ususario digitar "2"
  numero=int(input("Digite um numero: "))
  numeros_digitados+=1
  opção=int(input("quer continuar?[1:sim] [2:não] "))
  numeros.append(numero)
  if opção != 1 and opção != 2:
    print("opção invalida recomeçar")
  

media_total= sum(numeros)/numeros_digitados # media 
max_numero=  max(numeros) # maior valor
min_numero= min(numeros) # menor valor 


print(f" o maior valor digitado: {max_numero}")
print(f" o menor valor digitado: {min_numero}")
print(f" a media dos valores : {media_total:.1f}")
print(f" q quantidade de valores digitados foi: {numeros_digitados}")
print(f" os valores digitados foram: {numeros}")
  