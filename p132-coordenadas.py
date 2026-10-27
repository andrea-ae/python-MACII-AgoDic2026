# p132-coordenadas.py
# Registro de coordenadas

# Definición de tuplas para las coordenadas de dos ciudades
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

MeIni = "Coordenadas" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 60  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 0 # Formato encabezados|||||||||||||||||||||||||||||||||||||
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

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

# Acceso a los elementos de la tupla usando índices
texto = f"Coordenadas de Zacatecas"
print(gelb + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print("    Tipo:", type(zacatecas))
print("  Ciudad:", zacatecas[0])
print(" Latitud:", zacatecas[1])
print("Longitud:", zacatecas[-1])
print(SepInf, end="")

# Acceso a los elementos de la tupla usando desempaquetado
ciudad, latitud, longitud = guadalupe
texto = f"Coordenadas de Guadalupe"
print(lila + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print("    Tipo:", type(guadalupe))
print("  Ciudad:", ciudad)
print(" Latitud:", latitud)
print("Longitud:", longitud)
print(SepInf, end="")

# Iteración sobre una lista de tuplas para mostrar coordenadas
color = [grun, braun] # cada lista sale con un color
for i, lugar in enumerate([zacatecas, guadalupe]):
    texto = f"Coordenadas de {lugar[0]}"

    print(color[i] + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
    print(" Latitud:", lugar[1])
    print("Longitud:", lugar[2])
    print(SepInf, end="")

print(rot + SepSup)   
# Desempaquetar coordenadas, ignora el primer elemento (nombre de la ciudad)
_, lat1, lon1 = zacatecas
_, lat2, lon2 = guadalupe

# Cálculo del punto medio entre las dos coordenadas
centro = ((lat1 + lat2) / 2,  (lon1 + lon2) / 2)
print("Punto medio: ", centro)

# Verificar pertenencia
print("Zacatecas pertenece a la tupla: ","Zacatecas" in zacatecas)

# Crear otra tupla con datos extra
ampliada = zacatecas + ("México",)

print("Tupla original:", zacatecas)
print("Tupla ampliada:", ampliada)
print(SepInf)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)