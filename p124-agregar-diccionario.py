# p124-agregar-diccionario.py
# Crea un diccionario llamado ventas con los siguientes datos: 
# Juan: 1550, Jose: 2600, Maria: 2220.
# Muestra el diccionario.
# Agrega los siguientes vendedores y sus ventas al diccionario:
# Rocio: 2500 (usando []).
# Mateo: 1567 (usando []).
# Andrea: 9567 (usando update()).
# Miguel: 1234 (usando update()).
# Muestra el diccionario actualizado.

MeIni = "Ventas" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 65  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 20 # Formato encabezados|||||||||||||||||||||||||||||||||||||
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

ventas = {
    "Juan": 1550,
    "Jose": 2600,
    "Maria": 2220
}

texto = f"Diccionario inicial"
print(grun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(ventas)

# Agregar vendedores
ventas["Rocio"] = 2500
ventas["Mateo"] = 1567

ventas.update({"Andrea": 9567})
ventas.update({"Miguel": 1234})

texto = f"Diccionario modificado"
print(gelb + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(ventas)

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
