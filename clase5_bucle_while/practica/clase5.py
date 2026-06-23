"""
Necesitamos registrar los ingresos mensuales de una persona durante 6 meses.
Además, hay que validar que éstos sean números positivos.
Y,por supuesto, calcular el importe total de los ingresos acumulados durante los 6 meses.
"""
print("Bienvenido al sistema de registros mensuales ")
contador=0
ingresos=[]
while contador < 6:
    print(f"registra tu ingreso mensual del mes {contador + 1}")
    mes=input("ingresa el monto del mes :")
    if mes.isdigit():
        ingresos.append(int(mes))
        contador +=1
    else :
        print("error ingresalo de nuevo")
        
    
total= sum(ingresos)
print(f"La suma de los 6 meses de ingresos es {total}")