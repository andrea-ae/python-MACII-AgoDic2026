# p043-calculadora-anio-bisiesto.py 
# Determine si un año, ingresado por el usuario, es bisiesto


#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("4️⃣                 Determinar si un año es bisiesto                 4️⃣")
print("∵" * 70)

anio = int(input("Escribe un año de la forma AAAA: "))

print("…" * 70)

print(f"Año ingresado: {anio}")

if anio % 4 == 0:
  
    if anio % 100 == 0:

        if anio % 400 == 0:
            print("✔️  SI es año bisiesto  ✔️")
        else:                
            print("❌  NO es año bisiesto  ❌")

    else:

        print("✔️  SI es año bisiesto  ✔️")
else:
    print("❌  NO es año bisiesto  ❌")



print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)