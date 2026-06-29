"""
# Desafío - Registro de notas con validación

Vas a crear un programa que registre **notas escolares** ingresadas por el usuario,  
y las guarde en un archivo llamado `notas.txt`.

---

🔧 ¿Qué tiene que hacer el programa?

1. Pedir al usuario que ingrese una nota (número entre 1 y 10)
2. Validar que sea un número válido y dentro del rango
3. Guardar la nota en el archivo (una por línea)
4. Repetir el proceso hasta que el usuario escriba `salir`
5. Al final, mostrar todas las notas cargadas leyendo el archivo

📌 Usá `try-except` para evitar errores si se escribe texto u otro valor inválido  
📌 Usá `open()` con modo `'a'` para no borrar notas anteriores

"""

print("Bienvenido al registro de notas escolares.")
while True:
    nota = input("Ingrese una nota entre 1 y 10 (o escriba 'salir' para finalizar): ")
    if nota.lower() == 'salir':
        break
    try:
        nota_float = float(nota)
        if 1 <= nota_float <= 10:
            with open("notas.txt", "a") as archivo:
                archivo.write(f"{nota_float}\n")
            print("Nota registrada correctamente.")
        else:
            print("Error: La nota debe estar entre 1 y 10.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

print("\nNotas registradas:")
try:
    with open("notas.txt", "r") as archivo:
        notas = archivo.readlines()
        for nota in notas:
            print(nota.strip())
except FileNotFoundError:
    print("No se encontraron notas registradas.")
