import json

# Ruta al archivo con los datos
ruta_archivo = 'ruta/del/archivo.txt'

# Función para cargar los datos desde el archivo
def cargar_datos_desde_archivo(ruta):
    with open(ruta, 'r') as archivo:
        datos = [json.loads(line) for line in archivo]
    return datos

# Cargar los datos desde el archivo
datos = cargar_datos_desde_archivo(ruta_archivo)

# Inicializar una lista para almacenar las 5 mejores configuraciones
mejores_configuraciones = []

# Iterar a través de los conjuntos de datos y encontrar las 5 mejores configuraciones
for conjunto_datos in datos:
    adg_actual = conjunto_datos.get('adg', float('-inf'))
    worst_drawdown_actual = conjunto_datos.get('worst_drawdown', float('inf'))

    # Seleccionar configuraciones con worst_drawdown < 0.6
    if worst_drawdown_actual < 0.6:
        # Si la lista aún no tiene 5 elementos, o la configuración actual es mejor que la peor de las 5
        if len(mejores_configuraciones) < 5 or (adg_actual > mejores_configuraciones[-1]['adg'] or 
                                                (adg_actual == mejores_configuraciones[-1]['adg'] and 
                                                worst_drawdown_actual < mejores_configuraciones[-1]['worst_drawdown'])):
            # Agregar o reemplazar la configuración actual en la lista
            mejores_configuraciones.append(conjunto_datos)
            # Ordenar la lista por adg (descendente) y worst_drawdown (ascendente)
            mejores_configuraciones = sorted(mejores_configuraciones, key=lambda x: (x['adg'], -x['worst_drawdown']), reverse=True)
            # Limitar la lista a los 5 mejores elementos
            mejores_configuraciones = mejores_configuraciones[:5]

# Imprimir las 5 mejores configuraciones
print("Las 5 mejores configuraciones (adg más alto con worst_drawdown más bajo, worst_drawdown < 0.6):")
for i, configuracion in enumerate(mejores_configuraciones, start=1):
    print(f"Configuración #{i}: {configuracion}")
