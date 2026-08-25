# p025-verificar-suma.py
# Pide tres números, suma los dos primeros y verifica si el resultado es igual al tercero

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 70)
print("🤔 Verificar si la suma de dos números es igual al tercero 🤔")
print("." * 70)

# Entrada
n1 = int(input("1️⃣  Escribe el primer número entero:  "))
n2 = int(input("2️⃣  Escribe el segundo número entero: "))
n3 = int(input("3️⃣  Escribe el tercer número entero:  "))

print("." * 70)

suma = n1 + n2

if suma == n3:
    print(f"✔️  ¡Correcto! ✔️ \n{n1} + {n2} = {n3} y {suma} es igual a {n3}.")
else:
    print(f"❌ ¡Incorrecto! ❌ \n{n1} + {n2} = {suma} y {suma} es diferente a {n3}.")

print("." * 70)
print("Fin del programa.")
print("." * 70)