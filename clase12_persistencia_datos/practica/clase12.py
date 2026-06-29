"""
1. Creá un programa que permita ingresar los datos de un cliente: nombre, apellido y correo electrónico. Usá try-except para manejar posibles errores durante la entrada de datos. Por ejemplo:
Si el archivo no puede abrirse para escritura.
Si los datos ingresados no son válidos (por ejemplo, si el correo no contiene una "@" o el nombre está vacío).
Por ejemplo: 
Si el archivo no puede abrirse para escritura. 
Si los datos ingresados no son válidos (por ejemplo, si el correo no contiene una "@" o el nombre está vacío).
2. Guardá los datos ingresados en un archivo de texto llamado clientes.txt, 
de forma que cada cliente quede registrado en una nueva línea. 
3. Una vez guardados los datos, mostrá un mensaje de confirmación al usuario y cerrá el archivo correctamente.

Ejemplo de salida exitosa

=== Registro de Cliente ===
Ingrese el nombre: Juan
Ingrese el apellido: Pérez
Ingrese el correo electrónico: juan@example.com

Cliente registrado exitosamente.

Ejemplo de manejo de error

=== Registro de Cliente ===
Ingrese el nombre: María
Ingrese el apellido: González
Ingrese el correo electrónico: maria@example.com

Error: No se pudo guardar el cliente.
Verifique los permisos del archivo.
"""
if __name__ == "__main__":
    print("=== Registro de Cliente ===")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    correo = input("Ingrese el correo electrónico: ")

    try:
        if not nombre or not apellido or "@" not in correo:
            raise ValueError("Datos ingresados no válidos.")

        with open("clientes.txt", "a") as archivo:
            archivo.write(f"{nombre} {apellido} {correo}\n")
        
        print("\nCliente registrado exitosamente.")
    except ValueError as ve:
        print(f"\nError: {ve}")
    except IOError:
        print("\nError: No se pudo guardar el cliente. Verifique los permisos del archivo.")   

 

    
    

