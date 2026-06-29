import datetime
from colorama import Fore, Back, init
init()
print(Fore.GREEN + "Texto en verde")
print(Back.RED + "Fondo rojo" + Back.RESET)
print(Fore.BLUE + Back.YELLOW + "Texto azul en fondo amarillo")

print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour) 
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.date.today())
print(datetime.date.today().year)
print(datetime.date.today().month)
print(datetime.date.today().day)


from datetime import datetime

fecha_hora_actual = datetime.now()
print("Fecha y hora actual:", fecha_hora_actual)
print("Solo la fecha:", fecha_hora_actual.strftime("%Y-%m-%d"))
print("Solo la hora:", fecha_hora_actual.strftime("%H:%M:%S"))
print("Fecha legible:", fecha_hora_actual.strftime("%d de %B de %Y"))