
"""Programa principal del proyecto modular BCCR."""

from lectura_datos import cargar_tabla_bccr, mostrar_top_10
from limpieza_datos import limpiar_datos, resumir_por_tipo_entidad
def ejecutar():
    """Cargar los datos y prsentar el menú del sistema"""
    datos_crudos = cargar_tabla_bccr()
    datos = limpiar_datos(datos_crudos)
    
    while True: 
        print("\nPROYECTO DE ÁNALISIS BCCR")
        print("1. Mostrar primeras 10 entidades limpias.")
        print("2. Promedio por tipo entidad.")
        print("3. Mostrar entidades financieras con diferencial mayor al promedio.")
        print("4. Mostrar lista entidades y exportar CSV.")
        print("5. Graficar")
        print("6. Salir")
        
        opcion = input("Seleccione un opción: ").strip()
        if opcion == "1":
            print(mostrar_top_10(datos))
            
        elif opcion == "2":
            promedios = resumir_por_tipo_entidad(datos)
            print(f"El promedio del diferencial es:", promedios[0])
            
            #Agrupa por TIPO, calcula el promedio de COMPRA, VENTA y DIFERENCIAL, redondea y ordena por DIFERENCIAL.
            columnas = ["COMPRA", "VENTA", "DIFERENCIAL"]
            print(datos.groupby("TIPO")[columnas].mean().round(2).sort_values("DIFERENCIAL", asending=False))
        
        elif opcion == "3":
            print("Entidades con diferencial mayor al promedio:")
            entidades_altas = filtrar_diferencial_alto(datos)
            print(mostrar_top_10(entidades_altas))
            
        elif opcion == "4":
            pass    
            
        elif opcion == "5":
            print("Graficando ...")
        elif opcion == "6":
            input("Análisis finalizado. Presione enter para salir ...")
            break
        else:
            print("Opción inválida. Escriba un número del 1 al 6.")
        input("\nPresione enter para continuar...\n")
if __name__ == "__main__":
    ejecutar()