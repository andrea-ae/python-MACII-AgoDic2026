# p021-distancia-entre-puntos.py
# Calcule la distancia entre dos puntos en un plano cartesiano.

import math

print("." * 60)
print("Calcular distancia entre dos puntos")
print("." * 60)

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Entrada
print("Escribe las coordenadas de los puntos A y B \nseparadas por <,> de la forma (x1, y1, x2, y2): ")
x1, y1, x2, y2 = input().split(",")
x1, y1, x2, y2 = [float(x1), float(y1), float(x2), float(y2)]

# Proceso
d = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

# Salida
salida = (
    "RESULTADO\n"
    f"Punto A: ({x1}, {y1})\n"
    f"Punto B: ({x2}, {y2})\n"
    f"La distancia calculada entre los puntos A y B es: {d:.2f}"
)

print("." * 60)
print(salida)
print("." * 60)