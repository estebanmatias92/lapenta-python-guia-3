from helpers.stdio.stdio import *

print(
    "8. Escribir un programa que almacene las asignaturas de un curso (por ejemplo,"
    + "\nMatemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la"
    + "\nnota que ha sacado en cada asignatura y elimine de la lista las asignaturas"
    + "\naprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el"
    + "\nusuario tiene que repetir."
)
print("")

subjects = {
    "Matematicas": 0,
    "Fisica": 0,
    "Quimica": 0,
    "Historia": 0,
    "Lengua": 0,
    "Dibujo": 0,
}

print("Lista de materias: ")
for name in subjects.keys():
    print(name)

print("")

# Asking for input dynamically
for name in subjects.keys():
    points = float_input(f"Ingrese el puntaje de {name}: ")

    # Validate input data, to be consistent, if not, throw an error and leave
    if points < 0 or points > 100:
        print("El puntaje ingresado es invalido.")
        exit()
    # If the data is correct, add them to the list
    subjects[name] = points


print("")

# Removing unapproved subjects from the dictionary
filtered_subjects = subjects.copy()
for name in subjects:
    if subjects[name] > 70:
        filtered_subjects.pop(name)

print("El alumno debe repetir las siguientes materias: ")
# Showing the filtered subjects
for name in filtered_subjects.keys():
    print(name)
