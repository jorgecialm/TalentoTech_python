# declaracion de la funcion
# def calcular(n,n2):#la funcion puede o no recibir calores (parametros)
#     #  cuerpo del funcion
#       return #devolver un valor


def sumar(a, b):
    """
    Recibe dos numeros (a, b)
    Guarda el resultado de la suma en una variable 'resultado'
    devuelve el valor de 'resultado'
    """

    resultado = a + b
    return resultado


def restar(a, b):
    """
    Recibe dos numeros (a, b)
    Guarda el resultado de la resta en una variable 'resultado'
    devuelve el valor de 'resultado'
    """

    resultado = a - b
    return resultado


def multiplicar(a, b):
    """
    Recibe dos numeros (a, b)
    Guarda el resultado de la milti en una variable 'resultado'
    devuelve el valor de 'resultado'
    """

    resultado = a * b
    return resultado


def dividir(a, b):
    """
    Recibe dos numeros (a, b)
    Guarda el resultado de la división en una variable 'resultado'
    devuelve el valor de 'resultado'
    Valida que (b != 0) y retorna None

    """
    if b != 0:
        resultado = a / b
        return resultado

    return
    

print(sumar(1,2))
print(restar(1,2))
print(multiplicar(1,2))
print(dividir(1,2))