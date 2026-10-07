# p112-datos-estudiante.py
# Gestión de datos de estudiantes usando diccionarios

MeIni = "Gestión de datos de estudiantes" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 90  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
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

estudiante = {
'nombre':'Juan Perez',
'edad':45,
'email':'jperez@msn.com',
'carrera':'Sistemas'
}

print(f'\nEl diccionario original: \n\n{estudiante}')

estudiante['calificacion'] = 9.5
estudiante['email'] = 'juanp@gmail.com'
print(f'\nEl diccionario actualizado: \n\n{estudiante}')

print('\nLas llaves del diccionario: \n')
for k in estudiante.keys():
    print(k)

print('\nLos valores del diccionario: \n')

for v in estudiante.values():
    print(v)

print("\nListado de llaves y valores:\n")
for k, v in estudiante.items():
    print(f'{k:<10} : {v}')

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
