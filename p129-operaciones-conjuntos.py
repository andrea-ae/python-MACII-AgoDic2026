# p129-operaciones-conjuntos.py
# Operaciones entre conjuntos
# Se debe realizar una demostración práctica de todas las operaciones entre conjuntos
# Se proporcionan cuatro conjuntos de números (c1, c2, c3, c4) 
# Realizar las operaciones posibles (unión, intersección, diferencia, diferencia simétrica) 
# y mostrar el resultado de cada operación
# Realizar las comprobaciones de subconjunto/superconjunto, mostrando el resultado 
# de cada operación

c1 = {1, 2, 3, 4, 5}
c2 = {5, 6, 7, 8, 9, 10}
c3 = {9, 10, 11, 12, 13}
c4 = {3, 4, 5}

MeIni = "Operaciones entre conjuntos" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 80  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 20 # Formato encabezados|||||||||||||||||||||||||||||||||||||
LinSup = "∴" * aaa # Línea superior ....................................
LinInf = "∵" * aaa # Línea inferior ....................................
SepSup = "\n" + "-" * aab # Separador superior /////////////////////////
SepInf = "-" * aab + "\n" # Separador inferior /////////////////////////
error = "❌  ¡Ha ocurrido un error! ❌" # Mensaje error ---------------
exito = "✔️  ¡Operación exitosa! ✔️"    # Mensaje éxito ---------------

gelb = "\033[93m" # amarillo
grun = "\033[92m" # verde
rot = "\033[91m" # rojo
blau = "\033[94m" # azul
lila = "\033[95m"  # morado
cyan = "\033[96m"  # cyan
default = "\033[0m"
italic = "\033[3m"  # cursiva
orange = "\033[38;5;208m"  # naranja
braun = "\033[38;5;130m"  # café

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

texto = f"Conjuntos base"
print(italic + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"c1: {c1}\nc2: {c2}\nc3: {c3}\nc4: {c4}")

texto = f"Unión de conjuntos"
print(default + grun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"c1 ∪ c2: {c1.union(c2)}")
print(f"c1 ∪ c3: {c1 | c3}")

texto = f"Intersección de conjuntos"
print(braun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"c1 ∩ c2: {c1.intersection(c2)}")
print(f"c2 ∩ c3: {c2 & c3}")

texto = f"Diferencia de conjuntos"
print(cyan + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"c1 - c2: {c1.difference(c2)}")
print(f"c2 - c3: {c2 - c3}")

texto = f"Diferencia Simétrica de conjuntos"
print(lila + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"c1 Δ c2: {c1.symmetric_difference(c2)}")
print(f"c2 Δ c3: {c2 ^ c3}")

texto = f"Subconjuntos"
print(rot + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"¿c4 es subconjunto de c1? {c4.issubset(c1)}")
print(f"¿c3 es subconjunto de c2? {c3 <= c2}")

texto = f"Superconjuntos"
print(gelb + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"¿c1 es superconjunto de c4? {c1.issuperset(c4)}")
print(f"¿c2 es superconjunto de c3? {c2 >= c3}")

texto = f"Pertenencia y no pertenencia"
print(orange + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"¿Está el 5 en c1? {5 in c1}")
print(f"¿No está el 6 en c1? {6 not in c1}")

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)