# p053-conjetura-collatz.py
# Calcular la conjetura de Collatz
# Dado n, si es par dividir n/2, si es impar 3*n+1 hasta llegar a n

while True:
    
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 70)
    print("🔢         Imprime los números de la conjetura de Collatz           🔢")
    print("∵" * 70)

    while True:
        n = int(input("Escribe un número entero positivo: "))
        if n > 0: break
        print("…" * 70)
        print("❌ ¡Ha ocurrido un error! ❌ \nEl número ingresado debe ser mayor que 0.\nIntente de nuevo. ")
        print("…" * 70)
    
    print("…" * 70)

    print("La conjetura de Collatz es: \n")

    while n != 1:
        
        print(f" {n} ", end = "")

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    print(n)    
    if input("\n¿Deseas continuar? (S/N) ").upper() == "N": break

print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)