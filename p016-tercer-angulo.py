# p016-tercer-angulo-py
# Determinar el tercer ángulo de un triángulo.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("Escribe los dos ángulos (en grados) conocidos del triángulo, separados por un <Espacio>: ")

ang1, ang2 = input().split()
ang1, ang2 = [float(ang1), float(ang2)]

ang3 = 180 - (ang1 + ang2)

print(f"\nÁngulo 1: {ang1:>4.2f}°")
print(f"Ángulo 2: {ang2:>4.2f}°")
print(f"Ángulo 3: {ang3:>4.2f}°")