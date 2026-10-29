# p135-alumnos-tuplas.py
"""Modela el siguiente registro escolar como una tupla de alumnos. Cada alumno contiene nombre, carrera y una
tupla de calificaciones:
● ("Ana", "ISC", (9, 10, 9, 8))
● ("Luis", "ISW", (8, 8, 9, 10))
● ("Mar", "ISC", (10, 9, 10, 10))
Instrucciones:
● Crear y mostrar la tupla externa con los tres registros. Imprimir cuántos alumnos contiene.
● Recorrer los registros mediante desempaquetado y mostrar el nombre, la carrera y el promedio de cada
alumno con dos decimales.
● Construir y mostrar una nueva tupla con pares (nombre, promedio). Identificar e imprimir el alumno con el
promedio más alto.
● Consultar las calificaciones usando índices de tuplas anidadas. Para cada alumno, mostrar cuántas veces
aparece 10 con count() y la posición de la primera calificación con index().
● Ordenar los pares (nombre, promedio) por promedio de menor a mayor usando sorted() y mostrar el
resultado como una tupla.
● Formar y mostrar una tupla nueva con el nombre "Eva", la carrera "ISC" y las calificaciones (9, 9, 10), sin
modificar la tupla original de alumnos."""

MeIni = "Registro escolar" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 115  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 35 # Formato encabezados|||||||||||||||||||||||||||||||||||||
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

# Crear y mostrar la tupla externa con los tres registros. Imprimir cuántos alumnos contiene
alumnos = (
            ("Ana", "ISC", (9, 10, 9, 8)),
            ("Luis", "ISW", (8, 8, 9, 10)),
            ("Mar", "ISC", (10, 9, 10, 10)),
          )

print(f"\nRegistro de alumnos: {alumnos} \nTotal de alumnos: {len(alumnos)}\n")

print(orange + SepInf, end="")
# Recorrer los registros mediante desempaquetado
for nombre, carrera, calificaciones in alumnos:
# Mostrar el nombre, la carrera y el promedio de cada alumno con dos decimales
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Nombre: {nombre} - Carrera: {carrera} - Calificaciones: {calificaciones} -> Promedio: {promedio:.2f}")
print(SepInf, end="")

# Construir y mostrar una nueva tupla con pares (nombre, promedio)
promedios = tuple((nombre, sum(calificaciones) / len(calificaciones)) for nombre, _, calificaciones in alumnos)
texto = f"Pares (nombre, promedio): {promedios}"
print(lila + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

# Identificar e imprimir el alumno con el promedio más alto
mayor = max(promedios, key=lambda x: x[1])
texto = f"Alumno con mayor promedio: {mayor[0]} con {mayor[1]}"
print(grun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

print(cyan + SepSup)
# Consultar las calificaciones usando índices de tuplas anidadas
for alumno in alumnos:
    nombre = alumno[0]
    calificaciones = alumno[2]

    # Para cada alumno, mostrar cuántas veces aparece 10 con count()
    diez = calificaciones.count(10)
    # Y la posición de la primera calificación con index()
    indice = calificaciones.index(calificaciones[0])

    print(f"{nombre} -> Conteo de 10s: {diez}, Índice de primera calificación: {indice}")
print(SepInf, end="")

# Ordenar los pares (nombre, promedio) por promedio de menor a mayor usando sorted()
ordenados = tuple(sorted(promedios, key=lambda alumno: alumno[1]))
# Mostrar el resultado como una tupla
#print("Alumnos ordenados por promedio:", ordenados)
texto = f"Orfenados por promedio: {ordenados}"
print(gelb + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

print(braun + SepSup)
# Formar y mostrar una tupla nueva con el nombre "Eva", la carrera "ISC" y las calificaciones (9, 9, 10), 
# sin modificar la tupla original de alumnos
eva = ("Eva", "ISC", (9, 9, 10))
nueva = alumnos + (eva,)
print("Tupla original intacta:", alumnos)
print("Tupla nueva con Eva:", nueva)
print(SepInf)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)