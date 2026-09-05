# p064-verificar-palindromo.py
# Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 70)
    print("🔢              Verificar si un número es palíndromo                🔢")
    print("∵" * 70)

    num = input("Escribe un número entero: ")

    print("…" * 70)
    print(f"El número: {num}")

    m =  len(str(num)) - 1 # m - 1 porque empieza en 0
    i = 0 # 0 porque el primer dígito tiene posición 0
    while i < m:

        if num[i] != num[m]: 
            print("❌  NO es palindromo  ❌")
            print("…" * 70)
            break
        else:
            print("✔️  SÍ es palindromo  ✔️")
            print("…" * 70)

        i += 1
        m -= 1

    while True:
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