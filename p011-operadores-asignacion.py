# p011-operadores-asignacion.py
#

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("Operadores de asignación en Python")

x = int(input("Escribe el valor de x: "))

x += 5
print(f"Sumar 5 a x: {x}")

x -= 3
print(f"Restar 3 a x: {x}")

x *= 2
print(f"Multiplicar x por 2: {x}")

x /= 4
print(f"Dividir x entre 4: {x}")

x %= 4
print(f"Módulo 3 de x: {x}")

x **= 2
print(f"x elevada al cuadradp: {x}")

x //= 2
print(f"Dividir x entre 2 ent: {x}")