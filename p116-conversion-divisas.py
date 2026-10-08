# p116-conversion-divisas.py
# Conversor de divisas a pesos mexicanos usando diccionarios

conversiones = {
'USD': 17.98,   # 1 USD = 17.98 MXN
'EUR': 20.13,   # 1 EUR = 20.13 MXN
'GBP': 23.76,   # 1 GBP = 23.76 MXN
'JPY': 0.11,    # 1 JPY = 00.11 MXN
'CAD': 12.61    # 1 CAD = 12.61 MXN
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

gelb = "\033[93m" # amarillo
grun = "\033[92m" # verde
rot = "\033[91m" # rojo
blau = "\033[94m" # azul
default = "\033[0m"

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

print("\nOpciones de monedas: ")
for moneda in conversiones:
    print(f"- {moneda} ")

while True:
    moneda = input("\nIngrese la moneda a convertir (USD, EUR, CAN, GBP, JPY): ").upper()
    if moneda in conversiones:
        break
    else:
        texto = f"La moneda no es válida. Intente de nuevo."
        print(SepSup + f"{error :^{aab}}\n" + texto + "\n" + SepInf)

while True:
    try:
        cantidad = float(input(f"Ingrese la cantidad en {moneda}: "))
        if cantidad > 0:
            break
        else:
            texto = f"La cantidad debe ser un número positivo. Intente de nuevo."
            print(SepSup + f"{error :^{aab}}\n" + texto + "\n" + SepInf)

    except ValueError:
        texto = f"Entrada no válida. Por favor, ingrese un número (ej. 150.50)."
        print(SepSup + f"{error :^{aab}}\n" + texto + "\n" + SepInf)

resultado = cantidad * conversiones[moneda]

print(SepSup)
print(f"{cantidad:,.2f} {moneda} equivalen a  {resultado:,.2f} MXN")
print(SepInf)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
