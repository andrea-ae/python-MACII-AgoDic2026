# p068-conteo-descendente-for-v2.py
# Imprimir números de n a 1 en decrementos de m usando for

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Versión II

print("∴" * 70)
print("🔢             Imprimir números descendentes usando for             🔢")
print("∵" * 70)

n = int(input("¿Desde qué número entero quieres que inicie la secuencia? "))
m = int(input("¿De cuánto quieres que sea el decremento? "))

print("…" * 70)

print("Iniciando secuencia de conteo descendente...")

for x in range(n, 0, -m):
    print(x, end=" ")

print(" ")
print("∴" * 70)
print("✳️                      ¡Secuencia completada!                      ✳️")
print("∵" * 70)