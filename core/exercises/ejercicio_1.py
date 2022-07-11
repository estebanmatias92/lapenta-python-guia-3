from helpers.stdio.stdio import *

print(
    "1. Crea una tupla con los meses del año, pide números al usuario, si el número esta"
    + "\nentre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino"
    + "\nmuestra un mensaje de error. El programa termina cuando el usuario introduce un"
    + "\ncero."
)
print("")


months = (
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
)


while True:
    # Get an integer or terminate the program with a error message if the input is not the type required
    month = int_input("Ingrese el numero del mes a mostrar: ")

    if month == 0:
        break

    i = month - 1

    if (month < 1) or (month > 12):
        print("El numero del mes es incorrecto")

    print(f"El mes {month} es: {months[i]}")
