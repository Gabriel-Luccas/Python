#Faça uma tabuado com for in range 

num = int(input("Tabuado do : "))

for c in range(0, 11):
    vezes = num * c
    print(f"{num} x {c} = {vezes}")
print("FIM")
