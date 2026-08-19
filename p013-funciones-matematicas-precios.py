# p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones matemáticas de redondeo

import math as mt

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("Funciones matemáticas de redondeo: ")

precio = 15.65

print(f"Precio original:               ${precio:.2f}")
print(f"Redondeo hacia arriba:         ${mt.ceil(precio):.2f}")
print(f"Redondeo hacia arriba:         ${mt.floor(precio):.2f}")
print(f"Truncar/redondeo entero:       ${mt.trunc(precio):.2f}")
print(f"Redondeo automático:           ${round(precio):.2f}")
print(f"Redondeo automático decimales: ${round(precio,3):.2f}")
