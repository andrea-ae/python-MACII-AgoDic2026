# p116-conversion-divisas.py
# Conversor de divisas a pesos mexicanos usando diccionarios

conversiones = {
'USD': 17.98,
'EUR': 20.13,
'GBP': 23.76,
'JPY': 0.11,
'CAD': 12.61
}

MeIni =  "Conversor de monedas a pesos mexicanos (MXN)" # Mensaje inicial --------
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

print("\nOpciones de monedas: ")
for moneda in conversiones:
    print(f"- {moneda} ")

while True:
    moneda = input("\nIngrese la moneda a convertir: ").upper()
    if moneda in conversiones:
        break
    else:
        print("Moneda no válida. Intente de nuevo.")

while True:
    try:
        cantidad = float(input(f"Ingrese la cantidad en {moneda}: "))
        if cantidad > 0:
            break
        else:
            print("La cantidad debe ser un número positivo. Intente de nuevo.")

    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número (ej. 150.50).")

resultado = cantidad * conversiones[moneda]
print(f"{cantidad:,.2f} {moneda} son {resultado:,.2f} MXN")

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
