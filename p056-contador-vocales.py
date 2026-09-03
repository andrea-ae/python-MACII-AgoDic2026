# p056-contador-vocales.py
# Dada una frase, contar vocales, consonantes y otros

while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    print("∴" * 70)
    print("🔡               Cuenta los caracteres de una frase                 🔡")
    print("∵" * 70)

    frase = input("Escribe una frase: ").lower()

    print("")
    print("—"*50)
    print("             ANÁLISIS DE LA FRASE             ")
    print("—"*50)

    print(f" Frase: '{frase}'\n Caracteres: {len(frase)}")

    i = vocal = consonante = otro = 0
    while i < len(frase):
        c = frase[i]
        # print(c, end = " ")

        # Verificar si es una letra del alfabeto
        if "a" <= c <= "z":
        #  print("si")
            # Verificar si es una voval
            if c in "aeiou":
                vocal += 1
            else:
                consonante += 1
        else:
        #  print("no")
            otro += 1

        i += 1


    print(f" Vocales: {vocal}\n Consonantes: {consonante}\n Otros: {otro}")

    if input("\n¿Deseas continuar (S/N)? ").upper() == "N": break
             
print("∴" * 70)
print("✳️                         Fin del programa                         ✳️")
print("∵" * 70)
