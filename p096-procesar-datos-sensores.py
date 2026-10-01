# p096-procesar-datos-sensores.py
# Se tienen dos sensores que recogen 10 mediciones numéricas cada uno.
# Necesitamos un programa que realice las siguientes tareas:

aaa = 75  # formato inicio y fin
aab = aaa - 0 # formato encabezados
sep_sup = "\n" + "-" * aab
sep_inf = "-" * aab + "\n"

print("\033[H\033[J")

MensajeInicial =  "Procesamiento de datos de sensores"
print("∴" * aaa)
print("✳️ " + MensajeInicial.center(aaa-5) + " ✳️")
print("∵" * aaa)

sensor1 = []
sensor2 = []

# Genere dos listas con 10 números aleatorios (entre 1 y 100) para simular los datos de cada sensor y las muestre
from random import randint
mediciones = 20
for _ in range(mediciones):
    sensor1.append(randint(1, 10))
    sensor2.append(randint(1, 10))

print(sep_sup)
texto = f"DATOS"
print(f"{texto:^{aab}}")
print(sep_inf)

print("Sensor 1: ", sensor1)
print()
print("Sensor 2: ", sensor2)


# Aplique una "transformación" a los datos, que consiste en elevar al cuadrado cada medición en ambas listas
for i in range(mediciones):
    sensor1[i] = sensor1[i] ** 2
    sensor2[i] = sensor2[i] ** 2

print(sep_sup)
texto = f"DATOS DESPUÉS DE LA TRANSFORMACIÓN"
print(f"{texto:^{aab}}")
print(sep_inf)

print("Sensor 1: ", sensor1)
print()
print("Sensor 2: ", sensor2)

# Cree una tercera lista que contenga la suma combinada de los datos transformados de ambos sensores (la suma del primer 
#                                                 elemento de la lista 1 conel primero de la lista 2, y así sucesivamente)
total_suma = []
for i in range(mediciones):
    total_suma.append(sensor1[i] + sensor2[i])

print(sep_sup)
texto = f"DATOS TRANSFORMADOS DE AMBOS SENSORES"
print(f"{texto:^{aab}}")
print(sep_inf)
print("Suma combinada: ", total_suma)

print()
MensajeFinal = "¡Programa terminado!"
print("∴" * aaa)
print("✳️ " + MensajeFinal.center(aaa-5) + " ✳️")
print("∵" * aaa)