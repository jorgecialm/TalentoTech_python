# clase_13,14
# sqlite3 SQL (SQL Server, Mysql, MariaDB, Postgres)
import sqlite3

# generar una conexion 
conexion= sqlite3.connect("midatabase.db")
print('Conexion a la db exitosa')

#  cursor
cursor= conexion.cursor()
# SQL
comado_crear_tabla="""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    promedio REAL
);
"""
# Crear la tabla en sqlite
cursor.execute(comado_crear_tabla)
print("Tabla creada o ya existe")

# insertar un dato
print("Ejecutando comando INSERT")

comando_insertar="INSERT INTO estudiantes (nombre, promedio) VALUES (?,?);"
# set de datos
datos_juan_manuel= ("Juan Manuel",8)
#  ejecuatr la consulta
cursor.execute(comando_insertar, datos_juan_manuel)
datos_veronica= ("Veronica",9.5)
cursor.execute(comando_insertar, datos_veronica)
datos_jorge= ("Jorge",7.5)
cursor.execute(comando_insertar, datos_jorge)

# confirmar
conexion.commit()
print("Estudiante creado exitosamente")

# hacer una consulta a la base de datos
comando_seleccionar= "SELECT * FROM estudiantes;"

#  ejecutar el comando
cursor.execute(comando_seleccionar)

estudiantes= cursor.fetchall()#lista de tuplas
# python
print(estudiantes)
for estudiante in estudiantes:
    print(estudiante[0], estudiante[1],estudiante[2])






