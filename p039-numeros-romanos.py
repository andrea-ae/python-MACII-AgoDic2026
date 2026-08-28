# p039-numeros-romanos.py
# Pide un número entero entre 1 y 10
# Muestra su equivalente en números romanos
# Si el número está fuera de este rango, debe mostrar un mensaje de error


#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("🔢              Mostrar equivalente en números romanos             🔢")
print("∵" * 70)

num = int(input("Escribe un número entero entre 1 y 10:  "))

print("…" * 70)

if 1 <= num and num <= 10:
    if num == 1:
        print(f"El número {num} en romano es I.")
    elif num == 2:
        print(f"El número {num} en romano es II.")
    elif num == 3:
        print(f"El número {num} en romano es III.")
    elif num == 4:
        print(f"El número {num} en romano es IV.")
    elif num == 5:
        print(f"El número {num} en romano es V.")
    elif num == 6:
        print(f"El número {num} en romano es VI.")
    elif num == 7:
        print(f"El número {num} en romano es VII.")
    elif num == 8:
        print(f"El número {num} en romano es VIII.")
    elif num == 9:
        print(f"El número {num} en romano es IX.")
    elif num == 10:
        print(f"El número {num} en romano es X.")

else:
    print("❌  ¡Número fuera de rango!  ❌ \nPor favor reinicia el programa e ingresa un número entre 1 y 10.")


print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)