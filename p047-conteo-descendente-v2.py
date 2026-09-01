# p047-conteo-descendente-v2.py
# Imprimir números de n a 1 usando while

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Versión II

print("∴" * 70)
print("🔢           Imprimir números descendentes usando while            🔢")
print("∵" * 70)

n = int(input("¿Desde qué número entero quieres que inicie la secuencia? "))
m = int(input("¿De cuánto quieres que sea el decremento? "))

print("…" * 70)

print("Iniciando secuencia de conteo descendente...")

c = n
while c >= 1:
    print(f"{c:03d} ", end="")

    c -= m

print(" ")
print("∴" * 70)
print("✳️                      ¡Secuencia completada!                      ✳️")
print("∵" * 70)