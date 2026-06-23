productos = ["manzanas", "piñas", "bananas", "uvas"]

for producto in productos:
    print("Producto disponible:", producto)

palabra = "Hola"
for letra in palabra:
    print("Letra:", letra)

productos = ["P001", "P002", "P003", "P004", "P005"]
producto_a_buscar = "P003"
for producto in productos:
    if producto == producto_a_buscar:
        print("Producto encontrado:", producto)
        break
    print("Buscando...")
print("Fin de la búsqueda.")

# programa para hacer tablas de multiplicar
print("\n -----Programa de tablas de multiplicar------ \n")
tabla=input("ingresa el numero de la tabla que quieras entre 1 y 10 : ")
if tabla.isdigit():
    tabla=int(tabla)
else :
     print("Error no es un numero, se cierra el programa ")
     exit()
for i in  range(1,11):
        print(f"{tabla} x {i} = {i * tabla}")