# p127-contar-caracteres.py
# Escribe un programa que pida al usuario que ingrese una cadena de texto.
# Crea un diccionario vacío para almacenar la frecuencia (cantidad de apariciones) de cada carácter.
# Itera sobre cada carácter en la cadena ingresada.
# En cada iteración:
# Si el carácter no existe como llave en el diccionario, agrégalo con un valor de 1.
# Si el carácter ya existe, incrementa su valor actual en 1.
# Al finalizar el ciclo, muestra el diccionario resultante con el conteo de caracteres.

MeIni = "Contar caracteres" # Mensaje inicial --------
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

cadena = input("Ingresa una cadena de texto: ")

frecuencia = {}

for caracter in cadena:
    if caracter not in frecuencia:
        frecuencia[caracter] = 1
    else:
        frecuencia[caracter] += 1

texto = f"Frecuencia de cada carácter"
print(grun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(frecuencia)

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
