#faça o computador gerar ua lista de 0 a 5 e escolher um numero aleatorio, e o  usuario tem que tentat acertar esse numero, mostrando se perdeu ou venceu 

import random

# lista de numero

list_num=[0, 1 , 2 , 3 , 4 ,5 ]

# numero aleatorio

random_num = random.choice(list_num)

# resposta usuario 

print("DIgite um numero de 0 a 5 e tente acertar o numero correto")
us=int(input("DIgite um o numero "))
if us == random_num :
  print("Parabnes vocé acertou pege seu coockie")
else:
  print("Vocé errou try again T-T )")