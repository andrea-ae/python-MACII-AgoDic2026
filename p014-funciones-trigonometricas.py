# p014-funciones-trigonometricas.py
# Demostrar el uso de funciones trigonométricas y conversión de grados

import math as mt

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 70)
print("Demostrar el uso de funciones trigonométricas y conversión de grados")
print("." * 70)

angulo = 45

angulo = float(input("Escribe el valor del ángulo: "))

radianes = mt.radians(angulo)

seno = mt.sin(radianes)
coseno = mt.cos(radianes)
tangente = mt.tan(radianes)

grados = mt.degrees(radianes)

print("." * 70)
print("Resumen de funciones trigonométricas y de conversión:")
print("." * 70)

# Formatear la salida con f-strings para mejor presentación
salida = (
           f"El ángulo ingresado es {angulo}°\n"
           f"El seno de {angulo:.4f}° es {seno:.4f}\n"
           f"El coseno de {angulo:.4f}° es {coseno:.4f}\n"
           f"La tangente de {angulo:.4f}° es {tangente:.4f}\n"
           f"{angulo:.4f}° equivalen a {radianes:.4f} radianes\n"
           f"{radianes:.4f} radianes equivalen a {grados:.4f}°"
           )

# Mostrar la salida formateada
print(salida)
print("." * 70)
