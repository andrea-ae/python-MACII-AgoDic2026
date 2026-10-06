# p103b-resumen-ventas.py
# Transforma una lista de ventas usando una función y compresión de listas
# La transformación aplica tres pasos en una misma función
# la función procesa la trasformación, luego en el programa principal es llamada

# VERSION II

MeIni =  "Resumen de ventas versión II" # Mensaje inicial --------
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

# esta función aplica tres fansformaciones a cada elemento que le llega como parámetro (una venta)
# regresa el resultado de la transformación
def transformar_venta(venta):
    # PASO 1: si la venta es mayor o igual a 1000 aplica un descuento del 10%
    if venta >= 1000:
        venta = venta * 0.90
    else:
        # PASO 2: si la venta es menor que 1000 aplica un descuento del 5%
        venta = venta * 0.95

    # PASO 3: si la venta es mayor a 1000 regresa la venta, de lo contrario regresa None
    return venta if venta > 1000 else None
# ----------------------------------------------------------------------------------------

print("\033[2J\033[1;1H")

print(blau + LinSup + blank + MeIni.upper().center(aaa) + blank + LinInf + default)

# ventas del mes (10) varias con decimales
ventas = [1000, 2000, 3000, 400, 500, 1500.50, 800.75, 1200.25, 600.60, 2500.80]
ventas_transformadas = [transformar_venta(venta) for venta in ventas]

print(italic + blank + f"    Ventas originales: {ventas}" + blank)
print(rot + bold + f"Ventas transformadas: {ventas_transformadas}" + default  + blank)

print(blau + LinSup + blank + MeFin.upper().center(aaa) + blank + LinInf + default)