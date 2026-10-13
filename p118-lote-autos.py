# p118-lote-autos.py
# Crear una lista de diccionarios para representar un lote de autos

MeIni =  "Listado de autos" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 75  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 24 # Formato encabezados|||||||||||||||||||||||||||||||||||||
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

autos = [
  {"marca": "Toyota", "modelo": "Camry", "año": 2020, "precio": 25000},
  {"marca": "Honda", "modelo": "Civic", "año": 2019, "precio": 22000},
  {"marca": "Ford", "modelo": "Focus", "año": 2021, "precio": 23000}
]

autos.append({"marca": "Chevrolet", "modelo": "Malibu", "año": 2022, "precio": 27000})

texto = f"Todos los autos"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

print(f'{autos} \nTotal: {len(autos)}')
print(SepInf)

texto = f"Datos de cada auto"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
for auto in autos:
  print(auto)
print(SepInf)

texto = f"Datos en forma de Tabla"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
for k in autos[0].keys():
  print(f"{k:<10}", end=" | ")
print('\r')
print(SepInf, end="")

for auto in autos:
  for v in auto.values():
    print(f"{v:<10}", end=" | ")
  print('\r')
print(SepInf)

texto = f"Datos en forma de Registro"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

for auto in autos:
  for k,v in auto.items():
    print(f'{k:>10}: {v}')
  print()
print(SepInf)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
