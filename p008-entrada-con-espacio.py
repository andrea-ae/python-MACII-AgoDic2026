# p008-entrada-con-espacio.py
# Leer datos múltiples separados por un espacio u otro caracter

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("Escribe tres números separados por <Espacio>: ")

n1, n2, n3 = input().split() # split("-") para separar con - en vez del espacio
n1, n2, n3 = [int(n1), int(n2), int(n3)]

print("\nLos números escritos fueron: ")
print(n1, n2, n3)