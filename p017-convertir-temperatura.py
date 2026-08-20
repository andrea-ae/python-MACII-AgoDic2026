# p017-convertir-temperatura.py
# Convierta una temperatura de grados Celsius a grados Fahrenheit.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 50)
print("Convertir temperatura ")
print("." * 50)

# Entrada
c = float(input("Escribe la temperatura en grados Celisus: "))

# Proceso
f = (c * 9/5) + 32
k = c + 272.15

# Salida
salida = (
    "    TEMPERATURA\n"
    f"   Celsius: {c:>6.2f}°C\n"
    f"Fahrenheit: {f:>6.2f}°F\n"
    f"    Kelvin: {k:>6.2f} K"
)

print("." * 50)
print(salida)
print("." * 50)