# p070-suma-pares-impares.py
# Imprimir suma de los pares e impares de 1 a n
# El usuario elige hasta donde quiere que llegue, se muestra la suma de pares e impares

# Versión I (classroom)

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 70)
    print("🔢           Imprimir la suma de números pares o impares           🔢")
    print("∵" * 70)

    n = int(input("¿Hasta qué número quieres que llegue? "))
    print("…" * 70)

    np = ni = 0 # contador de pares e impares
    sp = si = 0 # acumular suma par e impar
    cp = ci = "" # cadena de texto vacía
         
    for x in range(1, n+1, 1): 
        if x % 2 == 0: # es par
            cp = cp + " " + f"{x:003d}"
            sp= sp + x
            np += 1

            if np % 18 == 0: cp += "\n" # cambio de línea después de 18 iteraciones


        else: # es impar
            ci = ci + " " + f"{x:003d}"           
            si = si + x
            ni += 1

            if ni % 18 == 0: ci += "\n" # cambio de línea después de 18 iteraciones

    print(f"\t▶ Números PARES de 1 a {n} ◀")
    print(cp)
    print("…" * 70)
    print(f"\t▶ Números IMPARES de 1 a {n} ◀")
    print(ci)

    print("…" * 70)
    print(f"Suma de {np} números  PARES  del 1 hasta el {n} = {sp} ")
    print(f"\nSuma de {ni} números IMPARES del 1 hasta el {n} = {si} ")


 
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