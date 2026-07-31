"""Funciones para limpiar y filtrar los datos cambiarios."""

import pandas as pd


def limpiar_datos(datos):
    """Prepara la tabla de tipos de cambio del BCCR."""
    datos_limpios = datos.copy()

    datos_limpios.ffill(inplace=True)
    datos_limpios.drop_duplicates(inplace=True)

    nombres_columnas = {
        0: "TIPO",
        1: "ENTIDAD",
        2: "COMPRA",
        3: "VENTA",
        4: "DIFERENCIAL",
        5: "FECHA",
    }
    datos_limpios.rename(columns=nombres_columnas, inplace=True)
    datos_limpios.drop(0, inplace=True)

    columnas_numericas = ["COMPRA", "VENTA", "DIFERENCIAL"]
    datos_limpios[columnas_numericas] = datos_limpios[
        columnas_numericas
    ].apply(pd.to_numeric, errors="coerce")
    datos_limpios["FECHA"] = pd.to_datetime(
        datos_limpios["FECHA"],
        dayfirst=True,
        errors="coerce",
    )
    datos_limpios.dropna(
        subset=["ENTIDAD", "COMPRA", "VENTA"],
        inplace=True,
    )

    return datos_limpios


def filtrar_diferencial_alto(datos):
    """Devuelve entidades coherentes con diferencial superior al promedio."""
    # TODO 6: cree dos condiciones y combínelas con &:
    # DIFERENCIAL superior al promedio y VENTA mayor que COMPRA.
    return datos.iloc[0:0].copy()


def resumir_por_tipo_entidad(datos):
    """Resume compra, venta y diferencial para cada tipo de entidad."""
    # TODO 7: agrupe por TIPO, calcule el promedio de COMPRA, VENTA y
    # DIFERENCIAL, redondee y ordene por DIFERENCIAL.
    return pd.DataFrame()
