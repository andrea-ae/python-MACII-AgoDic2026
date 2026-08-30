# p042-precio-entrada-cine.py
# Determinar el precio de una entrada según la edad del cliente para la taquilla de un cine
# Solicitar la edad y mostrar el precio correspondiente

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("🍿             Mostrar el precio de una entrada al cine             🍿")
print("∵" * 70)

edad = int(input("Escribe la edad del cliente en años: "))

print("…" * 70)

print(f"Edad del cliente: {edad} años")

if edad < 5:
    print(f" ▬▬▬▶ La entrada es 🎫 GRATIS 🎫")
elif edad >= 5 and edad <= 12:
    print(f" ▬▬▬▶ La entrada cuesta 🎫 5 pesos 🎫")
elif edad >= 13 and edad <= 64:
    print(f" ▬▬▬▶ La entrada cuesta 🎫 10 pesos 🎫")
elif edad >= 65:
    print(f" ▬▬▬▶ La entrada cuesta 🎫 7 pesos 🎫")

    

print("∴" * 70)
print("✳️                       ¡Disfruta la función!                       ✳️")
print("∵" * 70)