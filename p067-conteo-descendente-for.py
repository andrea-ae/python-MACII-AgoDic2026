# p067-conteo-descendente-for.py
# Imprimir números del 100 al 1 usando for

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Versión I

print("∴" * 70)
print("🔢             Imprimir números del 100 al 1 usando for             🔢")
print("∵" * 70)


print(" Iniciando secuencia de conteo descendente...")

for x in range(100, 0, -1):
    print(x, end=" ")

print(" ")
print("∴" * 70)
print("✳️                      ¡Secuencia completada!                      ✳️")
print("∵" * 70)