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
error = "❌  ¡Ha ocurrido un error! ❌" # Mensaje error ---------------
exito = "✔️  ¡Operación exitosa! ✔️"    # Mensaje éxito ---------------

gelb = "\033[93m" # amarillo
grun = "\033[92m" # verde
rot = "\033[91m" # rojo
blau = "\033[94m" # azul
default = "\033[0m"

# print(sep_sup)
# print(f"{exito :^{aab}}\n")
# texto = f"Gasto de {gasto} agregado."
# print(f"{texto:^{aab}}")
# print(sep_inf)

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)


materias = ['Fisica', 'Quimica', 'Matematicas', 'Geografia', 'Estadistica']
califs = [10, 9, 8, 7.5, 6]
print(f'Lista de materias : \n{materias}\n')
print(f'Lista de calificaciones: \n{califs}\n')

notas = dict(zip(materias, califs))
print(f'\nDiccionario nuevo juntando las listas: \n {len(notas)} - {notas} ')
notas.update({'Ingles':10})
notas.update({'Programacion':7})
print(f'\nSe agregaron elementos : \n{len(notas)} - {notas}')

notas.pop('Fisica')
notas.popitem()
print(f'\nSe removieron elementos : \n {len(notas)} - {notas}')

notas.update({'Quimica':10})
notas.update({'Matematicas':10})
print(f'\nSe modificaron elementos : \n{notas}')

s = 0
print('\nMaterias y calificaciones finales')
for m, c in notas.items():
    print(f'{m:<12} - {c:5}')
    s += c

p = s / len(notas)
print(f'\nLa suma: {s} y el promedio: {p:.2f}')

notas.clear()
print(f'\nSe borró todo : {notas}')

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
