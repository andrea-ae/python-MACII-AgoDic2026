# p012-funcion-matematicas-equacion.py 
# Evaluar la función f(x, y) = 3x**2 + √(x**2 + y**2) + e^(ln(x))
# Ejemplifica el uso de funciones matemáticas dentro de math

import math as mt

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")


x = float(input("Escribe el valor de x: "))
y = float(input("Escribe el valor de y: "))

# fxy = 3 * mt.pow(x, 2) + mt.sqrt(mt.pow(x,2) + mt.pow(y,2)) + mt.exp(mt.log(x))
# print(f"El resultado es: {fxy:,.2f}")

fxy2 = 3 * x**2 + mt.sqrt(x**2 + y**2) + mt.exp(mt.log(x))
print(f"\nEl resultado es: {fxy2:,.2f}")