# p067-conteo-descendente-for.py
# Imprimir números del 100 al 1 usando for

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Versión I

print("∴" * 70)
print("🔢             Imprimir números del 100 al 1 usando for             🔢")
print("∵" * 70)


print(" Iniciando secuencia de conteo descendente...")

i = 0

for x in range(100, 0, -1):
    print(f"{x:03d}", end=" ")
    i += 1

    if i % 18 == 0: print() # cambio de línea después de 18 iteraciones

print(" ")
print("∴" * 70)
print("✳️                      ¡Secuencia completada!                      ✳️")
print("∵" * 70)