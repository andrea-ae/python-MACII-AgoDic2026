# p134-coordenadas-tuplas.py
# Registro de coordenadas
# Zacatecas: nombre, latitud 22.77 y longitud -102.58
# Guadalupe: nombre, latitud 22.75 y longitud -102.52
#Instrucciones:
# Crear y mostrar las tuplas de Zacatecas y Guadalupe. Imprimir su tipo y
#       consultar el nombre, la latitud y la longitud usando índices positivos y negativos.
# Desempaquetar cada tupla en variables e imprimir las coordenadas con el formato 
#       nombre: (latitud, longitud).
# Recorrer ambas ubicaciones con un ciclo y mostrar para cada una el nombre y la
#       tupla de coordenadas obtenida con slicing.
# Calcular e imprimir el punto medio aproximado entre las dos ubicaciones usando 
#       las latitudes y longitudes.
# Crear una nueva tupla para Zacatecas que incluya el código "ZAC". Mostrar la
#       tupla nueva y comprobar que la original no cambió.
# Verificar si "Zacatecas" pertenece a su tupla. En un comentario, indicar qué
# ocurriría si se intentara reemplazar directamente uno de sus elementos.

MeIni = "Coordenadas" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 95  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 25 # Formato encabezados|||||||||||||||||||||||||||||||||||||
LinSup = "∴" * aaa # Línea superior ....................................
LinInf = "∵" * aaa # Línea inferior ....................................
SepSup = "\n" + "-" * aab # Separador superior /////////////////////////
SepInf = "-" * aab + "\n" # Separador inferior /////////////////////////

gelb = "\033[93m" # amarillo
grun = "\033[92m" # verde
rot = "\033[91m" # rojo
blau = "\033[94m" # azul
lila = "\033[95m"  # morado
cyan = "\033[96m"  # cyan
default = "\033[0m"
italic = "\033[3m"  # cursiva
orange = "\033[38;5;208m"  # naranja
braun = "\033[38;5;130m"  # café
bold = "\033[1m"    # negritas

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default + "\n")

# Crear y mostrar las tuplas de Zacatecas y Guadalupe.
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)
print(f"Tupla Zacatecas: {zacatecas} | Tipo {type(zacatecas)}")
print(f"Tupla Zacatecas: {guadalupe} | Tipo {type(guadalupe)}")

# Acceso a los elementos de la tupla usando índices
texto = f"Coordenadas de Zacatecas con índices"
print(italic + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
# Imprimir su tipo
print(f"     TIPO -  {type(zacatecas)} ")
# Consultar nombre, latitud y longitud usando índices POSITIVOS
print(grun + f"POSITIVOS - Ciudad: {zacatecas[0]} | Latitud: {zacatecas[1]} | Longitud: {zacatecas[2]}")
# Consultar nombre, latitud y longitud usando índices NEGATIVOS
print(rot + f"NEGATIVOS - Ciudad: {zacatecas[-3]} | Latitud: {zacatecas[-2]} | Longitud: {zacatecas[-1]}")
print(default + italic + SepInf, end="")

# Acceso a los elementos de la tupla usando índices
texto = f"Coordenadas de Guadalupe con índices"
print(italic + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
# Imprimir su tipo
print(f"     TIPO -  {type(guadalupe)} ")
# Consultar nombre, latitud y longitud usando índices POSITIVOS
print(grun + f"POSITIVOS - Ciudad: {guadalupe[0]} | Latitud: {guadalupe[1]} | Longitud: {guadalupe[2]}")
# Consultar nombre, latitud y longitud usando índices NEGATIVOS
print(rot + f"NEGATIVOS - Ciudad: {guadalupe[-3]} | Latitud: {guadalupe[-2]} | Longitud: {guadalupe[-1]}")
print(default + italic + SepInf, end="")

# Desempaquetar cada tupla en variables 
_, lat1, lon1 = zacatecas
_, lat2, lon2 = guadalupe
# Imprimir las coordenadas con el formato nombre: (latitud, longitud)
texto = f"Zacatecas: {lat1, lon1}"
print(default + bold + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

texto = f"Guadalupe: {lat2, lon2}"
print(default + bold + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

# Recorrer ambas ubicaciones con un ciclo
color = [cyan, lila] # cada lista sale con un color
for i, lugar in enumerate([zacatecas, guadalupe]):
     # Mostrar para cada una nombre y tupla de coordenadas obtenida con slicing
    texto = f"Ubicación: {lugar[0]}  |  Coordenadas {lugar[1:]}"
    print(color[i] + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

# Calcular e imprimir el punto medio aproximado entre las dos ubicaciones usando latitudes y longitudes
centro = ((lat1 + lat2) / 2,  (lon1 + lon2) / 2)
texto = f"Punto medio: {centro}"
print(default+ braun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

# Crear una nueva tupla para Zacatecas que incluya el código "ZAC"
Zac = zacatecas + ("ZAC",)
#  Mostrar la tupla nueva y comprobar que la original no cambió
texto = f"Nueva tupla Zacatecas: {Zac} \nOriginal sin cambios: {zacatecas}"
print(rot + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

# Verificar si "Zacatecas" pertenece a su tupla
texto = f"¿Zacatecas pertenece a su tupla? {'Zacatecas' in zacatecas}"
print(orange + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
# En un comentario, indicar qué ocurriría si se intentara reemplazar directamente uno de sus elementos
"""
Una de las propiedades de las tuplas es que son inmutables, es decir, que no se le pueden agregar, modificar ni
eliminar sus elementos. Para hacer eso de debe de crear una tupla nueva.
Si se intentara hacer saldría algo como TypeError.
"""
print(default + "\n#NOTA: Las tuplas son inmutables e intentar modificar un elemento directamente dará TypeError.")

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)