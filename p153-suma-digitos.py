# p153-suma-digitos.py
# Programa que procese una lista de números. Debes implementar lo siguiente: 
# 1. Una función que lea y devuelva una lista de números enteros 
# 2. Una función que reciba un número entero y devuelva la suma de sus dígitos individuales (ej: 1971 -> 1+9+7+1 = 18)
# 3. Una función principal que reciba la lista de números. Esta debe usar la función anterior para crear y devolver 
# una nueva lista que contenga la suma de los dígitos de cada número original
# El programa debe imprimir la lista original y la nueva lista con las sumas

# -------------------------------------------------------------------------------------------------
MeIni = "Sumar todos los dígitos de un número" # Mensaje inicial --------
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
            print("Error: Ingresa un número válido o 'fin' para terminar.")

    return datos

def suma(num: int) -> int:
    """Suma dígitos individuales de un número entero."""

    num = abs(num)
    sum = 0

    while num != 0:
        digito = num % 10
        sum += digito
        num = num // 10

    return sum

def listaNueva(sumas: list[int]) -> list[int]:
    """Regresa una lista nueva con la suma de los dígitos."""

    datosNuevos = []

    for num in sumas:
        datoNuevo = suma(num)
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