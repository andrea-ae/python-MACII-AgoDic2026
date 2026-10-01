# p094-precio-acciones.py
# Análisis de precios de acciones diarias
# Dada una lista de precios de cierre de una acción durante la semana
# Encontrar el precio más alto, el más bajo y el día en que ocurrieron

aaa = 75  # formato inicio y fin
aab = aaa - 0 # formato encabezados
sep_sup = "\n" + "-" * aab
sep_inf = "-" * aab + "\n"

print("\033[H\033[J")

MensajeInicial =  "Consolidar las ventas de dos sucursales"
print("∴" * aaa)
print("✳️ " + MensajeInicial.center(aaa-5) + " ✳️")
print("∵" * aaa)

# Precios de cierre de una acción (Lunes a Domingo)
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
precios = [150.25, 152.30, 149.80, 151.00, 153.45, 154.10, 155.00]

# Encontrar el precio máximo y mínimo
precio_max = max(precios)
precio_min = min(precios)

# Encontrar la posición (el día) de esos precios
pos_max = precios.index(precio_max)
pos_min = precios.index(precio_min)

print(sep_sup)
print(f"Precios de la semana: {precios}")
print(f"El precio más alto fue ${precio_max} el día {dias[pos_max]}.")
print(f"El precio más bajo fue ${precio_min} el día {dias[pos_min]}.")
print(sep_inf)

MensajeFinal = "¡Programa terminado!"
print("∴" * aaa)
print("✳️ " + MensajeFinal.center(aaa-5) + " ✳️")
print("∵" * aaa)