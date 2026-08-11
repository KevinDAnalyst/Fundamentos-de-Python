# ==============================================================================
# PROYECTO FINAL: ANÁLISIS DE RENDIMIENTO DE CAMPAÑAS DIGITALES CON PANDAS Y MATPLOTLIB
# Archivo de entrada: marketing_campaign_dataset.csv
# ==============================================================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# 1. VARIABLES GLOBALES (Requisito: al menos 4 variables globales)
# ------------------------------------------------------------------------------
RUTA_ARCHIVO_DEFAULT = "TAREAS/proyecto/marketing_campaign_dataset.csv"  # Ruta predeterminada del dataset
DATAFRAME_CAMPANAS = None                                 # Variable global para almacenar el DataFrame limpio
CANALES_VALIDOS = ["Search", "Social", "Email", "Display", "Influencer"] # Filtro de canales permitidos
SISTEMA_ACTIVO = True                                     # Flag global de control para el bucle del menú


# ------------------------------------------------------------------------------
# 2. MÓDULO DE CARGA, LIMPIEZA Y CONVERSIÓN CON PANDAS (Pasos 1 y 4 IteraFlex)
# ------------------------------------------------------------------------------
def cargar_y_limpiar_datos(ruta_archivo):
    """
    Carga el archivo CSV con Pandas, maneja errores de ruta/formato mediante try/except,
    elimina duplicados/nulos y realiza la conversión explícita de tipos de datos.
    Retorna un DataFrame de Pandas depurado o None si ocurre un error.
    """
    # Variables locales para el control del proceso de carga
    df_raw = None
    df_limpio = None
    registros_iniciales = 0
    registros_finales = 0

    try:
        print(f"\n[+] Intentando cargar el archivo de datos: '{ruta_archivo}'...")
        
        # Lectura con Pandas
        df_raw = pd.read_csv(ruta_archivo)
        registros_iniciales = len(df_raw)
        print(f"[✓] Archivo leído correctamente. Registros iniciales: {registros_iniciales}")

        # 1. Depuración: Eliminación de duplicados exactos
        df_limpio = df_raw.drop_duplicates()

        # 2. Depuración: Limpieza de filas con valores vacíos/nulos en campos clave
        columnas_criticas = ['Campaign_ID', 'Channel', 'Acquisition_Cost', 'ROI']
        columnas_presentes = [col for col in columnas_criticas if col in df_limpio.columns]
        df_limpio = df_limpio.dropna(subset=columnas_presentes)

        # 3. Conversiones de tipo de datos (Requisito: al menos 2 conversiones)
        
        # CONVERSIÓN 1: Mapeo de columnas de texto a formato fecha (datetime)
        if 'Date' in df_limpio.columns:
            df_limpio['Date'] = pd.to_datetime(df_limpio['Date'], errors='coerce')

        # CONVERSIÓN 2: Conversión explícita de campos numéricos (str/float a int/float)
        # Enteros (métrica de conteo)
        for col_int in ['Clicks', 'Conversions', 'Impressions']:
            if col_int in df_limpio.columns:
                df_limpio[col_int] = pd.to_numeric(df_limpio[col_int], errors='coerce').fillna(0).astype(int)

        # Flotantes (métrica monetaria y de porcentaje)
        for col_float in ['Acquisition_Cost', 'ROI', 'Conversion_Rate', 'Spend']:
            if col_float in df_limpio.columns:
                df_limpio[col_float] = pd.to_numeric(df_limpio[col_float], errors='coerce').fillna(0.0).astype(float)

        # Re-filtrar si alguna conversión generó NaNs inválidos
        df_limpio = df_limpio.dropna(subset=columnas_presentes)
        registros_finales = len(df_limpio)

        filas_eliminadas = registros_iniciales - registros_finales
        print(f"[✓] Limpieza completada. Filas omitidas (duplicadas/nulas/inválidas): {filas_eliminadas}")
        print(f"[✓] Registros limpios listos para análisis: {registros_finales}")

        return df_limpio

    except FileNotFoundError:
        print(f"\n[!] ERROR CRÍTICO: No se encontró el archivo '{ruta_archivo}'.")
        print("    Asegúrate de que el archivo CSV esté en la misma carpeta que este script.")
        return None

    except pd.errors.EmptyDataError:
        print(f"\n[!] ERROR: El archivo '{ruta_archivo}' está completamente vacío.")
        return None

    except Exception as e:
        print(f"\n[!] ERROR INESPERADO al procesar los datos: {e}")
        return None


