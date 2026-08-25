# p028-retira-cuenta.py
# Simula un retiro de dinero de una cuenta con validaciones anidadas

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 60)
print("🏧 Bienvenido al Cajero Automático 🏧")
saldo_actual = 1500.50
print(f"💵 Tu saldo actual es: ${saldo_actual:,.2f}")
print("." * 60)

retiro = float(input("Ingresa la cantidad a retirar: $"))

print("." * 60)

if retiro > 0:
    print("➡️   Procedemos al retiro...")
    # Si la cantidad es válida, verificamos si hay fondos.
    if retiro <= saldo_actual:
        nuevo_saldo = saldo_actual - retiro
        print("✔️  ¡Retiro exitoso! ✔️")
        print(f"💵 Tu nuevo saldo es: ${nuevo_saldo:,.2f} 💵")
    else:
        # Si la cantidad es válida pero excede el saldo
        print("❌ ¡Fondos insuficientes! ❌ \nNo se puede completar la transacción.")
        print(f"Quieres retirar ${retiro:,.2f} pero tu saldo es ${saldo_actual:,.2f}")
else:
    # Si la cantidad ingresada no es válida.
    
    print("❌ ¡No se puede retirar! ❌\nLa cantidad a retirar debe ser un número positivo.")

print("." * 60)
print("Gracias por usar nuestro servicio.")
print("." * 60)