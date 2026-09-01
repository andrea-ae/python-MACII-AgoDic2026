# p050-conteo-numeros.py
# Lee números hasta ingresar 999, luego, muestra un resumen estadístico

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("📊                     Analizador de números                      📊")
print("∵" * 70)

cuenta = 0
suma = 0
cuenta_positivos = 0
cuenta_negativos = 0
cuenta_ceros = 0

while True:
    num = int(input("Escribe un número entero [999 para finalizar]: "))

    if num == 999: # Condición de salida
        print("…" * 70)
        print("🔚 Código de salida [999] detectado 🔚")
        print("…" * 70)
        break # Rompe el ciclo infinito

    # Proceso
    cuenta += 1
    suma += num
    if num > 0:
        cuenta_positivos += 1
    elif num < 0:
        cuenta_negativos += 1
    else:
        cuenta_ceros += 1

print(f"Escribiste {cuenta} números:")
print(f"▶ {cuenta_positivos} positivos \n▶ {cuenta_negativos} negativos \n▶ {cuenta_ceros} ceros ")
print(f"La suma de todos los números es: {suma}")

print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)