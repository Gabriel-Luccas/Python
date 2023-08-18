#fibonacc

#fib_sequence é o nome da lista que estamos criando para armazenar os termos da sequência de Fibonacci.[0, 1] é a notação de lista em Python, onde estamos criando uma lista que contém dois elementos: 0 e 1. Esses são os dois primeiros termos da sequência de Fibonacci
n=int(input("termos: "))
termo_desejado =int(input("termo desejado: "))
fib_sequence = [0, 1]
while len(fib_sequence) < n:
  next_fib = fib_sequence[-1] + fib_sequence[-2]
  fib_sequence.append(next_fib)
if termo_desejado < len(fib_sequence):
    print(f"O termo {termo_desejado} da sequência é: {fib_sequence[termo_desejado]}")
else:
    print("Índice fora do intervalo da sequência gerada.")
print(fib_sequence)

  