# p156-mayores-promedio.py
# Función para obtener los números mayores al promedio de una lista

# -------------------------------------------------------------------------------------------------
MeIni = "Números mayores al promedio de una lista" # Mensaje inicial --------
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

def promedio_lista(lista: list[float]) -> float:
    """Calcula el promedio de los elementos de una lista de números."""
    suma = 0.0
    if not lista:
        return 0.0
    for numero in lista:
        suma += numero
    return suma / len(lista)

def mayores_al_promedio(lista: list[float]) -> list[float]:
    """Regresa números mayores al promedio."""
    prom = promedio_lista(lista)
    mayores = []
    for numero in lista:
        if numero > prom:
            mayores.append(numero)
    return mayores

# Programa principal
limpiar() # ----------------------------------- Limpiar pantalla
extremos(MeIni) # ----------------------------- Mensaje inicial

numeros = [12.22, 1.5, 2.3, 3.7, 4.1, 10.22, 34.5]
encabezado(f"Los números son: {numeros}", gelb)
prom = promedio_lista(numeros)
encabezado(f"El promedio es: {prom:.2f}", grun)
resultado = mayores_al_promedio(numeros)
encabezado(f"Números mayores al promedio: {resultado}", rot)

extremos(MeFin) # ------------------------------ Mensaje final