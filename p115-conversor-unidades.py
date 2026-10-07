# p115-conversor-unidades.py
# Conversor de unidades de longitud usando diccionarios

MeIni =  "Conversor de unidades de longitud usando diccionarios" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 75  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 0 # Formato encabezados|||||||||||||||||||||||||||||||||||||
LinSup = "∴" * aaa # Línea superior ....................................
LinInf = "∵" * aaa # Línea inferior ....................................
SepSup = "\n" + "-" * aab # Separador superior /////////////////////////
SepInf = "-" * aab + "\n" # Separador inferior /////////////////////////
error = "❌  ¡Ha ocurrido un error! ❌" # Mensaje error ---------------
exito = "✔️  ¡Operación exitosa! ✔️"    # Mensaje éxito ---------------

gelb = "\033[93m" # amarillo
grun = "\033[92m" # verde
rot = "\033[91m" # rojo
blau = "\033[94m" # azul
default = "\033[0m"

# print(sep_sup)
# print(f"{exito :^{aab}}\n")
# texto = f"Gasto de {gasto} agregado."
# print(f"{texto:^{aab}}")
# print(sep_inf)

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

conversiones = {
'km': 1000,
'm': 1,
'cm': 0.01,
'mm': 0.001
}

longitud = float(input("Escribe la longitud: "))

while True:
    unidad = input("Escribe su unidad (km, m, cm ,mm): ").lower()
    if unidad in conversiones:
        break
    else:
        print("Unidad no válida. Intente de nuevo.")

resultado = longitud * conversiones[unidad]

print(f"{longitud:,.2f} {unidad} son {resultado:,.2f} metros")

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
