# Proyecto Final - Análisis de Productividad del Equipo

## 📘 Descripción
Este proyecto analiza los datos de productividad del equipo entre enero y agosto de 2026, aplicando la metodología **IteraFlex**.  
El sistema permite identificar:
- Promedio de productividad por persona.
- Promedio mensual del equipo.
- Los 5 días con mayor productividad.

## ⚙️ Requisitos
- Python 3.14
- Librerías necesarias:
  - pandas
  - matplotlib
  - openpyxl (para leer archivos Excel)

Instalación rápida:
```bash
pip install pandas matplotlib openpyxl streamlit
```

## Dashboard

Inicia el dashboard desde la carpeta `Proyecto`:

```bash
streamlit run dashboard_productividad.py
```

El dashboard carga automáticamente el Excel predeterminado. Para actualizarlo
cada mes, selecciona el nuevo archivo `.xlsx` desde la barra lateral.
El archivo debe conservar las columnas `Date`, `Changed by`, `Full name` y
`Transaction`. Se consideran órdenes los registros cuya transacción sea `VA02`.