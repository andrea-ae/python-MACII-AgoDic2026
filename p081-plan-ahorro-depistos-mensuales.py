# p081-plan-ahorro-depistos-mensuales.py
# Simular plan de ahorro
# Solicitar al usuario: monto inicial, depósito mensual fijo, 
# tasa de interés mensual (porcentaje), y el número total de meses del plan
# Mostrar una tabla que detalle, para cada mes, el saldo inicial,
#  el interés ganado en ese mes, y el saldo final
#  El interés se calcula sobre el saldo inicial antes de sumar el nuevo depósito

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("💰                          PLAN DE AHORRO                          💰")
print("∵" * 70)

try:
    mi = float(input("Escribe el monto inicial: "))
    dmf = float(input("Escribe el depósito mensual fijo: "))
    i = float(input("Escribe la tasa de interés anual (en %): "))
    m = float(input("Escribe el número total de meses a proyectar: "))

    # Validar que sea número entero (en meses)
    if m != int(m):
        print("…" * 70)
        print("❌ ¡Ha ocurrido un error! ❌\nSolo se aceptan números enteros.")
        print("…" * 70)
    else:
        m = int(m)

    # Validar que sea números enteros
    if mi <= 0 or dmf <= 0 or i <= 0 or m <= 0:
        print("…" * 70)
        print("❌ ¡Ha ocurrido un error! ❌ \nLos valores deben ser positivos y la meta mayor al capital inicial.")
        print("…" * 70)

    print("…" * 70)
    print("\n        ----------- DATOS INGRESADOS -----------  ")
    print(f"\t  Monto inicial de ahorro: ${mi:,.2f}")
    print(f"\t    Depósito mensual fijo: ${dmf:.2f}")
    print(f"\t  Tasa de interés mensual: {i:.2f} %")
    print(f"\tNúmero de meses a simular: {m}\n")
    print()
 
    print("\t", end="")
    print("-" * 50)
    print(f"\t     PLAN DE AHORRO DETALLADO A {m} MESES")
    print("\t", end="")
    print("-" * 50)
    print("\t Mes | Saldo inicial |  Interés   |  Saldo final")
    print("\t", end="")
    print("-" * 50)

    for j in range(1, m + 1):
        ci = mi * (i/100)
        mf = mi + ci + dmf

        print(f"\t  {j:02d} |   ${mi:,.2f}   |   ${ci:,.2f}   |   ${mf:,.2f}  ", end="\n")
        mi = mf

    print("\t", end="")
    print("-" * 50)
    print()

    print(f"\tDespués de {m} meses, habrás ahorrado: ${mf:,.2f}")
    print()


# Validar que se ingrese un número
except ValueError:
    print("…" * 70)
    print("❌ ¡Ha ocurrido un error! ❌\n Solo se aceptan números.")
    print("…" * 70)
    print()

print("∴" * 70)
print("✳️                        ¡Fin del programa!                         ✳️")
print("∵" * 70)