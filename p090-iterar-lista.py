# p090-iterar-lista.py
# Iterar por los elementos de una lista
# 1 por elemento, 2 por índice, 3 por elemento sumando 2, 4 por índice sumando 10, 5 con enumerate

aaa = 75  # formato inicio y fin
aab = aaa - 0 # formato encabezados

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

MensajeInicial =  "Iterar sobre una lista:"
print("∴" * aaa)
print("✳️ " + MensajeInicial.center(aaa-5) + " ✳️")
print("∵" * aaa)

num = [2, 4, 6, 8, 10, 12, 14, 16]

print(f"\nNúmeros a procesar: {num}")

print(f"\n{'~~ 1. Iteración por elemento ' :~<{aab}}")
for n in num:
    print(n, end=" ")

print(f"\n\n{'~~ 2. Iteración por índice ' :~<{aab}}")
for i in range(len(num)):
    print(f"índice {i}: {num[i]}", end="\t")
    if (i + 1) % 4 == 0: print() # cambio de línea después de 4 iteraciones

print(f"\n{'~~ 3. Iteración por elemento para sumar 2 ' :~<{aab}}")
for n in num:
    n + 2
    print(n, end=" ")

print(f"\n\n{'~~ 2. Iteración por índice para sumar 10 ' :~<{aab}}")
for i in range(len(num)):
    num[i] += 10
    print(f"índice {i}: {num[i]}", end="\t")
    if (i + 1) % 4 == 0: print() # cambio de línea después de 4 iteraciones
    
print(f"\n{'~~ 5. Iteración con enumerate ' :~<{aab}}")
for i, n in enumerate(num):
    print(f"índice {i}: {n}", end="\t")
    if (i + 1) % 4 == 0: print() # cambio de línea después de 4 iteraciones

# Elevar al cuadrado cada elemento y guardar el resultado en la lista original
original = num.copy()
print(f"\n{'~~ 6. Elevar al cuadrado cada elemento ' :~<{aab}}")
print(f"                 Lista original: {original}")
for i in range(len(num)):
    num[i] = num[i] ** 2
print(f"Lista con elementos al cuadrado: {num} \n")

MensajeFinal = "¡Programa terminado!"
print("∴" * aaa)
print("✳️ " + MensajeFinal.center(aaa-5) + " ✳️")
print("∵" * aaa)