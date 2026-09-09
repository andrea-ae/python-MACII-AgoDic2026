# p065-conteo-ascendente-for.py
# Imprimir números del 1 al 100 usando for

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Versión I

print("∴" * 70)
print("🔢             Imprimir números del 1 al 100 usando for             🔢")
print("∵" * 70)


print(" Iniciando secuencia de conteo ascendente...")

for i in range(1, 101, 1):
    print(i, end=" ")

print(" ")
print("∴" * 70)
print("✳️                      ¡Secuencia completada!                      ✳️")
print("∵" * 70)