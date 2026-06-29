"""
¡Hola! Tu tarea es crear un programa en Python con las siguientes características:
Agregar productos: Permite al usuario o usuaria agregar productos a una lista, con nombre y precio.
Consultar productos: Muestra todos los productos en la lista junto con sus precios. 
Eliminar productos: A partir de su nombre.
 Menú interactivo: Debe ofrecer un menú para que se pueda elegir qué acción realizar.
"""
def agregar_producto(nombre, precio):
    return {"nombre": nombre, "precio": precio}

def consultar_productos(productos):
    for producto in productos:
        print(f"\nProducto: {producto['nombre']} - Precio: {producto['precio']}\n")

def eliminar_productos(productos, nombre):
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)
            print(f"Producto {nombre} eliminado correctamente")
            break

if __name__ =="__main__":
    productos=[]
    while True:
        print("==== REGISTRADORA DE PRODUCTOS ====\n")
        print("1- Agregar producto")
        print("2- Consultar productos")
        print("3- Eliminar producto")
        print("4- Salir\n")

        opcion=input("Elige una opcion entre 1-4 : ")
        if opcion =="4":
            print("gracias por utilizar la registradoara de productos")
            break
        if opcion not in ("1","2","3"):
            print("opcion no valida. Por favor elige un numero entre 1 y 3")
            continue

        if opcion =="1":
            nombre=input("\nIngresa el nombre del producto : ")
            precio= input("ingresa el precio del producto : ")
            producto=agregar_producto(nombre, precio)
            productos.append(producto)
        if opcion == "2":
            consultar_productos(productos)
        if opcion == "3":
            eliminar = input("Ingrese el nombre del producto que quiere eliminar: ")
            eliminar_productos(productos, eliminar)
            
        