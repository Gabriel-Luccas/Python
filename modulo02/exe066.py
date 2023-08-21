#Receba varios numeros retorne a soma total e use break
soma=0
while True:
  numero=int(input("DIgite[999 para parar] Numero: "))
  if numero == 999:
    break
  soma+=numero
print(f"a soma total dos numeros digitados é {soma} ")
