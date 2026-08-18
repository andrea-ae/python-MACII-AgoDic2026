# p002-area-circulo.py
# Calcular el área de un círculo

import math # importa libreria de constantes y funciones matemáticas

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("Calculando el área de un círculo: \n")

radio = float(input("Escribe el radio del círculo: "))

# area = math.pi * radio**2
area = math.pi * math.pow(radio, 2)

print(f"\nEl círculo de radio {radio}, tiene un área de {area:.2f}")