"""Practica opcional: diccionarios y tuplas con datos clinicos masivos.

Generamos primero los datos con ``python generar_clinica_s09.py``. Los nombres
reales solo identifican algunos registros: toda la informacion clinica es
sintetica y no describe a ninguna persona.

Completamos los TODO en orden. Probamos primero con ``muestra`` y usamos el
millon completo cuando llegamos a ``construir_indices``.
"""

import json
from pathlib import Path


ARCHIVO_DATOS = Path(__file__).with_name("clinica_s09.json")
TOTAL_ESPERADO = 1_000_000


def cargar_pacientes(ruta=ARCHIVO_DATOS, total_esperado=TOTAL_ESPERADO):
    """Carga y valida una lista de pacientes desde un archivo JSON."""
    try:
        with Path(ruta).open("r", encoding="utf-8") as archivo:
            pacientes = json.load(archivo)
    except FileNotFoundError as error:
        raise FileNotFoundError(
            "No se encontro clinica_s09.json. Ejecute generar_clinica_s09.py."
        ) from error
    except json.JSONDecodeError as error:
        raise ValueError(
            "El JSON esta incompleto. Genere nuevamente el archivo."
        ) from error
    except MemoryError as error:
        raise MemoryError(
            "No hay memoria suficiente. Cierre otras aplicaciones e intente "
            "de nuevo."
        ) from error

    if not isinstance(pacientes, list):
        raise TypeError("El JSON debe contener una lista de pacientes.")
    if total_esperado is not None and len(pacientes) != total_esperado:
        raise ValueError(
            f"Se esperaban {total_esperado:,} pacientes, pero se encontraron "
            f"{len(pacientes):,}."
        )

    return pacientes


# ACTIVIDAD 3 - Contamos cualquier campo
def contar_por_campo(registros, campo) -> dict:
    """Retorna un diccionario valor -> cantidad para el campo indicado."""
    conteo = {}

    # TODO 1 (guiado):
    # 1. Recorremos cada registro.
    # 2. Obtenemos el valor con registro[campo].
    # 3. Actualizamos conteo con .get(valor, 0) + 1.

    return conteo


# ACTIVIDAD 4 - Contamos listas internas
def contar_sintomas(registros) -> dict:
    """Cuenta las apariciones de sintomas mediante ciclos anidados."""
    conteo = {}

    # TODO 2 (pseudocodigo que convertimos a Python):
    # Recorremos cada paciente en registros:
    #     recorremos cada sintoma en la lista interna del paciente:
    #         aumentamos el conteo del sintoma

    return conteo


# ACTIVIDAD 5 - Mapeamos provincia -> enfermedad
def contar_enfermedades_por_provincia(registros) -> dict:
    """Retorna el mapa provincia -> enfermedad -> cantidad."""
    conteo_por_provincia = {}

    # TODO 3 (solo contrato): construimos el diccionario anidado.
    # Primero aseguramos que exista un diccionario para la provincia.

    return conteo_por_provincia


# ACTIVIDAD 6 - Integramos indices en un recorrido
def construir_indices(registros) -> tuple[dict, dict, dict]:
    """Construye tres indices en un unico ciclo externo sobre registros.

    Retornamos una tupla con:
    (conteo_enfermedades, conteo_sintomas, conteo_por_provincia).
    No llamamos las tres funciones anteriores: eso recorreria los datos varias
    veces. Usamos el unico ciclo anidado para recorrer los sintomas.
    """
    conteo_enfermedades = {}
    conteo_sintomas = {}
    conteo_por_provincia = {}

    # TODO 4 (sin plantilla): recorremos registros una sola vez y actualizamos
    # los tres diccionarios. Escribimos aqui el ciclo externo y el de sintomas.

    return conteo_enfermedades, conteo_sintomas, conteo_por_provincia


# ACTIVIDAD 8 - Fijamos maximos y masificamos consultas
def obtener_maximo(conteo) -> tuple[str, int]:
    """Retorna una tupla (categoria, cantidad) sin max, lambda ni Counter."""
    if not conteo:
        raise ValueError("No podemos obtener un máximo de un conteo vacío.")

    # TODO 5: recorremos conteo.items(), desempaquetamos cada tupla y
    # comparamos las cantidades. Retornamos una tupla (categoria, cantidad).

    pass


def obtener_maximos_por_grupo(
    mapa_anidado,
) -> dict[str, tuple[str, int]]:
    """Retorna grupo -> (categoria, cantidad) para un mapa anidado."""
    for grupo, conteo in mapa_anidado.items():
        if not conteo:
            raise ValueError(
                f"No podemos obtener el máximo del grupo {grupo!r}: "
                "está vacío."
            )

    # TODO 6: recorremos mapa_anidado.items(), reutilizamos obtener_maximo()
    # y retornamos el diccionario de tuplas maximas.

    pass


