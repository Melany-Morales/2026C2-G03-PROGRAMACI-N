"""Módulo para leer la tabla de tipos de cambio del BCCR."""

import pandas as pd


URL_BCCR = (
    "https://gee.bccr.fi.cr/IndicadoresEconomicos/Cuadros/"
    "frmConsultaTCVentanilla.aspx"
)


def cargar_tabla_bccr(fuente=URL_BCCR):
    """Carga la tabla cruda del BCCR desde una dirección web o un HTML."""
    tablas_web = pd.read_html(
        fuente,
        encoding="utf-8",
        decimal=",",
        thousands=".",
    )
    datos = tablas_web[2].copy()
    tablas_web.clear()
    return datos
