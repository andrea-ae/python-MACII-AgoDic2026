# p005-calculadora-imc.py
# Calcular el IMC de una persona

print("\033[2J\033[H", end="")

print("Calculadora del índice de masa corporal (IMC) \n")

peso_kg = float(input("Ingresa tu peso en kilogramos: "))
altura_m = float(input("Ingresa tu altura en metros: "))

imc = peso_kg / (altura_m**2)

print(f"")