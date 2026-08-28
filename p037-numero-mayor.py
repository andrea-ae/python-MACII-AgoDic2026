# p037-numero-mayor.py
# Recibe tres números enteros e identifiqu4 y muestAe cuál de ellos es el mayor.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("🔢                 Mostrar el mayor de tres números                 🔢")
print("∵" * 70)

print("Escribe 3 números enteros separados por espacio: ")
n1, n2, n3 = map(int, input().split()) 

print("…" * 70)

if n1 >= n2 and n1 >= n3:
    print(f"Números ingresados: {n1}, {n2} y {n3}")
    print(f"Número MAYOR ▬▬▬▶ {n1}")
elif n2 >= n1 and n2 >= n3:
    print(f"Números ingresados: {n1}, {n2} y {n3}")
    print(f"Número MAYOR ▬▬▬▶ {n2}")
elif n3 >= n2 and n3 >= n1:
    print(f"Números ingresados: {n1}, {n2} y {n3}")
    print(f"Número MAYOR ▬▬▬▶ {n3}")
    

print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)