import sqlite3
# inicio
def crear_conexion(database):
    conexion= sqlite3.connect(database)
    cursor = conexion.cursor()
    comado_crear_tabla="""
        CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        promedio REAL
        );
        """
    cursor.execute(comado_crear_tabla)
    conexion.commit()
    conexion.close()

crear_conexion('estudiantes.db')

def agregar_estudiente():
    nombre= input("Ingresa el nombre del estudiante: ")
    promedio= input("Ingresa el promedio del estudiante: ")
    # validamos la entradas
    promedio = float(promedio)

    conexion = sqlite3.connect('estudiantes.db')
    cursor = conexion.cursor()

    datos = (nombre, promedio)
    comado_insert="INSERT INTO estudiantes (nombre, promedio) VALUES (?,?)"
    cursor.execute(comado_insert, datos)
    conexion.commit()
    conexion.close()


agregar_estudiente()
agregar_estudiente()
# Create otra funcion que un select