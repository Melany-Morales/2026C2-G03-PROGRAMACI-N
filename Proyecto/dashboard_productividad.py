from io import BytesIO
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


ARCHIVO_POR_DEFECTO = (
    Path(__file__).parent
    / "Team productivity (01.01.2026 til 08.21.2026).xlsx"
)


st.set_page_config(
    page_title="Dashboard de órdenes",
    page_icon="📊",
    layout="wide",
)


@st.cache_data
def cargar_datos(contenido_archivo):
    datos = pd.read_excel(BytesIO(contenido_archivo))
    datos = datos.dropna(axis=1, how="all")
    datos.columns = datos.columns.astype(str).str.strip()

    columnas_requeridas = ["Date", "Changed by", "Full name", "Transaction"]
    columnas_faltantes = [
        columna
        for columna in columnas_requeridas
        if columna not in datos.columns
    ]

    if columnas_faltantes:
        faltantes = ", ".join(columnas_faltantes)
        raise ValueError(f"Faltan columnas requeridas: {faltantes}")

    datos["Date"] = pd.to_datetime(datos["Date"], errors="coerce")
    datos["Transaction"] = datos["Transaction"].astype(str).str.strip()
    datos["Full name"] = datos["Full name"].astype(str).str.strip()

    datos = datos.dropna(
        subset=["Date", "Changed by", "Full name", "Transaction"]
    ).copy()
    datos = datos[datos["Transaction"] == "VA02"]
    datos = datos.sort_values("Date").reset_index(drop=True)
    datos["Mes"] = datos["Date"].dt.to_period("M").astype(str)

    return datos


def crear_grafico_participacion(resumen):
    figura, eje = plt.subplots(figsize=(10, 5))
    eje.bar(resumen["Full name"], resumen["Porcentaje"])
    eje.set_title("Participación de órdenes por agente")
    eje.set_ylabel("Porcentaje del total (%)")
    eje.set_xlabel("Agente")
    eje.tick_params(axis="x", rotation=45)
    figura.tight_layout()
    return figura


def crear_grafico_mensual(resumen):
    figura, eje = plt.subplots(figsize=(10, 5))
    eje.bar(resumen["Mes"], resumen["Total de ordenes"])
    eje.set_title("Comparación mensual de órdenes")
    eje.set_ylabel("Cantidad de órdenes")
    eje.set_xlabel("Mes")
    eje.tick_params(axis="x", rotation=45)
    figura.tight_layout()
    return figura


st.title("Dashboard de órdenes del equipo")
st.caption("Cada registro con transacción VA02 representa una orden.")

with st.sidebar:
    st.header("Cargar datos")
    archivo_subido = st.file_uploader(
        "Selecciona el Excel del mes",
        type=["xlsx"],
    )

    if archivo_subido is None:
        if not ARCHIVO_POR_DEFECTO.exists():
            st.error("No se encontró el archivo Excel predeterminado.")
            st.stop()
        contenido = ARCHIVO_POR_DEFECTO.read_bytes()
        st.info(f"Usando: {ARCHIVO_POR_DEFECTO.name}")
    else:
        contenido = archivo_subido.getvalue()
        st.success(f"Archivo cargado: {archivo_subido.name}")

try:
    df = cargar_datos(contenido)
except ValueError as error:
    st.error(str(error))
    st.stop()

if df.empty:
    st.warning("No existen registros VA02 en el archivo seleccionado.")
    st.stop()

with st.sidebar:
    st.header("Filtros")
    nombres = sorted(df["Full name"].unique())
    agentes = st.multiselect(
        "Agente",
        options=nombres,
        default=nombres,
    )
    fecha_minima = df["Date"].min().date()
    fecha_maxima = df["Date"].max().date()
    fechas = st.date_input(
        "Periodo",
        value=(fecha_minima, fecha_maxima),
        min_value=fecha_minima,
        max_value=fecha_maxima,
    )

if len(fechas) != 2:
    st.warning("Selecciona una fecha inicial y una fecha final.")
    st.stop()

fecha_inicio = pd.Timestamp(fechas[0])
fecha_fin = pd.Timestamp(fechas[1]) + pd.Timedelta(days=1)
filtrado = df[
    df["Full name"].isin(agentes)
    & (df["Date"] >= fecha_inicio)
    & (df["Date"] < fecha_fin)
].copy()

ordenes_totales = len(filtrado)
dias_activos = filtrado["Date"].dt.date.nunique()
agentes_activos = filtrado["Full name"].nunique()
promedio_diario = ordenes_totales / dias_activos if dias_activos else 0

columna_1, columna_2, columna_3, columna_4 = st.columns(4)
columna_1.metric("Órdenes VA02", f"{ordenes_totales:,}")
columna_2.metric("Agentes activos", agentes_activos)
columna_3.metric("Días activos", dias_activos)
columna_4.metric("Promedio por día", f"{promedio_diario:.1f}")

if filtrado.empty:
    st.info("No hay órdenes con los filtros seleccionados.")
    st.stop()

resumen_personas = (
    filtrado.groupby(["Changed by", "Full name"])
    .size()
    .reset_index(name="Total de ordenes")
    .sort_values("Total de ordenes", ascending=False)
)
resumen_personas["Porcentaje"] = (
    resumen_personas["Total de ordenes"]
    / resumen_personas["Total de ordenes"].sum()
    * 100
)

resumen_diario = (
    filtrado.groupby(["Date", "Changed by", "Full name"])
    .size()
    .reset_index(name="Ordenes del dia")
    .sort_values("Date")
)

resumen_mensual = (
    filtrado.groupby("Mes")
    .size()
    .reset_index(name="Total de ordenes")
)

st.subheader("Órdenes por agente")
st.dataframe(
    resumen_personas.style.format({"Porcentaje": "{:.2f}%"}),
    use_container_width=True,
    hide_index=True,
)

pestana_1, pestana_2, pestana_3 = st.tabs(
    ["Participación", "Comparación mensual", "Detalle diario"]
)

with pestana_1:
    st.pyplot(crear_grafico_participacion(resumen_personas))

with pestana_2:
    st.pyplot(crear_grafico_mensual(resumen_mensual))

with pestana_3:
    st.dataframe(resumen_diario, use_container_width=True, hide_index=True)
