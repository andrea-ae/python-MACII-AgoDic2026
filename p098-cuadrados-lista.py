# p098-cuadrados-lista.py
# Genera cuadrados usando una comprensión de listas

MeIni =  "Cuadrados de 1 a n usando compresión de listas" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 75  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
LinSup = "∴" * aaa # Línea superior ....................................
LinInf = "∵" * aaa # Línea inferior ....................................

blau = "\033[94m"   # azul
default = "\033[0m" # default
bold = "\033[1m"    # negritas
italic = "\033[3m"  # cursiva
gelb = "\033[93m"   # amarillo
grun = "\033[92m"   # verde

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

n = int(input(italic + "\nEscribe el valor de n: " + default))

numeros = list(range(1, n + 1))
cuadrados = [numero ** 2 for numero in numeros]

print(bold + grun)
print(f"  Los números del 1 al {n} son: {numeros}")
print(gelb)
print(f"Los cuadrados del 1 al {n} son: {cuadrados}")
print(default)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)