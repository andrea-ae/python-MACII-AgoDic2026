# p154-calcula-factoriales.py
# Programa que calcule el factorial de cada número en una lista. Debes implementar: 
# 1. Una función que lea y devuelva una lista de números enteros 
# 2. Una función que reciba un número entero y devuelva su factorial (ej: 5 -> 120)
# 3. Una función principal que reciba la lista de números. Esta debe usar la función factorial para crear y 
# devolver una nueva lista con los factoriales de cada número
# El programa debe imprimir la lista original y la lista de factoriales

# -------------------------------------------------------------------------------------------------
MeIni = "Calcular factoriales de una lista" # Mensaje inicial --------
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
            if numero >= 0:
                datos.append(numero)
            else:
                encabezado(f"Error: No se permiten números negativos.", rot)
   
        except ValueError:
            encabezado("Error: Ingresa un número válido o 'fin' para terminar.", rot)

    return datos

def factorial(num: int) -> int:
    """Regresa el factorial de un número entero."""

    fact = 1

    while num > 1:
        fact *= num
        num -= 1

    return fact

def listaNueva(numeros: list[int]) -> list[int]:
    """Regresa una lista nueva con los factoriales."""

    datosNuevos = []

    for num in numeros:
        datoNuevo = factorial(num)
        datosNuevos.append(datoNuevo)

    return datosNuevos

# Programa principal
limpiar() # ----------------------------------- Limpiar pantalla
extremos(MeIni) # ----------------------------- Mensaje inicial

original = lista()
nueva = listaNueva(original)

print()
encabezado(f"Lista original: {original}", grun)

encabezado(f"Lista nueva: {nueva}", rot)

extremos(MeFin) # ------------------------------ Mensaje final