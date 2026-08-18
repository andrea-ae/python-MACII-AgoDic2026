# p008b-entrada-multiple.py
# Entrada múltiple de valores en una sola línea con map

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Leer 10 números en la misma línea (separados por espacio)
print("Escribe 10 números separados por <Espacio>: ")

n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = map( float, input().split() )

print("\nLos números escritos fueron: ")
print(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)

# Sumar los 10 números
suma = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10

# Resultado
print(f"\nLa suma de los 10 números es: {suma}")