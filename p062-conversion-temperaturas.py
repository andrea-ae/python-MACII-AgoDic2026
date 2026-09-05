# p062-conversion-temperaturas.py
# Introducir una temperatura inicial y una final en grados Celsius
# Convertir a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 70)
    print("🌡️                 Tabla de conversión de °C a °F                   🌡️")
    print("∵" * 70)

    while True: # valida que los valores inicial y final sean correctos
        inicial = float(input("Valor inicial del rango (en °C): "))
        final = float(input("Valor final del rango (en °C): "))

        if inicial < final and inicial > 0 and final > 0: break
        else: 
            print("…" * 70)
            print("❌ ¡Error en los valores! ❌ \nEl valor inicial debe ser mayor que cero y menor que el final.\nIntente de nuevo. ")
            print("…" * 70)

    
    print("…" * 70)

    print("\n\t°C\t=\t°F")
    print("—"*40)

    c = inicial    
    while c <= final:
        print(f"\t{c:.2f}\t=\t{(c * 9/5) + 32:.2f}")
        c += 1
    #print("—"*40)

    print("…" * 70)

    while True:
            res = input("¿Deseas continuar (S/N)? ").upper()
    
            if res == "N": 
                break
            elif res == "S": 
                print() 
                break
            else:
                print("…" * 90)
                print("❌ ¡Ha ocurrido un error! ❌ \nEscribiste algo distinto a 'S' o 'N'.\nIntenta nuevamente.")
                print("…" * 90)
    
    if res == "N": 
            break

print("∴" * 70)
print("✳️                  ¡Terminamos de imprimir tablas!                  ✳️")
print("∵" * 70)