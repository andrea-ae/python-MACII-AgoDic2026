# p033-aceptar-estudiante-v2.py
# Aceptar a un estudiante en base a la edad y calificaciones (usando AND)


#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("VERSIÓN II")

print("∴" * 70)
print("🏫                  Admisiones de la Universidad                  🏫")
print("∵" * 70)

nombre = input("Escribe tu nombre: ").upper()
edad = int(input("Escribe tu edad: "))

print("…" * 70)

# Primer filtro: verificar la edad
if edad >= 18:
    # Si persona es mayor de edad, pasar al siguiente nivel de verificación
    print(f"{nombre}, ¡pasaste el primer filtro! \n⏳  Puedes continuar con el proceso.  ⏳")
    
    print("…" * 70)

    print("Ingresa 2 calificaciones, separadas por un espacio:")
    c1, c2 = input().split()
    c1, c2 = [float(c1), float(c2)]

    print("…" * 70)

    # Segundo filtro: verificar las calificaciones
    if c1 >= 8 and c2 >= 8:
        # Si se pasan ambos filtros (de edad y calificaciones)
        print(f"✔️  ¡Bienvenid@, {nombre}!   ✔️\nCumpliste satisfactoriamente con los requisitos.")
        
    else:
        print(f"❌   ¡Lo sentimos, {nombre}!   ❌ \nNo aceptamos calificaciones menores a 8.")
       

else:
    # Si la persona es menor de edad
    print(f"❌   ¡Lo sentimos, {nombre}!   ❌ \n🔞  Solamente aceptamos a mayores de 18 años.  🔞")


print("∴" * 70)
print("Fin del programa.")
print("∵" * 70)