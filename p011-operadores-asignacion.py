# p011-operadores-asignacion.py
# Demostrar el uso de los operadores de asignación

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 50)
print("Operadores de asignación en Python")
print("." * 50)

# Operador de asignación básico (=)
x = int(input("Escribe el valor de x: "))


print("." * 50)
print("Operadores de asignación de x")
print("." * 50)

print(f"     x:  {x:>5,.2f} <- Valor inicial de x")

# Aplicar diferentes operadores de asignación
x += 5 # x = x + 5
print(f"x += 5:  {x:>5,.2f} <- Sumar 5 a x")

x -= 3 # x = x - 3
print(f"x -= 3:  {x:>5,.2f} <- Restar 3 a x")

x *= 2 # x = x * 2
print(f"x *= 2:  {x:>5,.2f} <- Multiplicar x por 2")

x /= 4 # x = x / 4
print(f"x /= 4:  {x:>5,.2f} <- Dividir x entre 4")

x %= 3 # x = x % 3
print(f"x %= 3:  {x:>5,.2f} <- Módulo 3 de x")

x **= 2 # x = x ** 2
print(f"x **= 2: {x:>5,.2f} <- x elevada al cuadrado")

x //= 2 # x = x // 2
print(f"x //= 2: {x:>5,.2f} <- Dividir x entre 2 (entero)")
print("." * 50)