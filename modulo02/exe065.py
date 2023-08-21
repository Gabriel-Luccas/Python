#Receba um n / quer continuar sim ou ? / no final mostre a media entre os n digitados e o seu max e min 
numeros= [] 
opção=0
numeros_digitados=0
opção = "S"

while opção in "Ss": # loop para o "Numeros" e quebra ao ususario digitar "2"
  numero=int(input("Digite um numero: "))
  numeros_digitados+=1
  opção=str(input("quer continuar?[1:sim] [2:não] ")).upper().strip()[0]
  numeros.append(numero)
if opção not in "S" and opção not in "N" :
   print("Opção invalida, incerrarmos agora ")

media_total= sum(numeros)/numeros_digitados # media 
max_numero=  max(numeros) # maior valor
min_numero= min(numeros) # menor valor 

print("Aqui os resultados")
print(f" o maior valor digitado: {max_numero}")
print(f" o menor valor digitado: {min_numero}")
print(f" a media dos valores : {media_total:.1f}")
print(f" quantidade de valores digitados foi: {numeros_digitados}")
print(f" os valores digitados foram: {numeros}")
  