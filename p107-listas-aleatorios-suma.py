# p107-listas-aleatorios-suma.py
# Generar 2 listas de 10 números aleatorios cada una. 
# Crear una tercera lista donde el elemento sea la suma de los correspondientes de las listas A y B,
# solo si AMBOS elementos son impares; de lo contrario, el elemento de la tercera lista será 0.
# Imprimir las 3 listas.

MeIni =  "Sumar dos listas" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 60  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
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

Lista1 = []
Lista2 = []
Lista3 = []

from random import randint
mediciones = 10
for _ in range(mediciones):
    Lista1.append(randint(1, 20))
    Lista2.append(randint(1, 20))

for i in range(mediciones):
    if Lista1[i] % 2 != 0 and Lista2[i] % 2 != 0:
        Lista3.append(Lista1[i] + Lista2[i])
    else:
        Lista3.append(0)

print(bold)
print(rot + "Lista A:", Lista1)
print(lila + "Lista B:", Lista2)
texto = f"Resultado (Suma solo si A[i] y B[i] son ambos impares)"
print(grun + SepSup + "\n" + f"{texto :^{aab}}" + "\n" + SepInf,   end="")
print(grun + "Lista C:", Lista3)

print(default)
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)