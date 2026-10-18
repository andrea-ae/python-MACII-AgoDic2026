# p126-procesar-diccionario.py
# Define dos listas:
nombres = ["Juan", "Pedro", "Manuel", "Elias", "Maria", "Felipe", "Julia", "Roberto"]
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]
# Crea un diccionario nómina combinando ambas listas (los nombres son las llaves, los sueldos son los valores).
# Muestra el diccionario nómina resultante.
# Itera sobre el diccionario y muestra su contenido de cuatro formas:
# Mostrando solo las llaves (usando keys()).
# Mostrando solo los valores (usando values()).
# Iterando por las llaves y accediendo al valor (ej. for llave in dic: ...).
# Mostrando la llave y el valor simultáneamente (usando items()).
# Calcula y muestra la suma total de los sueldos.
# Calcula y muestra el promedio de los sueldos.

MeIni = "Municipios" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 65  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 0 # Formato encabezados|||||||||||||||||||||||||||||||||||||
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

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

nomina = {}
for i in range(len(nombres)):
    nomina[nombres[i]] = sueldos[i]

texto = f"Diccionario inicial"
print(grun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(nomina)

texto = "Mostrando solo las llaves"
print(gelb + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
for llave in nomina.keys():
    print(llave)

texto = "Mostrando solo los valores"
print(lila + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
for valor in nomina.values():
    print(valor)

texto = "Iterando por las llaves y accediendo al valor"
print(rot + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
for llave in nomina:
    print(f"{llave} -> {nomina[llave]}")

texto = "Mostrando llave y valor con items()"
print(cyan + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
for llave, valor in nomina.items():
    print(f"('{llave}', {valor:.2f})")

texto = "Cálculos"
print(default + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

# Suma
suma = sum(nomina.values())
print(f"    SUMA = ${suma:.2f}")

# Promedio

promedio = suma / len(nomina)
print(f"PROMEDIO = ${promedio:.2f}")

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
