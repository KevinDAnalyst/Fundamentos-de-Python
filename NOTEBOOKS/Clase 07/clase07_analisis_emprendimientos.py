"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

# variables constantes
# Funciones

def calcular_total(ventas):
    """Recibo una lista, la sumo y retorno el total
    
    Args:
        ventas (list): Lista con las ventas del emprendimiento
        
    Returns:
        float: Sumatoria total de ventas
    """
    return sum(ventas)


def calcular_promedio(lista):
    """Retorna el promedio de ventas de una lista

    Args:
        lista (list)
    """
    return sum(lista) / len(lista)

def calcular_porcentaje(total, meta, formato = False):
    porcentaje = total / meta * 100
    if formato:
        return f"{porcentaje:.2f}%"
    return porcentaje

def calcular_clasificacion(total, meta):
    porcentaje = calcular_porcentaje(total, meta)
    if porcentaje >= 100:  
        mensaje_sede = "Meta alcanzada"
    elif porcentaje >= 80:
        mensaje_sede = "Meta casi alcanzada, prestar atencion"
    else:
        mensaje_sede = "Meta no alcanzada, URGE ATENCION."
    return mensaje_sede

def reporte_sedes(reporte):
    for sede in reporte:
        print("Sede:", sede['Nombre de sede'])
        print("Provincia:", sede['Provincia'])
        print("Tipo:", sede['Tipo'])
        print("Total de Ventas:", sede['Total de Ventas'])
        print("Promedio de Ventas:", sede['Promedio de ventas'])
        print("Cumplimiento de meta (%):", sede['Cumplimiento de meta (%)'])
        print("Estado:", sede['Estado'])
        print("="*40, "\n")

#print("Cantidad de sedes:", len(sedes))
#print("Tipo de variable Sedes:", type(sedes))
#print("Tipo de variable Sedes:[0]", type(sedes[0]))
#print("Datos por sede:", sedes[0].keys())
#print("Datos por sede:", sedes[0])
#print("Datos por sede:", sedes[0]['nombre'])
#print("Primera sede:", sedes[0].values())

reporte = []
venta_mas_alta = 0
top_sedes = []
provincias = []


for sede in sedes:
    ventas = sede["ventas"]
    meta = sede['meta']
    total_sede = calcular_total(ventas)
    promedio_sede = calcular_promedio(ventas)
    porcentaje_sede = calcular_porcentaje(total_sede, meta, True)
    estado = calcular_clasificacion(total_sede, meta)

    
    #print(porcentaje_sede, total_sede)
    #print(estado)
    if venta_mas_alta <= total_sede:
        venta_mas_alta = total_sede
        top_sedes.append(sede['nombre'])
        
    provincias.append(sede['provincia'])
    
    reporte.append({
        "Nombre de sede": sede['nombre'],
        "Provincia": sede["provincia"],
        "Tipo": sede["tipo"],
        "Total de Ventas": total_sede,
        "Promedio de ventas": promedio_sede,
        "Cumplimiento de meta (%)": porcentaje_sede,
        "Estado": estado
    })
    
reporte_sedes(reporte)

print("\nRESUMEN FINAL") 
print("\nMejor sede:", top_sedes[-1])
print("\nProvincias analizadas")

for provincia in set(provincias):
    print(provincia)

        
        
# reporte con una funcion
# todas las provincias sin repetir
# sede con la venta mas alta