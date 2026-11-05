# p143-funcion-retorno.py
# Función que regresa unvalor

def suma(n1:int, n2:int) -> int:
    return n1 + n2

# se guarda el valor retornado por la función
res = suma(10,20)
print(f"\nLa suma de dos números constantes es: {res}")

print("\nIngresa dos números separados por enter: ")
a, b = int(input()), int(input())
# se imprime directamente el valor retornado por la función
print(f"La suma de {a} + {b} es {suma(a,b)}")