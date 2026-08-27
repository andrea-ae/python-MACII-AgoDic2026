# p035-tipo-triangulo.py
# Clasificar un triángulo según la longitud de sus tres lados.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("🔼     Clasificar un triángulo según la longitud de sus lados     🔼")
print("∵" * 70)

print("Ingresa la longitud de los tres lados de un triángulo: ")

# Solicitar la longitud de los lados
lado_a = float(input("Lado A = "))
lado_b = float(input("Lado B = "))
lado_c = float(input("Lado C = "))

print("…" * 70)
# Usar la sentencia elif para verificar las condiciones en orden
if lado_a == lado_b and lado_b == lado_c:
   # print(f"A = {lado_a}, \tB = {lado_b} y \tC = {lado_c} ")
    print(f"Como todos sus los lados son iguales:")
    print(f"➡️  Es un triángulo ▶ EQUILÁTERO ◀")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
   # print(f"A = {lado_a}, \tB = {lado_b} y \tC = {lado_c} ")
    print(f"Como dos de sus lados son iguales:")
    print(f"➡️  Es un triángulo ► ISÓSCELES ◄ ")
else:
  #  print(f"A = {lado_a}, \tB = {lado_b} y \tC = {lado_c} ")
    print(f"Como ningún lado es igual:")
    print(f"➡️  Es un triángulo ◣ ESCALENO ◢")


print("∴" * 70)
print("Fin del programa.")
print("∵" * 70)