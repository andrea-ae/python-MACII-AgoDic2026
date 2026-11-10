# p155-mayor-menor.py
# Encuentra el mayor y el menor de una lista no vacía.

# -------------------------------------------------------------------------------------------------
MeIni = "Encontrar número mayor y menor" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 80  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
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

def captura_datos() -> list[float]:
    """Captura números del usuario y regresa una lista de números."""
    datos = []
    print("Ingresa números (escribe 'fin' para terminar):")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            datos.append(numero)
        except ValueError:
            print("Por favor, ingresa un número válido o 'fin' para terminar.")
    return datos

def mayor(lista: list[float]) -> float:
    """Regresa el número mayor de la lista."""
    mayor_num = lista[0]
    for numero in lista:
        if numero > mayor_num:
            mayor_num = numero
    return mayor_num

def menor(lista: list[float]) -> float:
    """Regresa el número menor de la lista."""
    menor_num = lista[0]
    for numero in lista:
        if numero < menor_num:
            menor_num = numero
    return menor_num

# Programa principal
limpiar() # ----------------------------------- Limpiar pantalla
extremos(MeIni) # ----------------------------- Mensaje inicial

numeros = captura_datos()
if numeros:
    num_mayor = mayor(numeros)
    num_menor = menor(numeros)
    encabezado(f"Total de números ingresados: {len(numeros)}", grun)
    encabezado(F"Lista de números: {numeros}", lila)
    encabezado(f"El número mayor es: {num_mayor}", gelb)
    encabezado(f"El número menor es: {num_menor}", rot)
else:
    encabezado("No se ingresaron números.")

extremos(MeFin) # ------------------------------ Mensaje final