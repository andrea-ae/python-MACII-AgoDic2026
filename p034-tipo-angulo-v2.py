# p034-tipo-angulo-v2.py
# Mostrar el tipo de ángulo según su medida en grados
# Dado un ángulo en el rango 0 a 360

print("VERSIÓN II")

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("📐       Mostrar el tipo de ángulo según su medida en grados       📐")
print("∵" * 70)

# Pedir al usuario que ingrese un ángulo
angulo = int(input("Escribe un ángulo en grados: "))

print("." * 70)

# La estructura if/elif evalúa cada posible tipo de ángulo
if angulo < 0 or angulo > 360:
    # Este if de validación es útil para un mejor manejo de datos
    print(f"❌  El ángulo de {angulo:.2f}° está fuera del rango de 0 a 360 grados.  ❌")
elif angulo < 90:
    print(f"➡️   El ángulo de {angulo:.2f}° es un ángulo AGUDO.")
elif angulo == 90:
    print(f"➡️   El ángulo de {angulo:.2f}° es un ángulo RECTO.")
elif angulo < 180:
    print(f"➡️   El ángulo de {angulo:.2f}° es un ángulo OBTUSO.")
elif angulo == 180:
    print(f"➡️   El ángulo de {angulo:.2f}° es un ángulo LLANO.")
elif angulo < 360:
    print(f"➡️   El ángulo de {angulo:.2f}° es un ángulo CÓNCAVO.")
else: # En caso de que el ángulo sea exactamente 360
    print(f"➡️   El ángulo de {angulo:.2f}° es un ángulo COMPLETO.")


print("∴" * 70)
print("Fin del programa.")
print("∵" * 70)