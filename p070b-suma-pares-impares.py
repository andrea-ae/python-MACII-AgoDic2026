# p070b-suma-pares-impares.py
# Imprimir suma de los pares e impares de 1 a n
# El usuario elige si quiere sumar pares o impares y hasta donde

# Versión II (clase)

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 70)
    print("🔢           Imprimir la suma de números pares o impares           🔢")
    print("∵" * 70)
    print("Opciones: \n[1] Suma de números PARES de 1 a n. \n[2] Suma de números IMPARES de 1 a n.")

    op = int(input("Elige una opción: "))

    print("…" * 70)


    if op == 1:
        print("\t▶ Números PARES de 1 a n ◀")
        print("…" * 70)
        n = int(input("¿Hasta qué número quieres que llegue? "))
        print("…" * 70)
        print("Iniciando secuencia de conteo ascendente...")

        i = 0
        suma = 0
         
        for x in range(2, n+1, 2): # pares
            print(f"{x:03d}", end=" ")
            suma = suma + x
            i += 1

            if i % 18 == 0: print() # cambio de línea después de 18 iteraciones

        print(" ")
        print("…" * 70)
        print(f"\nLa suma de los números PARES del 1 hasta el {n}  es: {suma} ")
    

    elif op == 2:
        print("\t▶ Números IMPARES de 1 a n ◀")
        print("…" * 70)
        n = int(input("¿Hasta qué número quieres que llegue? "))
        print("…" * 70)
        print("Iniciando secuencia de conteo ascendente...")

        i = 0
        suma = 0
             
        for x in range(1, n+1, 2): # impares
            print(f"{x:03d}", end=" ")
            suma = suma + x
            i += 1

            if i % 18 == 0: print() # cambio de línea después de 18 iteraciones

        print(" ")
        print("…" * 70)
        print(f"\nLa suma de los números IMPARES del 1 hasta el {n}  es: {suma} ")

    else:
        print("❌ ¡Ha ocurrido un error! ❌ \nEscribiste algo distinto a '1' o '2'.\nIntenta nuevamente.")
  
    while True:
        
        print("…" * 70)
        res = input("¿Deseas continuar (S/N)? ").upper()
    
        if res == "N": 
            break
        elif res == "S": 
            print() 
            break
        else:
            print("…" * 70)
            print("❌ ¡Ha ocurrido un error! ❌ \nEscribiste algo distinto a 'S' o 'N'.\nIntenta nuevamente.")
            print("…" * 70)
    
    if res == "N": 
            break

print("∴" * 70)
print("✳️                      ¡Secuencia completada!                      ✳️")
print("∵" * 70)