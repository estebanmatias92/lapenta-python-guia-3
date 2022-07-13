from helpers.stdio.stdio import *

print(
    "6. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,"
    + "\nMatemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por"
    + "\npantalla."
)
print("")

subjects = []

response = ""

# Loop while the user doesnt introduce N or n and keep asking for input to populate the list
while response != "n" and response != "N":
    # Get an string or terminate the program with a error message if the input is not the type required
    subject = string_input("Ingrese nombre de la materia: ")

    subjects.append(subject)
    response = input("Desea continuar: ")


print("")

print("Lista de materias: ")

# Show the result
for materia in subjects:
    print(materia)
