# p010-operaciones-matematicas.py
# Demostrar el uso de operadores aritmeticos

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("-" * 50)
print("Calculadora de operaciones matemáticas")
print("-" * 50)

x = float(input("Escribe el valor de x: "))
y = float(input("Escribe el valor de y: "))

suma = x + y
resta = x - y
mult = x * y
div = x / y
mod = x % y
pot = x ** y
dive = x // y

print(f"Resultado de las operaciones realizadas: \n")
print("=" * 50)
print(f"Números: x = {x}, y = {y}")
print(f"x + y = {suma:>20,.2f} <- Suma")
print(f"Resta:           {resta:>20,.2f}")
print(f"Multiplicación:  {mult:>20,.2f}")
print(f"División:        {div:>20,.2f}")
print(f"Módulo:          {mod:>20,.2f}")
print(f"Potencia:        {pot:>20,.2f}")
print(f"División entera: {dive:>20,.2f}")
print("=" * 50)