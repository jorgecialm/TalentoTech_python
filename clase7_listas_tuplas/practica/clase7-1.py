""" 
# Desafío - Limpiar y mostrar una lista de nombres

Queremos registrar el nombre de las personas que se anotan a un taller.  Pero a veces escriben mal o dejan el campo vacío.

Tu desafío es:

1. Usar un bucle para **cargar nombres** (por ejemplo, 5)
2. Ignorar los vacíos o espacios en blanco
3. Guardar los nombres válidos usando `.append()`
4. Ordenar la lista alfabéticamente con `.sort()`
5. Mostrar solo los **primeros 3 nombres válidos**, usando slicing

🎯 Bonus: mostrar la cantidad total de nombres registrados correctamente.

(Intenta resolverlo antes de mirar la posible solución que aparece más abajo!)

"""
print("Lista de nombres : \n")
nombres=[]
cantidad=0

while cantidad < 5 :
    nombre=input("ingresa tu nombre : ")
    if nombre.strip():
        nombres.append(nombre)
        cantidad+=1
nombres.sort()
for nombre in nombres[:3]:
    print(f"\nNombre ingresado {nombre}")
print(f"La cantidad total de nombres ingresados es {len(nombres)}")
