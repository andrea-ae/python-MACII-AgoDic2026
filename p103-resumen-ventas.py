# p103-resumen-ventas.py
# Transforma y filtra ventas con comprensiones

MeIni =  "Resumen de ventas" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 75  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
LinSup = "∴" * aaa # Línea superior ....................................
LinInf = "∵" * aaa # Línea inferior ....................................
blank = "\n"

blau = "\033[94m"   # azul
default = "\033[0m" # default
bold = "\033[1m"    # negritas
italic = "\033[3m"  # cursiva
gelb = "\033[93m"   # amarillo
grun = "\033[92m"   # verde
lila = "\033[35m"   # verde
rot = "\033[91m"    # rojo

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + blank + MeIni.upper().center(aaa) + blank + LinInf + default)

ventas = [250, 800, 1200, 450, 1800, 950]

# Ventas mayores a 1000 aplica 10% de descuento, menores a 1000 aploca 5% de descuento
descuento = [round(v * 0.90, 2) if v >= 1000 else v * 0.95 for v in ventas]

relevantes = [v for v in descuento if v > 1000]

print(italic + blank + f"                 Ventas originales: {ventas}" + blank)
print(bold + gelb + f"              Ventas con descuento: {descuento}" + blank)
print(grun + f"Ventas relevantes (mayores a 1000): {relevantes}" + blank)
print(rot + f"        Total de ventas relevantes: ${sum(relevantes)}" + default  + blank)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)