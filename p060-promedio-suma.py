# p060-promedio-suma.py
# Leer números introducidos por el usuario hasta que ingrese un 0
# Al finalizar, mostrar el conteo total de números, la suma y el promedio de la serie

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 80)
    print("🔢   Contar los números introducidos por el usuario, sumarlos y promediarlos  🔢")
    print("∵" * 80)

    i = 0 
    suma = prom = 0

    print("Escribe números enteros [0 para terminar]: ")

    while True:
        n = int(input())
        if n == 0: break
               
        suma += n
        i += 1
        prom = suma / i

    

    salida = (
        f"   Total de números = {i}\n" # no se toma en cuenta el 0
        f"               Suma = {suma:.2f}\n"
        f"           Promedio = {prom:.2f}"
    )
    print("…" * 80)    
    print(salida)
    print("…" * 80)

    while True:
        res = input("¿Deseas continuar (S/N)? ").upper()

        if res == "N": 
            break
        elif res == "S": 
            print() 
            break
        else:
            print("…" * 80)
            print("❌ ¡Ha ocurrido un error! ❌ \nEscribiste algo distinto a 'S' o 'N'.\nIntenta nuevamente.")
            print("…" * 80)

    if res == "N": 
        break

print("∴" * 80)
print("✳️                            ¡Programa terminado!                            ✳️")
print("∵" * 80)