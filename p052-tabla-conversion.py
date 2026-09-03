# p052-tabla-conversion.py
# Imprimir una tabla de conversión de peso a dolar

tc = 16.80 # tasa de cambio actual

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")
    print("∴" * 70)
    print("🔄️              Tabla de conversión de peso a dólar                🔄️")
    print(f"💵              Tipo de cambio: {tc} pesos por 1 dólar             💵")
    print("∵" * 70)

    while True: # valida que los valores inicial y final sean correctos
        inicial = float(input("\nValor inicial del rango: "))
        final = float(input("Valor final del rango: "))

        if inicial < final and inicial > 0 and final > 0: break
        else: 
            print("…" * 70)
            print("❌ ¡Error en los valores! ❌ \nEl valor inicial debe ser mayor que cero y menor que el final.\nIntente de nuevo. ")
            print("…" * 70)

    c = inicial
    print("\n\tPeso\t\tDólar")
    print("—"*40)

    while c <= final:
        print(f"\t{c}\t\t{c/tc:.2f}")
        c += 1
    print("—"*40)

    if input("\n¿Deseas continuar (S/N)? ").upper() == "N": break
             
print("∴" * 70)
print("✳️                   Terminamos de imprimir tablas                   ✳️")
print("∵" * 70)