# p109-lista-impares.py
# Leer un entero n. Llenar una lista con los primeros n números impares. 
# Calcular e imprimir: 
# La suma y el promedio de los números.
# Los números que son divisibles entre 3 y su suma.
# Pedir un elemento a buscar en la lista original e indicar si está y en qué posición (índice).

MeIni =  "Multiplicar dos listas" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 70  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
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
rot = "\033[91m"    # rojo
lila = "\033[35m"   # verde

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default + italic)

n = int(input("Escribe la cantidad de números impares (n): "))

Impares = []
num = 1

for i in range(n):
    Impares.append(num)
    num += 2

texto = f"Generación de Lista"
print(default + bold + grun + SepSup + "\n" + f"{texto.upper() :^{aab}}" + "\n" + SepInf, end="")

print(f"Lista de los primeros {n} números impares:", Impares)


texto = f"Cálculos"
print(rot + SepSup + "\n" + f"{texto.upper() :^{aab}}" + "\n" + SepInf, end="")
suma = 0

for i in range(n):
    suma += Impares[i]

if n > 0:
    promedio = suma / n
    print("       Suma de los números:", suma)
    print("   Promedio de los números:", promedio)
else:
    print("No se puede calcular el promedio.")

Divisibles = []
suma_divisibles = 0

for i in range(n):
    if Impares[i] % 3 == 0:
        Divisibles.append(Impares[i])
        suma_divisibles += Impares[i]

texto = f"DIVISIBLES ENTRE 3"
print(lila + SepSup + "\n" + f"{texto.upper() :^{aab}}" + "\n" + SepInf, end="")

print(lila + "    Números divisibles entre 3:", Divisibles)
print("Suma de los divisibles entre 3:", suma_divisibles)

texto = f"Búsqueda"
print(gelb + SepSup + "\n" + f"{texto.upper() :^{aab}}" + "\n" + SepInf, end="")
buscar = int(input("Introduce el número que deseas buscar: "))
encontrado = False

for i in range(n):
    if Impares[i] == buscar:
        print(f"El número {buscar} sí está en la lista, en la pocisión {i}")
        encontrado = True
        break

if encontrado == False:
    print("El número", buscar, "no está en la lista.")

print(default)
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)