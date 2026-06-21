# Valores trhuty o falsy

# is_active = ""
# print(type(is_active))

# if is_active:# True
#      # codigo a ejecutar
#     print("El usuario esta en activo en plataforma")


nombre = input("Ingresa tu nombre:")

if nombre:
    print("Hola", nombre)
else:
    print("El campo nombre no puede esta vacio")


# OP logicos and or not (!=)

# es_verdad= True
# # print(type(es_verdad))
# print(es_verdad)
# print(not es_verdad)
# es_mentira = False
# # print(type(es_mentira))
# print(es_mentira)
# print(not es_mentira)

# es_mayor = 15 > 9
# print(es_mayor)
# print(not es_mayor)

# AND
# True and True = True || True and False = False | False and True = False

# print(5 < 5 and "hola" == "hola")

# OR
# True or True = True || True or False = True | False or True = True | False or False = False

# us_guardado= "dani"
# pass_guardado= "1234"
# usuario= input("ingresa tu usuario: ")
# password= input("ingresa tu password: ")

# credenciales_validas= us_guardado == usuario and pass_guardado == password

# if credenciales_validas:
#     print("bienvenido", usuario)
# else:
#     print("Credenciales invalidas")