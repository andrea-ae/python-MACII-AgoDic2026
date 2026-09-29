# p086-acceder-lista.py
# Acceder a elementos de una lista

aaa = 60  # formato inicio y fin
aab = aaa - 10 # formato encabezados

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

MensajeInicial =  "Acceder a los elementos de una lista"
print("∴" * aaa)
print("✳️ " + MensajeInicial.center(aaa-6) + " ✳️")
print("∵" * aaa)

nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]

print(f"\n{'~~ Datos iniciales ' :~<{aab}}")
print(f"Contenido: {nums}")
print(f"Longitud: {len(nums)}\n")

print(f"{'~~ Por índice positivo ' :~<{aab}}")
print(f"Elemento en el índice 0 y 8: {nums[0]} - {nums[8]}\n")

print(f"{'~~ Por índice negativo ' :~<{aab}}")
print(f"Elemento en el índice -9 y -1: {nums[-9]} - {nums[-1]}\n")

print(f"{'~~ Por rango ' :~<{aab}}")
print(f"Del 2 al 6 (sin incluir al 6): {nums[2:6]}\n")

print(f"{'~~ Por saltos ' :~<{aab}}")
print(f"Elementos con saltos de 2: {nums[::2]}")
print(f"Elementos con saltos de 3: {nums[::3]}\n")

MensajeFinal = "¡Programa terminado!"
print("∴" * aaa)
print("✳️ " + MensajeFinal.center(aaa-6) + " ✳️")
print("∵" * aaa)