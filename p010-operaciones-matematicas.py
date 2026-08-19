# p010-operaciones-matematicas.py
# Demostrar el uso de operadores aritméticos

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 50)
print("Calculadora de operaciones matemáticas")
print("." * 50)

# Entrada
x = float(input("Escribe el valor de x: "))
y = float(input("Escribe el valor de y: "))

# Proceso
suma = x + y
resta = x - y
mult = x * y
div = x / y
mod = x % y
pot = x ** y
dive = x // y

# Salida
print("." * 50)
print(f"Resultados con: x = {x}, y = {y}")
print("." * 50)
print(f"x + y =  {suma:>15,.2f} <- Suma")
print(f"x - y =  {resta:>15,.2f} <- Resta")
print(f"x * y =  {mult:>15,.2f} <- Multiplicación")
print(f"x / y =  {div:>15,.2f} <- División")
print(f"x % y =  {mod:>15,.2f} <- Módulo")
print(f"x ** y = {pot:>15,.2f} <- Potencia")
print(f"x // y = {dive:>15,.2f} <- División entera")
print("." * 50)