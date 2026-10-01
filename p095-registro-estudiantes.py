# p095-registro-estudiantes.py
""""
Planteamiento del problema: Registro de estudiantes para evento
• Se está organizando un evento y necesitas registrar a los asistentes.
• El programa debe permitir al usuario introducir el nombre y la edad de cada
persona.
• El registro termina cuando se introduce un * como nombre.
• Al finalizar, el sistema debe mostrar dos informes:
• una lista de todos los asistentes que son mayores de edad (18 años o más).
• y el nombre y la edad de la persona con mayor edad para entregarle un reconocimiento.
"""

aaa = 75  # formato inicio y fin
aab = aaa - 0 # formato encabezados
sep_sup = "\n" + "-" * aab
sep_inf = "-" * aab + "\n"
error = "❌  ¡Ha ocurrido un error! ❌"

print("\033[H\033[J")

MensajeInicial =  "Sistema de Registro para Evento"
print("∴" * aaa)
print("✳️ " + MensajeInicial.center(aaa-5) + " ✳️")
print("∵" * aaa)


print("Introduce los nombres y edades de los asistentes (* en nombre para terminar)\n")

# Listas paralelas para almacenar los datos
nombres = []
edades = []

# Ciclo para la captura de datos
while True:
    nombre = input("Nombre del asistente: ")
    if nombre == "*":
        break # Termina el ciclo si el nombre es *
    try:
        edad = int(input(f"Edad de {nombre}: "))
        if edad < 0:
            print(sep_sup)
            print(f"{error :^{aab}}")
            texto = f"Edad inválida. Debe ser un número positivo."
            print(f"{texto:^{aab}}")
            print(sep_inf)
            continue

        nombres.append(nombre) # Agrega el nombre a la lista
        edades.append(edad) # Agrega la edad en la misma posición

    except ValueError:
        print("Por favor, introduce una edad válida (número entero).")
        print(sep_sup)
        print(f"{error :^{aab}}")
        texto = f"Entrada inválida. Por favor, ingrese un número entero para la edad."
        print(f"{texto:^{aab}}")
        print(sep_inf)

print()
# Generación de Reportes 
if nombres:
    # Filtrar asistentes mayores de edad
    for i in range(len(edades)):
        if edades[i] >= 18:
            print(f"{nombres[i]} es mayor de edad con {edades[i]} años.")

    # Encontrar la persona con mayor edad
    max_edad = max(edades)
    indice_max_edad = edades.index(max_edad)
    print(f"\nLa persona con mayor edad es {nombres[indice_max_edad]} con {edades[indice_max_edad]} años. \n")

MensajeFinal = "¡Programa terminado!"
print("∴" * aaa)
print("✳️ " + MensajeFinal.center(aaa-5) + " ✳️")
print("∵" * aaa)