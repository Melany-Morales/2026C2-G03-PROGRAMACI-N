"""Genera un millon de pacientes sinteticos para Semana 09.

Uso:
    python3 generar_clinica_s09.py

El archivo generado se llama `clinica_s09.json` y queda en esta misma carpeta.
La semilla fija permite repetir los mismos datos en cualquier ejecucion.
"""

import argparse
import json
import random
import tempfile
from pathlib import Path


TOTAL_PACIENTES = 1_000_000
ARCHIVO_SALIDA = "clinica_s09.json"

# Los nombres se asignan a posiciones cuyo genero sintetico ya coincide. De
# este modo no se altera la secuencia aleatoria usada por las verificaciones.
ESTUDIANTES_CURSO = {
    1: "Germán Antonio Cerdas Valle",
    2: "Bryan Cruz Flores",
    6: "José Pablo Delgado Martínez",
    8: "Eduardo Jesús Jiménez Hernández",
    9: "Diego Leitón Porras",
    11: "Álvaro Andrés Morales Jiménez",
    12: "Anthony Lorenzo Navarro Aguilar",
    14: "Francisco José Ochoa Medina",
    15: "Orlando Antonio Quirós Díaz",
    3: "Ana Beatriz Ramos Arguedas",
    4: "Angie Pamela Salazar Valverde",
    5: "María Vanessa Torres Jara",
}

ENFERMEDADES = [
    "gripe",
    "migraña",
    "estrés",
    "conjuntivitis",
    "alergia",
    "diabetes",
    "anemia",
    "artritis",
    "gastritis",
    "dermatitis",
    "bronquitis",
    "hipertensión",
    "colitis",
    "lumbalgia",
    "asma",
    "sinusitis",
    "otitis",
    "faringitis",
    "cistitis",
    "varicela",
    "psoriasis",
    "fibromialgia",
    "tiroiditis",
    "epilepsia",
    "arritmia",
    "obesidad",
    "hipotiroidismo",
    "hipertiroidismo",
    "osteoporosis",
    "gota",
    "úlcera péptica",
    "hepatitis",
    "insuficiencia renal",
    "parkinson",
    "alzheimer",
    "depresión mayor",
    "trastorno bipolar",
    "ansiedad generalizada",
    "lupus",
    "esclerosis múltiple",
]

MEDICAMENTOS = [
    "paracetamol",
    "ibuprofeno",
    "amoxicilina",
    "omeprazol",
    "metformina",
    "losartán",
    "atorvastatina",
    "levotiroxina",
    "amlodipino",
    "metoprolol",
    "enalapril",
    "fluoxetina",
    "alprazolam",
    "diazepam",
    "cetirizina",
    "loratadina",
    "azitromicina",
    "ciprofloxacino",
    "doxiciclina",
    "naproxeno",
    "tramadol",
    "prednisona",
    "salbutamol",
    "montelukast",
    "ranitidina",
    "pantoprazol",
    "simvastatina",
    "espironolactona",
    "furosemida",
    "warfarina",
    "insulina",
    "metronidazol",
    "clotrimazol",
    "aciclovir",
    "vitamina D",
]

