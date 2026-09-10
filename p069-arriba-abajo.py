# p069-arriba-abajo.py
# Imprimir números de 1 a n o de n a 1

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 70)
    print("🔢           Imprimir números ascendentes o descendentes           🔢")
    print("∵" * 70)
    print("Opciones: \n[1] Números de 1 a n. \n[2] Números de n a 1.")

    op = int(input("Elige una opción: "))

    print("…" * 70)


    if op == 1:
        print("Imprimir números de 1 a n:")
        print("…" * 70)
        n = int(input("¿Hasta qué número quieres que llegue? "))
        print("…" * 70)
        print("Iniciando secuencia de conteo ascendente...")

        i = 0
         
        for x in range(1, n+1, 1):
            print(f"{x:03d}", end=" ")
            i += 1

            if i % 18 == 0: print() # cambio de línea después de 18 iteraciones

        print(" ")

    elif op == 2:
        print("Imprimir números de n a 1:")
        print("…" * 70)
        n = int(input("¿Desde dónde quieres que empiece? "))
        print("…" * 70)
        print("Iniciando secuencia de conteo descendente...")

        i = 0
             
        for x in range(n, 0, -1):
            print(f"{x:03d}", end=" ")
            i += 1

            if i % 18 == 0: print() # cambio de línea después de 18 iteraciones

        print(" ")

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