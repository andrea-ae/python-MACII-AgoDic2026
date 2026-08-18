# p003-area-triangulo.py
# Calcular el área de un triángulo

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("Calculando el área de un triángulo: \n")

print("Escribe la base y la altura del triángulo, separados por un <Enter>: ")

base, altura = int(input()), int(input())

area = (base * altura)/2

print(f'\nEl triángulo de base {base} y altura {altura} tiene un area de {area}')