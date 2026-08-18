# p001-hola-mundo.py
# Lee datos y envía un saludo

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("Leyendo datos y enviando un saludo: \n")

# Leer datos
nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
peso = float(input("Escribe tu peso: "))

print(f" \n {nombre}, bienvenid@ a python. Tienes {edad} años y pesas {peso} kg. \n")

print(type(nombre))
print(type(edad))
print(type(peso))

print("\n" + nombre + ", bienvenid@ a python. Tienes " + str(edad) + " años y pesas " +str(peso) + " kg. \n")