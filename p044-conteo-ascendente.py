# p044-conteo-ascendente.py
# Imprimir números del 1 al 100 usando while

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Versión I

print("∴" * 70)
print("🔢            Imprimir números del 1 al 100 usando while            🔢")
print("∵" * 70)


print(" Iniciando secuencia de conteo ascendente...")

c = 1
while c <= 100:
    print(f" {c:02d} ", end="")

    # Salto de renglón
    if c % 18 == 0:
        print()

    c += 1

print(" ")
print("∴" * 70)
print("✳️                      ¡Secuencia completada!                      ✳️")
print("∵" * 70)