# Inicializamos la variable nombre vacía
nombre = ""

# Mientras nombre siga vacío, repetimos
while nombre == "":
    nombre = input("Ingresá tu nombre: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío. Intentá de nuevo.")

print(f"¡Hola, {nombre}!")