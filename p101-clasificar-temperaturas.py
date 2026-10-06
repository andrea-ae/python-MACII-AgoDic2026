# p101-clasificar-temperaturas.py
# Clasifica datos con una expresión condicional

MeIni =  "Clasificar temperaturas" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 75  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 0 # Formato encabezados|||||||||||||||||||||||||||||||||||||
LinSup = "∴" * aaa # Línea superior ....................................
LinInf = "∵" * aaa # Línea inferior ....................................

blau = "\033[94m"   # azul
default = "\033[0m" # default
bold = "\033[1m"    # negritas
italic = "\033[3m"  # cursiva
gelb = "\033[93m"   # amarillo
grun = "\033[92m"   # verde
lila = "\033[35m"   # verde

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

temperaturas = [8, 14, 18, 22, 27, 35]

clasificacion = [
    "Fría" if t < 15 else
    "Templada" if t <= 25 else
    "Caliente"
    for t in temperaturas
] 

print(italic)
print(f"Temperaturas: {temperaturas}")
print(default + bold)
print(f"Clasificación: {clasificacion}" + default)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)