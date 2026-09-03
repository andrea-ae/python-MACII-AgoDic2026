# p055-tabla-multiplicar-while-v2.py
# Imprime las tablas hasta la del t, del 1 al n usando while
# t y n son elegidos por el usuario

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 70)
    print("🔢                     TABLAS DE MULTIPLICAR                       🔢")
    print("∵" * 70)
    print("")
    
    while True:
        n = int(input("¿Hasta qué tabla quieres? "))
        m = int(input("¿Hasta dónde las quieres? "))

        if n > 0 and m > 0: break
        print("…" * 70)
        print("❌ ¡Ha ocurrido un error! ❌ \nLos ingresados debes ser mayores que 0.\nIntente de nuevo. ")
        print("…" * 70)

    
    t = 1
    while t <= n:
        print("")
        print("—"*20)
        print("    TABLA DEL " + str(t), end="\n")
        print("—"*20)
       
        c = 1
        while c <= m:
            print(f"  {t:3} x {c:3} = {c*t}")
            c += 1

        t += 1

    if input("\n¿Deseas continuar? (S/N) ").upper() == "N": break


print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)