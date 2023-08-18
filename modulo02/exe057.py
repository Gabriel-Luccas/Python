# Receba M of F enquanto esse valor n for m ou f reinicie 
sexo=(input("Digite [M/F]: ")).upper().strip()
while sexo != "M" and sexo != "F":
  print("Informação inválida")
  sexo = input("Digite [M/F]: ").upper().strip()
if sexo == "M":
    print("Masculino")
elif sexo == "F":
    print("Feminino")
print("FIM")
