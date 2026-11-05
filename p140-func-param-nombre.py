# p140-func-param-nombre.py
# Ejemplo de función con parámetros con nombre

def saluda(apaterno: str, amaterno: str, nombre: str) -> None:
    print(f"Hola {nombre} {apaterno} {amaterno}")

saluda("Valero", "Izquierdo", "Serafina")
saluda(nombre="Serafina", amaterno="Izquierdo", apaterno="Valero")
