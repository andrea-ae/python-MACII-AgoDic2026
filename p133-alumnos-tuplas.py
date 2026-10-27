# p133-alumnos-tuplas.py
# Registro escolar con tuplas

# Definición de tupla de tuplas
alumnos = (
            ("Ana", "ISC", (9, 10, 9)),
            ("Luis", "ITC", (8, 9, 10)),
            ("María", "ISD", (10, 8, 9)),
          )

MeIni = "Registro escolar" # Mensaje inicial --------
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

# Imprime el total de alumnos
texto = f"total de alumnos: {len(alumnos)}"
print(orange + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
# Itera sobre la tupla de alumnos y calcula el promedio de calificaciones
for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{nombre:>17} - {carrera} - {calificaciones}: {promedio:.2f}")
print(SepInf, end="")

# Imprime los datos de cada alumno usando índices
color = [lila, grun, cyan]
orden = ["primer", "segundo", "tercer"]

for i in range(3):
    texto = f"{orden[i]} Alumno"
    print(color[i] + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
    print(f"{'Nombre:':>30}", alumnos[i][0])
    print(f"{'Carrera:':>30}", alumnos[i][1])
    print(f"{'Calificaciones:':>30}", alumnos[i][2])
    print(SepInf, end="")

promedios = tuple((nombre, sum(calificaciones) / len(calificaciones)) for nombre, _, calificaciones in alumnos)
texto = f"Promedios: {promedios}"
print(rot + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

mayor = max(promedios, key=lambda x: x[1])
texto = f"Mayor promedio: {mayor}"
print(gelb + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

nombres = tuple(a[0] for a in alumnos)
texto = f"Nombres: {nombres}"
print(braun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)