# ------------------------------------------------------------------------------
# 3. MÓDULO DE ANÁLISIS ESTADÍSTICO Y VISUALIZACIÓN CON MATPLOTLIB (Pasos 2 y 3 IteraFlex)
# ------------------------------------------------------------------------------
def calcular_metricas_generales(df):
    """
    Calcula y despliega las métricas estadísticas globales del dataset,
    tales como inversión total, ROI promedio, conversiones y estadísticas descriptivas.
    """
    if df is None or df.empty:
        print("\n[!] No hay datos disponibles para realizar el cálculo.")
        return

    print("\n" + "=" * 55)
    print("           RESUMEN ESTADÍSTICO GENERAL")
    print("=" * 55)

    # Variables locales para métricas agregadas
    total_campanas = len(df)
    inversion_total = df['Acquisition_Cost'].sum() if 'Acquisition_Cost' in df.columns else 0.0
    roi_promedio = df['ROI'].mean() if 'ROI' in df.columns else 0.0
    clics_totales = df['Clicks'].sum() if 'Clicks' in df.columns else 0
    conversiones_totales = df['Conversions'].sum() if 'Conversions' in df.columns else 0

    # Métrica derivada: Costo por Adquisición Promedio (CPA)
    cpa_promedio = (inversion_total / conversiones_totales) if conversiones_totales > 0 else 0.0

    # Despliegue de métricas principales
    print(f"• Total de Campañas Analizadas:  {total_campanas:,}")
    print(f"• Inversión / Costo Total:      ${inversion_total:,.2f}")
    print(f"• Clics Totales Generados:      {clics_totales:,}")
    print(f"• Conversiones Totales:          {conversiones_totales:,}")
    print(f"• ROI Promedio General:         {roi_promedio:.2f}x")
    print(f"• Costo por Adquisición (CPA):  ${cpa_promedio:,.2f}")

    print("\n" + "-" * 55)
    print("  DESGLOSE DESCRIPTIVO DE VARIABLES CLAVE (Pandas)")
    print("-" * 55)

    # Extracción de estadísticas descriptivas a diccionario
    cols_analizar = [c for c in ['Acquisition_Cost', 'ROI', 'Clicks', 'Conversions'] if c in df.columns]
    stats_dict = df[cols_analizar].describe().round(2).to_dict()

    # Recorrido del diccionario extraído de Pandas
    for columna, metricas in stats_dict.items():
        print(f"\n Variable: [{columna}]")
        print(f"   - Mínimo:          {metricas['min']}")
        print(f"   - Máximo:          {metricas['max']}")
        print(f"   - Promedio (Media): {metricas['mean']}")
        print(f"   - Mediana (50%):    {metricas['50%']}")
        print(f"   - Desv. Estándar:   {metricas['std']}")

    print("=" * 55)


def analizar_y_graficar_por_canal(df):
    """
    Agrupa los datos por canal de marketing con groupby y genera un gráfico de barras con Matplotlib.
    """
    # AGRUPACIÓN EN PANDAS:
    # df_canal = df.groupby('Channel').agg({
    #     'ROI': 'mean',
    #     'Acquisition_Cost': 'sum',
    #     'Campaign_ID': 'count'
    # }).reset_index()
    #
    # VISUALIZACIÓN CON MATPLOTLIB:
    # plt.figure(figsize=(10, 5))
    # plt.bar(df_canal['Channel'], df_canal['ROI'], color='skyblue')
    # plt.title('ROI Promedio por Canal Publicitario')
    # plt.xlabel('Canal')
    # plt.ylabel('ROI Promedio')
    # plt.grid(axis='y', linestyle='--', alpha=0.7)
    # plt.show()
    pass


