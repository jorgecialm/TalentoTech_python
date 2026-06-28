# scpoe y return

nombre= "juan"

def saludar():
    # global nombre
    nombre="dani"
    print(nombre)


saludar()

print(nombre)
contador=0 #global

def incrementar():
    global contador
    contador+=1

incrementar()
print(contador)
