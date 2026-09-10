# p073-cifrado-cesar.py
# Cifra un mensaje con desplazamientos (Cifrado de Cesar)


# p073-cifrado-cesar.py
# Cifra un mensaje usando el Cifrado César.
while True:
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")
    print("∴" * 70)
    print("🔢                         Cifrado de Cesar                        🔢")
    print("∵" * 70)

    original = input("Ingresa el mensaje a encriptar: ")
    desplazamiento = int(input("Ingresa la clave de desplazamiento (un número entero): ")) 
    
    cifrado = nuevo = ""

    for caracter in original:
        if caracter.isalpha(): # Solo ciframos las letras
            ascii = ord(caracter)

            # Verificamos si es mayúscula o minúscula para mantener el caso   
            base = ord('a') if caracter.islower() else ord('A')         
            # if caracter.islower():
            #      base = ord('a') 
            # else:
            #      base = ord('A')

            # Aplicamos la fórmula del cifrado
            nuevo = base + (ascii - base + desplazamiento) % 26
            cifrado = cifrado + chr(nuevo)

        else:
            cifrado = cifrado + caracter # Los otros caracteres pasan igual

    print(f"\nMensaje Original: {original}")
    print(f"Mensaje Cifrado: {cifrado}")

    
    while True:
        
        print("…" * 50)
        res = input("¿Deseas continuar (S/N)? ").upper()
    
        if res == "N": 
            break
        elif res == "S": 
            print() 
            break
        else:
            print("…" * 50)
            print("❌ ¡Ha ocurrido un error! ❌ \nEscribiste algo distinto a 'S' o 'N'.\nIntenta nuevamente.")
            print("…" * 50)
    
    if res == "N": 
            break






print("∴" * 70)
print("✳️                        ¡Fin del cifrado!                         ✳️")
print("∵" * 70)