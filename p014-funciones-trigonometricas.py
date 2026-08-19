# p014-funciones-trigonometricas.py
# Demostrar el uso de funciones trigonométricas y conversión de grados

import math as mt

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("Demostrar el uso de funciones trigonométricas y conversión de grados")

angulo = 45
radianes = mt.radians(angulo)

seno = mt.sin(radianes)
coseno = mt.cos(radianes)
tangente = mt.tan(radianes)

grados = mt.degrees(radianes)

salida = (
          "\nResumen de funciones trigonométricas y de conversión\n"
          f"El seno es {seno:.4f}\n"
          f"El coseno es {coseno:.4f}\n"
          f"La tangente es {tangente:.4f}\n"
          f"El ángulo {angulo} grados, en radianes equivale a {radianes:.4f}\n"
       #   f"Los {radianes:.4f} radianes, equivalen a {grados:.f}°"
          )


