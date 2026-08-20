# p018-area-volumen-cilindro.py
# Calcular el área y volumen de un cilindro.

import math

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 50)
print("Calcular volumen y área de un cilindro")
print("." * 50)

# Entrada
print("Escribe el radio y la altura del cilindro, separada por <->: ")
r, h = input().split("-")
r, h = [float(r), float(h)]

# Proceso
area = 2 * math.pi * ( r + h)
volumen = math.pi * (r**2) * h

# Salida
salida = (
    #"RESULTADO\n"
    f"El cilindro con radio {r} y altura {h}, tiene un \n"
    f"   área de: {area:>10,.2f}\n"
    f"volumen de: {volumen:>10,.2f}"
)

print("." * 50)
print(salida)
print("." * 50)

# print(f"\nEl cilindro con radio {r} y altura {h}, tiene un: ")
# print(f"Área de: {area:.2f}")
# print(f"Volumen de: {volumen:.2f}")