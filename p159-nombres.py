# p159-nombres.py
# Escribe una función que tome dos listas de nombres, las una, invierta el orden y convierta todos 
# los nombres a mayúsculas.

# -------------------------------------------------------------------------------------------------
MeIni = "Toma dos listas de nombres, las une, invierte el orden y convierte a mayúsculas" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 100  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
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


def capturar_nombres() -> list[str]:
    """Captura una lista de nombres ingresados por el usuario."""
    datos = []
    print("Introduce nombres (deja en blanco para terminar):")
    while True:
        nombre = input("Nombre: ")
        if nombre.lower() == "":
            break
        datos.append(nombre)
    return datos

def une_procesa(lista1: list[str], lista2: list[str]) -> list[str]:
    """Regresa una lista con nombres que están en amas listas, invertidos y en mayúsculas."""
    nombres_unidos = lista1 + lista2
    nombres_invertidos = nombres_unidos[::-1]
    nombres_mayusculas = []
    for nombre in nombres_invertidos:
        nombres_mayusculas.append(nombre.upper())
    return nombres_mayusculas

# Programa principal
limpiar() # ----------------------------------- Limpiar pantalla
extremos(MeIni) # ----------------------------- Mensaje inicial

nombres1 = ["Ana", "Luis", "Carlos", "Marta", "Sofía"]
nombres2 = capturar_nombres()
nombres_procesados = une_procesa(nombres1, nombres2)

encabezado(f"Lista 1: {nombres1} - Cantidad: {len(nombres1)}", lila)
encabezado(f"Lista 2: {nombres2} - Cantidad: {len(nombres2)}", grun)
encabezado(f"Nombres procesados: {nombres_procesados} - Cantidad: {len(nombres_procesados)}", rot)

extremos(MeFin) # ------------------------------ Mensaje final