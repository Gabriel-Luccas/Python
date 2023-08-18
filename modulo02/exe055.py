#faça um programa que receba 5  peso diferentes e depois mostre o maior e o menor entre eles 
list_peso=[]
for c in range(6):
  peso=int(input("Quanto vocé pesa? "))
  list_peso.append(peso)
print(f" o maior peso é {max(list_peso)} e o menor é {min(list_peso)}")