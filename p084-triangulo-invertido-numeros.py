# p084-triangulo-invertido-numeros.py
# Solicitar al usuario un número entero n 
# Determinará la altura de un triángulo numérico invertido
# Imprimir n renglones. 
# Primero: contendrá los números de 1 a n
# Segundo de 1 a n-1
# Así sucesivamente hasta que el último renglón contenga solo el número 1

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("∴" * 70)
print("◤                   Triángulo invertido de números                   ◤")
print("∵" * 70)

n = int(input("Escribe un número entero: "))

print("…" * 70)
print("                ⏳ Imprimiendo triángulo ⏳          ")
print("…" * 70)

print()

# Renglones
for i in range(n, 0, -1):

    for j in range(1, i + 1):
        print(j, end=" ")
    #n -=1   
    print()
     
print()
print("∴" * 70)
print("✳️                        ¡Fin del programa!                         ✳️")
print("∵" * 70)