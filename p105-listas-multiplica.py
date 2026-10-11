# p105-listas-multiplica.py
# Leer dos listas, cada una con 5 elementos numéricos.
# Crear una tercera lista multiplicando los elementos de las dos listas correspondientes. 
# Imprimir las tres listas. 

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

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

lista1 = []
lista2 = []
lista3 = []

print(italic + lila + "Introduce 5 números para la lista A:")
for i in range(5):
    num = int(input(f"Número {i + 1}: "))
    lista1.append(num)

print(grun + "\nIntroduce 5 números para la lista B:")
for i in range(5):
    num = int(input(f"Número {i + 1}: "))
    lista2.append(num)
print(default, end="")

for i in range(5):
    lista3.append(lista1[i] * lista2[i])

texto = f"Resultado"
print(default + bold + rot + SepSup + "\n" + f"{texto.upper() :^{aab}}" + "\n" + SepInf,   end="")
print("        Lista A: ", lista1)
print("        Lista B: ", lista2)
print("Lista C (A * B): ", lista3)

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)