# p120-reporte-ventas.py
# Crear una lista de diccionarios para representar un reporte de ventas

MeIni =  "Reporte de ventas" # Mensaje inicial --------
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

texto = f"Registro de compras de la tienda"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
n = int(input("Número de compras a registrar: "))

compras = []
for i in range(1,n+1):
  print(f'\nCOMPRA {i}:')
  compra = {
    "cliente" : input("Nombre Cliente: "),
    "producto": input("Nombre Producto: "),
    "cantidad": int( input("Cantidad: ")),
    "precio" : float(input("Precio: "))
  }
  compras.append(compra)

texto = f"Lista de compras registradas"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(compras)

clientes = {} # Diccionario de diccionarios

for compra in compras:
  cliente = compra["cliente"]
  if cliente not in clientes:
    clientes[cliente] = {"cantidad": 0, "total": 0}
  clientes[cliente]["cantidad"] += compra["cantidad"]
  clientes[cliente]["total"] += compra["cantidad"] * compra["precio"]

texto = f"Reporte de Totales por Cliente"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
for cliente, datos in clientes.items():
  print("Cliente: ", cliente)
  print("Cantidad total de productos:", datos["cantidad"])
  print("Cantidad total a pagar: $", datos["total"])
  print()

texto = f"Diccionario de Clientes (Estructura Interna)"
print(SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(clientes)

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
