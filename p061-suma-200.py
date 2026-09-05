# p061-suma-200.py
# Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200
#  Al terminar, mostrar cuántos números se introdujeron y la suma final

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 90)
    print("🔢 Contar números introducidos por el usuario hasta que su suma sea mayor o igual a 200🔢")
    print("∵" * 90)

    i = 0 
    suma = 0
    while True:
        if suma >= 200: break
        n = int(input(f"Suma actual: {suma:03d}.  Escribe un número entero: "))
        suma += n
        i += 1
          
    salida = (
        " ✔️   ¡Se ha alcanzado la meta de 200!   ✔️\n"
        f"               Suma final = {suma}\n"
        f"         Total de números = {i}"
    )
    print("…" * 90)    
    print(salida)
    print("…" * 90)

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

print("∴" * 90)
print("✳️                                 ¡Programa terminado!                                 ✳️")
print("∵" * 90)