"""Verificaciones reutilizables para las actividades de la Semana 09."""

from collections import Counter


def verificar_tupla(resultado, etiqueta):
    """Comprueba que un resultado se haya fijado en una tupla."""
    if not isinstance(resultado, tuple) or len(resultado) != 2:
        raise AssertionError(
            f"Revisamos {etiqueta}: debe ser una tupla de dos elementos."
        )
    print(f"Correcto: verificamos {etiqueta} como una tupla de dos elementos.")


def _contador_esperado(registros, campo, campo_lista=False):
    if campo_lista:
        return Counter(
            valor
            for registro in registros
            for valor in registro[campo]
        )
    return Counter(registro[campo] for registro in registros)


def verificar_contador(
    conteo, registros, campo, etiqueta, campo_lista=False
):
    """Comprueba estructura, tipos y cantidades exactas de un contador."""
    if not isinstance(conteo, dict):
        raise AssertionError(f"Revisamos {etiqueta}: debe ser un diccionario.")

    esperado = _contador_esperado(registros, campo, campo_lista)
    if set(conteo) != set(esperado):
        raise AssertionError(
            f"Revisamos {etiqueta}: faltan claves o aparecen claves inesperadas."
        )
    if any(type(cantidad) is not int or cantidad < 0 for cantidad in conteo.values()):
        raise AssertionError(
            f"Revisamos {etiqueta}: cada cantidad debe ser un entero no negativo."
        )
    if conteo != dict(esperado):
        raise AssertionError(
            f"Revisamos {etiqueta}: una o más cantidades no corresponden a los datos."
        )

    total = sum(esperado.values())
    if sum(conteo.values()) != total:
        raise AssertionError(
            f"Revisamos {etiqueta}: el total no corresponde a los datos."
        )
    print(f"Correcto: verificamos el conteo de {etiqueta}.")


def verificar_contador_filtrado(
    conteo, registros, campo_filtro, valor_filtro, campo_lista, etiqueta
):
    """Comprueba un contador de listas limitado a un grupo."""
    filtrados = [
        registro
        for registro in registros
        if registro[campo_filtro] == valor_filtro
    ]
    verificar_contador(
        conteo, filtrados, campo_lista, etiqueta, campo_lista=True
    )


def verificar_inicio_mapa(mapa, registro, campo_grupo, campo_lista, etiqueta):
    """Comprueba el mapa inicial construido a partir de un solo registro."""
    grupo = registro[campo_grupo]
    esperado = {grupo: Counter(registro[campo_lista])}
    if mapa != {clave: dict(conteo) for clave, conteo in esperado.items()}:
        raise AssertionError(
            f"Revisamos {etiqueta}: debe representar únicamente el primer registro."
        )
    print(f"Correcto: verificamos {etiqueta}.")


def verificar_mapa_anidado(
    mapa,
    registros,
    campo_grupo,
    campo_valor,
    etiqueta,
    campo_valor_lista=False,
):
    """Comprueba cada cantidad exacta de un mapa grupo-categoría."""
    if not isinstance(mapa, dict):
        raise AssertionError(f"Revisamos {etiqueta}: debe ser un diccionario.")

    if campo_valor_lista:
        esperado = Counter(
            (registro[campo_grupo], valor)
            for registro in registros
            for valor in registro[campo_valor]
        )
    else:
        esperado = Counter(
            (registro[campo_grupo], registro[campo_valor])
            for registro in registros
        )
    grupos_esperados = {grupo for grupo, _ in esperado}
    if set(mapa) != grupos_esperados:
        raise AssertionError(
            f"Revisamos {etiqueta}: faltan grupos o aparecen grupos inesperados."
        )
    if any(not isinstance(conteos, dict) for conteos in mapa.values()):
        raise AssertionError(
            f"Revisamos {etiqueta}: cada grupo debe contener otro diccionario."
        )

    obtenido = {}
    for grupo, conteos in mapa.items():
        for categoria, cantidad in conteos.items():
            if type(cantidad) is not int or cantidad < 0:
                raise AssertionError(
                    f"Revisamos {etiqueta}: cada cantidad debe ser un entero no negativo."
                )
            obtenido[(grupo, categoria)] = cantidad

    if set(obtenido) != set(esperado):
        raise AssertionError(
            f"Revisamos {etiqueta}: las combinaciones internas no corresponden a los datos."
        )
    if obtenido != dict(esperado):
        raise AssertionError(
            f"Revisamos {etiqueta}: una o más cantidades internas son incorrectas."
        )
    total_esperado = sum(esperado.values())
    if sum(obtenido.values()) != total_esperado:
        raise AssertionError(
            f"Revisamos {etiqueta}: el total no corresponde a los datos."
        )
    print(f"Correcto: verificamos el mapa de {etiqueta}.")


def verificar_maximo(resultado, conteo, etiqueta):
    """Comprueba que una tupla represente un máximo del contador."""
    if not conteo:
        raise AssertionError(f"Revisamos {etiqueta}: el conteo está vacío.")
    if not isinstance(resultado, tuple) or len(resultado) != 2:
        raise AssertionError(
            f"Revisamos {etiqueta}: debe ser una tupla de dos elementos."
        )
    clave, cantidad = resultado
    if (
        clave not in conteo
        or conteo[clave] != cantidad
        or cantidad != max(conteo.values())
    ):
        raise AssertionError(
            f"Revisamos {etiqueta}: la tupla no representa el máximo."
        )
    print(f"Correcto: verificamos {etiqueta}.")


def verificar_totales_por_grupo(totales, mapa, etiqueta):
    """Comprueba un resumen de totales sin revelar cantidades esperadas."""
    if not isinstance(totales, dict) or set(totales) != set(mapa):
        raise AssertionError(
            f"Revisamos {etiqueta}: debe incluir todos los grupos del mapa."
        )
    esperados = {
        grupo: sum(conteos.values())
        for grupo, conteos in mapa.items()
    }
    if totales != esperados:
        raise AssertionError(
            f"Revisamos {etiqueta}: uno o más totales no corresponden al mapa."
        )
    print(f"Correcto: verificamos {etiqueta}.")
