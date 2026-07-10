"""Semana 08: analisis basico de pacientes desde JSON.

Complete los requerimientos indicados. El objetivo principal es practicar
ciclos: recorrer una lista de pacientes leida desde JSON y acumular indicadores
simples.
"""

import json

ARCHIVO_DATOS = "Clase_08\datos_clinica.json"


def calcular_promedio(suma, cantidad):
    """Retorna el promedio de una suma entre una cantidad."""
    return suma / cantidad


def es_adulto_mayor(edad):
    """Retorna True si la edad corresponde a una persona adulta mayor."""
    return edad >= 60

with open(ARCHIVO_DATOS, 'r') as archivo:
    pacientes =json.load(archivo)
    
    print()
    print("Tipo: ", type(pacientes))
    print("Tipo: ", type(pacientes[0]))


# 2. Exploracion inicial
print("Cantidad de pacientes:", len(pacientes))
print("Tipo: ", type(pacientes))


if len(pacientes) == 0:
    print("Primero construya con el docente la lectura del JSON.")
    print("Cuando cargue correctamente, debe mostrar 15 pacientes.")
else:
    # REQUERIMIENTO 2:
    # Explore el primer paciente y muestre sus llaves y valores.
    primer_paciente = pacientes[0]
    print("Datos del paciente: ", primer_paciente.keys())
    #print("Datos del paciente: ", primer_paciente.values()) #retorna el valor
    print("Datos del paciente: ", primer_paciente.items()) #retorna la llave y el valor
    print("Primer paciente: ", primer_paciente["nombre"])
    print("Enfermedades: ", primer_paciente["enfermedades"])

    # Variables acumuladoras del analisis.  suma_edades, conteo_san_jose, 
    # conteo_mujeres, conteo_hombres y adultos_mayores.
    suma_edades = 0

    # 4. Ciclo principal
    # Cada vuelta del ciclo representa un paciente del JSON.
    for paciente in pacientes:
        nombre = paciente["nombre"]
        edad = paciente["edad"]
        provincia = paciente["provincia"]
        genero = paciente["genero"]

        # REQUERIMIENTO 3:
        # Complete aqui los acumuladores dentro del ciclo.
suma_edades = 0
conteo_san_jose = 0
conteo_mujeres = 0
conteo_hombres = 0
adultos_mayores = []
total_enfermedades = 0

        # 3.1 Sume la edad del paciente en suma_edades
suma_edades += edad

        # 3.2 Si la provincia es "San Jose", aumente conteo_san_jose
if provincia == "San Jose":
    conteo_san_jose += 1
    
        # 3.3 Si genero es "F", aumente conteo_mujeres
if genero == "F":
    conteo_mujeres += 1
    
        # 3.4 Si genero es "M", aumente conteo_hombres
if genero == "M":
    conteo_hombres += 1
        # 3.5 Si es_adulto_mayor(edad) es True, agregue el nombre
        # a adultos_mayores
if es_adulto_mayor(edad):
    adultos_mayores.append(nombre)
    
        # RETO FINAL OPCIONAL:
        # Cada paciente tiene una lista en paciente["enfermedades"].
        # Guarde esa lista en una variable y sume su cantidad con len().

    # REQUERIMIENTO 4:
    # Calcule la edad_promedio usando calcular_promedio().
edad_promedio = 0

edad_promedio = calcular_promedio(suma_edades, len(pacientes))


    # Resultados
print("\nRESUMEN BASICO")
    #rint("Edad promedio:", round(edad_promedio, 1))
print("Pacientes de San Jose:", conteo_san_jose)
print("Mujeres:", conteo_mujeres)
print("Hombres:", conteo_hombres)
print("Adultos mayores:", adultos_mayores)

    # REQUERIMIENTO 5:
    # Escriba dos conclusiones basadas en los resultados.
print("\nCONCLUSIONES")
print("Conclusion 1: La edad promedio de los pacientes es de", round(edad_promedio, 1), "años.")
print("Conclusion 2: Hay", len(adultos_mayores), "pacientes adultos mayores registrados.")

print("Conclusion 1: La mayoría de los pacientes son de San Jose.")
print("Conclusion 2: Hay más mujeres que hombres en el registro.")