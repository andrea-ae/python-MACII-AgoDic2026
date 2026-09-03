# p054-tabla-multiplicar-while-v1.py
# Imprime la tabla t de 1 a 10 usando while

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 70)
    print("🔢         Imprime la tabla de multiplicar del 1 al 10           🔢")
    print("∵" * 70)
    print("")
    
    # while True:
    #     n = int(input("Escribe un número entero positivo: "))
    #     if n > 0: break
    #     print("…" * 70)
    #     print("❌ ¡Ha ocurrido un error! ❌ \nEl número ingresado debe ser mayor que 0.\nIntente de nuevo. ")
    #     print("…" * 70)


    t = int(input("¿Qué tabla quieres? "))
    n = int(input("¿Hasta dónde? "))

    print("")
    print("—"*20)
    print("    TABLA DEL " + str(t), end="\n")
    print("—"*20)

    c = 1
    while c <= n:
        print(f"  {t:3} x {c:3} = {c*t}")
        c += 1

    if input("\n¿Deseas continuar? (S/N) ").upper() == "N": break

print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)