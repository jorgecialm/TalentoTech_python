# talle= input('Ingresa un numero: 1 , 2 , 3 para conocer tu talle de remera ')

# if talle == "1":
#     print("Tu talle es S, los productos estan en la primera estanteria")
# elif talle =="2":
#     print("Tu talle es M, los productos estan en la segunda estanteria")
# elif talle =="3":
#     print("Tu talle es XL, los productos estan en la tercer estanteria")

# else:
#     print("Es talle no existe")

edad = int(input("Ingresa tu edad: "))

# if edad >= 18 and edad <= 69:
#     print('Es obligatorio votar')
# elif edad >= 16:
#     print("Podes votar si queres")
# else:
#     print("NO podes votar")

# mensaje = ""

if edad >= 18 and edad <= 69:
    mensaje = 'Es obligatorio votar'
elif edad >= 16:
    mensaje = "Podes votar si queres"
else:
    mensaje = "NO podes votar"

print(mensaje)