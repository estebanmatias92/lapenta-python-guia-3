from helpers.stdio.stdio import *

print(
    "2. Pide un número por teclado y guarda en una lista su tabla de multiplicar hasta el 10."
    + "\nPor ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50"
)
print("")

# Get an integer or terminate the program with a error message if the input is not the type required
num = int_input("Ingrese un numero para generar una tabla de multiplicar: ")

print("")

table = []

for elem in range(1, 11):
    table.append(elem * num)

for i, value in enumerate(table):
    print(f"{i+1} x {num} = {value}")
