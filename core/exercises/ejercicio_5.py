from helpers.math.math import *
from helpers.stdio.stdio import *

print(
    "5. Crea una tupla con números e indica el número con mayor valor y el que menor"
    + "\ntenga."
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


# Convert each value from the list from characters to integers, then transform the list to a tuple
tupla = tuple(map(int, lista))

print("")

# Show the result
print(f"El valor minimo en la tupla {tupla} es {minimum(tupla)}")
print(f"El valor maximo en la tupla {tupla} es {maximum(tupla)}")
