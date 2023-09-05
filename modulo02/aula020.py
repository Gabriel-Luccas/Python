def soma(a, b):
    s = a + b
    print(f"{a} + {b}")
    print(f"= {s}")


def double(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
        

valores = [2,4,6]
double(valores)
print(valores)


soma(10, 45)
soma(a=34, b=12)
soma(b=173, a=953)
