# p049-sumar-consecutivos.py
# Suma números hasta que el total sea >= 100

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

# Versión II

print("∴" * 70)
print("💰                       Meta de ahorro: $100                       💰")
print("∵" * 70)

print("Empezando a sumar números...")

c = 0
suma = 0

# El ciclo está programado para correr hasta 200, pero el 'break' lo detendrá antes
while c < 200:
    c += 1
    suma += c
    print(f"+[{c}] ", end="")

    
    # Verificamos si hemos alcanzado o superado la meta.
    if suma >= 100:
        print(" ")
        print("…" * 70)
        print(f"🏆 ¡Llegaste a ${suma}! 🏆")
        print(f"Se necesitaron los primeros {c} números para alcanzarla.")
        # La palabra 'break' termina el ciclo INMEDIATAMENTE.
        break

# Este mensaje se imprime después de que el ciclo ha terminado (por 'break' o de forma natural).
print("∴" * 70)
print("✳️                         ¡Meta alcanzada!                         ✳️")
print("∵" * 70)