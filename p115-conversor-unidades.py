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

gelb = "\033[93m" # amarillo
grun = "\033[92m" # verde
rot = "\033[91m" # rojo
blau = "\033[94m" # azul
default = "\033[0m"

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

conversiones = {
'km': 1000,   # 1 km = 1000 m
'm': 1,       # 1 m = 1 m
'cm': 0.01,   # 1 cm = 0.01 m
'mm': 0.001   # 1 mm = 0.001 m
}

longitud = float(input("Escribe la longitud: "))

while True:
    unidad = input("Escribe su unidad (km, m, cm, mm): ").lower()
    if unidad in conversiones:
        break
    else:
        texto = f"La unidad {unidad} no es válida. Intente de nuevo."
        print(SepSup + f"{error :^{aab}}\n" + texto + "\n" + SepInf)

resultado = longitud * conversiones[unidad]

print(SepSup)
print(f"{longitud:,.2f} {unidad} equivalen a {resultado:,.2f} metros")
print(SepInf)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
