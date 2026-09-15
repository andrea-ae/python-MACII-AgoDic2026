# p076-piramide-caracter.py
# Imprimir una piramide de caracteres

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 60)
print("▲              Dibujar pirámide de caracteres              ▲")
print("∵" * 60)

altura = int(input("¿Cuántos renglones tendrá el triángulo? "))
c = input("¿Qué carácter quieres usar? ")

print("…" * 60)
print("          ⏳ Imprimiendo pirámide ⏳          ")
print("…" * 60)

# altura = 11
# c = "*"
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


print("∴" * 60)
print("✳️                   ¡Fin del programa!                   ✳️")
print("∵" * 60)