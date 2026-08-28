# p040-calculo-notas.py
# Calcular el promedio de 5 calificaciones ingresadas por el usuario
# Basado en el promedio, el programa deberá mostrar un mensaje


#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("📝                     Calcular promedio                     📝")
print("∵" * 70)

print("Escribe 5 calificaciones (en base 10) separadas por un espacio: ")
c1, c2, c3, c4, c5 = map(float, input().split()) 

print("…" * 70)



if 0 <= c1 <= 10 and 0 <= c2 <= 10 and 0 <= c3 <= 10 and 0 <= c4 <= 10 and 0 <= c5 <= 10:
    print(f"Calificaciones ingresadas: {c1}, {c2}, {c3}, {c4}, {c5}.")
    print("⏳ Calculando promedio...⏳")
    prom = (c1 + c2 + c3+ c4 + c5)/5
    print(f"➡️  Tu promedio es {prom:.1f}")

    if prom < 6:
        print(f"❌  ¡Quedas reprobad@!  ❌")
    elif prom >= 6 and prom < 7:
        print(f"✔️  ¡Pasas de panzazo!  ✔️")
    elif prom >= 7 and prom < 8:
        print(f"✔️  ¡Muy bien!  ✔️   Puedes mejorar.")
    elif prom >= 8 and prom < 9:
        print(f"✔️  ¡Excelente!  ✔️   Sigue así.")
    elif prom >= 9 and prom <= 10:
        print(f"✔️  ¡Perfecto!  ✔️   Tu esfuerzo valió la pena.")

else:
    print("❌  ¡Ha ocurrido un error!  ❌")
    print("Las calificaciones deben estar en base 10.")
    print(f"Ingresaste: {c1}, {c2}, {c3}, {c4}, {c5}.")
    print("Vuelve a intentarlo.")

print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)