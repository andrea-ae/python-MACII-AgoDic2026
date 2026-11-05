# p138-funcion-parametro.py
# Ejemplo de una función con parámetros

def saluda(nombre: str) -> None:
    """Función que muestra mensaje de bienvenida y muestra cuántos caracteres tiene el nombre."""
    print(f"Hola {nombre}, ¡bienveni@ a Python!\nTu nombre tiene {len(nombre)} caracteres")

saluda("Marta de la Reina")
saluda("Serafina Valero")
saluda("Luisa Gómez")
saluda("Amelia Ledesma")