SINTOMAS = [
    "fiebre",
    "dolor de cabeza",
    "tos",
    "fatiga",
    "náuseas",
    "vómitos",
    "diarrea",
    "dolor abdominal",
    "mareos",
    "dificultad para respirar",
    "dolor de pecho",
    "dolor muscular",
    "dolor articular",
    "inflamación",
    "picazón",
    "erupciones",
    "ojos rojos",
    "secreción nasal",
    "estornudos",
    "dolor de garganta",
    "dificultad para tragar",
    "pérdida de apetito",
    "pérdida de peso",
    "aumento de peso",
    "sed excesiva",
    "micción frecuente",
    "visión borrosa",
    "hormigueo",
    "entumecimiento",
    "debilidad muscular",
    "calambres",
    "insomnio",
    "ansiedad",
    "depresión",
    "irritabilidad",
    "confusión",
    "pérdida de memoria",
    "palpitaciones",
    "sudoración nocturna",
    "escalofríos",
    "ictericia",
    "heces oscuras",
    "sangrado",
    "moretones",
    "caída de cabello",
    "uñas frágiles",
    "boca seca",
    "mal aliento",
    "dolor lumbar",
    "rigidez matutina",
    "sensibilidad a la luz",
    "sensibilidad al sonido",
    "zumbido en oídos",
    "pérdida de equilibrio",
    "desmayos",
    "convulsiones",
    "tos con sangre",
    "esputo amarillo",
    "heridas que no sanan",
    "piel seca",
    "piel grasosa",
    "acné",
    "manchas en la piel",
    "dolor al orinar",
]

PROVINCIAS_CANTONES = {
    "San José": [
        "San José",
        "Escazú",
        "Desamparados",
        "Mora",
        "Goicoechea",
        "Santa Ana",
    ],
    "Alajuela": ["Alajuela", "San Ramón", "Grecia", "Atenas", "Naranjo"],
    "Cartago": ["Cartago", "El Guarco", "La Unión", "Oreamuno"],
    "Heredia": ["Heredia", "Barva", "Santo Domingo", "Santa Bárbara"],
    "Guanacaste": ["Liberia", "Nicoya", "Santa Cruz", "Bagaces"],
    "Puntarenas": ["Puntarenas", "Esparza", "Buenos Aires", "Quepos"],
    "Limón": ["Limón", "Pococí", "Siquirres", "Talamanca"],
}

NOMBRES_M = [
    "Juan", "Carlos", "Luis", "José", "Andrés", "Miguel", "Diego",
    "Marcos", "Pablo", "Roberto", "David", "Jorge", "Fernando",
    "Alberto", "Sergio", "Manuel", "Ricardo", "Alejandro", "Cristian",
    "Héctor", "Rafael", "Sebastián", "Gabriel", "Emilio", "Ernesto",
    "Tomás", "Iván", "Óscar", "Rodrigo", "Víctor", "Esteban",
    "Mauricio", "Gerardo", "Arturo", "Raúl",
]
NOMBRES_F = [
    "María", "Ana", "Laura", "Sofía", "Carmen", "Elena", "Diana",
    "Gabriela", "Paola", "Valeria", "Andrea", "Claudia", "Patricia",
    "Mónica", "Rosa", "Silvia", "Isabel", "Jimena", "Natalia",
    "Fernanda", "Lucía", "Carolina", "Daniela", "Mariana", "Adriana",
    "Alicia", "Beatriz", "Rocío", "Verónica", "Liliana", "Alejandra",
    "Stephanie", "Vanessa", "Rebeca", "Yolanda",
]
APELLIDOS = [
    "González", "Rodríguez", "López", "Martínez", "García", "Pérez",
    "Sánchez", "Ramírez", "Torres", "Vargas", "Castro", "Jiménez",
    "Vega", "Morales", "Herrera", "Núñez", "Ortiz", "Romero",
    "Flores", "Cruz", "Méndez", "Ríos", "Gutiérrez", "Chaves",
    "Mora", "Brenes", "Solano", "Monge", "Araya", "Quesada",
    "Salas", "Campos", "Fernández", "Rojas", "Alfaro", "Madrigal",
    "Segura", "Vásquez", "Picado", "Aguilar",
]


