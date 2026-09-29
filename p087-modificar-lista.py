# p087-modificar-lista.py
# Modificar los elementos de una lista

aaa = 80  # formato inicio y fin
aab = aaa - 0 # formato encabezados

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

MensajeInicial =  "Modificar los elementos de una lista"
print("∴" * aaa)
print("✳️ " + MensajeInicial.center(aaa-5) + " ✳️")
print("∵" * aaa)

cal = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]

print(f"\nTodas las calificaciones: {cal} \n")

print(f"{'~~ Modificar calificaciones en posiciones [0] y [1] con 7 y 7 ' :~<{aab}}")
cal[0] = 7
cal[1] = 7
print(f"Resultado: {cal}\n")

print(f"{'~~ Modificar calificaciones en el rango [2:5] (sin incluir 5) con 9, 9, 9 ' :~<{aab}}")
cal[2:5] = [9, 9, 9]
print(f"Resultado: {cal}\n")


MensajeFinal = "¡Programa terminado!"
print("∴" * aaa)
print("✳️ " + MensajeFinal.center(aaa-5) + " ✳️")
print("∵" * aaa)