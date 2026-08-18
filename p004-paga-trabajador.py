# p004-paga-trabajador.py
# Calcular la paga de un trabajador

print("\033[2J\033[H", end="")

print("Calculando la paga de un trabajador \n")

# Entrada

nombre = input("Nombre del trabajador: ")
horas = int(input("Escribe las horas trabajadas: "))
paga = float(input("Escribe su paga por hora: "))

# Proceso
tasa = 0.3
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

# Salida
print("Resumen de pagos \n ")
print(f"El trabajador {nombre}, trabajó {horas} horas, a una paga de {paga} pesos por hora.")
print(f"Paga bruta = {pagabruta:>10,.2f}")
print(f"Impuesto = {impuesto:>10,.2f}")
print(f"Paga neta = {paganeta:>10,.2f}")