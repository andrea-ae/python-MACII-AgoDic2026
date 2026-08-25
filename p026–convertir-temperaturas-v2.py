# p026–convertir-temperaturas-v2.py
# Convierte temperaturas y valida la opción del usuario
# De °C A °F o de °F a °C, según elija el usuario

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 60)
print("🌡️  Convierte entre grados Celsius y Fahrenheit 🌡️")
print("." * 60)

print("Opciones: \n[1] Convertir de Fahrenheit a Celsius. \n[2] Convertir de Celsius a Fahrenheit.")
op = int(input("Escribe lo que deseas hacer: ")) 

# Validación de la opción
if op == 1:
    print("." * 60)
    print("➡️   Convirtiendo a grados Celsius...")
    f = float(input("Escribe la temperatura en grados Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("." * 60)
    print(f"🌡️  Resultado:  🌡️ \n{f:.2f}°F equivalen a {c:.2f}°C.")
else:
    if op == 2:
        print("." * 60)
        print("➡️   Convirtiendo a grados Fahrenheit...")
        c = float(input("Escribe la temperatura en grados Celsius: "))
        f = (c * 9 / 5) + 32
        print("." * 60)
        print(f"🌡️  Resultado:  🌡️ \n{c:.2f}°C equivalen a {f:.2f}°F.")
    else:
        print("." * 60)
        print(f"❌ ¡Opción '{op}' inválida! ❌ \nPor favor, reinicia el programa y elige 1 o 2.")

print("." * 60)
print("Fin del programa.")
print("." * 60)