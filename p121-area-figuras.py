# p121-area-figuras.py
# Crear una lista de diccionarios para representar figuras geométricas

MeIni = "Área de figuras geométricas" # Mensaje inicial --------
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

import math

figuras = {
    "Circulo": {"radio": 0, "formula": "math.pi * r ** 2"},
    "Triangulo": {"base": 0, "altura": 0, "formula": "0.5 * b * a"},
    "Rectangulo": {"largo": 0, "ancho": 0, "formula": "l * a"}
}

texto = f"Calculadora de áreas de figuras geométricas"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print("Figuras disponibles:")
for k,v in figuras.items():
  print(f'{k:>10} - Fórmula: {v["formula"]}')
print(SepInf, end="")


while True:
  fig = input('\nElige una Figura: ').title()
  if fig in figuras : break
  print(error)
  print("Figura no válida. Intenta de nuevo.")

area = 0

if fig == 'Circulo':
  r = int(input('Radio: '))
  area = eval(figuras[fig]['formula'].replace('r', str(r)))
elif fig=='Triangulo':
  b = int(input('Base: '))
  a = int(input('Altura: '))
  formula_lista = figuras[fig]['formula'].replace('b',
  str(b)).replace('a',str(a))
  area = eval(formula_lista)
elif fig=='Rectangulo':
  l = int(input('Largo: '))
  a = int(input('Ancho: '))
  formula_lista = figuras[fig]['formula'].replace('l',
  str(l)).replace('a',str(a))
  area = eval(formula_lista)

texto = f"El Área del {fig} es igual a {area:.4f}"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
