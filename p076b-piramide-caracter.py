# p076b-piramide-caracter.py
# Imprimir una rombo de caracteres

# Versión II

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 60)
print("◆               Dibujar rombo de caracteres               ◆")
print("∵" * 60)

altura = int(input("¿Cuántos renglones tendrá el triángulo? "))
c = input("¿Qué carácter quieres usar? ")

print("…" * 60)
print("          ⏳ Imprimiendo rombo ⏳          ")
print("…" * 60)

espacios = caracteres = 0

# Renglones
for i in range(1, altura + 1):
    espacios = altura - i
    caracteres = 2 * i - 1

    # Espacios
    for e in range(espacios):
        print(" ", end="")

    # Caracteres
    for j in range(1, caracteres + 1):
        print(c, end="")
    print()

for i in range(altura - 1, 0, -1):
    espacios = altura - i
    caracteres = 2 * i - 1

    for e in range(espacios):
        print(" ", end="")
    for j in range(caracteres):
        print(c, end="")
    print()

print("∴" * 60)
print("✳️                   ¡Fin del programa!                   ✳️")
print("∵" * 60)