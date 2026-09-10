# p071-suma-promedio-numeros.py
# Calcular la suma y promedio de n calificaciones

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 70)
    print("🔢           Suma y promedio de n calificaciones           🔢")
    print("∵" * 70)

    n = int(input("¿Cuántas calificaciones son? "))
    print("…" * 70)

    i = 0 # contador
    sum = 0 # acumular suma calificaciones
    cadena = "" # cadena de texto vacía
         
    for x in range(1, n+1, 1): 

        while True:

            cal = float(input(f"Escribe la calificación {x:02d} (base 10): "))

            if 0 <= cal <= 10:

                i += 1
                
                cadena = cadena + "\t" + f"{cal:05.2f}"
                sum = sum + cal
            
                if i % 5 == 0: cadena += "\n\t\t" # cambio de línea después de 5 iteraciones

                break
    
            else:
                print("…" * 70)
                print("❌  ¡Ha ocurrido un error!  ❌")
                print("Las calificaciones deben estar en base 10.")
                print(f"Ingresaste: {cal}\nError en calificación {i}")
                print("Vuelve a intentarlo.")
                print("…" * 70)

    print("…" * 70)
    print(f"→ {n} calificaciones: {cadena}")
    print(f"\t\tSUMA = {sum:05.2f}\t\tPROMEDIO = {sum/n:05.2f}")
  
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
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)