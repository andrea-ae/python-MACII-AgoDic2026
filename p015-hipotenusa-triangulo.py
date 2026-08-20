# p015-hipotenusa-triangulo.py
# Calcule la longitud de la hipotenusa de un triángulo rectángulo.

import math

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")
print("." * 50)
print("Calcular la hipotenusa de un triángulo rectángulo")
print("." * 50)
# print("Escribe la longitud del cateto opuesto y del adyacente separada por <->: ")
# co, ca = input().split("-")
# co, ca = [float(co), float(ca)]

# Entrada
co = float(input("Escribe el valor del cateto opuesto: "))
ca = float(input("Escribe el valor del cateto adyacente: "))

# Proceso
h = math.sqrt( (co**2) + (ca**2) )

# Salida

salida = (
    "Valores del triángulo rectángulo: \n"
    f"  Cateto opuesto = {co:>5.2f}\n"
    f"Cateto adyacente = {ca:>5.2f}\n"
    f"      Hipotenusa = {h:>5.2f}"
)
print("." * 50)
print(salida)
#print(f"La hipotenusa del triángulo rectángulo con cateto opuesto {co} y cateto adyacente {ca} es: {h:.2f}")
print("." * 50)