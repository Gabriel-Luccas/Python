#Receba varios numeros retorne a soma total e use break
soma= cont = 0
while True:
  numero=int(input("DIgite[999 para parar] Numero: "))
  if numero == 999:
    break
  soma+=numero
  cont+=1
print(f"a soma total dos numeros digitados é {soma} e tem um total de {cont} numeros digitados  ")
