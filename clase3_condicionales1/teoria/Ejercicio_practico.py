"""¡Hola!

Necesito que desarrolles un pequeño programa en Python que haga exactamente lo siguiente:
Solicite al cliente su nombre, apellido, edad y correo electrónico.
Compruebe que el nombre, el apellido y el correo no estén en blanco, y que la edad sea mayor de 18 años.
Muestre los datos por la terminal, en el orden que se ingresaron. Si alguno de los datos ingresados no cumple los requisitos, sólo mostrar el texto “ERROR!”.
Saludos, Mariana"""

print("Bienvenidos")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

try:
    edad = int(input("Ingresa tu edad: "))
except ValueError:
    edad = None  # marcamos que falló, para no seguir validando con un valor inválido

email = input("Ingresa tu email: ")

if nombre.strip()=="":
    print("ERROR! el nombre no puede estar vacío")
elif apellido.strip() == "":
    print("ERROR! el apellido no puede estar vacío")
elif edad is None:
    print("ERROR! la edad ingresada no es un numero valido")
elif email.strip() == "":
    print("ERROR! el email no puede estar vacío")
elif edad < 18:
    print("Es menor de 18 no cumple con la condicion")

else:
    print(nombre)
    print(apellido)
    print(edad)
    print(email)


