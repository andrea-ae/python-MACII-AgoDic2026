# p030-verifica-suma.py
# Verificar si la suma de dos números es igual a un tercero

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("🧮   Verificar si la suma de dos números es igual a un tercero   🧮")
print("∵" * 70)

# Asignar y convertir las entradas a enteros
print("Escribe 3 números enteros separados por espacio: ")
n1, n2, n3 = map(int, input().split()) 

print("…" * 70)

# Evaluar las posibles combinaciones con if/elif
if n1 + n2 == n3:
    print(f"✔️  ¡n1 + n2 es igual a n3! ✔️\n➡️   {n1} + {n2} = {n3}")
elif n1 + n3 == n2:
    print(f"✔️  ¡n1 + n3 es igual a n2! ✔️\n➡️   {n1} + {n3} = {n2}")
elif n2 + n3 == n1:
    print(f"✔️  ¡n2 + n3 es igual a n1! ✔️\n➡️   {n2} + {n3} = {n1}")
else:
    # Si ninguna de las condiciones anteriores se cumple
    print("❌ ¡Ninguna combinación de suma es igual al tercer número! ❌")


print("∴" * 70)
print("Fin del programa.")
print("∵" * 70)