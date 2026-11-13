# p151–medidas-longitud.py
# Programa que funcione como un conversor de unidades de longitud
# Debe mostrar un menú y utilizar dos funciones separadas:
# 1. Una función para convertir pulgadas a centímetros (fórmula: $cm = pulgadas \times 2.54$)
# 2. Una función para convertir metros a pies (fórmula: $pies = metros \times 3.281$)
# Debe solicitar los datos al usuario según la opción elegida y mostrar el resultado

# -------------------------------------------------------------------------------------------------
MeIni = "Convensor de unidades de longitud" # Mensaje inicial --------
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

def centimetros(pulgadas: float) -> float:
    """Convierte pulgadas a centímetros (fórmula: cm = pulgadas * 2.54)."""

    centimetros = pulgadas * 2.54

    return centimetros

def pies(metros: float) -> float:
    """Convierte metros a pies (fórmula: pies = metros * 3.281)."""

    pies = metros * 3.281
    
    return pies

# Programa principal
limpiar() # ----------------------------------- Limpiar pantalla
extremos(MeIni) # ----------------------------- Mensaje inicial

print(italic + grun + Sep)
menu = f"Conversor de unidades"
print(menu.upper().center(aab))
print(Sep)
print("[1] PULGADAS A CENTÍMETROS \n[2] METROS A PIES \n[3] SALIR")
print(Sep)

while True:
    try:
        longitud = int(input("\n" + grun + "Selecciona una opción: " ))
        print()
       
        if longitud == 1:
            encabezado("Pulgadas a centímetros...", gelb)
            pulgadas = float(input(gelb + "Ingrese la cantidad en pulgadas: "))
            print()
            encabezado(f"{pulgadas:.2f} pulgadas equivalen a {centimetros(pulgadas):.2f} centímetros", gelb)

        elif longitud == 2:
            encabezado("Metros a pies...", lila)
            metros = float(input(lila + "Ingrese la cantidad en metros: "))
            print()
            encabezado(f"{metros:.2f} metros equivalen a {pies(metros):.2f} pies", lila)
        
        elif longitud == 3:            
            encabezado("Saliendo...", rot)
            break

        else: 
            encabezado(f"Error: Se ingresó {longitud}, debe ser 1, 2 o 3.", rot)
    except ValueError:
        encabezado(f"Error: Ingrese un valor numérico.", rot)

extremos(MeFin) # ------------------------------ Mensaje final