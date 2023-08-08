#sen con tang triangulo retangulo 

import math 

co=float(input("Cateto oposto "))
ca=float(input("Cateto Adjacente "))
hi=math.hypot(co, ca)

print(f"se cateto oposto é {co} , e o cateto adjacente {ca}\nentão a Hipotenusa é {hi:.2f}")