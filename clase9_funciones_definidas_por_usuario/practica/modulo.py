def suma(a, b):
    """
    recibe dos numeros y retorna la suma entre ellos
    """
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return
    return a / b

if __name__ == "__main__":
    while True:
        print("\n==============================")
        print("   CALCULADORA v1.0    ")
        print("==============================")
        print("1: Sumar")
        print("2: Restar")
        print("3: Multiplicar")
        print("4: Dividir")
        print("5: Salir")
        print("------------------------------")

        opcion = input("Elige una opción (1-5): ")
        if opcion == "5":
            print("¡Gracias por usar la calculadora! Adiós.")
            break
        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida. Por favor, elige un número del 1 al 5.")
            continue

        num1 = input("Ingresa el primer numero : ")
        num2 = input("Ingresa el segundo numero : ")

        num1 = float(num1)
        num2 = float(num2)

        resultado = None

        if opcion == "1":
            resultado = suma(num1, num2)
        elif opcion == "2":
            resultado = resta(num1, num2)
        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
        elif opcion == "4":
            resultado = division(num1, num2)
        print(f"\n--- Resultado de la operación : {resultado} ---")

    # __name__ = "__main__"
