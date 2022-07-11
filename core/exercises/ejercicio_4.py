from helpers.stdio.stdio import *

print(
    "4. Crea una tupla con números, pide un número por teclado e indica cuantas veces se"
    + "\nrepite."
)
print("")

lista = []

response = ""

# Loop while the user doesnt introduce N or n and keep asking for input to populate the list
while response != "n" and response != "N":
    # Get an integer or terminate the program with a error message if the input is not the type required
    num = int_input("Ingrese un numero a la tupla: ")

    lista.append(num)
    response = input("Desea continuar: ")

# Convert each value from the list from characters to integers
int_lista = map(int, lista)

# Transform the list to a tuple
tupla = tuple(int_lista)

print("")

# Get an integer or terminate the program with a error message if the input is not the type required
num = int_input("Ingrese numero a buscar en la tupla: ")

# Create empty list
occurrences = 0

# Walk through the tuple and copy in the list every occurrence for (num)
for value in tupla:
    if value == num:
        occurrences += 1

# Show the result
print(
    f"El valor {num} aparece en la tupla {occurrences} {'vez' if occurrences == 1 else 'veces'}"
)
