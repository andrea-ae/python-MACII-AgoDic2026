# p141-func-param-defecto.py
# Uso de parámetros de valores por defecto

def calcular_total(monto: float, iva: float = 0.16) -> float:
    """Calcula el monto total."""
    return monto + (monto * iva)

# Llama usando el valor por defecto (0.16)
print(f"Total 1: ${calcular_total(1000):,.2f}")
# Llama con un valor específico (0.08)
print(f"Total 2: ${calcular_total(1000, 0.10):,.2f}")