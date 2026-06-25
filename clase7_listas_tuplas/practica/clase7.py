"""
Solicite los nombres de los y las clientes uno por uno y valide que cada nombre no esté vacío. 
Si se deja el campo vacío, mostrar un mensaje de advertencia y volver a pedir el nombre.
Guarde cada nombre válido en una lista, asegurándote de agregarlo con el método .append(). 

Permití que se finalice la carga de nombres escribiendo la palabra "fin". 

Una vez finalizada la carga, ordená alfabéticamente los nombres en la lista y mostrá la lista ordenada utilizando un bucle for.

"""

print("Bienvenido a la app de carga de cliente/a : \n")
nombres=[]
while True:
    nombre=input("Ingresa el nombre de la clienta o cliente : ")
    if nombre =="":
        print("Error no puede ingresar un nombre vacio")
    elif nombre=="fin":
        break
        
    else:
        nombres.append(nombre)
nombres.sort()
for nombre_ordenado in nombres:
    print(f"El nombre del cliente/a es : {nombre_ordenado}")

