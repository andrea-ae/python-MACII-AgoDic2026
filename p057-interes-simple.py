# p057-interes-simple.py
# Calcular los años necesarios para alcanzar una meta de ahorro (interés simple)

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 70)
    print("💵             Calculadora de años para meta de ahorro             💵")
    print("∵" * 70)

    while True:
        ci = float(input("Escribe el capital inicial: "))
        ti = float(input("Escribe la tasa de interés anual (%): "))
        ma = float(input("Escribe la meta de ahorro: "))

        

        if ci > 0 and ti > 0 and ma > ci:
            break
        else:
            print("…" * 70)
            print("❌ ¡Ha ocurrido un error! ❌ \nLos valores deben ser positivos y la meta mayor al capital inicial.")
            print("…" * 70)

    ca = ci
    anios = iaf = 0
    td = ti / 100

    print("")
    print("—"*20)
    print("  AHORRO POR AÑO")
    print("—"*20)
    print(f" Años\tAhorro")

    while ca <= ma:

        print(f"{anios:3}\t{ca:.2f}")
        iaf = ca * td
        ca += iaf
        anios += 1

    print("")
    print("…" * 70)
    print(f"Para llegar a tu meta de ${ma:,.2f}, necesitarás {anios} años")
    print(f"El monto final acumulado será de ${ca:,.2f}")
    print("…" * 70)

    if input("\n¿Deseas continuar (S/N)? ").upper() == "N": break
             
print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)


