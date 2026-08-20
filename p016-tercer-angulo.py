# p016-tercer-angulo-py
# Determinar el tercer ángulo de un triángulo.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 50)

# Entrada
print("Escribe los dos ángulos (en grados) conocidos del triángulo")

ang1 = float(input("Ángulo 1: "))
ang2 = float(input("Ángulo 2: "))

# ang1, ang2 = input().split()
# ang1, ang2 = [float(ang1), float(ang2)]

# Proceso
ang3 = 180 - (ang1 + ang2)

# Salida
salida = (
    "RESULTADO\n"
    f"Ángulo 1: {ang1:>4.2f}°\n"
    f"Ángulo 2: {ang2:>4.2f}°\n"
    f"Ángulo 3: {ang3:>4.2f}°"
)

print("." * 50)
print(salida)
# print(f"Ángulo 1: {ang1:>4.2f}°")
# print(f"Ángulo 2: {ang2:>4.2f}°")
# print(f"Ángulo 3: {ang3:>4.2f}°")
print("." * 50)