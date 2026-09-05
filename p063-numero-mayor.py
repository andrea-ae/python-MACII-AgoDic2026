# p063-numero-mayor.py
# Leer una serie de números hasta que el usuario ingrese un 0
# Al terminar, el programa deberá mostrar cuál fue el número más grande de todos los introducidos


while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 80)
    print("🔢   Mostrar el número mayor introducido por el usuario  🔢")
    print("∵" * 80)

    mayor = 0

    print("Escribe números enteros [0 para terminar]: ")

    while True:
        n = int(input())

        if n == 0: break
               
        if mayor < n:
            mayor = n

    salida = (
        f"       Número mayor = {mayor}"
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