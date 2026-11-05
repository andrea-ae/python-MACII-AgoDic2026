# p139-funcion-parametros.py
# Ejemplo de función con varios parámetros

def saluda(apaterno: str, nombre: str) -> None:
    print(f"Hola {nombre} {apaterno}")

saluda("Belmonte", "Marta")
# saluda("Marta") # Genera error (pocos)
# saluda("Belmonte", "Marta", "Extra") # Error: demasiados argumentos