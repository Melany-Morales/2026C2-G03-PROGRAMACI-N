# Guia de caso - Semana 08

## Ciclos con datos de pacientes desde JSON

**Archivo de trabajo:** `clase08_analisis_hospital.py`  
**Notebook de apoyo:** `NOTEBOOK 05 - Verificador Basico Semana 08.ipynb`  
**Fuente de datos:** `datos_clinica.json`  
**Solucion docente:** `analisis_hospital_solucion.py`  

El tema principal de la clase es **ciclos**:
leer una lista de pacientes desde JSON, recorrerla con `for` y acumular
indicadores simples.

El contexto hospitalario solo da sentido a los datos. La habilidad que se
practica es recorrer registros y tomar decisiones dentro del ciclo.

---

## 1. Que vamos a aprender

Al terminar, el estudiante debe poder:

- construir con el docente la lectura de un archivo JSON,
- reconocer que el JSON se convierte en una lista de diccionarios,
- acceder a datos con claves como `paciente["edad"]`,
- recorrer pacientes con `for`,
- usar `if` para contar casos,
- usar dos funciones basicas ya dadas,
- calcular un promedio,
- escribir conclusiones simples,
- resolver un reto opcional contando diagnosticos con `len()`.

---

## 2. Por que usamos JSON

JSON es importante porque permite trabajar con datos guardados fuera del codigo.
En lugar de escribir pacientes manualmente dentro del `.py`, el programa los lee
desde un archivo.

Esto se parece mas a escenarios reales:

- una clinica exporta datos,
- una plataforma envia informacion,
- una API responde datos,
- otro sistema guarda registros en un formato que Python puede leer.

En esta clase no estudiamos APIs todavia. JSON es el primer paso para entender
como Python recibe datos estructurados desde fuera del programa.

---

## 3. Conexion con Semana 07

En Semana 07 se recorria una lista de sedes. En Semana 08 se recorre una lista
de pacientes.

```python
for paciente in pacientes:
    edad = paciente["edad"]
    provincia = paciente["provincia"]
```

La idea es la misma: tomar un registro, extraer datos y acumular resultados.

La frase clave de la semana es:

> Cada vuelta del ciclo representa un paciente.

---

## 4. Que es JSON

JSON es un formato de texto para guardar datos. Se usa en sistemas, aplicaciones
y APIs.

Cuando Python lee `datos_clinica.json`, obtiene una lista. Cada elemento de esa
lista es un diccionario que representa un paciente.

Ejemplo de un paciente:

```python
{
    "nombre": "Ana Gómez",
    "edad": 34,
    "genero": "F",
    "provincia": "Heredia",
    "enfermedades": ["migraña", "gripe"],
}
```

---

## 5. El ciclo como centro de la clase

El programa usa un solo ciclo principal:

```python
for paciente in pacientes:
    nombre = paciente["nombre"]
    edad = paciente["edad"]
    provincia = paciente["provincia"]
    genero = paciente["genero"]
```

Dentro de ese ciclo se hacen tres acciones:

1. Extraer datos del paciente actual.
2. Preguntar condiciones con `if`.
3. Acumular resultados en variables.

Ejemplo:

```python
if provincia == "San Jose":
    conteo_san_jose += 1
```

Esa estructura se repite para los demas indicadores.

---

## 6. Antes de programar: `for` o `while`

Antes de completar el archivo `.py`, revise en el notebook la seccion inicial
**"Antes de verificar: `for` y `while`"**.

La decision importante de esta practica es:

| Situacion | Ciclo recomendado | Por que |
|---|---|---|
| Recorrer todos los pacientes del JSON | `for` | Ya tenemos una lista de pacientes. |
| Pedir una opcion hasta que sea valida | `while` | No sabemos cuantos intentos hara el usuario. |

En esta practica usamos principalmente `for`:

```python
for paciente in pacientes:
    # analizar paciente actual
```

No usamos `while` para recorrer pacientes porque ya tenemos la coleccion
completa. Usar `while` obligaria a manejar posiciones manualmente y aumentaria
la posibilidad de errores.

---

## 7. Indicadores de la practica

El programa debe calcular:

| Indicador | Como se resuelve |
|---|---|
| Cantidad de pacientes | `len(pacientes)` |
| Edad promedio | suma de edades / cantidad de pacientes |
| Pacientes de San Jose | `if provincia == "San Jose"` |
| Mujeres | `if genero == "F"` |
| Hombres | `if genero == "M"` |
| Adultos mayores | `if es_adulto_mayor(edad)` y `append(nombre)` |
| Reto opcional: diagnosticos | sumar `len(paciente["enfermedades"])` |

