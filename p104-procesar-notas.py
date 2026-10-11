# p104-procesar-notas.py
# Leer un número indeterminado de notas (notas) entre 0 y 100. 
# Deteniéndose cuando el usuario introduzca un 0. 
# Validar que todas las notas introducidas estén dentro del rango [0, 100].

MeIni =  "Leer notas con listas" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 50  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 0 # Formato encabezados|||||||||||||||||||||||||||||||||||||
LinSup = "∴" * aaa # Línea superior ....................................
LinInf = "∵" * aaa # Línea inferior ....................................
SepSup = "\n" + "-" * aab # Separador superior /////////////////////////
SepInf = "-" * aab + "\n" # Separador inferior /////////////////////////
error = "❌  ¡Ha ocurrido un error! ❌" # Mensaje error ---------------

blau = "\033[94m"   # azul
default = "\033[0m" # default
bold = "\033[1m"    # negritas
italic = "\033[3m"  # cursiva
gelb = "\033[93m"   # amarillo
grun = "\033[92m"   # verde
lila = "\033[35m"   # verde
rot = "\033[91m"    # rojo

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

print(italic + "\nIntroduce notas entre 0 y 100 (0 para detener)")

notas = []
suma = 0.0

while True:
    try:
        nota = int(input("Nota: "))
        if nota == 0: 
            break

        elif 0 <= nota <= 100:
            notas.append(nota)
            suma += nota

        else:
            texto = f"La nota debe estar entre 0 y 100."
            print(default + rot + SepSup + "\n" + f"{error :^{aab}}\n" + f"{texto :^{aab}}" + "\n" + SepInf + default)

    except ValueError:
        texto = f"Entrada no válida. Por favor, introduce un número."
        print(default + rot + SepSup + "\n" + f"{error :^{aab}}\n" + f"{texto :^{aab}}" + "\n" + SepInf + default)

if notas:
    prom = suma / len(notas)
    nota_alta = max(notas)
    nota_baja = min(notas)
    prom_menores = [cal for cal in notas if cal < prom]

    texto = f"RESULTADO DE NOTAS"
    print(default + bold + lila + SepSup + "\n" + f"{texto :^{aab}}" + "\n" + SepInf,   end="")

    print(f"Número ingresadas: {len(notas)}")
    print(f"            Lista: {notas}")
    print(f"             Suma: {suma}")
    print(f"         Promedio: {prom}")
    print(f"           Máxima: {nota_alta}")
    print(f"           Mínima: {nota_baja}")
    texto = f"Notas menores al promedio ({prom})"
    print(grun + SepSup + "\n" + f"{texto :^{aab}}" + "\n" + SepInf,    end="")
    print(f"           Número: {len(prom_menores)}")
    print(f"            Lista: {prom_menores}" + default)

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)