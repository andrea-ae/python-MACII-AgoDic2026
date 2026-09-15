# p074-tablas-todas.py
# Imprimir las tablas de multiplicar de 1 a t, hasta n

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 60)
print("🔢                 TABLAS DE MULTIPLICAR                 🔢")
print("∵" * 60)

t = int(input("¿Hasta qué tabla de multiplicar deseas generar? "))
n = int(input("¿Hasta qué número deseas multiplicar cada tabla? "))

print("…" * 60)
print("            ⏳ Generando Tablas de Multiplicar ⏳            ")
print("…" * 60)

# Hasta qué tabla va a imprimir
for i in range(1, t + 1):

    print("=" * 30)
    print(f" ------- TABLA DEL {i} ------- ")
    print("=" * 30)

    # Hasta qué número va a imprimir cada tabla
    for j in range(1, n + 1):
        resultado = i * j

        print(f"\t{i} x {j} = {resultado}")
    print("=" * 30)
    print()

print("∴" * 60)
print("✳️                    Fin del programa                     ✳️")
print("∵" * 60)