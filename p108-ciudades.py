# p108-ciudades.py
# Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $. Imprimir:
# Cuántos elementos tiene la lista.
# La lista completa.
# La lista ordenada en orden descendente.
# Cuántas ciudades inician con una letra consonante y sus nombres.

MeIni =  "Multiplicar dos listas" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 100  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
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

Ciudades = []

print("Introduce el nombre de una ciudad ($ para terminar)")
while True:
    ciudad = input("Ciudad: ")

    if ciudad == "$":
        break

    Ciudades.append(ciudad)

# Contar ciudades que comienzan con consonante
Consonantes = "BCDFGHJKLMNÑPQRSTVWXYZ"
ListaConsonantes = []

for ciudad in Ciudades:
    if ciudad[0].upper() in Consonantes:
        ListaConsonantes.append(ciudad)

ListaOrdenada = Ciudades.copy() # se hace una copia para no modificar la original
for i in range(len(ListaOrdenada)):
    for j in range(i + 1, len(ListaOrdenada)):
        if ListaOrdenada[i].upper() < ListaOrdenada[j].upper():
            auxiliar = ListaOrdenada[i]
            ListaOrdenada[i] = ListaOrdenada[j]
            ListaOrdenada[j] = auxiliar

texto = f"RESULTADOS"
print(grun + SepSup + "\n" + f"{texto :^{aab}}" + "\n" + SepInf, end="")
print(gelb + "                           Total de ciudades:", len(Ciudades))
print("                              Lista original:", Ciudades)
print(rot + "                  Lista ordenada descendente:", ListaOrdenada)
print(lila + "         Ciudades que inician con consonante:", len(ListaConsonantes))
print("Lista de ciudades que inician con consonante:", ListaConsonantes)

print()

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)