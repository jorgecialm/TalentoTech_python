# condicionales if
# indentacion
"""if condicion:
# bloque de codigo
"""

# hace_frio = False
# if hace_frio:
#     print("Esta fresco")
#     print("hola desde hace_frio")
# print("hola")

# print("Bienvenidos a casino")

# es_mayor = int(input("Ingresa tu edad: "))
# # Estructura de control
# if es_mayor >= 18:
#     print("Podes entrar a Casino")
#     print("Gracias por venir")
# else:
#     print("NO Podes entrar a Casino")
#     print("Gracias por venir")

#print("Gracias por venir")

# palabra_secreta = "nino"

# ingreso = input("Adivina la palabra secreta:")

# if ingreso == palabra_secreta:
#      print("Adivinaste!")
# else:
#      print("no era esa, segui intentado...")


user_guardado = "juan"
pass_guardado = "1234"
ingreso_usuario = input("Ingresa tu usuario:")
#Inicio de sesion

if user_guardado == ingreso_usuario:

     ingreso_pass = input("Ingresa tu contraseña:")
     # if anidado
     if pass_guardado == ingreso_pass:
         print("Bienvenido usuario")
     else:
         print("Credendcial invalida")
else:
     print("Usuario no valido")