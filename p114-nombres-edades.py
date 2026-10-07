# p114-nombres-edades.py
# Gestión de nombres y edades usando diccionarios

MeIni = "Gestión de nombres y edades usando diccionarios" # Mensaje inicial --------
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

#print(sep_sup)
# print(f"{exito :^{aab}}\n")
# texto = f"Gasto de {gasto} agregado."
# print(f"{texto:^{aab}}")
# print(sep_inf)

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

datos = {}

print('Introduce nombres y edades (nombre vacío para terminar)')

while True:
    nombre = input('Nombre: ')
    if nombre == '':
        break
    else:
        datos[nombre] = int(input(f'Edad de {nombre}: '))

texto = f'El diccionario de datos creado'
print(SepSup + '\n' + f"{texto:^{aab}}" + '\n' + SepInf)
print(f'# de datos ingresados - {len(datos)} \nDatos: {datos}\n')
print('\nListado y promedio de edades:')

s = 0
for n, e in datos.items():
    print(f'{n:<20} - {e:2}')
    s += e

p = s / len(datos) if datos else 0
print(f'\n\nSuma: {s} y promedio: {p:.2f}')

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
