# ==============================================================================
# INICIO DE LA SECCIÓN DE ENTRADA
# Propósito: Capturar e ingresar iterativamente los datos de los vuelos de AeroRegistro,
# validando que los datos numéricos sean positivos y estandarizando las cadenas a mayúsculas.
# ==============================================================================

# Lista principal 'inventario' que almacena la colección de diccionarios (un diccionario por vuelo)
inventario = []

print("\033[2J\033[1;1H")
print("--- Sistema de Vuelos: AeroRegistro ---")
print("Ingrese '*' o deje el campo vacío y presione Enter para terminar la captura.\n")

# Ciclo principal de captura continua de datos
while True:
    # Captura del identificador de vuelo:
    # - .strip() elimina espacios en blanco al inicio/final.
    # - .upper() convierte el texto ingresado a mayúsculas para estandarizar la salida.
    numero_vuelo = input("Número de vuelo (ej. AA-101): ").strip().upper()
    
    # Condición de salida del ciclo: termina la captura si se ingresa '*' o se deja en blanco
    if numero_vuelo == '*' or numero_vuelo == '':
        break
        
    # Lectura y estandarización a mayúsculas de origen, destino y aerolínea
    origen = input("Ciudad de origen (ej. Ciudad de México): ").strip().upper()
    destino = input("Ciudad de destino (ej. Guadalajara): ").strip().upper()
    aerolinea = input("Aerolínea (ej. AeroMexico): ").strip().upper()
    
    # Bucle de validación para el número de pasajeros (debe ser entero y mayor a 0)
    while True:
        try:
            pasajeros = int(input("Número de pasajeros (ej. 180): "))
            if pasajeros > 0:
                break
            print("  [Error] El número de pasajeros debe ser un número entero positivo.")
        except ValueError:
            print("  [Error] Entrada inválida. Ingrese un número entero.")

    # Bucle de validación para la tarifa del boleto (debe ser valor numérico flotante y mayor a 0)
    while True:
        try:
            tarifa = float(input("Tarifa del boleto en pesos (ej. 2350.75): "))
            if tarifa > 0:
                break
            print("  [Error] La tarifa debe ser un valor positivo superior a 0.")
        except ValueError:
            print("  [Error] Entrada inválida. Ingrese un valor numérico adecuado.")
    
    # Creación del diccionario de vuelo con los pares clave-valor de cada atributo
    vuelo = {
        'numero_vuelo': numero_vuelo,
        'origen': origen,
        'destino': destino,
        'aerolinea': aerolinea,
        'pasajeros': pasajeros,
        'tarifa': tarifa
    }
    
    # Agregar el diccionario individual al inventario principal
    inventario.append(vuelo)
    print("-> Vuelo guardado correctamente en el inventario.\n")

# --- PROCESAMIENTO DE DATOS DEL INVENTARIO ---

# 1. Extracción de destinos únicos mediante comprensión de conjuntos (Set Comprehension).
#    Garantiza la eliminación automática de valores duplicados.
destinos_unicos = {vuelo['destino'] for vuelo in inventario}

# 2. Generación de lista de tuplas inmutables mediante comprensión de listas (List Comprehension).
#    Crea una tupla de tres elementos (numero_vuelo, aerolinea, destino) por cada registro.
historial = [
    (vuelo['numero_vuelo'], vuelo['aerolinea'], vuelo['destino']) 
    for vuelo in inventario
]

# 3. Cálculos matemáticos y analítica de datos
# Cálculo de la cantidad general de registros capturados en la lista
total_vuelos = len(inventario)

if total_vuelos > 0:
    # Conteo de frecuencia y cálculo del número de aerolíneas distintas usando dict.get()
    conteo_aerolineas = {}
    for vuelo in inventario:
        aero = vuelo['aerolinea']
        conteo_aerolineas[aero] = conteo_aerolineas.get(aero, 0) + 1
    aerolineas_unicas = len(conteo_aerolineas)

    # Conteo de frecuencia por cada destino único registrado
    conteo_destinos = {}
    for vuelo in inventario:
        dest = vuelo['destino']
        conteo_destinos[dest] = conteo_destinos.get(dest, 0) + 1
    num_destinos_unicos = len(conteo_destinos)
    
    # Totales acumulados y cálculo del promedio de pasajeros
    total_pasajeros = sum(vuelo['pasajeros'] for vuelo in inventario)
    promedio_pasajeros = total_pasajeros / total_vuelos

    # Totales acumulados y cálculo del promedio de tarifas por vuelo
    total_tarifas = sum(vuelo['tarifa'] for vuelo in inventario)
    promedio_tarifa = total_tarifas / total_vuelos
    
    # Identificación del vuelo con la tarifa máxima y mínima utilizando max/min y funciones lambda como clave de evaluación
    vuelo_max_tarifa = max(inventario, key=lambda x: x['tarifa'])
    vuelo_min_tarifa = min(inventario, key=lambda x: x['tarifa'])
    
    # Identificación del vuelo con el mayor y menor número de pasajeros a bordo
    vuelo_max_pasajeros = max(inventario, key=lambda x: x['pasajeros'])
    vuelo_min_pasajeros = min(inventario, key=lambda x: x['pasajeros'])

