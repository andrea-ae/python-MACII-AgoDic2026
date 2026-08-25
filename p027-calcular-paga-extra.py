# p027-calcular-paga-extra.py
# Calcula la paga de un trabajador considerando horas extra.

#print("\033[2J\033[H", end="")
print("\033[H\033[J", end="")

print("." * 60)
print("💰 Calculando la paga de un trabajador 💰")
print("." * 60)

# Entrada
print("💼 Escribe los datos del trabajador 💼")
nombre = input("Nombre: ").upper()
horas = int(input("Horas trabajadas: "))
paga_hora = float(input("Paga por hora: "))



# Cálculo de la paga
horas_normales = 40
extra = paga_hora * 2
horas_extra = paga_extra =  0

if horas >= horas_normales:
    paga_normal = horas_normales * paga_hora
    horas_extra = horas - horas_normales
    paga_extra = horas_extra * (paga_hora*2)    
else:
    paga_normal = horas * paga_hora

total = paga_normal + paga_extra

salida = (
    f"✔️  ¡Cálculo completado! ✔️\n"
    f"{nombre} ha trabajado {horas} horas.\n"
    f"🔸 {horas_normales} horas normales a ${paga_hora:,.2f} por hora. \n"
    f"🔸 {horas_extra} horas extra a ${extra:,.2f} por hora.\n"
    + "." * 60 + "\n"
    #" RESUMEN \n"
    f" 💵 Paga normal: {paga_normal:13,.2f} pesos\n"
    f" 💵  Paga extra: {paga_extra:13,.2f} pesos\n"
    f" 💵  Paga total: {total:13,.2f} pesos"
)

print("." * 60)
print(salida)

print("." * 60)
print("Fin del programa.")
print("." * 60)