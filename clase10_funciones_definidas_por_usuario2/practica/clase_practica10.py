import random

#  generar personas aleatorias
def generar_personas(cantidad):

    nombres = ["Luis", "Pablo", "Maria", "Luca", "Ana", "Sofia", "Juan", "Pedro"]
    apellidos = [
        "Lopez",
        "Martinez",
        "Juarez",
        "Santos",
        "Perez",
        "Gomez",
        "Fernandez",
    ]
    
    cantidad_maxima = min(len(nombres), len(apellidos))#
    # min(a,b) sia a < b retunr a o si b < a retun b
    if cantidad > cantidad_maxima:
        print(f"La cantidad no puede exceder {cantidad_maxima} de personas")
        return []
    # que pasa si cambio sample por choice
    nombres_random = random.sample(nombres, cantidad)
    apellidos_random = random.sample(apellidos, cantidad)

    personas =[]

    for i in range(cantidad):
        nombre_completo= nombres_random[i] + " " + apellidos_random[i]
        personas.append(nombre_completo)
    
    # print(personas)
    # devuelvo personas
    return personas



personas_generadas = generar_personas(5)
print(personas_generadas[4])
print(personas_generadas[0])
# print(personas_generadas)


# for persona in personas_generadas:
#     print(persona)