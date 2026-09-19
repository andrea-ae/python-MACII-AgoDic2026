# p082-cuadro-hueco-caracter.py
# Solicitar al usuario que ingrese el tamaño del lado de un cuadrado y el carácter con el que se dibujará
# Imprimir en la consola un "cuadrado hueco", donde el carácter solo se utilice para dibujar el contorno del mismo.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("▢                    Dibujar un cuadrado hueco                      ▢")
print("∵" * 70)

l = int(input("¿Cuánto va a medir cada lado del cuadrado? "))
c = input("¿Qué carácter quieres usar? ")

print("…" * 70)
print("               ⏳ Imprimiendo cuadrado hueco ⏳               ")
print("…" * 70)

# Renglones
for i in range(1, l + 1):

    # Caracteres
    for j in range(1, l + 1):

        # Identifica si es el renglón 1 o el l (i == 1, i == l)
        # Identifica si es la colimna 1 o la l (j == 1, j == l)
        if i == 1 or i == l or j == 1 or j == l:
            print(c, end=" ")
        else:
            # Identifica si es el centro
            print(" ", end=" ")
    print()

print("∴" * 70)
print("✳️                        ¡Fin del programa!                         ✳️")
print("∵" * 70)