#receba 3 numeros em ordem aleatoria e retorne o maior e o menor 

# numeros 
num=float(input("DIgite um numero "))
num2=float(input("DIgite um numero "))
num3=float(input("DIgite um numero "))

maior=max(num,num2,num3)
menor=min(num,num2,num3)

print(f"O maior entre os 3 numeros é o {maior:.1f}\nE o menor numero é o {menor:.1f}")
