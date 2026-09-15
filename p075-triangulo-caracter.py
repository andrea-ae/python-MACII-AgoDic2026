# p075-triangulo-caracter.py
# Imprimir un triángulo rectángulo de caracteres

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("◢                  Dibujar un triángulo rectángulo                  ◣")
print("∵" * 70)

r = int(input("¿Cuántos renglones tendrá el triángulo? "))
c = input("¿Qué carácter quieres usar? ")

print("…" * 70)
print("               ⏳ Imprimiendo triángulo rectángulo ⏳               ")
print("…" * 70)

# Renglones
for i in range(1, r + 1):

    # Caracteres
    for j in range(1, i + 1):
        print(c, end= "")
    print()

print("∴" * 70)
print("✳️                        ¡Fin del programa!                         ✳️")
print("∵" * 70)