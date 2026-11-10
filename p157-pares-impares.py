# p157-pares-impares.py
# Escribe una función que tome una lista de números y devuelva dos listas: una con los números pares 
# y otra con los números impares.

# -------------------------------------------------------------------------------------------------
MeIni = "Lista de pares e impares" # Mensaje inicial --------
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

def separar_pares_impares(lista: list[int]) -> tuple[list[int], list[int]]:
    """Separa los números pares e impares de la lista original y regresa dos listas."""
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

# Programa principal
limpiar() # ----------------------------------- Limpiar pantalla
extremos(MeIni) # ----------------------------- Mensaje inicial

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar_pares_impares(numeros)

encabezado(f"Lista original: {numeros} - Cantidad: {len(numeros)}", rot)
encabezado(f"Números pares: {pares} - Cantidad: {len(pares)}", grun)
encabezado(f"Números impares: {impares} - Cantidad: {len(impares)}", lila)

extremos(MeFin) # ------------------------------ Mensaje final