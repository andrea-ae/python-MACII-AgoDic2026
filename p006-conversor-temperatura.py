# p006-conversor-temperatura.py
# Convertir una temperatura de grados Celsius a grados Fahrenheit

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("Convertir temperatura de Celsius a Fahrenheit: \n")

cel = float(input("Escribe la temperatura en grados Celsius: "))
far = (cel * 9/5) + 32

print(f"\nLa temperatura de {cel} grados Celsius equivale a {far} grados Fahrenheit.")