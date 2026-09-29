# p090-iterar-lista.py
# Iterar por los elementos de una lista
# 1 por elemento, 2 por índice, 3 por elemento sumando 2, 4 por índice sumando 10, 5 con enumerate

aae = 60
#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

MensajeInicial =  "Iterar por los elementos de una lista:"
print("∴" * aae)
print("✳️ " + MensajeInicial.center(aae-5) + " ✳️")
print("∵" * aae)

num = [2, 4, 6, 8, 10, 12, 14, 16]


print(f"Números a procesar: {num}\n")

print("…" * aae)
print("1. Iteración por elemento:")

for n in num:
    print(n, end=" ")

print("…" * aae)    
print("\n\n2. Iteración por índice:")

for i in range(len(num)):
    print(num[i], end=" ")

print("…" * aae)
print("\n\n3. Iteración por elemento para sumar 2")

for n in num:
    n + 2
    print(n, end=" ")

print("…" * aae)
print("\n\n4. Iteración por índice para sumar 10")

for i in range(len(num)):
    num[i] += 10
    print(num[i], end=" ")

print("…" * aae)
print("\n\n5. Iteración con enumerate")
print("Pos\tValor")

for i, n in enumerate(num):
    print(i,"\t", n,)