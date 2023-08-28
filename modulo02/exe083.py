#confirmar se a expressão esta correta 
expre=str(input("Digite a expresão: "))
pilha=[]
for simb in expre:
  if simb == "(":
    pilha.append()
  elif simb == ")":
    if len(pilha) > 0:
      pilha.pop()
    else:
      break
if len(pilha) == 0 :
  print("Está correto")
else:
  print("Incorreto")