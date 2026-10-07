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
'taco': 18.50,
'burrito': 45.00,
'quesadilla': 35.00,
'refresco': 20.00,
'agua': 15.00
}

print("--- Bienvenido a 'El Taco Feroz' ---")
print("Este es nuestro menú:")
for item, precio in menu.items():
    print(f" - {item:<12} : ${precio:,.2f}")
print("-" * 35)

orden = {}
total_general = 0

while True:
    producto = input("\n¿Qué desea ordenar? (escriba 'fin' para terminar): ").lower()
    if producto == 'fin':break
    if producto not in menu:
        print("Error: Ese producto no está en el menú. Intente de nuevo.")
        continue
    try:
        cantidad = int(input(f"Cantidad: "))
        if cantidad <= 0:
            print("Error: La cantidad debe ser un número positivo.")
            continue
    except ValueError:
        print("Error: Debe ingresar un número entero (ej. 2).")
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

    print("-" * 35)
    print(f"TOTAL A PAGAR: ${total_general:,.2f}")
    print("¡Gracias por su compra!")

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
