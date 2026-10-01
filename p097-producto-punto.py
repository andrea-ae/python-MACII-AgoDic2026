# p097-producto-punto.py
# Cálculo del producto punto de dos vectores

aaa = 75  # formato inicio y fin
aab = aaa - 0 # formato encabezados
sep_sup = "\n" + "-" * aab
sep_inf = "-" * aab + "\n"
error = "❌  ¡Ha ocurrido un error! ❌"

print("\033[H\033[J")

MensajeInicial =  "Cálculo del producto punto de dos vectores"
print("∴" * aaa)
print("✳️ " + MensajeInicial.center(aaa-5) + " ✳️")
print("∵" * aaa)

# Se tienen dos vectores de la misma longitud y se desea calcular su producto punto
vector1 = [1, 2, -5]
vector2 = [4, -2, -1]

# Validar que ambos vectores tengan la misma longitud antes de calcular el producto punto
if len(vector1) != len(vector2):
    print(sep_sup)
    print(f"{error :^{aab}}")
    texto = f"Los vectores deben tener la misma longitud."
    print(f"{texto:^{aab}}")
    print(sep_inf)

else:
    # Calcular el producto punto de los dos vectores y mostrar el resultado
    producto_punto = 0

    for i in range(len(vector1)):
        producto_punto += vector1[i] * vector2[i]

    print(sep_sup)
    print("      Vector 1: ", vector1)
    print("      Vector 2: ", vector2)
    print("Producto punto: ", producto_punto)
    print(sep_inf)


MensajeFinal = "¡Programa terminado!"
print("∴" * aaa)
print("✳️ " + MensajeFinal.center(aaa-5) + " ✳️")
print("∵" * aaa)