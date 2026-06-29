"""
Tu tarea es volver a modificar el programa que escribiste la clase anterior, 
para que realice las mismas tareas, 
pero que su interacción mediante la terminal esté mejorada utilizando Colorama. 
También sería genial si agregas un dato a cada producto que contenga la fecha y hora de la compra, usando la librería datetime
"""

from datetime import datetime
from colorama import init, Fore, Back, Style

init(autoreset=True)


def agregar_producto(nombre, precio):
    return {
        "nombre": nombre,
        "precio": precio,
        "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def consultar_productos(productos):
    if not productos:
        print(Fore.YELLOW + "No hay productos registrados todavía.")
        return

    print(Style.BRIGHT + Fore.CYAN + "\nProductos registrados:\n")
    for producto in productos:
        print(
            Fore.WHITE
            + Back.BLUE
            + f" Producto: {producto['nombre']} | Precio: {producto['precio']} | Fecha y Hora: {producto['fecha_hora']} "
        )


def eliminar_productos(productos, nombre):
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            print(Fore.GREEN + f"Producto '{nombre}' eliminado correctamente.")
            return

    print(Fore.RED + f"No se encontró el producto '{nombre}'.")


if __name__ == "__main__":
    productos = []

    while True:
        print(Style.BRIGHT + Fore.MAGENTA + "\n==== REGISTRADORA DE PRODUCTOS ====\n")
        print(Fore.BLUE + "1- Agregar producto")
        print(Fore.BLUE + "2- Consultar productos")
        print(Fore.BLUE + "3- Eliminar producto")
        print(Fore.BLUE + "4- Salir\n")

        opcion = input(Fore.WHITE + "Elige una opción entre 1 y 4: ")

        if opcion == "4":
            print(Fore.GREEN + "Gracias por utilizar la registradora de productos.")
            break

        if opcion not in ("1", "2", "3"):
            print(Fore.RED + "Opción no válida. Por favor elige un número entre 1 y 4.")
            continue

        if opcion == "1":
            nombre = input("\nIngresa el nombre del producto: ")
            precio = input("Ingresa el precio del producto: ")
            producto = agregar_producto(nombre, precio)
            productos.append(producto)
            print(Fore.GREEN + f"Producto '{nombre}' agregado correctamente.")

        elif opcion == "2":
            consultar_productos(productos)

        elif opcion == "3":
            eliminar = input("Ingrese el nombre del producto que quiere eliminar: ")
            eliminar_productos(productos, eliminar)
        