#receba a velocidad de um carro m k/h e se estiver acima de 80 receberá uma multa de 7 reias pra cada k/h exedente a 80 caso n estiver acima de 80 nada aconteçe 

# kilometro do carro

km=int(input("K/p do carro "))
limite=int(80)

# multa pra cada km que exede 80 7 reias
dif=(km-limite)
multa=(dif*7)
 
# multa se estiver acima de 80

if km > limite :
  print(f"Vocé recebeu uma multa de R${multa} , pois exedeu em {dif}km o limite de velocidade")
else:
  print("Vocé não recebeu multa")