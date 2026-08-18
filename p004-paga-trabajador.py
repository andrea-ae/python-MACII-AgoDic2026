# p004-paga-trabajador.py
# Calcular la paga de un trabajador con y sin impuestos

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("Calculando la paga de un trabajador: \n")

# Entrada
nombre = input("Escribe el nombre del trabajador: ")
horas = int(input("Escribe las horas trabajadas: "))
paga = float(input("Escribe su paga por hora: "))

# Proceso
tasa = 0.03 
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

# Salida
print("Resumen de pagos: \n ")
print(f"El trabajador {nombre}, trabajó {horas} horas, con una paga de {paga} pesos por hora. \n")
print(f"Paga bruta = {pagabruta:>10,.2f}")
print(f"Impuesto   = {impuesto:>10,.2f}")
print(f"Paga neta  = {paganeta:>10,.2f}")