El archivo incluye dos funciones basicas ya implementadas:

```python
def calcular_promedio(suma, cantidad):
    return suma / cantidad


def es_adulto_mayor(edad):
    return edad >= 60
```

Estas funciones existen para que el estudiante vea funciones pequenas en uso,
sin convertir la practica en una arquitectura compleja.

---

## 8. Ruta de trabajo en el archivo `.py`

El archivo `clase08_analisis_hospital.py` esta organizado por requerimientos.
Trabaje en este orden:

| Requerimiento | Que debe hacer | Como lo verifica |
|---|---|---|
| 1 | Construir la lectura del JSON con el docente. | `Cantidad de pacientes: 15` |
| 2 | Explorar el primer paciente y sus llaves. | Se imprime el primer diccionario y sus campos. |
| 3.1 | Sumar edades dentro del ciclo. | Edad promedio `45.2` |
| 3.2 | Contar pacientes de San Jose. | Resultado `4` |
| 3.3 | Contar mujeres. | Resultado `8` |
| 3.4 | Contar hombres. | Resultado `7` |
| 3.5 | Guardar adultos mayores. | Lista con Elena Castro, Jorge Alfaro y Roberto Arias. |
| Reto opcional | Contar la cantidad total de diagnosticos registrados. | Resultado `23` |
| 4 | Calcular el promedio con `calcular_promedio()`. | El resumen muestra `45.2`. |
| 5 | Escribir dos conclusiones. | Las conclusiones se basan en los resultados. |

La mayor parte del analisis ocurre dentro de este bloque:

```python
for paciente in pacientes:
    nombre = paciente["nombre"]
    edad = paciente["edad"]
    provincia = paciente["provincia"]
    genero = paciente["genero"]
```

### Reto final opcional

Cada paciente tambien tiene una lista de enfermedades diagnosticadas:

```python
enfermedades = paciente["enfermedades"]
```

El reto es contar la cantidad total de diagnosticos registrados en todos los
pacientes. Para mantener el nivel basico, no se pide contar enfermedades unicas
ni calcular cuantas veces aparece cada enfermedad.

---

## 9. Como trabajar

1. Abra `clase08_analisis_hospital.py`.
2. Abra el notebook `NOTEBOOK 05 - Verificador Basico Semana 08.ipynb`.
3. Revise la seccion inicial sobre `for` y `while`.
4. Construya con el docente la lectura del JSON.
5. Ejecute el archivo hasta obtener `Cantidad de pacientes: 15`.
6. Complete los requerimientos de analisis uno por uno.
7. Despues de cada requerimiento, guarde el `.py`.
8. Vuelva al notebook, recargue el archivo y ejecute la prueba correspondiente.

No complete todo de una sola vez. Pruebe por partes.

---

## 10. Resultados esperados

Al final, el resumen debe mostrar:

```text
Cantidad de pacientes: 15
Edad promedio: 45.2
Pacientes de San Jose: 4
Mujeres: 8
Hombres: 7
Adultos mayores: ['Elena Castro', 'Jorge Alfaro', 'Roberto Arias']
Cantidad total de diagnosticos: 23
```

El primer paciente y sus campos tambien se imprimen para explorar el JSON.

---

## 11. Preguntas de cierre

1. Por que `pacientes` es una lista?
2. Por que cada paciente es un diccionario?
3. Para que usamos `paciente["edad"]`?
4. Que representa una vuelta del ciclo `for`?
5. Que variable usamos para sumar edades?
6. Que condicion usamos para encontrar pacientes de San Jose?
7. Por que JSON es util si los datos vienen de otro sistema?
8. Por que `paciente["enfermedades"]` es una lista?
9. Como ayuda `len()` a resolver el reto final?
10. Que conclusion puede escribir con los resultados?

---

## 12. Checklist

- [ ] El programa carga el JSON.
- [ ] El programa muestra 15 pacientes.
- [ ] Reviso en el notebook cuando usar `for` y cuando usar `while`.
- [ ] El estudiante puede explicar el primer paciente.
- [ ] Calcula la edad promedio.
- [ ] Cuenta pacientes de San Jose.
- [ ] Cuenta mujeres y hombres.
- [ ] Lista adultos mayores.
- [ ] Si hace el reto opcional, cuenta 23 diagnosticos en total.
- [ ] Escribe dos conclusiones simples.
