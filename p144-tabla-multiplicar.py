# p144-numero-multiplicar.py
# Dada una numero y un límite de la numero, imprime la numero hasta el límite

def numero_multiplicar(numero: int, limite: int) -> None:
    """Imprime la tabla de muntiplicad de un número hasta un límite."""
    print(f"\nTabla de multiplicar del {numero} hasta el {limite}:")
    for i in range(1, limite + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    print("")

# Solicita al usuario el número y el límite
numero = int(input("Ingrese el número de la tabla multiplicar que desea (ej. 5): "))
limite = int(input("Ingrese el límite hasta donde desea multiplicar (ej. 10): "))
numero_multiplicar(numero, limite)

# # Ejemplo de uso:
# numero_multiplicar(5, 10)