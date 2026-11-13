# p152-suma-pares-impares.py
# Programa que sume números pares o impares dentro de un rango especificado
# Debe tener una función que reciba tres parámetros: un número de inicio, un número de fin y una letra ('P' o 'I')
# Si la letra es 'P', la función debe devolver la suma de todos los números pares en ese rango (incluyendo los límites).
# Si la letra es 'I', la función debe devolver la suma de todos los números impares en el rango
# Programa principal debe mostrar un menú, pedir los datos al usuario y mostrar el resultado de la suma

# -------------------------------------------------------------------------------------------------
MeIni = "Sumar pares o impares de un rango" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 70  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 5 # Formato encabezados|||||||||||||||||||||||||||||||||||||
LinSup = "∴" * aaa # Línea superior ....................................
LinInf = "∵" * aaa # Línea inferior ....................................
Sep = "-" * aab # Separador :::::::::::::::::::::::::::::::::::::::

# COLORES
gelb = "\033[93m"         # amarillo
grun = "\033[92m"         # verde
rot = "\033[91m"          # rojo
blau = "\033[94m"         # azul
lila = "\033[95m"         # morado
cyan = "\033[96m"         # cyan
default = "\033[0m"       # original
italic = "\033[3m"        # cursiva
orange = "\033[38;5;208m" # naranja
braun = "\033[38;5;130m"  # café

def limpiar():
    """Limpiar pantalla."""
    print("\033[2J\033[1;1H")

def extremos(texto, color=blau):
    """Mensaje de inicio y fin del programa."""
    print("\n" + color + LinSup + "\n" + texto.upper().center(aaa) + "\n" + LinInf + default + "\n")

def encabezado(texto, color=default):
    """Mensaje de encabezado."""
    print(color + Sep + "\n" + f"{texto.upper():^{aab}}" + "\n" + Sep + default)
# -------------------------------------------------------------------------------------------------

def suma(ni: int, nf: int, letra: str) -> int:
    """Suma números pares o impares dentro de un rango."""

    sum = 0

    for num in range(ni, nf + 1):
        if letra.upper() == "P" and num % 2 == 0:
            sum += num
        elif letra.upper() == "I" and num % 2 != 0:
            sum += num

    return sum

# Programa principal
limpiar() # ----------------------------------- Limpiar pantalla
extremos(MeIni) # ----------------------------- Mensaje inicial

print(italic + grun + Sep)
menu = f"Suma en rango"
print(menu.upper().center(aab))
print(Sep)

ni = int(input("Ingrese el número de inicio del rango: "))
nf = int(input("Ingrese el número de fin del rango: "))



print(Sep)
print("OPCIONES: \n[P] PARES \n[I] IMPARES \n[S] SALIR")
print(Sep)

while True:
    if ni > nf:
        encabezado("Error: El número de inicio debe ser menor o igual que el número final.", rot)
        break
    tipo = input("\n" + grun + "Selecciona el tipo de suma que deseas: ")
    print()

    if tipo.upper() == "P":
        encabezado("Sumando números pares...", gelb)
        pares = suma(ni, nf, tipo)
        encabezado(f"La suma de los números pares es: {pares}", gelb)
        break

    elif tipo.upper() == "I":
        encabezado("Sumando números impares...", lila)
        impares = suma(ni, nf, tipo)
        encabezado(f"La suma de los números impares es: {impares}", lila)
        break

    elif tipo.upper() == "S":
        encabezado("Saliendo...", rot)
        break

    else:
        encabezado(f"Error: Se ingresó {tipo}, debe ser P, I o S.", rot)

extremos(MeFin) # ------------------------------ Mensaje final