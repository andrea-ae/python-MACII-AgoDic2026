# p092-procesar-calificaciones.py
# Procesa calificaciones en una lista
# Procesa n calificaciones entre 1 y 10 en una lista hasta intoducir 999
# Al final muestra: lista, suma, promedio, calificación más alta y la más baja,
# Cuántos alumnos superaron el promedio
# Valida que no introduzca letras en lugar de números

aaa = 75  # formato inicio y fin
aab = aaa - 0 # formato encabezados
error = "❌  ¡Ha ocurrido un error! ❌"
sep_sup = "\n" + "-" * aab
sep_inf = "-" * aab + "\n"

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

MensajeInicial =  "Procesador de calificaciones de un curso"
print("∴" * aaa)
print("✳️ " + MensajeInicial.center(aaa-5) + " ✳️")
print("∵" * aaa)

print("\nIntroduce calificaciones entre 0 y 10 (usa 999 para terminar):\n")

calificaciones = []
suma = 0.0

while True:
    try:
        calif = float(input("Calificación: "))
        if calif == 999: 
            break

        elif 1 <= calif <= 10:
            calificaciones.append(calif)
            suma += calif

        else:
            print(sep_sup)
            print(f"{error :^{aab}}")
            texto = f"La calificación debe estar entre 1 y 10."
            print(f"{texto:^{aab}}")
            print(sep_inf)

    except ValueError:
        print(sep_sup)
        print(f"{error :^{aab}}")
        texto = f"Entrada no válida. Por favor, introduce un número."
        print(f"{texto:^{aab}}")
        print(sep_inf)

if calificaciones:
    prom = suma / len(calificaciones)
    calif_alta = max(calificaciones)
    calif_baja = min(calificaciones)
    prom_mayores = sum(1 for cal in calificaciones if cal > prom)

    print(sep_sup)
    texto = f"RESULTADOS"
    print(f"{texto:^{aab}}")
    print(sep_inf)
    print(f"Lista: {calificaciones}\n")
    print(f"                 Suma: {suma}")
    print(f"             Promedio: {prom}")
    print(f"Calificación más alta: {calif_alta}")
    print(f"Calificación más baja: {calif_baja}\n")
    print(f"         Número de calificaciones ingresadas: {len(calificaciones)}")
    print(f"Número de calificaciones mayores al promedio: {prom_mayores}")

print()
MensajeFinal = "¡Programa terminado!"
print("∴" * aaa)
print("✳️ " + MensajeFinal.center(aaa-5) + " ✳️")
print("∵" * aaa)