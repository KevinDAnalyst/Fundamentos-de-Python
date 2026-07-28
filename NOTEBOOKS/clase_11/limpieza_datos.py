"""Funciones para limpiar y filtrar los datos cambiarios."""

import pandas as pd


def limpiar_datos(datos):
    """Prepara la tabla del BCCR y calcula la columna Diferencial."""
    datos_limpios = datos.copy()

    datos_limpios.columns = datos_limpios.iloc[0]
    datos_limpios = datos_limpios.iloc[1:].reset_index(drop=True)
    datos_limpios["Tipo de Entidad"] = (
        datos_limpios["Tipo de Entidad"].ffill()
    )
    datos_limpios = datos_limpios.dropna(
        subset=["Entidad Autorizada"]
    ).copy()

    columnas_numericas = ["Compra", "Venta"]

    if "Diferencial Cambiario" in datos_limpios.columns:
        columnas_numericas.append("Diferencial Cambiario")

    for columna in columnas_numericas:
        datos_limpios[columna] = pd.to_numeric(
            datos_limpios[columna],
            errors="coerce",
        )

    datos_limpios = datos_limpios.dropna(
        subset=["Compra", "Venta"]
    ).copy()
    datos_limpios["Diferencial"] = (
        datos_limpios["Venta"] - datos_limpios["Compra"]
    )
    
    #Renombrar nombres Columnas
    datos_limpios.rename(columns = {
        'Tipo de Entidad':'TIPO',
        'Entidad Autorizada': 'ENTIDAD',
        'Diferencial Cambiario': 'DIFERENCIAL',
        'Última Actualización': 'FECHA',
        'Compra':'COMPRA',
        'Venta': 'VENTA'
    }, inplace=True)
    datos_limpios.head()

    return datos_limpios


def filtrar_diferencial_alto(datos: pd.DataFrame) -> pd.DataFrame:
    """Devuelve diferenciales altos"""
    promedio_diferencial = datos["DIFERENCIAL"].mean()
    filtro = datos["DIFERENCIAL"] > promedio_diferencial
    
    return datos[filtro].copy()

def filtrar_tipo_entidad(datos: pd.DataFrame):
    """Agrupar por tipo de entidad y calcular el promedio de compra, venta y diferencial"""
    columnas = ['COMPRA', 'VENTA', 'DIFERENCIAL']
    datos_agrupados = (
        datos.groupby('TIPO')[columnas]
        .mean()
        .round(2)
        .sort_values(by='DIFERENCIAL', ascending=False)
    ).copy()
    
    return datos_agrupados