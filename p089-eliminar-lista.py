# p089-eliminar-lista.py
# Eliminar elementos de una lista

aae = 65
#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

MensajeInicial =  "Eliminar elementos a una lista"
print("∴" * aae)
print("✳️ " + MensajeInicial.center(aae-5) + " ✳️")
print("∵" * aae)

num = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]

print(f'\nDatos originales con anomalías: {num}\n')

print("…" * aae)

print(f'Eliminar el valor 99:')
num.remove(99)
print(f'Resultado : {num}\n')

print("…" * aae)

print(f'Eliminar el elemento en la posición 8')
num_removido = num.pop(8)
print(f'Resultado : Removido ({num_removido}), {num}\n')

print("…" * aae)

print(f'Eliminar el último elemento:')
ultimo_num = num.pop()
print(f'Resultado: Removido({ultimo_num}): {num}\n')

print("…" * aae)

print(f'Eliminar todos los elementos de la lista:')
num.clear()
print(f'Resultado: {num}\n')


MensajeFinal = "¡Programa terminado!"
print("∴" * aae)
print("✳️ " + MensajeFinal.center(aae-5) + " ✳️")
print("∵" * aae)