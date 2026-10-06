# p102-aplanar-matriz.py
# Recorre una matriz con ciclos anidados
# Matriz aplanada de 2 dimensiones a unalista de 1 dimension usando compresión de listas

MeIni =  "Aplanar una matriz" # Mensaje inicial --------
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
lila = "\033[35m"   # morado
rot = "\033[91m"    # rojo

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

matriz = [[4, -2, 8], [0, 5, -1], [7, 3, -6]]

# Se aplana la matriz usando compresión de listas
aplanada = [elemento for fila in matriz for elemento in fila]
positivos = [elemento for fila in matriz for elemento in fila if elemento > 0]
negativos = [elemento for fila in matriz for elemento in fila if elemento < 0]

print(blank + italic + f"Matriz: {matriz}" + blank)
print(bold + gelb + f"Lista plana: {aplanada}" + blank)
print(grun + f"Valores positivos: {positivos}")
print(rot + blank + f"Valores negativos: {negativos}" + default + blank)

print(blau + LinSup + blank + MeFin.upper().center(aaa) + blank + LinInf + default)