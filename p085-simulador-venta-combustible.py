# p085-simulador-venta-combustible.py)
# Se requiere desarrollar un sistema interactivo de consola para la gestión de una 
# estación de servicio (gasolinera). El programa debe permitir a los operadores 
# realizar cálculos de ventas, proyecciones de rendimiento y categorización de 
# clientes mediante un flujo lógico robusto.

while True:

    #print("\033[2J\033[H", end="")
    print("\033[H\033[J", end="")

    # -------------------------------------------------------------
    # DESPLIEGUE DEL MENÚ PRINCIPAL
    # -------------------------------------------------------------
    print("\n" + "=" * 45)
    print("     SISTEMA DE GESTIÓN DE GASOLINERA")
    print("=" * 45)
    print("1. Venta de combustible")
    print("2. Simulación de rendimiento")
    print("3. Clasificador de cliente")
    print("4. Salir")
    print("=" * 45)
    
    # Captura de opción como tipo string (str)
    opcion = input("Seleccione una opción (1-4): ").strip()

    # Validación de opción sin usar listas ni tuplas
    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
        print("\n[ERROR] Opción no válida. Debe ingresar un número entre 1 y 4.")
        continue  # Reinicia el ciclo menú inmediatamente

    # -------------------------------------------------------------
    # MÓDULO 1: VENTA DE COMBUSTIBLE
    # -------------------------------------------------------------
    if opcion == "1":
        print("\n--- MÓDULO 1: VENTA DE COMBUSTIBLE ---")
        tipo_combustible = str(input("Ingrese el tipo de combustible (ej. Magna, Premium, Diesel): "))

        # Validación de precio (float)
        precio_litro = 0.0
        while precio_litro <= 0:
            try:
                precio_litro = float(input("Ingrese el precio por litro: "))
                if precio_litro <= 0:
                    print("[ERROR] El precio debe ser un valor positivo mayor a cero.")
            except ValueError:
                print("[ERROR] Entrada inválida. Debe ingresar un número entero o decimal.")

        # Validación de cantidad de litros (float)
        cantidad_litros = 0.0
        while cantidad_litros <= 0:
            try:
                cantidad_litros = float(input("Ingrese la cantidad de litros: "))
                if cantidad_litros <= 0:
                    print("[ERROR] La cantidad de litros debe ser mayor a cero.")
            except ValueError:
                print("[ERROR] Entrada inválida. Debe ingresar un número entero o decimal.")

        # Cálculo del total a pagar (float)
        total_pagar = precio_litro * cantidad_litros

        # Ticket de venta formateado con f-strings, 2 decimales y alineación a la derecha
        print("\n" + "=" * 40)
        print("             TICKET DE VENTA            ")
        print("=" * 40)
        print(f"Combustible:       {tipo_combustible}")
        print(f"Precio por litro: $ {precio_litro:>10.2f}")
        print(f"Litros cargados:    {cantidad_litros:>10.2f} L")
        print("-" * 40)
        print(f"Total a pagar:    $ {total_pagar:>10.2f}")
        print("=" * 40)

    # -------------------------------------------------------------
    # MÓDULO 2: SIMULACIÓN DE RENDIMIENTO
    # -------------------------------------------------------------
    elif opcion == "2":
        print("\n--- MÓDULO 2: SIMULACIÓN DE RENDIMIENTO Y CONSUMO ---")

        # Conversión a float de kilometraje inicial
        km_inicial = -1.0
        while km_inicial < 0:
            try:
                km_inicial = float(input("Ingrese el kilometraje inicial del vehículo (km): "))
                if km_inicial < 0:
                    print("[ERROR] El kilometraje inicial no puede ser negativo.")
            except ValueError:
                print("[ERROR] Entrada inválida. Ingrese un número entero o decimal.")

        # Conversión a float del factor de rendimiento
        factor_rendimiento = 0.0
        while factor_rendimiento <= 0:
            try:
                factor_rendimiento = float(input("Ingrese el factor de rendimiento (km por litro): "))
                if factor_rendimiento <= 0:
                    print("[ERROR] El factor de rendimiento debe ser mayor a cero.")
            except ValueError:
                print("[ERROR] Entrada inválida. Ingrese un número entero o decimal.")

        # Distancia mensual (float)
        km_por_mes = 0.0
        while km_por_mes <= 0:
            try:
                km_por_mes = float(input("Ingrese la distancia estimada a recorrer por mes (km): "))
                if km_por_mes <= 0:
                    print("[ERROR] Los kilómetros mensuales deben ser mayor a cero.")
            except ValueError:
                print("[ERROR] Entrada inválida. Ingrese un número entero o decimal.")

        # Conversión explícita a entero (int) para la duración de la simulación
        total_meses = 0
        while total_meses <= 0:
            try:
                total_meses = int(input("Ingrese la cantidad de meses a simular: "))
                if total_meses <= 0:
                    print("[ERROR] El número de meses debe ser al menos 1.")
            except ValueError:
                print("[ERROR] Entrada inválida. Debe ingresar un número entero.")

        # Impresión de la tabla de simulación
        print("\n" + "=" * 62)
        print(f"{'TABLA PROYECTADA DE CONSUMO MENSUAL':^62}")
        print("=" * 62)
        print(f"{'Mes':^6} | {'Km Inicial':^12} | {'Km Final':^12} | {'Consumo Est. (L)':^18}")
        print("-" * 62)

        km_actual = km_inicial
        consumo_acumulado = 0.0

        # Ciclo for con range()
        for mes in range(1, total_meses + 1):
            km_final = km_actual + km_por_mes

            consumo_mes = km_por_mes / factor_rendimiento
            consumo_acumulado += consumo_mes

            print(f"{mes:^6d} | {km_actual:>12.1f} | {km_final:>12.1f} | {consumo_mes:>18.2f}")
            km_actual = km_final


        # USO DE DIVISIÓN ENTERA (//) Y RESIDUO (%): Cálculo del tiempo equivalente y tanques llenos
        anios_equivalentes = total_meses // 12
        meses_sobrantes = total_meses % 12
        tanques_completos = int(consumo_acumulado) // 50
        litros_residuo = consumo_acumulado % 50

        print("=" * 62)
        print(f" Distancia total proyectada: {total_meses * km_por_mes:>10.1f} km")
        print(f" Consumo total acumulado:    {consumo_acumulado:>10.2f} L")
        print(f" Tiempo equivalente:         {anios_equivalentes} año(s) y {meses_sobrantes} mes(es)")
        print(f" Estimación en tanques (50L): {tanques_completos} tanques llenos y {litros_residuo:.2f} L restantes")
        print("=" * 62)

    # -------------------------------------------------------------
    # MÓDULO 3: CLASIFICADOR DE CLIENTE
    # -------------------------------------------------------------
    elif opcion == "3":
        print("\n--- MÓDULO 3: CLASIFICACIÓN DE CLIENTES ---")

        # Validación de volumen mensual (float)
        volumen_mensual = -1.0
        while volumen_mensual < 0:
            try:
                volumen_mensual = float(input("Ingrese el volumen de compra mensual en litros: "))
                if volumen_mensual < 0:
                    print("[ERROR] El volumen de compra no puede ser un número negativo.")
            except ValueError:
                print("[ERROR] Entrada inválida. Debe ingresar un número entero o decimal.")

        # Captura y VALIDACIÓN ESTRICTA de entrada S/N (str) sin usar listas ni tuplas
        es_empresa = input("¿El cliente cuenta con registro de empresa/flotilla? (S/N): ").strip().upper()
        while es_empresa != "S" and es_empresa != "N":
            print("[ERROR] Entrada no válida. Ingrese exclusivamente 'S' para Sí o 'N' para No.")
            es_empresa = input("¿El cliente cuenta con registro de empresa/flotilla? (S/N): ").strip().upper()

        # Clasificación mediante if/elif/else y operadores lógicos (and, or)
        if volumen_mensual > 500 or (es_empresa == "S" and volumen_mensual >= 300):
            categoria = "Flotilla"
            descuento = 10.0
            beneficio = "Descuento preferencial + Facturación acumulada"
        elif volumen_mensual >= 10**2 and volumen_mensual <= 500:
            categoria = "Premium"
            descuento = 5.0
            beneficio = "Descuento en consumos + Puntos dobles"
        elif volumen_mensual >= 0 and volumen_mensual < 10**2:
            categoria = "Regular"
            descuento = 0.0
            beneficio = "Acumulación de puntos básicos"
        else:
            categoria = "No clasificado"
            descuento = 0.0
            beneficio = "Sin beneficios"

        print("\n" + "=" * 52)
        print(f"{'DIAGNÓSTICO DE CATEGORÍA DE CLIENTE':^52}")
        print("=" * 52)
        print(f"Volumen mensual acumulado: {volumen_mensual:>12.2f} L")
        print(f"Registro corporativo:      {es_empresa:>12}")
        print("-" * 52)
        print(f"Categoría asignada:        {categoria}")
        print(f"Descuento aplicable:       {descuento:>12.1f} %")
        print(f"Beneficios del programa:   {beneficio}")
        print("=" * 52)

    # -------------------------------------------------------------
    # MÓDULO 4: SALIR DEL PROGRAMA
    # -------------------------------------------------------------
    elif opcion == "4":
        print("\n" + "=" * 50)
        print(f"{'CERRANDO SISTEMA DE GESTIÓN':^50}")
        print("=" * 50)
        print(" Guardando registros de la sesión...")
        print(" Liberando memoria del sistema...")
        print(" Estado de la terminal: Finalizada correctamente.")
        print("-" * 50)
        print(" ¡Gracias por utilizar el sistema de la gasolinera!")
        print(" ¡Que tenga un excelente día!")
        print("=" * 50)
        break  # Rompe el ciclo while True limpiamente

    while True:
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

print("∴" * 50)
print("✳️             ¡Programa terminado!             ✳️")
print("∵" * 50)