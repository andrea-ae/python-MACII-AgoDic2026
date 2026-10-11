# p110-comprension-filtra-palabras.py
# Dada una lista de palabras introducidas por el usuario separadas por espacios, utilizar comprensión de listas 
# para crear una nueva lista que contenga solo aquellas palabras que tengan más de 4 caracteres y convertirlas a 
# mayúsculas. Imprimir la lista original y la lista filtrada.

MeIni =  "Multiplicar dos listas" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 50  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 0 # Formato encabezados|||||||||||||||||||||||||||||||||||||
LinSup = "∴" * aaa # Línea superior ....................................
LinInf = "∵" * aaa # Línea inferior ....................................
SepSup = "\n" + "-" * aab # Separador superior /////////////////////////
SepInf = "-" * aab + "\n" # Separador inferior /////////////////////////
error = "❌  ¡Ha ocurrido un error! ❌" # Mensaje error ---------------

blau = "\033[94m"   # azul
default = "\033[0m" # default
bold = "\033[1m"    # negritas
italic = "\033[3m"  # cursiva
gelb = "\033[93m"   # amarillo
grun = "\033[92m"   # verde
lila = "\033[35m"   # verde

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default + italic)

Palabras = input("Introduce varias palabras separadas por espacios: ").split()

Filtradas = [palabra.upper() for palabra in Palabras if len(palabra) > 4]

print(default + bold + grun + "Lista original:", Palabras)
print(lila + "Lista filtrada:", Filtradas)

print(default)
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)