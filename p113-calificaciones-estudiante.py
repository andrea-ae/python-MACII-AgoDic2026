# p113-calificaciones-estudiante.py
# Gestión de calificaciones de un estudiante usando diccionarios

MeIni =  "Gestión de calificaciones de un estudiante usando diccionarios" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 75  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
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

materias = ["Física", "Química", "Matemáticas", "Geografía", "Estadística"]
califs = [10, 9, 8, 7.5, 6]
print(f"Lista de materias: {materias}")
print(f"Lista de calificaciones: {califs}")

notas = dict(zip(materias, califs))
print(f"\nDiccionario nuevo juntando las listas: \nElementos: {len(notas)} - Calificaciones: {notas}")
notas.update({"Inglés":10})
notas.update({"Programacion":7})
print(f"\nSe agregaron elementos: \nElementos: {len(notas)} - Calificaciones: {notas}")

notas.pop("Física")
notas.popitem()
print(f"\nSe removieron elementos: \nElementos: {len(notas)} - Calificaciones: {notas}")

notas.update({"Química":10})
notas.update({"Matemáticas":10})
print(f"\nSe modificaron elementos: \nElementos: {len(notas)} - Calificaciones:{notas}")

s = 0
print("\nMaterias y calificaciones finales")
for m, c in notas.items():
    print(f"{m:<12} - {c:5}")
    s += c

p = s / len(notas)
print(f"\nEl promedio: {p:.2f}")

notas.clear()
print(f"\nSe borró todo: {notas}")

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
