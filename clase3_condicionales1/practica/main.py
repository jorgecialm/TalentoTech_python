# Datos de entrada
nombre = input("Ingresa tu nombre: ").strip().capitalize()
apellido = input("Ingresa tu apellido: ").strip().capitalize()
email = input("Ingresa tu email: ").strip().lower()
edad_input = input("Ingresa tu edad : ")

#Validaciones
email_valido = True

if email == "":
    email_valido = False

if email.count("@") != 1:
    email_valido = False

# Clasificacion
if edad_input.isdigit() and email_valido:
    edad = int(edad_input)

    if edad >= 0 and edad < 15:
        categoria = "Niño/a"
    elif edad <= 18:
        categoria = "Adolescente"
    elif edad > 18:
        categoria = "Adulto/a"
    else:
        categoria = "Edad invalida"

    # Resultados
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Email: {email}")
    print(f"Categoria: {categoria}")
else:
    print(edad_input.isdigit())
    print(email_valido)
    print(email.count("@"))
    print("Alguno de los datos ingresados es invalido")









