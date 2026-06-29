def agregar(lista, producto):
    lista.append(producto)
    print(f"Producto '{producto['nombre']}' agregado correctamente.")

def eliminar(lista, producto):
    for p in lista:
        if p["nombre"].lower() == producto.lower():
            lista.remove(p)
            print(f"Producto '{producto}' eliminado correctamente.")
            return
    print(f"No se encontró el producto '{producto}'.")

def mostrar(lista):
    if not lista:
        print("No hay productos registrados.")
        return
    print("\nProductos registrados:")
    for producto in lista:
        print(f"Producto: {producto['nombre']} - Precio: {producto['precio']} - Fecha y Hora: {producto['fecha_hora']}")

def ordenar(lista):
    lista.sort(key=lambda x: x["nombre"])
    print("Productos ordenados alfabéticamente por nombre.")