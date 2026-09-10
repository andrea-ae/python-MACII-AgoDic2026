# p072-suma-mutiplos.py
# Imprimir los números de 1 a n, solo múltiplos de m

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 50)
    print("🔢           Múltiplos de m, de 1 a n           🔢")
    print("∵" * 50)

    n = int(input("¿Hasta qué número quieres que llegue? "))
    m = int(input("¿Qué múltiplos quieres? "))
    print("…" * 50)

    i = 0 # contador de multiplos de m
    suma = 0 # acumular suma de multiplos de m
    cadena = "\t" # cadena de texto vacía
         
    for x in range(1, n+1): 
        if x % m == 0: # es par
            cadena = cadena + " " + f"{x:03d}"
            suma = suma + x
            i += 1

            if i % 5 == 0: cadena += "\n\t" # cambio de línea después de 18 iteraciones

    print(f"\tNÚMEROS DEL 1 AL {n}: \n\tMÚLTIPLOS DE {m}\n")
    print(cadena)
    print(f"\tSuma = {suma:03d}")

 
    while True:
        
        print("…" * 50)
        res = input("¿Deseas continuar (S/N)? ").upper()
    
        if res == "N": 
            break
        elif res == "S": 
            print() 
            break
        else:
            print("…" * 50)
            print("❌ ¡Ha ocurrido un error! ❌ \nEscribiste algo distinto a 'S' o 'N'.\nIntenta nuevamente.")
            print("…" * 50)
    
    if res == "N": 
            break

print("∴" * 50)
print("✳️               Fin del programa                ✳️")
print("∵" * 50)