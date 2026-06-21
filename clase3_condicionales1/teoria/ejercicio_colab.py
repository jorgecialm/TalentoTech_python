# Solicitar datos del usuario
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad_texto = input("Edad: ")
correo = input("Correo electrónico: ")

# Verificamos que los campos no estén vacíos
# Y que la edad ingresada sea un número mayor a 18
if nombre != "" and apellido != "" and correo != "" and edad_texto.isdigit():
    edad = int(edad_texto)
    if edad > 18:
        print("\n--- Datos del cliente ---")
        print("Nombre:", nombre)
        print("Apellido:", apellido)
        print("Edad:", edad)
        print("Correo:", correo)
    else:
        print("ERROR! debe tener mas de 18 años")
else:
    print("ERROR! no puede haber datos en blanco ")
