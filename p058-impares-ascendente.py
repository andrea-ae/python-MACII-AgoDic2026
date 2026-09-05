# p058-impares-ascendente.py
# Imprimir números impares y su suma total 
# Rango ascendente del 1 hasta n
# n es elegido por el usuario

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 76)
    print("🔢             Imprimir números impares ascendentes y su suma             🔢")
    print("∵" * 76)

    n = int(input("¿Hasta qué número entero quieres que llegue la secuencia? "))

    print("…" * 76)
    print("⏳  Iniciando secuencia de conteo ascendente...  ⏳")
    print("…" * 76)

    c = 1
    suma = 0
    while c <= n:
        print(f"{c:03d} ", end="")
        suma += c
        c += 2

    print(f"\n\nSuma de los números anteriores: {suma}")
    print("…" * 76)

    while True:
        res = input("¿Deseas continuar (S/N)? ").upper()

        if res == "N": 
            break
        elif res == "S": 
            print() 
            break
        else:
            print("…" * 76)
            print("❌ ¡Ha ocurrido un error! ❌ \nEscribiste algo distinto a 'S' o 'N'.\nIntenta nuevamente.")
            print("…" * 76)

    if res == "N": 
        break

print("∴" * 76)
print("✳️                         ¡Secuencia completada!                         ✳️")
print("∵" * 76)