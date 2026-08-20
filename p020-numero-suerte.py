# p020-numero-suerte.py
# Número de la suerte

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 60)
print("Mostrar número de la suerte")
print("." * 60)

# Entrada
numero = int(input("Escribe tu año de nacimiento en cuatro dígitos: "))

# Proceso
dig1 = numero//1000
dig2 = (numero%1000)//100
dig3 = ((numero%1000)%100)//10
dig4 = (((numero%1000)%100)%10)

suma = dig1 + dig2 + dig3 + dig4
print()
print()
print({dig3})
print({dig4})

# Salida
salida = (
    f"El año {numero} en dígitos individuales: \n"
    f"      {dig1} \n"
    f"      {dig2}\n"
    f"      {dig3} \n"
    f"      {dig4}\n"
    f"El número de la suerte es: {suma}"
)

print("." * 60)
print(salida)
print("." * 60)