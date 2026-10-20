# p128-municipios.py
# Padrón de municipios
# Se requiere implementar un sistema simple para administrar el padrón de
# municipios. El sistema debe permitir:
# Registrar municipios (evitando duplicados automáticamente), 
# Mostrar todos los municipios registrados,
# Verificar si un municipio específico ya existe, y 
# Gestionar las altas y bajas del padrón.

municipios = {"Zacatecas", "Guadalupe", "Jerez", "Fresnillo", "Fresnillo", "Sombrerete"}

MeIni = "Padrón de Municipios (con Conjuntos)" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 120  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
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
lila = "\033[95m"  # morado
cyan = "\033[96m"  # cyan
default = "\033[0m"
italic = "\033[3m"  # cursiva

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

print("\n" + italic + f"La colección es del tipo: {type(municipios)} \t||\t Longitud del padrón: {len(municipios)}")
print(f"\nPadrón original: {municipios}\n")

print("Lista de municipios registrados: | ", end="")
for mun in municipios:
    print(mun, end=" | ")

print("\n" + SepSup + "\n" + f"¿Está Zacatecas en el padrón?: {"Zacatecas" in municipios}" + "\n" + SepInf, end="")

municipios.add("Teul")
texto = f"Altas en el Padrón con Add() \t||\t Longitud del padrón: {len(municipios)}"
print(default + grun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"➡️   {municipios}")

otros_municipios = {"Luis Moya", "Ojocaliente", "Tepetongo"}
municipios.update(otros_municipios)
texto = f"Altas en el Padrón con Update() \t||\t Longitud del padrón: {len(municipios)}"
print(lila + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"➡️   {municipios} ")

municipios.remove("Zacatecas")
texto = f"Bajas en el Padrón con Remove()\t||\t Longitud del padrón: {len(municipios)}"
print(rot + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"➡️   {municipios} ")

municipios.discard("Ojocaliente")
texto = f"Bajas en el Padrón con Discard()\t||\t Longitud del padrón: {len(municipios)}"
print(gelb + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"➡️   {municipios} ")

mun_eliminado = municipios.pop()
texto = f"Bajas en el Padrón con Pop()\t||\t Longitud del padrón: {len(municipios)}"
print(cyan + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"➡️   {municipios} ")
print(f"Municipio eliminado arbitrariamente: {mun_eliminado}")

municipios.clear()
texto = f"Padrón vaciado con Clear()\t||\t Longitud del padrón: {len(municipios)}"
print(default + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"➡️   {municipios} ")

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)
