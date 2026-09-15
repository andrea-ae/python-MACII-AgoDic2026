# p077-factorial-numeros.py
# Calcular el factorial de n números
# Imprime el factorial de los números desde 1 hasta n

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("❗                Calcula el factorial de n números                ❗")
print("∵" * 70)

try:
    n = int(input("¿Hasta qué número deseas calcular el factorial? "))

    print("…" * 70)
    print("               ⏳ Imprimiendo factoriales ⏳               ")
    print("…" * 70)

    # Número
    for x in range(1, n+1):
        print(f"{x}! = ", end="")
        f = 1 

        # Factorial de cada número
        for i in range(1, x + 1):
            print(f"{i} {'x' if x > i else ''} ", end="")
            f = f * i 
            
        print(f"= {f:,}")

except ValueError:
    print("…" * 70)
    print("❌ ¡Ha ocurrido un error! ❌ \nSolo se aceptan números enteros.")

print("∴" * 70)
print("✳️                        ¡Fin del programa!                         ✳️")
print("∵" * 70)