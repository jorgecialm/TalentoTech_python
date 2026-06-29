from datetime import datetime

def calcular_estadia(fecha_ingreso, fecha_salida):
    ingreso=datetime.strptime(fecha_ingreso, "%d/%m/%Y")
    salida=datetime.strptime(fecha_salida, "%d/%m/%Y")
    
    if salida <= ingreso:
        print("La fecha de salida no puede ser menor a la fecha de entrada")
        return None
    
    dias= (salida - ingreso).days
    return dias

entrada=input("Ingresa la fecha de entrada (DD/MM/AAAA)")
salida=input("Ingresa la fecha de salida (DD/MM/AAAA)")

print(calcular_estadia(entrada, salida))

# Refactorizar la funcion para que no devuelva mensajes y validar por fuera lohag falta