"""Práctica opcional: diccionarios y tuplas con datos clínicos sintéticos."""

from datos_s09 import cargar_datos


USAR_MILLON = False


def main():
    """Carga el volumen elegido y presenta las ocho actividades."""
    registros, ruta_datos = cargar_datos(USAR_MILLON)

    print("ADVERTENCIA: todos los datos clínicos son sintéticos.")
    print("Archivo utilizado:", ruta_datos.name)
    print(f"Registros que analizamos: {len(registros):,}")

    # ACTIVIDAD 1 - Exploramos un registro
    # TODO 1: Seleccionamos el primer registro. Mostramos sus claves y
    # consultamos los campos enfermedad, provincia y síntomas. También
    # mostramos el tipo del conjunto, del registro y de la lista de síntomas.

    # ACTIVIDAD 2 - Convertimos campos en pares y tuplas
    datos_observados = {}
    par_observado = ()
    campo_observado = ""
    valor_observado = ""
    enfermedad_observada = ""

    # TODO 2: Guardamos en datos_observados los tres campos de la Actividad 1.
    # Recorremos sus asociaciones con .items(). Después guardamos enfermedad y
    # su valor en par_observado, lo desempaquetamos y conservamos el valor en
    # enfermedad_observada para consultarlo en la Actividad 3.

    # ACTIVIDAD 3 - Construimos un conteo pequeño
    conteo_pequeno_enfermedades = {}

    # TODO 3: Recorremos los primeros cinco registros y contamos manualmente
    # sus enfermedades con un diccionario y .get(). Mostramos el resultado y
    # consultamos la cantidad de enfermedad_observada.

    # ACTIVIDAD 4 - Generalizamos el conteo en una función
    def contar_por_campo(registros_recibidos, campo):
        """Retorna un diccionario que relaciona cada valor con su cantidad."""
        conteo = {}

        # TODO 4: Generalizamos el patrón de la Actividad 3. Recorremos los
        # registros recibidos y actualizamos el valor del campo con .get().

        return conteo

    # TODO 4: Usamos la función para construir conteo_enfermedades,
    # conteo_provincias y conteo_medicamentos. Consultamos en cada mapa una
    # categoría del primer paciente y comprobamos los totales.
    conteo_enfermedades = {}
    conteo_provincias = {}
    conteo_medicamentos = {}

    # ACTIVIDAD 5 - Contamos síntomas con dos ciclos
    conteo_sintomas = {}

    # TODO 5: Recorremos cada paciente y, dentro de ese ciclo, sus síntomas.
    # Adaptamos el patrón de la función y comprobamos el total obtenido.

    # ACTIVIDAD 6 - Filtramos síntomas de una provincia
    provincia_filtrada = ""
    conteo_sintomas_provincia = {}

    # TODO 6: Elegimos la provincia del primer paciente. Recorremos los
    # registros, filtramos esa provincia y contamos únicamente sus síntomas.
    # Comparamos cada cantidad filtrada con el conteo general de la Actividad 5.

    # ACTIVIDAD 7A - Iniciamos el mapa provincial
    sintomas_por_provincia = {}

    # TODO 7A: Iniciamos el mapa con el primer registro y mostramos ese primer
    # estado antes de continuar.

    # ACTIVIDAD 7B - Extendemos el mapa provincial

    # TODO 7B: Incorporamos registros[1:] al mismo mapa. Comparamos la entrada
    # de provincia_filtrada con conteo_sintomas_provincia de la Actividad 6.

    # ACTIVIDAD 7C - Consultamos el mapa provincial
    totales_sintomas_por_provincia = {}
    sintoma_mayor_provincia = ("", 0)

    # TODO 7C: Recorremos directamente ambos niveles con .items(), guardamos
    # cada total y fijamos en una tupla el síntoma más frecuente de
    # provincia_filtrada.

    # ACTIVIDAD 8 - Validamos con el millón y concluimos
    # TODO 8: Cuando la muestra funcione, cambiamos USAR_MILLON a True,
    # repetimos el análisis y escribimos tres conclusiones propias sobre el
    # volumen que realmente procesamos.
    conclusion_generalizacion = ""
    conclusion_mapa_provincial = ""
    conclusion_consulta_millon = ""

    print(conclusion_generalizacion)
    print(conclusion_mapa_provincial)
    print(conclusion_consulta_millon)


if __name__ == "__main__":
    main()
