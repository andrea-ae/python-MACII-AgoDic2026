# p036-numeros-consecutivos.py
# Recibe tres números enteros y determina si son consecutivos.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("🔢            Mostrar si tres números son consecutivos            🔢")
print("∵" * 70)

print("Escribe 3 números enteros separados por espacio: ")
n1, n2, n3 = map(int, input().split()) 

print("…" * 70)

if n1 + 1 == n2 and n1 + 2 == n3:
    print("✔️  ¡Los números ingresados son consecutivos!  ✔️")
    print(f"Ordenados de menor a mayor:\t{n1}\t{n2}\t{n3}")
elif n1 + 1 == n3 and n1 + 2 == n2:
    print("✔️  ¡Los números ingresados son consecutivos!  ✔️")
    print(f"Ordenados de menor a mayor:\t{n1}\t{n3}\t{n2}")
elif n2 + 1 == n1 and n2 + 2 == n3:
    print("✔️  ¡Los números ingresados son consecutivos!  ✔️")
    print(f"Ordenados de menor a mayor:\t{n2}\t{n1}\t{n3}")
elif n2 + 1 == n3 and n2 + 2 == n1:
    print("✔️  ¡Los números ingresados son consecutivos!  ✔️")
    print(f"Ordenados de menor a mayor:\t{n2}\t{n3}\t{n1}") 
elif n3 + 1 == n1 and n3 + 2 == n2:
    print("✔️  ¡Los números ingresados son consecutivos!  ✔️")
    print(f"Ordenados de menor a mayor:\t{n3}\t{n1}\t{n2}")
elif n3 + 1 == n2 and n3 + 2 == n1:
    print("✔️  ¡Los números ingresados son consecutivos!  ✔️")
    print(f"Ordenados de menor a mayor:\t{n3}\t{n2}\t{n1}") 
else:
    print("❌  ¡Los números ingresados NO son consecutivos!  ❌")
    

print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)