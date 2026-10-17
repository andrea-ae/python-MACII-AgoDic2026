# p125-eliminar-diccionario.py
# Crea un diccionario municipios con los datos:
# Apozol: 1863, Calera: 1868, Fresnillo: 1554, Guadalupe: 1821, Jalpa: 1824
# Jerez: 1824, Loreto: 1931, Mazapil: 1824, Momax: 1857.
# Muestra el diccionario inicial.
# Realiza las siguientes eliminaciones, mostrando el estado del diccionario después de cada operación:
# Elimina Apozol (usando del).
# Elimina Fresnillo (usando pop()).
# Elimina el último elemento insertado (Momax) (usando popitem()).
# Vacía el diccionario (usando clear()).
# Muestra el diccionario final (vacío).

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

municipios = {
    "Apozol": 1863,
    "Calera": 1868,
    "Fresnillo": 1554,
    "Guadalupe": 1821,
    "Jalpa": 1824,
    "Jerez": 1824,
    "Loreto": 1931,
    "Mazapil": 1824,
    "Momax": 1857
}

texto = f"Diccionario inicial"
print(grun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(municipios)

del municipios["Apozol"]
texto = f"Después de eliminar Apozol con del"
print(gelb + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(municipios)

municipios.pop("Fresnillo")
texto = f"Después de eliminar Fresnillo con pop()"
print(cyan + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(municipios)

municipios.popitem()
texto = f"Después de eliminar Momax con popitem()"
print(lila + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(municipios)

# Vaciar
municipios.clear()

texto = f"Diccionario final"
print(rot + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(municipios)

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