# ------------------------------------------------------------------------------
# 4. MÓDULO DE CONSULTAS Y FILTRADO (Interacción con el usuario)
# ------------------------------------------------------------------------------
def filtrar_por_umbral_roi(df, umbral_minimo):
    """
    INTERACCIÓN USUARIO 1: Aplica un filtro condicional sobre el DataFrame según la entrada del usuario.
    """
    # BÚSQUEDA CONDICIONAL EN PANDAS (Condicional if / mascaras de Pandas):
    # df_filtrado = df[df['ROI'] >= umbral_minimo]
    #
    # CONDICIONAL:
    # if df_filtrado.empty:
    #     print(f"No se encontraron campañas con un ROI mayor o igual a {umbral_minimo}")
    # else:
    #     print(f"Se encontraron {len(df_filtrado)} campañas:")
    #     print(df_filtrado[['Campaign_ID', 'Channel', 'Acquisition_Cost', 'ROI']].head(10))
    pass


def agregar_nueva_campana(df):
    """
    INTERACCIÓN USUARIO 2: Solicita datos por consola para incorporar una nueva campaña al DataFrame.
    """
    # Solicitud de inputs al usuario (ID, Canal, Clics, Costo, Conversiones, ROI)
    # Validar que los valores numéricos sean válidos con try/except
    # Crear un nuevo diccionario con los datos ingresados
    # Concatenar al DataFrame global: df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)
    # print("Campaña añadida exitosamente.")
    # return df
    pass


# ------------------------------------------------------------------------------
# 5. MENÚ INTERACTIVO PRINCIPAL POR CONSOLA (Paso 4 IteraFlex)
# ------------------------------------------------------------------------------
def mostrar_menu_principal():
    """
    Controla la navegación interactiva mediante consola utilizando un bucle while
    y condicionales para desplegar y procesar las opciones del usuario.
    """
    global DATAFRAME_CAMPANAS, SISTEMA_ACTIVO
    
    # Intentar cargar los datos al iniciar el programa
    print("Iniciando el sistema y cargando datos...")
    DATAFRAME_CAMPANAS = cargar_y_limpiar_datos(RUTA_ARCHIVO_DEFAULT)
    
    # Bucle principal de interacción (while)
    while SISTEMA_ACTIVO:
        print("\n" + "=" * 50)
        print("   SISTEMA DE ANÁLISIS DE CAMPAÑAS DIGITALES")
        print("=" * 50)
        print("1. Ver resumen estadístico general (Pandas)")
        print("2. Analizar y graficar rendimiento por canal (Matplotlib)")
        print("3. Filtrar campañas por umbral de ROI")
        print("4. Registrar una nueva campaña al sistema")
        print("5. Salir")
        print("=" * 50)
        
        # Interacción con el usuario: Entrada de la opción deseada
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        # Estructura condicional (if / elif / else)
        if opcion == "1":
            if DATAFRAME_CAMPANAS is not None and not DATAFRAME_CAMPANAS.empty:
                calcular_metricas_generales(DATAFRAME_CAMPANAS)
            else:
                print("\n[!] No hay datos cargados para realizar el análisis.")
                
        elif opcion == "2":
            if DATAFRAME_CAMPANAS is not None and not DATAFRAME_CAMPANAS.empty:
                analizar_y_graficar_por_canal(DATAFRAME_CAMPANAS)
            else:
                print("\n[!] No hay datos cargados para visualizar.")
                
        elif opcion == "3":
            if DATAFRAME_CAMPANAS is not None and not DATAFRAME_CAMPANAS.empty:
                try:
                    umbral = float(input("\nIngrese el ROI mínimo a consultar (ej. 2.5): "))
                    filtrar_por_umbral_roi(DATAFRAME_CAMPANAS, umbral)
                except ValueError:
                    print("\n[!] Error: Debe ingresar un valor numérico válido.")
            else:
                print("\n[!] No hay datos cargados para consultar.")
                
        elif opcion == "4":
            if DATAFRAME_CAMPANAS is not None:
                DATAFRAME_CAMPANAS = agregar_nueva_campana(DATAFRAME_CAMPANAS)
            else:
                print("\n[!] Primero debe cargar un archivo válido.")
                
        elif opcion == "5":
            SISTEMA_ACTIVO = False
            print("\nCerrando la sesión del sistema... ¡Hasta luego!")
            
        else:
            print("\n[!] Opción no válida. Por favor, ingrese un número del 1 al 5.")


# ------------------------------------------------------------------------------
# 6. EJECUCIÓN DEL SISTEMA
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    mostrar_menu_principal()