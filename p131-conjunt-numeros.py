# p131-conjunt-numeros.py
# Conjunto de números
# Lista 1: 50, 60, 70, 80, 90, 100, 200
# Lista 2: 60, 90, 100, 300, 400, 500
# Lista 3: 10, 20, 60, 90, 70, 100, 600, 700

A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}

MeIni = "Conjunto de números" # Mensaje inicial --------
MeFin = "¡Programa terminado!" # Mensaje final -------------------------
aaa = 80  # Formato inicio y fin |||||||||||||||||||||||||||||||||||||||
aab = aaa - 20 # Formato encabezados|||||||||||||||||||||||||||||||||||||
LinSup = "∴" * aaa # Línea superior ....................................
LinInf = "∵" * aaa # Línea inferior ....................................
SepSup = "\n" + "-" * aab # Separador superior /////////////////////////
SepInf = "-" * aab + "\n" # Separador inferior /////////////////////////

gelb = "\033[93m" # amarillo
grun = "\033[92m" # verde
rot = "\033[91m" # rojo
blau = "\033[94m" # azul
lila = "\033[95m"  # morado
cyan = "\033[96m"  # cyan
default = "\033[0m"
italic = "\033[3m"  # cursiva
orange = "\033[38;5;208m"  # naranja
braun = "\033[38;5;130m"  # café

#########################################################################

print("\033[2J\033[1;1H")

print(blau + LinSup + "\n" + MeIni.upper().center(aaa) + "\n" + LinInf + default)

texto = f"Mostrar conjuntos"
print(italic + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"Conjunto A: {A}\nConjunto B: {B}\nConjunto C: {C}")

texto = f"Unión de conjuntos (A | B) y (B | C)"
print(default + grun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"A ∪ B: {A | B}")
print(f"B ∪ C: {B | C}")


texto = f"Diferencia de conjuntos (B - C)"
print(cyan + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"A - C: {A - C}")

texto = f"Diferencia Simétrica de conjuntos (A ^ B)"
print(lila + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"B Δ C: {B ^ C}")

texto = f"Intersección de conjuntos (B & C)"
print(braun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"B ∩ C: {B & C}")

texto = f"Subconjuntos"
print(rot + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
#print(f"¿Es {'Pablo', 'Mateo'} un subconjunto de B? {'Pablo', 'Mateo'}.issubset(B)")
print("¿Es A subconjunto de B?", A.issubset(B))
print("¿Es C subconjunto de A?", C.issubset(A))

# texto = f"Superconjuntos"
# print(gelb + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
# print(f"¿Es A superconjunto de {"Reynaldo", "Angelica"}? {A.issuperset({"Reynaldo", "Angelica"})}")

texto = f"Pertenencia y no pertenencia"
print(orange + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"¿Está el número 100 en el conjunto A? {100 in A}")
print(f"¿Está el número 60 en el conjunto A? {60 in A and 60 in B and 60 in C}")
print(f"¿No está el número 900 en el conjunto B? {900 not in C}")

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)