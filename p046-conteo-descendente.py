# p046-conteo-descendente.py
# Imprimir números del 100 al 1 usando while

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Versión I

print("∴" * 70)
print("🔢            Imprimir números del 100 al 1 usando while            🔢")
print("∵" * 70)


print(" Iniciando secuencia de conteo descendente...")

c = 100
while c >= 1:
    print(f" {c:03d} ", end="")

    # Salto de renglón
    if (100 - c + 1) % 14 == 0:
        print()

    c -= 1

print(" ")
print("∴" * 70)
print("✳️                      ¡Secuencia completada!                      ✳️")
print("∵" * 70)