# ACTIVIDAD 9 - Resolvemos el reto individual
def construir_medicamentos_por_enfermedad(registros) -> dict:
    """Reto: retorna enfermedad -> medicamento -> cantidad."""
    medicamentos_por_enfermedad = {}

    # TODO 7 (reto individual, sin plantilla): construimos el mapa anidado.

    return medicamentos_por_enfermedad


def mostrar_verificacion(etiqueta, obtenido, esperado):
    """Muestra retroalimentacion breve sin revelar el algoritmo."""
    estado = "Correcto" if obtenido == esperado else "Revise su solucion"
    print(f"{estado}: {etiqueta} = {obtenido:,}")


def main():
    """Carga los datos y ejecuta la practica de ayuda decreciente."""
    try:
        pacientes = cargar_pacientes()
    except (FileNotFoundError, ValueError, TypeError, MemoryError) as error:
        print("No fue posible iniciar la practica:", error)
        return

    print("ADVERTENCIA: todos los datos clinicos son sinteticos.")
    print(f"Pacientes cargados: {len(pacientes):,}")
    print("Campos disponibles:", tuple(pacientes[0].keys()))

    # ACTIVIDAD 1 - Exploramos un registro
    # TODO: seleccionamos el primer paciente e inspeccionamos en 5-7 lineas
    # los tipos de la coleccion, del registro y de su lista de sintomas.

    # ACTIVIDAD 2 - Mapeamos y fijamos
    pacientes_por_turno = {"mañana": 18, "tarde": 25}
    # TODO: recorremos .items(), construimos la tupla mayor, la desempaquetamos
    # y comprobamos su inmutabilidad capturando TypeError.

    # ACTIVIDAD 3 - Contamos cualquier campo
    muestra = pacientes[:5_000]
    enfermedades_muestra = contar_por_campo(muestra, "enfermedad")

    # ACTIVIDAD 4 - Contamos listas internas
    sintomas_muestra = contar_sintomas(muestra)

    # ACTIVIDAD 5 - Mapeamos provincia -> enfermedad
    provincias_muestra = contar_enfermedades_por_provincia(muestra)

    print("\nPRACTICA CON 5,000 REGISTROS")
    mostrar_verificacion(
        "diagnosticos", sum(enfermedades_muestra.values()), len(muestra)
    )
    mostrar_verificacion(
        "sintomas", sum(sintomas_muestra.values()), len(muestra) * 3
    )
    mostrar_verificacion("provincias", len(provincias_muestra), 7)

    # ACTIVIDAD 6 - Integramos indices en un recorrido
    resumenes = construir_indices(pacientes)
    conteo_enfermedades, conteo_sintomas, conteo_por_provincia = resumenes

    # ACTIVIDAD 7 - Recorremos un diccionario anidado
    totales_por_provincia = {}
    # TODO: recorremos conteo_por_provincia.items() con dos ciclos for
    # explicitos, acumulamos cada total y lo guardamos por provincia.

    print("Totales calculados por provincia:", totales_por_provincia)

    # ACTIVIDAD 8 - Fijamos maximos y masificamos consultas
    enfermedad_mas_frecuente = obtener_maximo(conteo_enfermedades)
    maximos_por_provincia = obtener_maximos_por_grupo(conteo_por_provincia)

    print("\nINDICES DEL MILLON")
    mostrar_verificacion(
        "diagnosticos", sum(conteo_enfermedades.values()), len(pacientes)
    )
    mostrar_verificacion(
        "sintomas", sum(conteo_sintomas.values()), len(pacientes) * 3
    )
    mostrar_verificacion("provincias", len(conteo_por_provincia), 7)
    print("Enfermedad mas frecuente:", enfermedad_mas_frecuente)
    print("Maximos por provincia:", maximos_por_provincia)

    # ACTIVIDAD 9 - Resolvemos el reto individual
    medicamentos = construir_medicamentos_por_enfermedad(pacientes)
    medicamentos_principales = obtener_maximos_por_grupo(medicamentos)
    print("\nRETO INDIVIDUAL")
    print("Medicamento principal para diabetes:", end=" ")
    print(medicamentos_principales.get("diabetes", ("", 0)))

    # ACTIVIDAD 10 - Cerramos con el ticket de salida
    # TODO: redactamos cuatro respuestas breves con nuestras propias palabras.
    respuesta_diccionario = ""
    respuesta_tupla = ""
    respuesta_ciclo_anidado = ""
    respuesta_consulta_masiva = ""

    print("Elegimos un diccionario porque", respuesta_diccionario)
    print("Elegimos una tupla porque", respuesta_tupla)
    print("Usamos un ciclo anidado porque", respuesta_ciclo_anidado)
    print("Consultamos el indice masivo porque", respuesta_consulta_masiva)


if __name__ == "__main__":
    main()
