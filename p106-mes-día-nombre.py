# p106-mes-día-nombre.py
# Leer un número de mes (ej. 4). 
# Guardar los días de cada mes en una lista y los nombres de los meses en otra lista.
# Asumir 28 días para febrero. 
# Imprimir el nombre del mes y la cantidad de días del mes correspondiente (ej.marzo, 30).

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
rot = "\033[91m"    # rojo

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default + italic)

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = int(input("Introduce un número de mes (1-12): "))
print(default + bold, end="")

if 1 <= mes <= 12:
    texto = f"RESULTADOS"
    print(grun + SepSup + "\n" + f"{texto :^{aab}}" + "\n" + SepInf, end="")
    print(f"Mes: {meses[mes - 1]}")
    print(f"Días: {dias[mes - 1]}")
else:
    texto = f"El número de mes {mes} no es válido."
    print(rot + SepSup + "\n" + f"{error :^{aab}}\n" + f"{texto :^{aab}}" + "\n" + SepInf, end="")

print(default)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)