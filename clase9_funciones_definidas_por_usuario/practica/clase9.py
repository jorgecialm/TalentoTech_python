"""
¡Hola! Tu tarea es crear un programa en Python con las siguientes características: 
Agregar productos: Permite agregar productos a una lista. Cada producto debe tener un nombre y un precio.
Consultar productos: Muestra todos los productos en la lista junto con sus precios.
Eliminar productos: Elimina un producto de la lista a partir de su nombre.
Menú interactivo: El programa debe ofrecer un menú para que se pueda elegir qué acción realizar. Debe incluirse una opción para salir del programa.
"""


if __name__ =="__main__":
    productos=[]
    producto={}
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
            producto={"nombre":nombre, "precio":precio}
            productos.append(producto)
        if opcion == "2":
            for producto in productos:
                print(f"\nProducto: {producto['nombre']} - Precio: {producto['precio']}\n")
        if opcion == "3":
            eliminar = input("Ingrese el nombre del producto que quiere eliminar: ")
            for producto in productos:
                if producto["nombre"] == eliminar:
                    productos.remove(producto)
                    print(f"Producto {eliminar} eliminado correctamente")
                    break
        