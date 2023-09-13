# try e exept
try:
    a = int(input("D: "))
    b = int(input("D: "))
    v=a/b
except ZeroDivisionError:
    print("imposivel divisão por 0")
except TypeError:
    print("Valor digitado invalido")
except ValueError:
    print("Valor digitado invalido")

  

