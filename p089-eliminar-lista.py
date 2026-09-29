# p089-eliminar-lista.py
# Eliminar elementos de una lista

aaa = 80  # formato inicio y fin
aab = aaa - 0 # formato encabezados

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

MensajeInicial =  "Eliminar elementos a una lista"
print("∴" * aaa)
print("✳️ " + MensajeInicial.center(aaa-5) + " ✳️")
print("∵" * aaa)

num = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]

print(f"\n{'~~ Datos iniciales ' :~<{aab}}")
print(f"Contenido: {num} | Longitud: {len(num)}\n")

print(f"{'~~ Eliminar el valor 99 ' :~<{aab}}")
num.remove(99)
print(f"Resultado: {num} | Longitud: {len(num)}\n ")

print(f"{'~~ Eliminar el elemento en la posición 3 usando del' :~<{aab}}")
del num[3]
print(f"Resultado: {num} | Longitud: {len(num)}\n ")

print(f"{'~~ Eliminar el elemento en la posición 8 usando pop() ' :~<{aab}}")
num_eliminado = num.pop(8)
print(f'Resultado: Removido ({num_eliminado}), {num} | Longitud: {len(num)}\n')

print(f"{'~~ Eliminar el último elemento usandoo pop() sin parámetros' :~<{aab}}")
ultimo_num = num.pop()
print(f'Resultado: Removido({ultimo_num}): {num} | Longitud: {len(num)}\n')

print(f"{'~~ Eliminar todos los elementos de la lista usando clear() ' :~<{aab}}")
num.clear()
print(f"Resultado: {num} | Longitud: {len(num)}\n ")

MensajeFinal = "¡Programa terminado!"
print("∴" * aaa)
print("✳️ " + MensajeFinal.center(aaa-5) + " ✳️")
print("∵" * aaa)