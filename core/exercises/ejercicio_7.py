from helpers.stdio.stdio import *

print(
    "7. Escribir un programa que pregunte al usuario los números ganadores de la lotería"
    + "\nprimitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a"
    + "\nmayor."
)
print("")

count = 0

winners = []

while count < 6:
    num = int_input("Ingresar numero ganador de loteria: ")
    winners.append(num)
    count += 1

print("")

print(f"Numeros ganadores ordenados de menor a mayor: {sorted(winners)}")
print(f"Numeros ganadores ordenados de mayor a menor: {sorted(winners, reverse=True)}")
