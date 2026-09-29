# p091-lista-de-gastos.py
# Desarrolla una aplicación que almacene gastos en una lista y permita al usuario 
# manipularla a través de un menú que se mostrará continuamente hasta que decida salir

aaa = 75  # formato inicio y fin
aab = aaa - 0 # formato encabezados

gastos = []

def mostrar_menu():
    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    MensajeInicial =  "Aplicación de gastos"
    print("∴" * aaa)
    print("✳️ " + MensajeInicial.center(aaa-5) + " ✳️")
    print("∵" * aaa)

    print("[ 1 ] Agregar gasto")
    print("[ 2 ] Mostrar gastos")
    print("[ 3 ] Eliminar gasto")
    print("[ 4 ] Modificar gasto")
    print("[ 5 ] Ver total de gastos")
    print("[ 6 ] Salir")

    #print("\nElige una opción: ")
    opcion = input("\nElige una opción: ")
    return opcion

def main():
    while True:

        opcion = mostrar_menu()

        exito = "✔️  ¡Operación exitosa! ✔️"
        error = "❌  ¡Ha ocurrido un error! ❌"
        separador = "\n" + "-" * aab + "\n"

        if opcion == "1":
            print(separador)
            print(f"{' 1. AGREGAR GASTO ' :^{aab}}")
            print(separador)

            try:
                gasto = float(input("Ingresa el monto del gasto: "))
            except ValueError:
                print(separador)
                print(f"{error :^{aab}}\n")
                texto = f"El monto ingresado no es válido."
                print(f"{texto:^{aab}}")
                print(separador)
            else:
                gastos.append(gasto)
                print(separador)
                print(f"{exito :^{aab}}\n")
                texto = f"Gasto de {gasto} agregado."
                print(f"{texto:^{aab}}")
                print(separador)

        elif opcion == "2":
            print(separador)
            print(f"{' 2. MOSTRAR GASTO ' :^{aab}}")
            print(separador)
        
            if gastos:
                print("Gastos actuales: ", end="")
                for i, gasto in enumerate(gastos):
                    print(f" Gasto {i + 1} - {gasto}", end="  ")
                    if (i + 1) % 3 == 0: print("\n\t\t") # cambio de línea después de 3 iteraciones

                print(separador)
                print(f"{exito :^{aab}}\n")
                texto = f"Gastos mostrados."
                print(f"{texto:^{aab}}")
                print(separador)

            else:
                print(separador)
                print(f"{error :^{aab}}\n")
                texto = f"No hay gastos registrados."
                print(f"{texto:^{aab}}")
                print(separador)

        elif opcion == "3":
            print(separador)
            print(f"{' 3. ELIMINAR GASTO ' :^{aab}}")
            print(separador)

            try:
                indice = int(input("Ingresa el número del gasto a eliminar: "))
            except ValueError:
                print(separador)
                print(f"{error :^{aab}}\n")
                texto = f"El número de gasto no es válido."
                print(f"{texto:^{aab}}")
                print(separador)
            else:
                if 0 <= indice < len(gastos):
                    eliminado = gastos.pop(indice)
                    print(separador)
                    print(f"{exito :^{aab}}\n")
                    texto = f"Gasto de {eliminado} eliminado."
                    print(f"{texto:^{aab}}")
                    print(separador)
                else:
                    print(separador)
                    print(f"{error :^{aab}}\n")
                    texto = f"Gasto no encontrado."
                    print(f"{texto:^{aab}}")
                    print(separador)

        elif opcion == "4":
            print(separador)
            print(f"{' 4. MODIFICAR GASTO ' :^{aab}}")
            print(separador)

            try:
                indice = int(input("Ingresa el número del gasto a modificar: "))
            except ValueError:
                print(separador)
                print(f"{error :^{aab}}\n")
                texto = f"El número del gasto no es válido."
                print(f"{texto:^{aab}}")
                print(separador)
            else:
                if 0 <= indice < len(gastos):
                    try:
                        nuevo_gasto = float(input("Ingresa el nuevo monto del gasto: "))
                    except ValueError:
                        print(separador)
                        print(f"{error :^{aab}}\n")
                        texto = f"El monto ingresado no es válido."
                        print(f"{texto:^{aab}}")
                        print(separador)
                    else:
                        gastos[indice] = nuevo_gasto
                        print(separador)
                        print(f"{exito :^{aab}}\n")
                        texto = f"Gasto modificado a {nuevo_gasto}."
                        print(f"{texto:^{aab}}")
                        print(separador)
                else:
                    print(separador)
                    print(f"{error :^{aab}}\n")
                    texto = f"Gasto no encontrado."
                    print(f"{texto:^{aab}}")
                    print(separador)

        elif opcion == "5":
            print(separador)
            print(f"{' 5. VER TOTAL DE GASTO ' :^{aab}}")
            print(separador)

            total = sum(gastos)
   
            print(separador)
            print(f"{exito :^{aab}}\n")
            texto = f"Total de gastos: {total}."
            print(f"{texto:^{aab}}")
            print(separador)

        elif opcion == "6":
            print(separador)
            print(f"{' Saliendo de la aplicación. ' :^{aab}}")
            print(separador)
            break

        else:
            print(separador)
            print(f"{error :^{aab}}\n")
            texto = f"Opción inválida. Intenta de nuevo."
            print(f"{texto:^{aab}}")
            print(separador)

        input("\nPresiona ENTER para volver al menú.")

if __name__ == '__main__':
    main()

MensajeFinal = "¡Programa terminado!"
print("∴" * aaa)
print("✳️ " + MensajeFinal.center(aaa-5) + " ✳️")
print("∵" * aaa)