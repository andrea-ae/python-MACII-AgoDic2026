# p122-acceder-diccionario.py
# Crea un diccionario llamado dias usando llaves numéricas para los días de la semana # Muestra el diccionario completo
# Accede y muestra los siguientes valores específicos:
# El valor de la llave 1 (usando [])
# El valor de la llave 7 (usando [])
# El valor de la llave 5 (usando get())
# El valor de la llave 7 (usando get())
# Vuelve a mostrar el diccionario completo

MeIni = "Días de la semana" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 65  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
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
default = "\033[0m"

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

texto = f"Diccionario inicial"
print(grun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(dias)

texto = f"Valores"
print(rot + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print("Llave 1:", dias[1])
print("Llave 7:", dias[7])

print("Llave 5:", dias.get(5))
print("Llave 7:", dias.get(7))

texto = f"Diccionario final"
print(gelb + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(dias)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
