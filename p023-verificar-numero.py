# p023-verificar-numero.py
# Verificar si un número es positivo, negativo o cero

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 60)
print("🤔 Verificar si un número es positivo, negativo o cero 🤔\n")
#print("." * 60)

# Entrada
num = int(input("Escribe un número entero: "))

#print("." * 60)

if num > 0:
    print(f"\n〰️👍〰️ El número {num} es POSITIVO (➕) 〰️👍〰️")
if num < 0:
    print(f"\n〰️👎〰️ El número {num} es NEGATIVO (➖) 〰️👎〰️")
if num == 0:
    print(f"\n〰️👊〰️ El número {num} es CERO (0️⃣ ) 〰️👊〰️")

#print("." * 60)
print("\nAquí terminamos de tomar decisiones.")
print("." * 60)