# ==============================================================================
# FIN DE LA SECCIÓN DE ENTRADA
# ==============================================================================

# ==============================================================================
# INICIO DE LA SECCIÓN DE SALIDA
# Propósito: Formatear y proyectar visualmente en pantalla las lecturas de los datos
# crudos, conjuntos, tuplas, tabla formateada con alineación y reporte estadístico.
# ==============================================================================

print("\n" + "="*80)
print("                           REPORTES Y SALIDAS DE DATOS")
print("="*80)

# 1. Impresión directa de la lista de diccionarios (datos sin procesar)
print("\n--- 1. DATOS CRUDOS ---")
print("Inventario completo (Lista de diccionarios):")
print(inventario)

# 2. Muestra de las colecciones derivadas (Set y Lista de Tuplas)
print("\n--- 2. ESTRUCTURAS DE DATOS DERIVADAS ---")
print("Destinos únicos registrados (Conjunto):")
print(destinos_unicos)

print("\nHistorial inmutable de vuelos (Tuplas):")
print(historial)

# 3. Presentación visual del inventario formateado en columnas tabulares
print("\n--- 3. TABLA DE DATOS DE VUELOS ---")
if not inventario:
    print("No se registraron vuelos en el inventario.")
else:
    # Encabezados con formateo f-strings: < indica alineación izquierda y > alineación derecha con ancho especificado
    header = f"{'#VUELO':<10} | {'ORIGEN':<20} | {'DESTINO':<20} | {'AEROLÍNEA':<15} | {'PASAJEROS':<10} | {'TARIFA (MXN)':>12}"
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    # Recorrido del inventario formateando valores numéricos de tarifas a dos decimales (,.2f)
    for vuelo in inventario:
        print(
            f"{vuelo['numero_vuelo']:<10} | "
            f"{vuelo['origen']:<20} | "
            f"{vuelo['destino']:<20} | "
            f"{vuelo['aerolinea']:<15} | "
            f"{vuelo['pasajeros']:<10} | "
            f"${vuelo['tarifa']:>11,.2f}"
        )
    print("-" * len(header))

# 4. Impresión estructurada del análisis matemático y conteos analíticos
print("\n--- 4. APARTADO DE CÁLCULOS Y ANALÍTICA ---")
if total_vuelos == 0:
    print("No hay datos suficientes para realizar cálculos analíticos.")
else:
    # Cantidad total de vuelos procesados
    print(f"• Total de vuelos registrados: {total_vuelos}\n")
    
    # Desglose numérico por cada aerolínea registrada
    print(f"• Cantidad de aerolíneas distintas: {aerolineas_unicas}")
    print("  Desglose por aerolínea:")
    for aerolinea, cantidad in conteo_aerolineas.items():
        print(f"    - {aerolinea}: {cantidad} vuelo(s)")
    
    # Desglose numérico por cada destino registrado
    print(f"\n• Número de destinos únicos: {num_destinos_unicos}")
    print("  Desglose por destino:")
    for destino, cantidad in conteo_destinos.items():
        print(f"    - {destino}: {cantidad} vuelo(s)")
        
    print("-" * 60)
    
    # Totales y promedios aplicados a la variable pasajeros
    print(f"• Total de pasajeros registrados:   {total_pasajeros:,} pasajeros")
    print(f"• Promedio de pasajeros por vuelo:  {promedio_pasajeros:.2f} pasajeros")
    print("-" * 60)
    
    # Totales y promedios aplicados al monto monetario de tarifas
    print(f"• Suma total de tarifas:            ${total_tarifas:,.2f} MXN")
    print(f"• Promedio de tarifa por vuelo:     ${promedio_tarifa:,.2f} MXN")
    print("-" * 60)
    
    # Enunciados descriptivos que destacan los valores extremos (Máximos y Mínimos)
    print("• Análisis de Tarifas (Máximo y Mínimo):")
    print(f"  {vuelo_max_tarifa['numero_vuelo']} de ${vuelo_max_tarifa['tarifa']:,.2f} MXN es el más caro, "
          f"{vuelo_min_tarifa['numero_vuelo']} de ${vuelo_min_tarifa['tarifa']:,.2f} MXN es el más barato.")
    
    print("\n• Análisis de Pasajeros (Máximo y Mínimo):")
    print(f"  {vuelo_max_pasajeros['numero_vuelo']} con {vuelo_max_pasajeros['pasajeros']} pasajeros es el que tiene más pasajeros, "
          f"{vuelo_min_pasajeros['numero_vuelo']} con {vuelo_min_pasajeros['pasajeros']} pasajeros es el que tiene menos pasajeros.")

# ==============================================================================
# FIN DE LA SECCIÓN DE SALIDA
# ==============================================================================