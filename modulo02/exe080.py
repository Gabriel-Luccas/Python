# receba 5 valores e os coloque na orem crecente sem usar sorte 
valores=[]
for _ in range(5):
  valor=int(input("Numero: "))
  valores.append(valor)

# buble sorte 
Len_valores= len(valores) # tamanho da lista para repetição 
for j in range(Len_valores-1): # repete o precesso varias vezes 
  for i in range(Len_valores-1): # anda os "i" indeces da lista -1 
    if valores[i] > valores[i+1]: # se indece andado for maior que o seu proixo 
      valores[i],valores[i+1]= valores[i+1],valores[i] # troca a posição dos  elementos 
print(valores)