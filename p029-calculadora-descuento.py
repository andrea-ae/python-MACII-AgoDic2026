# p029-calculadora-descuento.py
# Simula una calculadora de descuentos basada el el monto de la compra

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 60)
print("💳  Calculadora de descuentos 💳")
print("." * 60)

compra = float(input("🛍️  Ingresa el total de tu compra: $"))

# Definimos las variables para el descuento
descuento = 0
porcentaje = 0

if compra > 2000:
    porcentaje = 0.20 # 20% de descuento
  #  descuento = compra * porcentaje
else:
    if compra > 1000:
        porcentaje = 0.10 # 10% de descuento
    #    descuento = compra * porcentaje
    else:
        if compra > 500:
            porcentaje = 0.05 # 5% de descuento
     #       descuento = compra * porcentaje
        else:
            # Si no aplica ninguno de los anteriores
            porcentaje = 0.00 # 0% de descuento
           # descuento = compra * porcentaje
            
descuento = compra * porcentaje

# Calculamos y mostramos el resultado
total = compra - descuento

salida = (
    f"💳 RESUMEN DE COMPRA 💳\n"
    f"💵      Total de la compra: ${compra:,.2f}\n"
    f"💵 Porcentaje de descuento: {int(porcentaje * 100):,.2f} %\n"
    f"💵    Ahorro por descuento: ${descuento:,.2f}\n"
    f"💵           Total a pagar: ${total:,.2f}"
)

print("." * 60)
print(salida)

print("." * 60)
print("¡Gracias por su compra!")
print("." * 60)