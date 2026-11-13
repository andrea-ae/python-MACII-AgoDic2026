# p155-estadisticas-basicas.py
# Programa que calcule estadísticas básicas (poblacionales) para una lista de números
#  El programa debe incluir: 
# 1. Una función para leer una lista de números enteros
# 2. Funciones separadas para calcular y devolver cada una de las siguientes estadísticas:
    # - Número mayor 
    # - Número menor 
    # - Media (promedio)
    # - Varianza poblacional
    # - Desviación estándar poblacional
# El programa principal debe leer la lista e imprimir todos los resultados estadísticos de forma clara

# -------------------------------------------------------------------------------------------------
MeIni = "Estadísticas poblacionales de una lista" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 60  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
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

def lista() -> list[int]:
    """Captura números enteros ingresados por el usuario y regresa una lista."""

    datos = []

    encabezado("Ingresa números (escribe 'fin' para terminar)")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = int(entrada)
            datos.append(numero)
   
        except ValueError:
            encabezado("Error: Ingresa un número válido o 'fin' para terminar.", rot)

    return datos

def mayor(numeros: list[int]) -> int:
    """Regresa el número mayor de la lista."""

    num = numeros[0]

    for numero in numeros:
        if numero > num:
            num = numero

    return num

def menor(numeros: list[int]) -> int:
    """Regresa el número menor de la lista."""

    num = numeros[0]
    
    for numero in numeros:
        if numero < num:
            num = numero

    return num

def promedio(numeros: list[int]) -> float:
    """Regresa el promedio de los elementos de una lista de números."""

    suma = 0.0

    if not numeros:
        return 0.0
    for numero in numeros:
        suma += numero

    prom = suma / len(numeros)

    return prom

def varianza(numeros: list[int]) -> float:
    """Regresa la varianza de los elementos de una lista de números."""

    prom = promedio(numeros)

    suma = 0.0

    if not numeros:
        return 0.0
    for numero in numeros:
        diferencia = numero - prom
        suma += diferencia ** 2

    var = suma / len(numeros)

    return var

def desviacion(numeros: list[int]) -> float:
    """Regresa la desviación estándar de los elementos de una lista de números."""

    des = varianza(numeros) ** 0.5

    return des

# Programa principal
limpiar() # ----------------------------------- Limpiar pantalla
extremos(MeIni) # ----------------------------- Mensaje inicial

original = lista()

print()
encabezado(f"Lista de números: {original}", grun)

if original:
    encabezado(f"Estadísticas", rot)
    print(rot + f"     Media: {promedio(original):.3f}")
    print(f"     Mayor: {mayor(original)}")
    print(f"     Menor: {menor(original)}")
    print(f"  Varianza: {varianza(original):.3f}")
    print(f"Desviación: {desviacion(original):.3f}")
else:
    encabezado("No se ingresaron números.", rot)

extremos(MeFin) # ------------------------------ Mensaje final