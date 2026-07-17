# Guia de trabajo - Semana 09

## Mapeando datos y fijando valores

**Tema:** Dominando diccionarios y tuplas en Python

**Notebook:** `NOTEBOOK 06 - Conteo y Bucles Anidados.ipynb`

Trabajamos con registros clinicos sinteticos. Los nombres iniciales nos ayudan
a reconocer el conjunto, pero las edades, provincias, enfermedades, sintomas y
medicamentos fueron generados para esta practica. El archivo no contiene
correos electronicos ni informacion medica real.

Desarrollamos una sola cadena de analisis. Exploramos un paciente, expresamos
sus datos como pares, construimos un conteo pequeno, lo generalizamos y
avanzamos desde un resumen plano hasta un mapa provincial.

## Preparamos y cargamos los datos

Ejecutamos las celdas iniciales del notebook en orden. Conservamos esta
configuracion durante las primeras siete actividades:

```python
USAR_MILLON = False
```

Con este valor generamos y cargamos solamente la muestra de 5,000 registros.
No necesitamos cargar el millon mientras desarrollamos y revisamos nuestro
codigo.

Si reiniciamos el kernel, volvemos a ejecutar las celdas desde el inicio. Cada
actividad utiliza variables creadas anteriormente.

---

## Actividad 1 - Exploramos un registro

**Donde escribimos**

Completamos la celda de codigo ubicada inmediatamente debajo de la seccion
**Actividad 1 - Exploramos un registro**.

**Partimos de**

Partimos de `registros`, la muestra cargada en la preparacion.

**Construimos**

Seleccionamos `primer_paciente`. Mostramos el tipo del conjunto, el tipo del
registro, sus campos y los valores de enfermedad, provincia y sintomas.

**Lo usamos despues en**

Usamos el primer paciente en **Actividad 2 - Convertimos campos en pares y
tuplas** para trabajar con las asociaciones que contiene.

---

## Actividad 2 - Convertimos campos en pares y tuplas

**Donde escribimos**

Completamos la celda de codigo ubicada inmediatamente debajo de la seccion
**Actividad 2 - Convertimos campos en pares y tuplas**.

**Partimos de**

Partimos de `primer_paciente` y de los campos que observamos en la actividad
anterior.

**Construimos**

Creamos `datos_observados` con la enfermedad, la provincia y los sintomas del
paciente. Recorremos sus asociaciones mediante `.items()`, conservamos un par
significativo en `par_observado` y desempaquetamos sus componentes. Mostramos
cada asociacion obtenida con `.items()`, mostramos la tupla y mostramos por
separado los dos valores obtenidos al desempaquetarla. Conservamos la enfermedad
en `enfermedad_observada`.

**Lo usamos despues en**

Consultamos `enfermedad_observada` dentro del resultado de **Actividad 3 -
Construimos un conteo pequeno**.

---

## Actividad 3 - Construimos un conteo pequeño

**Donde escribimos**

Completamos la celda de codigo ubicada inmediatamente debajo de la seccion
**Actividad 3 - Construimos un conteo pequeño**.

**Partimos de**

Partimos de los primeros cinco registros, del campo `enfermedad` y de
`enfermedad_observada`, que conservamos en la actividad anterior.

Antes de contar, usamos `diccionario.get(clave, valor_predeterminado)` para
consultar una clave sin producir un error cuando todavía no existe. Si la clave
esta presente, obtenemos su valor actual; si no esta presente, obtenemos el
valor predeterminado. En nuestros conteos usamos `0` como punto de partida.

**Construimos**

Creamos manualmente `conteo_pequeno_enfermedades` con las enfermedades y sus
cantidades en `registros[:5]`. Mostramos el conteo y comprobamos que sus
cantidades representen los cinco registros. Consultamos si
`enfermedad_observada` aparece en este conteo.

**Lo usamos despues en**

Convertimos este conteo pequeno en una operacion reutilizable en **Actividad 4
- Generalizamos el conteo en una funcion**.

---

## Actividad 4 - Generalizamos el conteo en una función

**Donde escribimos**

Completamos la celda de codigo ubicada inmediatamente debajo de la seccion
**Actividad 4 - Generalizamos el conteo en una función**.

**Partimos de**

Partimos del conteo manual de cinco pacientes y del mismo tipo de diccionario
`categoria: cantidad`.

**Construimos**

Completamos `contar_por_campo(registros, campo)`. La aplicamos al campo
`enfermedad` de la muestra completa y la reutilizamos con los campos `provincia`
y `medicamento`. Construimos `conteo_enfermedades`, `conteo_provincias` y
`conteo_medicamentos`, consultamos una clave existente en cada resultado y
comprobamos sus totales sin escribir respuestas esperadas en la guia.

**Lo usamos despues en**

Reutilizamos el patron de actualizacion con `.get()` en **Actividad 5 - Contamos
síntomas con dos ciclos** para procesar un campo que contiene una lista.

---

## Actividad 5 - Contamos síntomas con dos ciclos

**Donde escribimos**

Completamos la celda de codigo ubicada inmediatamente debajo de la seccion
**Actividad 5 - Contamos síntomas con dos ciclos**.

**Partimos de**

Partimos de la lista de sintomas observada en el primer paciente y del patron
de conteo que generalizamos en la actividad anterior.

**Construimos**

