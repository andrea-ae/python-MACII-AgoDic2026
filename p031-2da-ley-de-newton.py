# p031-2da-ley-de-newton.py
# Calcular fuerza, masa o aceleración según la elección del usuario.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("🍎             Calculadora de la Segunda Ley de Newton             🍎")
print("∵" * 70)

print("Opciones:")
print("[1] Calcular la Fuerza      (F = m*a)")
print("[2] Calcular la Masa        (m = F/a)")
print("[3] Calcular la Aceleración (a = F/m)")
op = int(input("Escribe lo que deseas calcular (1, 2 o 3): ")) 

print("…" * 70)

# La estructura if/elif/else ejecuta el cálculo correcto
if op == 1:
    print("⏳ Calculando la Fuerza...⏳")
    m = float(input("Escribe la masa en kilogramos: "))
    a = float(input("Escribe la aceleración en metros por segundo al cuadrado: "))
    f = m * a
    print("…" * 70)
    print(f"El objeto tiene una masa de {m:.2f} kg y una aceleración de {a:.2f} m/s²:")
    print(f"➡️  Su fuerza es de {f:.2f} N ")
elif op == 2:
    print("⏳ Calculando la Masa...⏳")
    f = float(input("Escribe la fuerza en newtons: "))
    a = float(input("Escribe la aceleración en metros por segundo al cuadrado: "))
    m = f / a
    print("…" * 70)
    print(f"El objeto tiene una fuerza de {f:.2f} N y una aceleración de {a:.2f} m/s²:")
    print(f"➡️  Su masa es de {m:.2f} kg ")
elif op == 3:
    print("⏳ Calculando la Aceleración...⏳")
    f = float(input("Escribe la fuerza en newtons: "))
    m = float(input("Escribe la masa en kilogramos: "))
    a = f / m
    print("…" * 70)
    print(f"El objeto tiene una fuerza de {f:.2f} N y una masa de {m:.2f} kg:")
    print(f"➡️  Su aceleración es de {a:.2f} m/s²")
else:
    print("…" * 70)
    print(f"❌ ¡Opción '{op}' inválida! ❌ \nPor favor, reinicia el programa y elige 1 o 2.")

print("∴" * 70)
print("Fin del programa.")
print("∵" * 70)