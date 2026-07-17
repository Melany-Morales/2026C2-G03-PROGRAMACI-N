"""Prepara y carga el conjunto de datos usado en la Semana 09."""

import json
from pathlib import Path

from generar_clinica_s09 import generar_archivo


TOTAL_MUESTRA = 5_000
TOTAL_COMPLETO = 1_000_000
ARCHIVO_MUESTRA = "clinica_s09_muestra.json"
ARCHIVO_COMPLETO = "clinica_s09.json"


def cargar_datos(usar_millon=False, carpeta=None):
    """Genera cuando sea necesario y carga el volumen seleccionado."""
    carpeta = Path(carpeta) if carpeta is not None else Path(__file__).parent
    total = TOTAL_COMPLETO if usar_millon else TOTAL_MUESTRA
    nombre_archivo = ARCHIVO_COMPLETO if usar_millon else ARCHIVO_MUESTRA
    ruta = carpeta / nombre_archivo

    if not ruta.exists():
        generar_archivo(total=total, destino=ruta)

    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            registros = json.load(archivo)
    except FileNotFoundError as error:
        raise FileNotFoundError(
            "No encontramos el archivo de datos. Ejecutamos nuevamente la carga."
        ) from error
    except json.JSONDecodeError as error:
        raise ValueError(
            "El archivo de datos está incompleto. Lo eliminamos y repetimos la carga."
        ) from error
    except MemoryError as error:
        raise MemoryError(
            "No hay memoria suficiente. Cerramos otras aplicaciones y reiniciamos."
        ) from error

    if not isinstance(registros, list) or len(registros) != total:
        raise ValueError(
            "El archivo no contiene el volumen esperado. Lo generamos nuevamente."
        )

    return registros, ruta
