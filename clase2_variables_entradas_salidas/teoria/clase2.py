# Declaramos algunas variables y mostramos su contenido

nombre = "Mariana"
edad = 30
altura = 1.68
es_estudiante = True

# # print("Nombre:", nombre)
# # print("Edad:", edad)
# # print("Altura:", altura)
# # print("¿Es estudiante?:", es_estudiante)

# Usamos type() para identificar el tipo de cada variable

print("El tipo de 'nombre' es:", type(nombre))
print("El tipo de 'edad' es:", type(edad))
print("El tipo de 'altura' es:", type(altura))
print("El tipo de 'es_estudiante' es:", type(es_estudiante))

# Probamos qué tipo de dato devuelve input()

dato_ingresado = input("Ingresá algo (un número o una palabra): ")

print("Ingresaste:", dato_ingresado)
print("Python lo interpreta como:", type(dato_ingresado))

# variables reglas del no (#- Caracteres especiales, numeros)
edad = 43  # Asignamos un valor # int
# print(edad)
edad = 44  # reasignamos un nuevo valor
# print(edad)

edad = "juan"  # str - cadena
# print(edad)

altura = 168.509  # float (decimal)
# concatenacion (+),- (,)
# print("La altura es:",  altura, "cm")

# booleano True/False (Si, no - Prendido/Apagado, 0/1)
# esta_activo = True
# print("Ingreso a la plataforma? ", esta_activo)
# esta_activo = False
# print("Ingreso a la plataforma? ", esta_activo)

# CONOCER EL TIPO DE DATO
"""edad = 33
print(edad)
print(type(edad))
longitud = "145.6"
print(longitud)
print(type(longitud))
esta_activo = True
print(esta_activo)
print(type(esta_activo))
nombre = "Lucas"
print(nombre)
print(type(nombre))"""

# ENTRDA DE DATOS input()
# nombre = input("Ingresa tu nombre: ")
# print(nombre)

# Castear datos
# edad = int(input("Ingresa tu edad: "))
# print(edad)
# print(type(edad))
# edad = int(edad)
# print(edad)
# print(type(edad))


altura= input("Ingresa tu altura: ")
altura = float(altura)
print(altura)
print(type(altura))
altura = str(altura)
print("Tu altura es: " + altura)
print(type(altura))