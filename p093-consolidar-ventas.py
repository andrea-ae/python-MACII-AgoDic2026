# p093-consolidar-ventas.py
# Consolidar las ventas de dos sucursales, usando listas
# Una empresa tiene dos sucursales y necesita consolidar sus ventas en una sola lista
# Se ingresan n ventaspara cada sucursal, el usuario lo define

aaa = 75  # formato inicio y fin

print("\033[H\033[J")

MensajeInicial =  "Consolidar las ventas de dos sucursales"
print("∴" * aaa)
print("✳️ " + MensajeInicial.center(aaa-5) + " ✳️")
print("∵" * aaa)

n = int(input("Ingrese el número de ventas: "))

# Inicializar listas
ventas1 = []
ventas2 = []
ventas_consolidadas = []

# Leer datos de la Sucursal 1
print("\nRegistro de ventas para la Sucursal 1:")
for i in range(n):
    venta = int(input(f"Venta {i+1}: "))
    ventas1.append(venta)

# Leer datos de la Sucursal 2
print("\nRegistro de ventas para la Sucursal 2:")
for i in range(n):
    venta = int(input(f"Venta del día {i+1}: "))
    ventas2.append(venta)

# Consolidar las ventas en una lista
ventas_consolidadas = ventas1 + ventas2
print("\nVentas consolidadas: ")
for i, venta in enumerate(ventas_consolidadas, start=1):
    print(f"Venta {i}: {venta}")

# Total de ventas en dinero
total_ventas = sum(ventas_consolidadas)
print(f"Total de ventas: {total_ventas}")

print()
MensajeFinal = "¡Programa terminado!"
print("∴" * aaa)
print("✳️ " + MensajeFinal.center(aaa-5) + " ✳️")
print("∵" * aaa)