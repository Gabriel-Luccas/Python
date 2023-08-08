#me de um angulo e retorne seu sen con e tang

import math
angulo=float(input("Me de um angulo e eu retornarei seu sen con e tang "))
radio=math.radians(angulo)
sin=math.sin(radio)
cos=math.cos(radio)
tan=math.tan(radio) 
print(f"o angulo {angulo}\ntem como seno {sin:.2f}\ne como coseno {cos:.2f}\n e como tangeno {tan:.2f}")