Construimos `conteo_sintomas`, un diccionario plano que relaciona cada sintoma
con su cantidad de apariciones en la muestra. Recorremos los pacientes y las
listas internas, y comprobamos el total de ocurrencias representadas.

**Lo usamos despues en**

Usamos `conteo_sintomas` como referencia de contraste para el resultado de un
solo grupo en **Actividad 6 - Filtramos síntomas de una provincia**.

---

## Actividad 6 - Filtramos síntomas de una provincia

**Donde escribimos**

Completamos la celda de codigo ubicada inmediatamente debajo de la seccion
**Actividad 6 - Filtramos síntomas de una provincia**.

**Partimos de**

Partimos de las provincias contadas en la Actividad 4 y del conteo plano de
sintomas construido en la Actividad 5.

**Construimos**

Conservamos la provincia del primer paciente en `provincia_filtrada` y
construimos `conteo_sintomas_provincia`, un diccionario plano
`sintoma: cantidad`. Mostramos el grupo seleccionado y comprobamos que el
resumen contiene solamente sus registros.

**Lo usamos despues en**

En **7B - Extendemos el mapa a todos los registros**, comparamos
`conteo_sintomas_provincia` con la entrada de `sintomas_por_provincia`
correspondiente a `provincia_filtrada` y confirmamos que ambas contienen
exactamente las mismas claves y cantidades.

---

## Actividad 7 - Construimos y consultamos el mapa provincial

**Donde escribimos**

Completamos una celda de codigo debajo de cada uno de estos titulos:

- **7A - Iniciamos el mapa con un registro**;
- **7B - Extendemos el mapa a todos los registros**;
- **7C - Consultamos los dos niveles del mapa**.

Ejecutamos el punto de control preparado en cada celda antes de continuar.

**Partimos de**

Partimos de `primer_paciente`, de `provincia_filtrada`, de
`conteo_sintomas_provincia` y del patron aplicado a las listas de sintomas.

**Construimos**

1. **Mapa inicial:** iniciamos `sintomas_por_provincia` con el primer registro y
   observamos la forma obtenida en el primer punto de control.
2. **Mapa completo:** ampliamos la misma estructura con los registros restantes
   hasta representar todas las provincias de la muestra. Confirmamos los grupos
   y las ocurrencias en el segundo punto de control.
3. **Consulta provincial:** recorremos ambos niveles mediante `.items()`,
   construimos `totales_sintomas_por_provincia` y fijamos en
   `sintoma_mayor_provincia` el sintoma mayor de `provincia_filtrada` como una
   tupla. Confirmamos los resumenes en el tercer punto de control.

**Lo usamos despues en**

Reutilizamos el mapa, sus totales y sus tuplas en **Actividad 8 - Validamos con
el millón y concluimos**.

---

## Actividad 8 - Validamos con el millón y concluimos

**Donde escribimos**

Cambiamos `USAR_MILLON` en la celda de codigo ubicada inmediatamente debajo de
la seccion **Preparamos y cargamos los datos**. Completamos las conclusiones en
la celda de codigo ubicada inmediatamente debajo de la seccion
**Actividad 8 - Validamos con el millón y concluimos**.

**Partimos de**

Partimos de la cadena completa que ya funciona con la muestra de 5,000
registros.

**Construimos**

Cambiamos la configuracion a:

```python
USAR_MILLON = True
```

Volvemos a ejecutar desde la celda de configuracion hasta el final. Generamos o
cargamos el archivo de un millon de registros y repetimos la misma cadena de
analisis.

Redactamos exactamente tres conclusiones con nuestras palabras:

1. explicamos como el conteo manual de cinco registros se convirtio en una
   funcion reutilizable para la muestra y el millon;
2. explicamos como el filtro de una provincia se convirtio en un mapa con los
   conteos de todas las provincias;
3. explicamos como usamos las claves, los totales y la tupla maxima del mapa
   provincial para consultar el millon.

**Lo usamos despues en**

Usamos los puntos de control y las tres conclusiones como evidencia del
analisis realizado con el conjunto completo.

---

## Revisamos nuestro trabajo

| Senal observable | Pregunta de revision |
|---|---|
| `NameError: registros is not defined` | ¿Ejecutamos las celdas de preparacion y carga? |
| El conteo pequeno no suma cinco | ¿Representamos los primeros cinco registros? |
| Todos los conteos quedan en `1` | ¿Conservamos las apariciones anteriores? |
| El total de sintomas no coincide | ¿Incluimos todas las listas internas? |
| El filtro contiene otras provincias | ¿Aplicamos la provincia seleccionada? |
| Faltan grupos en el mapa | ¿Representamos todas las provincias de la muestra? |
| Un total provincial no coincide | ¿Recorrimos los dos niveles del mapa? |
| Una tupla no pertenece a su grupo | ¿Conservamos un sintoma y su cantidad asociada? |

No escribimos resultados exactos en la guia. Comparamos nuestros totales con
el conjunto seleccionado y atendemos cada punto de control del notebook.

## Memoria disponible

El millon de registros puede requerir cerca de 1.5 GB de memoria durante la
carga. Cerramos otras aplicaciones antes de cambiar `USAR_MILLON` a `True`.
Si aparece `MemoryError`, reiniciamos el kernel, volvemos a `False` y
conservamos el trabajo validado con 5,000 registros. Ejecutamos la validacion
del millon posteriormente en un equipo con memoria suficiente.
