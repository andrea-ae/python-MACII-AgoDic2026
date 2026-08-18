# p007-entrada-multiple.py
# Leer tres números separados con <Enter>

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("Escribe tres números separados por <Enter>: \n")

n1, n2, n3 = float(input()), float(input()), float(input())

print("\nLos números escritos fueron: ")
print(n1, n2, n3)