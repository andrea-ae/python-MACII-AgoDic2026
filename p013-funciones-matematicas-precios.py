# p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones matemáticas de redondeo

import math as mt

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 50)
print("Funciones matemáticas de redondeo ")
print("." * 50)

precio = float(input("Escribe el precio a redondear: "))

print("." * 50)
print(f"Precio original:          ${precio:.2f}")
print(f"Hacia arriba:             ${mt.ceil(precio):.2f}")
print(f"Hacia arriba:             ${mt.floor(precio):.2f}")
print(f"Truncar/entero:           ${mt.trunc(precio):.2f}")
print(f"Automático:               ${round(precio):.2f}")
print(f"Automático con decimales: ${round(precio,2):.2f}")
print("." * 50)