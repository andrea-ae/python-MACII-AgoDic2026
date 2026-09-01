# p048-multiplos-continue.py
# Imprimir solo los múltiplos de 10 hasta 200

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Versión II

print("∴" * 70)
print("🔢           Buscando múltiplos de 10 entre 1 y 200...            🔢")
print("∵" * 70)

c = 0
while c < 200:
    c += 1
    if c % 10 != 0:
        # Ignora todo lo que sigue y salta a la siguiente iteración
        continue
    # Esta línea SÓLO se ejecuta si el 'if' fue falso (es decir, si es un múltiplo de 10)
    print(f"{c:03d} ", end="")

print(" ")
print("∴" * 70)
print("✳️                      ¡Búsqueda finalizada!                      ✳️")
print("∵" * 70)