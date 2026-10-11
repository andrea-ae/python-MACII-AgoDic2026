# p111-comprension-pares-cuadrados.py
# Generar una lista de números enteros del 1 al n (donde n es ingresado por el usuario). 
# Utilizando comprensión de listas, obtener una nueva lista que contenga los cuadrados únicamente de los números pares.
#  Imprimir la lista con el rango completo, la lista resultante de cuadrados y la suma de dichos cuadrados.

MeIni =  "Pares cuadrados" # Mensaje inicial --------
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

n = int(input("Introduce un límite: "))

Numeros = [i for i in range(1, n + 1)]

Cuadrados = [num ** 2 for num in Numeros if num % 2 == 0]

suma = sum(Cuadrados)
texto = f"RESULTADO"
print(default + bold + lila + SepSup + "\n" + f"{texto :^{aab}}" + "\n" + SepInf,   end="")
print("Lista original:", Numeros)
print("Cuadrados de los números pares:", Cuadrados)
print("Suma de los cuadrados:", suma)

print(default)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)