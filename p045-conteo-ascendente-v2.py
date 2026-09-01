# p045-conteo-ascendente-v2.py
# Imprimir números de 1 a n usando while

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Versión II

print("∴" * 70)
print("🔢            Imprimir números ascendentes usando while            🔢")
print("∵" * 70)

n = int(input("¿Hasta qué número entero quieres que llegue la secuencia? "))
m = int(input("¿De cuánto quieres que sea el incremento? "))

print("…" * 70)

print("Iniciando secuencia de conteo ascendente...")

c = 1
while c <= n:
    print(f"{c:03d} ", end="")

    c += m

print(" ")
print("∴" * 70)
print("✳️                      ¡Secuencia completada!                      ✳️")
print("∵" * 70)