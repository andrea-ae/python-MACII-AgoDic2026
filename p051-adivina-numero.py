# p051-adivina-numero.py
# Permitir que el usuario realice múltiples intentos hasta que encuentre la respuesta correcta

import random
#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("🔮             ¡Bienvenid@ al juego ADIVINA EL NÚMERO!              🔮")
print("🤔      He pensado un número entre 1 y 50, ¿podrás adivinarlo?      🤔")
print("∵" * 70)

numero_secreto = random.randint(1, 50) # Se elige un número entero al azar entre 1 y 50
intento_usuario = 0
contador_intentos = 0

# Usamos 'while True' para que el juego continúe hasta que adivinemos el número y rompamos el ciclo con 'break'
while True:
    intento_usuario = int(input("🤔 ¿En qué número estoy pensando? 🤔: "))
    print("…" * 70)
    contador_intentos += 1

    # Lógica de pistas
    if intento_usuario < numero_secreto:
        print(f"📉 ¡El número {intento_usuario} es demasiado bajo! 📉 \nIntenta con uno más alto.")
        print("…" * 70)
    elif intento_usuario > numero_secreto:
        print(f"📈 ¡El número {intento_usuario} es demasiado alto! 📈 \nIntenta con uno más bajo.")
        print("…" * 70)
    else:
        # Si no es ni más bajo ni más alto, ¡es el correcto!
        print(f"🎉🎉🎉 ¡Felicidades! 🎉🎉🎉 \n🥳 ¡Adivinaste que el número secreto era {numero_secreto}! 🥳")
        print(f"Lo lograste en {contador_intentos} intentos.")
        break # Rompe el ciclo infinito


print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)