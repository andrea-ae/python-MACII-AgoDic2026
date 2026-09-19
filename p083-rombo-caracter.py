# p083-rombo-caracter.py
# Solicitar al usuario un número entero impar n que representará la ancho y el ancho máximo de un rombo
# Dibujar el rombo utilizando el carácter que el usuario elija

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 60)
print("◆               Dibujar rombo de caracteres               ◆")
print("∵" * 60)

print("Para dibujar el rombo, escribe:")

while True:
    try:

        ancho = int(input("Ancho máximo del rombo (IMPAR): "))
        

# Validar que sea impar
        if ancho % 2 == 0:
            print("…" * 60)
            print("❌ ¡Ha ocurrido un error! ❌ \nEl ancho máximo del rombo debe ser un número IMPAR.")
            print("…" * 60)
            
            res = input("¿Deseas intentar nuevamente (S/N)? ").strip().upper()
            if res != "S":
                print("…" * 60)
                print("✳️                          ¡Fin del programa!                          ✳️")
                print("∵" * 60)
                exit()
            print()
            continue
        
        if ancho <= 0:
            print("…" * 60)
            print("❌ ¡Ha ocurrido un error! ❌ \nEl número debe ser mayor a cero.")
            print("…" * 60)
            continue
            
        break # Si todo es correcto, salimos del while
        
    except ValueError:
        print("…" * 60)
        print("❌ ¡Ha ocurrido un error! ❌ \nSolo se aceptan números enteros.")
        print("…" * 60)

c = input("Carácter que quieres usar: ")

print("…" * 60)
print("                ⏳ Imprimiendo rombo ⏳          ")
print("…" * 60)

espacios = caracteres = 0

mitad = (ancho//2) + 1

# Mitad superior
for i in range(1, mitad + 1):
    espacios = ancho - i
    caracteres = 2 * i - 1

        # Espacios
    for e in range(espacios):
        print(" ", end=" ")

        # Caracteres
    for j in range(1, caracteres + 1):
        print(c, end=" ")
    print()

# Mitad inferior
for i in range(mitad - 1, 0, -1):
    espacios = ancho - i
    caracteres = 2 * i - 1

    for e in range(espacios):
        print(" ", end=" ")
    for j in range(caracteres):
        print(c, end=" ")
    print()

print("∴" * 60)
print("✳️                   ¡Fin del programa!                   ✳️")
print("∵" * 60)