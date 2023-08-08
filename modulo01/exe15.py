#Aluguel de carro 


dia=int(input("por quantos dias voce alugou o carro "))
km=float(input("Qunatos km rodou o carro "))
valordia=int(dia*60)
kmvalor=float(km*0.15)
valortotal=float(kmvalor+valordia)

print(f"voce alugou o carro por {dia} dias isso gerou um valor de R${valordia} ,e percorreu {km}km ,isoo gerou um valor de R${kmvalor:.3f}")
print(f"num total de R#{valortotal:.2f}")