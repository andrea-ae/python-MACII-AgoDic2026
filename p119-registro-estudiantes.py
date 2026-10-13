# p119-registro-estudiantes.py
# Crear una lista de diccionarios para representar un registro de estudiantes

MeIni =  "Registro de estudiantes" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 85  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
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

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

estudiantes = [
    {"nombre": "Juan Pérez", "edad": 20, "carrera": "Ingeniería de Sistemas", "promedio": 8.5},
    {"nombre": "María López", "edad": 22, "carrera": "Medicina", "promedio": 9.2},
    {"nombre": "Carlos García", "edad": 21, "carrera": "Arquitectura", "promedio": 8.7}
]


texto = f"Grupo de estudiantes inicial"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f'{estudiantes} - Total: {len(estudiantes)}')
print(SepInf, end="")

texto = f"Captura de nuevos estudiantes"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

while True:
  print(f"Ingrese datos del estudiante")
  datos = {}
  nombre = input('Nombre: ')
  if nombre =='':
    break
  datos['nombre'] = nombre
  datos['edad'] = int(input('Edad: '))
  datos['carrera'] = input('Carrera: ')
  datos['promedio'] = float(input('Promedio: '))
  estudiantes.append(datos)

texto = f"Todos los estudiantes"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f'\n{estudiantes} - Total: {len(estudiantes)}')
print(SepInf)

texto = f"Datos en forma de tabla"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
for k in estudiantes[0].keys():
  print(f'{k:<20}', end=' | ')
print('')
print(SepInf, end="")

for alumno in estudiantes:
  for v in alumno.values():
    print(f'{v:<20}', end=' | ')
  print('')
print(SepInf)

texto = f"Datos en forma de Registro y Cálculo de Promedios"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

for estudiante in estudiantes:
  for k, v in estudiante.items():
    print(f"{k:>10}: {v}")
  print()

s = sum(estudiante["promedio"] for estudiante in estudiantes)
p = s / len(estudiantes)

print(f'La suma es {s}')
print(f'El promedio es {p:.2f}')

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
