# p088-agregar-lista.py
# Agregar elementos a una lista

aaa = 65  # formato inicio y fin
aab = aaa - 0 # formato encabezados

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

MensajeInicial =  "Agregar elementos a una lista"
print("∴" * aaa)
print("✳️ " + MensajeInicial.center(aaa-5) + " ✳️")
print("∵" * aaa)

num = [80.3, 12.5, 60.2, 30.4]

print(f"\n{'~~ Datos iniciales ' :~<{aab}}")
print(f"Contenido: {num} | Longitud: {len(num)}\n")

print(f"{'~~ Agregar 90 y 100 al final ' :~<{aab}}")
num.append(90)
num.append(100)
print(f"Resultado: {num} | Longitud: {len(num)}\n ")

print(f"{'~~ Insertar 80 en la posición 4 ' :~<{aab}}")
num.insert(4, 80)
print(f"Resultado: {num} | Longitud: {len(num)}\n ")

print(f"{'~~ Externder datos agregando [110, 120, 130] se agregan al final ' :~<{aab}}")
otros = [110, 120, 130]
num.extend(otros)
print(f"Resultado: {num} | Longitud: {len(num)}\n ")

MensajeFinal = "¡Programa terminado!"
print("∴" * aaa)
print("✳️ " + MensajeFinal.center(aaa-5) + " ✳️")
print("∵" * aaa)