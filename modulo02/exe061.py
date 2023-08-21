#contador de PA 

primeiro_numero = int(input("Digite um nemero: "))
razão= int(input("Qual a razão: "))

# um contador que começo no "1" e o primeiro termo que começa no "Primeiro_numero "
contador = 1 
termo = primeiro_numero

while contador < 11 :
  print(termo)
  termo += razão
  contador += 1 
print("FIM")
