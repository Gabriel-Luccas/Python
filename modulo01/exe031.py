#receba uma distancia em x km e terne o valor da viagme sendo que 1 km é 0.50 reias e pra distancias mais longas fica 0,45 reias 

# distancia 

dist=int(input("Qual a distancia da viagem "))

# valor pre 200km x 0.50

lower200km=float((dist*0.50))

# valor above 200km 0,45

above200km=float((dist*0.45))

# valor total 
if dist < 200:
  print(f"o valor da sua viagem com uma distancia de {dist}km deu um valor de R${lower200km}")
else:
  print(f"Sua viagem com a distanca de {dist} deu um valor de R${above200km}")
print("Boa-Viagem c: ")