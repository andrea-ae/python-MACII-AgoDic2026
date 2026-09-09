# p066-conteo-ascendente-for-v2.py
# Imprimir números de 1 a n en incrementos de m usando for

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Versión II

print("∴" * 70)
print("🔢              Imprimir números del 1 a n usando for              🔢")
print("∵" * 70)

n = int(input("¿Hasta qué número entero quieres que llegue la secuencia? "))
m = int(input("¿De cuánto quieres que sea el incremento? "))

print("…" * 70)

print("Iniciando secuencia de conteo ascendente...")

for i in range(1, n+1, m):
    print(i, end=" ")

print(" ")
print("∴" * 70)
print("✳️                      ¡Secuencia completada!                      ✳️")
print("∵" * 70)