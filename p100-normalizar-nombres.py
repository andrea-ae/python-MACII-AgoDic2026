# p100-normalizar-nombres.py
# Limpia nombres mediante una comprensión

MeIni =  "Normaliza escritura de los nombres" # Mensaje inicial --------
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

nombres = [' ana', 'LUIS ', '', ' maría josé ', 'Pedro']

normalizados = [ nombre.strip().title() for nombre in nombres if nombre.strip() ]

print(gelb)
print(f'  Nombres originales: {nombres}')
print(grun)
print(f'Nombres normalizados: {normalizados}')
print(default)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
