# Lista vacía
productos = []

# Agregamos algunos productos
productos.append("arroz")
productos.append("fideos")
productos.append("harina")
productos.append("leche")

print("Lista después de agregar:")
print(productos)

# Quitamos un producto
productos.remove("fideos")

print("\nLista después de quitar 'fideos':")
print(productos)

# Ordenamos alfabéticamente
productos.sort()

print("\nLista ordenada alfabéticamente:")
print(productos)


# Lista inicial de tareas
tareas = ["barrer", "lavar los platos", "hacer la cama"]

print("Lista original:")
print(tareas)

# Quitamos la segunda tarea (posición 1)
tareas.pop(1)

print("\nDespués de eliminar la tarea en posición 1:")
print(tareas)

# Insertamos una nueva tarea en primer lugar
tareas.insert(0, "sacar la basura")

print("\nDespués de insertar una tarea al principio:")
print(tareas)

# Extendemos la lista con otras tareas
tareas_extra = ["regar las plantas", "ordenar el escritorio"]
tareas.extend(tareas_extra)

print("\nDespués de extender con más tareas:")
print(tareas)

# Lista con invitados
invitados = ["Camila", "Juan", "Sofía", "Camila", "Damián"]

print("Lista de invitados:")
print(invitados)

# Buscamos la primera posición donde aparece "Camila"
posicion = invitados.index("Camila")
print(f"\nCamila aparece por primera vez en la posición {posicion}.")

# Contamos cuántas veces aparece "Camila"
cantidad = invitados.count("Camila")
print(f"Camila aparece {cantidad} veces en la lista.")

# Limpiamos la lista de invitados
invitados.clear()
print("\nDespués de usar .clear():")
print(invitados)

# Creamos una tupla con días de la semana
dias = ("lunes", "martes", "miércoles", "jueves", "viernes")

# Mostramos cada día
for dia in dias:
    print(f"Hoy es {dia}")


# Lista con notas de un estudiante
notas = [7, 8, 10, 6, 9, 5, 8]

print("Todas las notas:")
print(notas)

# Primeras tres notas
print("\nPrimeras tres:")
print(notas[:3])

# Últimas dos notas
print("\nÚltimas dos:")
print(notas[-2:])

# Notas del medio
print("\nNotas de la posición 2 a la 4:")
print(notas[2:5])
