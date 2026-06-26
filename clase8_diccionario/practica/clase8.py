"""
Crear un diccionario llamado productos donde las claves sean los nombres de los productos 
y los valores sean sus precios. 
Permitir que se agreguen productos y sus precios hasta que se decida finalizar. 
Mostrar el contenido del diccionario después de cada operación.
"""

print("Carga de productos \n")
rta=""
productos={}
while rta !="no":
    nombre_producto=input("ingrese el producto :")
    valor_producto=input("ingrese el valor del producto : ")
    productos[nombre_producto] = valor_producto
    print(productos)    
    rta=input("desea continuar si/no ")
