from productos import agregar, mostrar, eliminar, ordenar
from datetime import datetime
from colorama import init, Fore, Back, Style

init(autoreset=True)

def mostrar_fecha_hora():
    fecha_hora_actual = datetime.now()
    print(Fore.YELLOW + f"Fecha y hora de la operación: {fecha_hora_actual.strftime('%Y-%m-%d %H:%M:%S')}")

def menu():
    productos = []
    while True:
        print(Style.BRIGHT + Fore.MAGENTA + "\n==== REGISTRADORA DE PRODUCTOS ====\n")
        print(Fore.BLUE + "1- Agregar producto")
        print(Fore.BLUE + "2- Consultar productos")
        print(Fore.BLUE + "3- Eliminar producto")
        print(Fore.BLUE + "4- Ordenar productos")
        print(Fore.BLUE + "5- Salir\n")

        opcion = input(Fore.WHITE + "Elige una opción entre 1 y 5: ")

        if opcion == "5":
            print(Fore.GREEN + "Gracias por utilizar la registradora de productos.")
            break

        if opcion not in ("1", "2", "3", "4"):
            print(Fore.RED + "Opción no válida. Por favor elige un número entre 1 y 5.")
            continue

        if opcion == "1":
            nombre = input("\nIngresa el nombre del producto: ")
            precio = input("Ingresa el precio del producto: ")
            producto = {"nombre": nombre, "precio": precio, "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            agregar(productos, producto)
            mostrar_fecha_hora()

        elif opcion == "2":
            mostrar(productos)
            mostrar_fecha_hora()

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto que quiere eliminar: ")
            eliminar(productos, nombre)
            mostrar_fecha_hora()

        elif opcion == "4":
            ordenar(productos)
            mostrar_fecha_hora()

if __name__ == "__main__":
    menu()
        
          