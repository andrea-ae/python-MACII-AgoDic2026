# p078-combina-colores.py
# Generar combinaciones de dos colores a partir de una lista

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("🌈 🖌️                  Combinaciones de colores                  🖌️ 🌈")
print("∵" * 70)

c = input("Escribe los colores (o palabras) separados por comas: ").replace(' ','').split(',')

print("…" * 70)
print(f"Colores base: {c}")
print("…" * 70)

print("Combinaciones:")

# Primer color
for c1 in c:

    # Segundo color
    for c2 in c:

        # Evitar que se repitan
        if c1 != c2:
            print(f"{c1} - {c2}")

  

print("∴" * 70)
print("✳️                        ¡Fin del programa!                         ✳️")
print("∵" * 70)