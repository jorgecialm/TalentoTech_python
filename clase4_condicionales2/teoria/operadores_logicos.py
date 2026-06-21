# AND, OR y NOT

# es_verdad= True
# print(es_verdad)
# print(not es_verdad)
# es_mentira = False
# print(es_mentira)
# print(not es_mentira)

es_mayor = 5 < 6
# AND => True and True = True 

# print(5 == 6 and "Hola"== "hola")


#or => True or True => True

# print(5 == 6 or "hola " == "hola")

ingreso_usuario= input('Ingresa tu usuario ')
ingreso_pass= input('Ingresa tu pass ')
ingreso_edad= int(input('Ingresa tu edad '))

usuario_guarado= "maria"
pass_guarado= "1234"
edad_usuario= 18
credenciales_validas = usuario_guarado == ingreso_usuario and pass_guarado == ingreso_pass
es_mayor = ingreso_edad  >= edad_usuario

if credenciales_validas  and es_mayor :
    print('Bienvenido/a')
else:
    print('Crendenciales invalidas')