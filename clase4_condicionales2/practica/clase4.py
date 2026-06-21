"""Nuestro cliente nos pide que el programa ahora haga lo siguiente:
● Formatee correctamente los textos ingresados en “apellido”
y “nombre”, convirtiendo la primera letra de cada palabra a
mayúsculas y el resto en minúsculas.
● Asegurarse que el correo electrónico no tenga espacios y
contenga solo una “@”.
● Que clasifique a sus clientes por rango etario basándose en
su edad (“Niño/a” para los y las menores de 15 años,
“Adolescente” de 15 a 18 y “Adulto/a” para personas
mayores de 18 años.)
El programa debe mostrar el apellido, nombre y dirección de correo
con el formato pedido, y el texto correspondiente a su rango etario."""

print("Bienvenido")
nombre=input("Ingrese su nombre : ")
apellido = input("Ingrese su apellido : ")
nombre = nombre.title()
apellido = apellido.title()
correo = input("Ingrese su correo electronico : ")
edad = int(input("Ingrese su edad : "))
if edad < 15:
    rango = "Niño/a"
elif edad <= 18:
    rango = "Adolescente"
else:
    rango = "Adulto/a"


print(f"Nombre: {nombre} {apellido}")
print(f"Correo: {correo}")
print(f"Rango etario: {rango}")
if correo.count("@") == 0 or " " in correo:
    print("Correo electrónico inválido. Debe contener @ ,no tener espacios en blanco , ni estar vacio")   
elif correo.count("@") > 1:
    print("Correo invalido , solo debe contener un @")
else:
    print("Datos correctos")