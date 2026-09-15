# p079-suma-potencias.py
# Sumar las potencias de un número x desde x^1 hasta x^n

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("^                         SUMA DE POTENCIAS                         ^")
print("∵" * 70)

try:
    x = int(input("Escribe el valor de x: "))
    n = int(input("Escribe el número de términos: "))
    total = 0
    #i = 0

    print("…" * 70)
    print(F"           ⏳ Calculando la serie S = x^1 + ... + x^{n} ⏳           ")
    print("…" * 70)

    print("  S = ", end="")    

    # Número
    for i in range(1, n + 1):
        ta = 1

        # Potencia
        for j in range(i):
            ta = ta * x 
        print(f"{x}^{i} {'+' if n > i else ''} ", end="")
        total = total + ta 

        if i % 9 == 0: 
            print()
            print("      ", end="")
            
    print(f"= {total:,}")

except ValueError:
    print("…" * 70)
    print("❌ ¡Ha ocurrido un error! ❌ \nSolo se aceptan números enteros.")

print("∴" * 70)
print("✳️                        ¡Fin del programa!                         ✳️")
print("∵" * 70)