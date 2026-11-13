# p150-dia-semana.py
# Programa con una función que reciba un número entero entre 1 y 7, debe devolver el día de la 
# semana correspondiente en texto (ej: 1 = "Lunes", 7 = "Domingo")
# El programa principal debe pedir el número al usuario, llamar a la función y mostrar el nombre del día

# -------------------------------------------------------------------------------------------------
MeIni = "Mostrar día de la semana" # Mensaje inicial --------
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

def diaSemana(num: int) -> str:
    """Regresa el día de la semana según el número ingresado por el usuario (ej: 1 = "Lunes", 7 = "Domingo")."""
    
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias[num - 1]

# Programa principal
limpiar() # ----------------------------------- Limpiar pantalla
extremos(MeIni) # ----------------------------- Mensaje inicial

numero = int(input("Ingresa un número del 1 al 7: "))

if 1 <= numero <= 7:
    encabezado(f"El día de la semana es: {diaSemana(numero)}", grun)
else:
    encabezado(f"Error: El número debe estar entre 1 y 7.", rot)

extremos(MeFin) # ------------------------------ Mensaje final