# p009-promedio-de-calificaciones.py
# Calcular el promedio de tres calificaciones ingresadas por el usuario.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("Calculando el promedio de tres calificaciones: \n")

# Entrada
print("Escribe las tres calificaciones separadas por un <Espacio>: ")
cal1, cal2, cal3 = input().split()
#print(type(cal1), type(cal2), type(cal3))
cal1, cal2, cal3 = [float(cal1), float(cal2), float(cal3)]
#print(type(cal1), type(cal2), type(cal3))

# Proceso
suma = cal1 + cal2 + cal3
promedio = suma / 3

# Salida
print(f"\nLas calificaciones son: {cal1}, {cal2}, {cal3}")
print(f"La suma es: {suma:.2f}")
print(f"El promedio es: {promedio:.2f}")