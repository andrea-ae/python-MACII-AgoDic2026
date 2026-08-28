# p038-dia-semana.py
# Solicite un número entero del 1 al 7 y muestra el día de la semana
# 1 es domingo y 7 es sábado
# Si el número ingresado está fuera de ese rango,muestra un mensaje de error.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("🔢                     Mostrar día de la semana                     🔢")
print("∵" * 70)

dia = int(input("Escribe un número entero del 1 al 7:  "))

print("…" * 70)

if 1 <= dia and dia <= 7:
    if dia == 1:
        print("El día es: ▶ DOMINGO ◀.")
    elif dia == 2:
        print("El día es: ▶\tLUNES\t◀\t")
    elif dia == 3:
        print("El día es: ▶\tMARTES\t◀\t")
    elif dia == 4:
        print("El día es: ▶\tMIÉRCOLES\t◀\t")
    elif dia == 5:
        print("El día es: ▶\tJUEVES\t◀\t")
    elif dia == 6:
        print("El día es: ▶\tVIERNES\t◀\t")
    elif dia == 7:
        print("El día es: ▶\tSÁBADO\t◀\t")

else:
    print("❌  ¡Número fuera de rango!  ❌ \nPor favor reinicia el programa e ingresa un número entre 1 y 7.")


print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)