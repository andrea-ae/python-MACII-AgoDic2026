# p022-resistencia-equivalente-paralelo.py
# Calcular la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 60)
print("Calcular la resistencia total de un circuito en paralelo")
print("." * 60)

# Entrada
print("Escribe el valor de las cuatro resistencias separadas por un <Espacio>: ")
r1, r2, r3, r4 = input().split()
r1, r2, r3, r4 = [float(r1), float(r2), float(r3), float(r4)]

# Proceso
rt = 1 / ( (1/r1) + (1/r2) + (1/r3) + (1/r4) )

# Salida
salida = (
    "RESULTADO\n"
    f"Resistencia 1: {r1:.4f} \u03A9\n"
    f"Resistencia 2: {r2:.4f} \u03A9\n"
    f"Resistencia 3: {r3:.4f} \u03A9\n"
    f"Resistencia 4: {r4:.4f} \u03A9\n"
    f"La resistencia equivalente es: {rt:.4f} \u03A9"
)

print("." * 60)
print(salida)
print("." * 60)

