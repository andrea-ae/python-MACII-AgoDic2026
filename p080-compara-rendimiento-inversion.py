# p080-compara-rendimiento-inversion.py
# Desarrollar programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años
# Usuario ingresa: monto inicial y tasa de interés anual (porcentaje) para cada fondo y años a proyectar
# Mostrar tabla comparativa anual e indicar el fondo con mejor rendimientl

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("💰                COMPARACIÓN DE FONDOS DE INVERSIÓN                💰")
print("∵" * 70)

try:
    mi1 = float(input("Escribe el monto inicial del fondo de inversión A: "))
    i1 = float(input("Escribe la tasa de interés anual (en %) del fondo de inversión A: "))
    mi2 = float(input("Escribe el monto inicial del fondo de inversión B: "))
    i2 = float(input("Escribe la tasa de interés anual (en %) del fondo de inversión B: "))

    anios = float(input("Escribe en número de años a proyectar: "))

    # Validar que sea número entero (en años)
    if anios != int(anios):
        print("…" * 70)
        print("❌ ¡Ha ocurrido un error! ❌\nSolo se aceptan números enteros.")
        print("…" * 70)
    else:
        anios = int(anios)

    # Validar que sea números enteros
    if mi1 <= 0 or mi2 <= 0 or anios <= 0 or i1 <= 0 or i2 <= 0:
        print("…" * 70)
        print("❌ ¡Ha ocurrido un error! ❌ \nLos valores deben ser positivos y la meta mayor al capital inicial.")
        print("…" * 70)

    # # Validar porcentajes
    # if 100 <= i1 <= 0 and 100 <= i2 <= 0:
    #     print("…" * 70)
    #     print("❌ ¡Ha ocurrido un error! ❌ \nAl ser porcentaje deben la tasa de interés debe estar entre 0% y 100%")
    #     print("…" * 70)

    print("…" * 70)
    print("\n\t ------- FONDO DE INVERSIÓN A -------  ")
    print(f"\t        Monto inicial: ${mi1:,.2f}")
    print(f"\tTasa de interés anual: {i1:.2f} %\n")


    print("\t ------- FONDO DE INVERSIÓN B -------  ")
    print(f"\t        Monto inicial: ${mi2:,.2f}")
    print(f"\tTasa de interés anual: {i2:.2f} %\n")
 

    print(f"\t     AÑOS A PROYECTAR: {anios}\n")
    print("…" * 70)

    print("\n     COMPARACIÓN DE RENDIMIENTOS ANUALES ")
    print("\t Año |  Fondo A  |  Fondo B")
    print("\t", end="")
    print("-" * 30)


    for i in range(1, anios + 1):
        mi1 += mi1 * (i1/100)
        mi2 += mi2 * (i2/100)

        print(f"\t {i:02d} | ${mi1:,.2f} | ${mi2:,.2f}  ", end="\n")

    print("\t", end="")
    print("-" * 30)
    print()

    print(f"\tDespués de {anios} años, se calcularon los montos: ")
    print(f"\t →  ${mi1:,.2f} para el fondo de inversión A")
    print(f"\t →  ${mi2:,.2f} para el fondo de inversión B")

    if mi1 > mi2:
        print("\n\tConclusión: el Fondo A superó al Fondo B.\n")
    elif mi1 < mi2:
        print("\n\tConclusión: el Fondo B superó al Fondo A.\n")
    else:
        print("\n\tConclusión: el Fondo A y el Fondo B son iguales.\n")

# Validar que se ingrese un número
except ValueError:
    print("…" * 70)
    print("❌ ¡Ha ocurrido un error! ❌\n Solo se aceptan números.")
    print("…" * 70)
    print()

print("∴" * 70)
print("✳️                        ¡Fin del programa!                         ✳️")
print("∵" * 70)