# p117-punto-de-venta.py
# Simulación de un punto de venta usando diccionarios

MeIni =  "Simulación de un punto de venta usando diccionarios" # Mensaje inicial --------
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

menu = {
'Bollo': 18.50,
'Muffin': 45.00,
'Dona': 37.00,
'Café': 20.00,
'Agua': 15.00
}

print("--- Bienvenido a 'Panadería Fina' ---")
print("-" * 37)
print("MENÚ:")
for item, precio in menu.items():
    print(f" - {item:<12} ------ ${precio:,.2f}")
print("-" * 37)

orden = {}
total_general = 0

while True:
    producto = input("\nEscriba su orden ('fin' para terminar): ")
    if producto == 'fin':break
    if producto not in menu:
        texto = f"Ese producto no está en el menú. Intente de nuevo."
        print(SepSup + f"{error :^{aab}}\n" + texto + "\n" + SepInf)
        continue
    try:
        cantidad = int(input(f"Cantidad: "))
        if cantidad <= 0:
            print("Error: La cantidad debe ser un número positivo.")
            continue
    except ValueError:
        texto = f"Debe ingresar un número entero (ej. 2)."
        print(SepSup + f"{error :^{aab}}\n" + texto + "\n" + SepInf)
        continue

    orden[producto] = orden.get(producto, 0) + cantidad
    print(f"Agregados {cantidad} {producto}(s) a su orden.")

print("\n--- SU RECIBO ---")

if not orden:
    print("No se ordenó ningún producto.")
else:
    for producto, cantidad in orden.items():
        precio_unitario = menu[producto]
        subtotal = precio_unitario * cantidad
        print(f" {cantidad} x {producto:<12} : ${subtotal:,.2f}")
        total_general += subtotal

    print("-" * 37)
    print(f"TOTAL A PAGAR: ${total_general:,.2f}")
    print("¡Gracias por su compra!")

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
