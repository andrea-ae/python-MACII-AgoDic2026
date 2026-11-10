# p158-aleatorios.py
# Genera dos listas de números aleatorios y crea una tercera lista que sea la suma de las dos primeras.

# -------------------------------------------------------------------------------------------------
MeIni = "Sumar los elementos de una lista de números" # Mensaje inicial --------
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
import random

def generar_numeros_aleatorios(n: int, minimo: int, maximo: int) -> list[int]:
    """Genera una lista de n números aleatorios entre mínimo y máximo."""
    numeros_aleatorios = []
    for _ in range(n):
        numero = random.randint(minimo, maximo)
        numeros_aleatorios.append(numero)
    return numeros_aleatorios

def sumar_listas(lista1: list[int], lista2: list[int]) -> list[int]:
    """Suma los elementos de dos listas y regresa una nueva lista con los resultados."""
    # Precondición: ambas listas tienen la misma longitud.
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben tener la misma longitud.")
    suma = []
    for i in range(len(lista1)):
        suma.append(lista1[i] + lista2[i])
    return suma

# Programa principal
limpiar() # ----------------------------------- Limpiar pantalla
extremos(MeIni) # ----------------------------- Mensaje inicial

MAX = 10

lista1 = generar_numeros_aleatorios(MAX, 1, 10)
lista2 = generar_numeros_aleatorios(MAX, 50, 100)
lista3 = sumar_listas(lista1, lista2)

encabezado(f"Lista 1: {lista1}", grun)
encabezado(f"Lista 2: {lista2}", gelb)
encabezado(f"Suma de listas: {lista3}", rot)

extremos(MeFin) # ------------------------------ Mensaje final