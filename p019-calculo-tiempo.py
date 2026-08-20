# p019-calculo-tiempo.py
# Mostrar horas como número entero en días, minutos y segundos.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 50)
print("Mostrar horas como días, minutos y segundos")
print("." * 50)

# Entrada
horas = int(input("Escribe una cantidad en horas: "))

# Proceso
dias = horas / 24
minutos = horas * 60
segundos = horas * 3600

# Salida
salida = (
        f"   Horas: {horas:>10,.0f}\n"
        f"    Días: {dias:>10,.0f}\n"
        f" Minutos: {minutos:>10,.0f}\n"
        f"Segundos: {segundos:>10,.0f}"
)
# print(f"\nHoras: {horas}")
# print(f"Días: {dias}")
# print(f"Minutos: {minutos}")
# print(f"Segundos: {segundos}")

print("." * 50)
print(salida)
print("." * 50)