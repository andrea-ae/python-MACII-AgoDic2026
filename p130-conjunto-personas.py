# p130-conjunto-personas.py
# Conjunto de nombres
# Lista 1: Juan, Maria, Pedro, Jose, Rocio
# Lista 2: Pedro, Juan, Pablo, Mateo, Esther

A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}

MeIni = "Conjunto de nombres" # Mensaje inicial --------
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
print(f"Conjunto A: {A}\nConjunto B: {B}")

texto = f"Unión de conjuntos (A | B)"
print(default + grun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"A ∪ B: {A | B}")

texto = f"Intersección de conjuntos (A & B)"
print(braun + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"A ∩ B: {A & B}")

texto = f"Diferencia de conjuntos (A - B)"
print(cyan + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"A - B: {A - B}")

texto = f"Diferencia Simétrica de conjuntos (A ^ B)"
print(lila + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"A Δ B: {A ^ B}")

texto = f"Subconjuntos"
print(rot + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
#print(f"¿Es {'Pablo', 'Mateo'} un subconjunto de B? {'Pablo', 'Mateo'}.issubset(B)")
print("¿{Pablo, Mateo} es subconjunto de B?",
      {"Pablo", "Mateo"}.issubset(B))

texto = f"Superconjuntos"
print(gelb + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"¿Es A superconjunto de {"Reynaldo", "Angelica"}? {A.issuperset({"Reynaldo", "Angelica"})}")

texto = f"Pertenencia y no pertenencia"
print(orange + SepSup + "\n" + f"{texto.upper():^{aab}}" + "\n" + SepInf, end="")
print(f"¿Está el nombre 'Pedro' en el conjunto A? {"Pedro" in A}")
print(f"¿No está el nombre 'Lili' en el conjunto B? {6 not in B}")

print()
print(blau + LinSup + "\n" + MeFin.upper().center(aaa) + "\n" + LinInf + default)