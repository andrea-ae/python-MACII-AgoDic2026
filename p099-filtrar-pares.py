# p099-filtrar-pares.py
# Filtra números pares con una comprensión

MeIni =  "Filtro de números pares" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 50  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 0 # Formato encabezados|||||||||||||||||||||||||||||||||||||
LinSup = "∴" * aaa # Línea superior ....................................
LinInf = "∵" * aaa # Línea inferior ....................................

blau = "\033[94m"   # azul
default = "\033[0m" # default
bold = "\033[1m"    # negritas
italic = "\033[3m"  # cursiva
gelb = "\033[93m"   # amarillo
grun = "\033[92m"   # verde
lila = "\033[35m"   # verde

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

cant = int(input("\nEscribe la cantidad de números a introducir: "))
nums = []

print(italic) 
for i in range(cant): # se introducen los números en la lista
    num = int(input(f"Número {i + 1}: "))
    nums.append(num)
print(default)

pares = [x for x in nums if x % 2 == 0]   # par
impares = [x for x in nums if x % 2 != 0] # imppar

print(bold + lila + f"     Lista original: {nums}")
print(gelb + f"\n      Números pares: {pares}")
print(f"\n  Cantidad de pares: {len(pares)}")
print(grun + f"\n    Números impares: {impares}")
print(f"\nCantidad de impares: {len(impares)}\n" + default)

print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)