# random
import random

# randint(a,b)
# print(random.randint(1, 10))

# ingreso = input("ingresa el nuemro que estoy pensando de 1 al 10: ")
# nummero_secreto = random.randint(1, 10)
# if ingreso == nummero_secreto:
#     print("Adivinaste")
# else:
#     print(f"No era ese, era {nummero_secreto}")

# randrange
nuemro_par = random.randrange(0, 101, 2)
# print(nuemrp_par)

# random
aleatorio = random.random()
# print(aleatorio)
# uniform
temperatura = random.uniform(15.5, 25.6)
print(f"Temperatura actual: {temperatura:.2f}")

# choice
categorias = ["ropa deportiva", "calzado deportivo", "remeras", "pantalones"]
categoria_seleccionada = random.choice(categorias)
print(f"La categoria seleccionada es: {categoria_seleccionada} ")


# shuffle(lista)
cartas = ["As", "Rey", "Reina", "Jota", "10"]
print(f"Cartas sin barajar: {cartas}")
random.shuffle(cartas)
print(f"Cartas barajas: {cartas}")

# seed sembrar
lista_nombres = ["luis", "pablo", "maria", "luca"]
lista_apellidos = ["lopez", "martinez", "juarez", "santos"]
# sacar de cada lista y combiar el nombre y apellido en una nueva

# sample
numeros_posibles = range(1, 37)
numeros_ganadores = random.sample(numeros_posibles, 6)

print(f"Los ganadores de esta semana son: {numeros_ganadores}")