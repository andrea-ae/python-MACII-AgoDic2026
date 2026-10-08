# p112-datos-estudiante.py
# Gestión de datos de estudiantes usando diccionarios

MeIni = "Gestión de datos de estudiantes" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 100  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 0 # Formato encabezados|||||||||||||||||||||||||||||||||||||
LinSup = "∴" * aaa # Línea superior ....................................
LinInf = "∵" * aaa # Línea inferior ....................................
SepSup = "\n" + "-" * aab # Separador superior /////////////////////////
SepInf = "-" * aab + "\n" # Separador inferior /////////////////////////

gelb = "\033[93m" # amarillo
grun = "\033[92m" # verde
rot = "\033[91m" # rojo
blau = "\033[94m" # azul
default = "\033[0m"

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

estudiante = {
    "nombre":"Juan Perez",
    "edad":45,
    "email":"jperez@msn.com",
    "carrera":"Sistemas"
}

print(SepSup)
print(f"Datos del estudiante: \n{estudiante} - {len(estudiante)} elementos")
print(SepInf)

# Modificar un dato
estudiante["edad"] = "21"
estudiante["email"] = "juanp@gmail.com"

print(SepSup)
print(f"El diccionario actualizado: \n{estudiante}- {len(estudiante)} elementos")
print(SepInf)

# Agregar dato
estudiante["promedio"] = 9.5

print(SepSup)
print(f"El diccionario actualizado: \n{estudiante} - {len(estudiante)} elementos")
print(SepInf)

print(SepSup)
print("Mostrar las llaves del diccionario: \n")
for k in estudiante.keys():
    print(k)
print(SepInf)

print(SepSup)
print("Mostrar los valores del diccionario: ")
for v in estudiante.values():
    print(v)
print(SepInf)

print(SepSup)
print("Listado de llaves y valores:")
for k, v in estudiante.items():
    print(f"{k:<8}: {v}")
print(SepInf)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