def crear_paciente(numero):
    """Crea un paciente sintetico con estructura de diccionario."""
    genero = random.choice(["M", "F"])
    nombres = NOMBRES_M if genero == "M" else NOMBRES_F
    nombre = (
        f"{random.choice(nombres)} {random.choice(APELLIDOS)} "
        f"{random.choice(APELLIDOS)}"
    )
    provincia = random.choice(list(PROVINCIAS_CANTONES))

    paciente = {
        "carnet": 115_000_000 + numero,
        "nombre": nombre,
        "edad": random.randint(5, 90),
        "genero": genero,
        "provincia": provincia,
        "canton": random.choice(PROVINCIAS_CANTONES[provincia]),
        "visitas": random.randint(1, 30),
        "enfermedad": random.choice(ENFERMEDADES),
        "medicamento": random.choice(MEDICAMENTOS),
        "activo": random.random() > 0.20,
        "sintomas": random.sample(SINTOMAS, 3),
    }

    nombre_estudiante = ESTUDIANTES_CURSO.get(numero)
    if nombre_estudiante is not None:
        paciente["nombre"] = nombre_estudiante

    return paciente


def generar_archivo(
    total=TOTAL_PACIENTES, destino=None, mostrar_progreso=True
) -> Path:
    """Genera un JSON reproducible y lo publica solo cuando esta completo."""
    if total < 1:
        raise ValueError("El total de pacientes debe ser mayor que cero.")
    if destino is None and total != TOTAL_PACIENTES:
        raise ValueError(
            "Debe indicar un destino cuando el total sea distinto de "
            f"{TOTAL_PACIENTES:,}."
        )

    random.seed(42)
    if destino is None:
        destino = Path(__file__).with_name(ARCHIVO_SALIDA)
    else:
        destino = Path(destino)

    destino_temporal = None
    intervalo_progreso = min(100_000, max(1, (total + 9) // 10))

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=destino.parent,
            prefix=f".{destino.name}.",
            suffix=".tmp",
            delete=False,
        ) as archivo:
            destino_temporal = Path(archivo.name)
            archivo.write("[\n")
            for numero in range(1, total + 1):
                paciente = crear_paciente(numero)
                json.dump(paciente, archivo, ensure_ascii=False)

                if numero < total:
                    archivo.write(",\n")
                else:
                    archivo.write("\n")

                debe_mostrar = (
                    mostrar_progreso
                    and (numero % intervalo_progreso == 0 or numero == total)
                )
                if debe_mostrar:
                    porcentaje = numero / total * 100
                    print(
                        f"Progreso: {numero:,} de {total:,} "
                        f"pacientes ({porcentaje:.0f}%)"
                    )

            archivo.write("]\n")

        destino_temporal.replace(destino)
    except BaseException:
        if destino_temporal is not None:
            destino_temporal.unlink(missing_ok=True)
        raise

    return destino


def main():
    """Punto de entrada del generador."""
    parser = argparse.ArgumentParser(
        description="Genera clinica_s09.json con 1,000,000 pacientes sinteticos."
    )
    parser.add_argument(
        "--total",
        type=int,
        default=TOTAL_PACIENTES,
        help="Cantidad de pacientes por generar (por defecto: 1,000,000).",
    )
    parser.add_argument(
        "--destino",
        type=Path,
        default=None,
        help="Ruta opcional del archivo JSON de salida.",
    )
    parser.add_argument(
        "--sin-progreso",
        action="store_true",
        help="Oculta los mensajes de avance.",
    )
    argumentos = parser.parse_args()

    if argumentos.total < 1:
        parser.error("--total debe ser mayor que cero")
    if argumentos.total != TOTAL_PACIENTES and argumentos.destino is None:
        parser.error(
            "--destino es obligatorio cuando --total es distinto de "
            f"{TOTAL_PACIENTES}"
        )

    destino = generar_archivo(
        total=argumentos.total,
        destino=argumentos.destino,
        mostrar_progreso=not argumentos.sin_progreso,
    )
    print(f"Pacientes generados: {argumentos.total:,}")
    print(f"Archivo generado: {destino}")
    print(f"Enfermedades distintas: {len(ENFERMEDADES)}")
    print(f"Medicamentos distintos: {len(MEDICAMENTOS)}")
    print(f"Sintomas disponibles: {len(SINTOMAS)}")


if __name__ == "__main__":
    main()
