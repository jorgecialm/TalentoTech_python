# Creamos un diccionario con algunos datos
persona = {
    "nombre": "María",
    "edad": 30,
    "ciudad": "Rosario"
}

# Mostramos los valores accediendo por clave
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Ciudad:", persona["ciudad"])

# Agregamos una nueva clave:valor
persona["email"] = "maria@gmail.com"

print("\nDespués de agregar el email:")
print(persona)

# Diccionario con datos de una persona
persona = {
    "nombre": "María",
    "edad": 30,
    "ciudad": "Rosario"
}

# Usamos .get() para acceder de forma segura
print("Provincia:", persona.get("provincia"))  # No existe
print("Edad:", persona.get("edad"))

# Usamos .pop() para quitar una clave
ciudad_quitada = persona.pop("ciudad")
print("\nQuitamos la ciudad:", ciudad_quitada)

# Mostramos cómo quedó el diccionario
print("Diccionario actual:", persona)

# Diccionario con datos de una persona
persona = {
    "nombre": "María",
    "edad": 30,
    "email": "maria@gmail.com"
}

# Mostrar solo las claves
print("Claves:")
for clave in persona.keys():
    print(clave)

# Mostrar solo los valores
print("\nValores:")
for valor in persona.values():
    print(valor)

# Mostrar claves y valores juntos
print("\nClaves y valores:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Diccionario base
usuario = {
    "usuario": "techlab23",
    "nivel": "principiante"
}

# .setdefault(): solo agrega si la clave no existe
usuario.setdefault("email", "no_asignado@correo.com")
usuario.setdefault("nivel", "intermedio")  # No cambia nada

print("Después de setdefault:")
print(usuario)

# .update(): modifica o agrega valores
usuario.update({"nivel": "intermedio", "activo": True})

print("\nDespués de update:")
print(usuario)

# .copy(): hacemos una copia independiente
copia_usuario = usuario.copy()
copia_usuario["usuario"] = "admin123"

print("\nCopia modificada:")
print(copia_usuario)

print("\nOriginal sin cambios:")
print(usuario)


# Lista de personas (cada una es un diccionario)
personas = [
    {"nombre": "Camila", "edad": 28},
    {"nombre": "Damián", "edad": 35},
    {"nombre": "Sofía", "edad": 22}
]

# Recorremos la lista mostrando los datos
for persona in personas:
    print(f"{persona['nombre']} tiene {persona['edad']} años.")

# Diccionario vacío
productos = {}

# Cargamos 3 productos con su precio
for i in range(3):
    nombre = input(f"Ingresá el nombre del producto #{i + 1}: ").strip().lower()

    # Validación del precio
    while True:
        try:
            precio = float(input(f"Precio de '{nombre}': $"))
            if precio > 0:
                break
            else:
                print("El precio debe ser mayor a 0.")
        except:
            print("Ingresá un número válido.")

    productos[nombre] = precio  # Guardamos en el diccionario

# Mostramos los productos y precios
print("\nProductos cargados:")
for producto, precio in productos.items():
    print(f"{producto}: ${precio}")

# Calculamos el total
total = 0
for precio in productos.values():
    total += precio

print(f"\nTotal gastado: ${total}")

# Bonus: mostrar productos ordenados alfabéticamente
print("\nProductos en orden alfabético:")
for producto in sorted(productos.keys()):
    print(producto)
