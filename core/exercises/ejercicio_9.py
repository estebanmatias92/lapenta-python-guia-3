import string

print(
    "9. Escribir un programa que almacene el abecedario en una lista, elimine de la lista las"
    + "\nletras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante."
)
print("")

alphabet = list(string.ascii_lowercase)
print(f"Alfabeto original: {alphabet}")

filtered_alphabet = [
    letter for i, letter in enumerate(alphabet) if i == 0 or (i + 1) % 3 != 0
]
print(f"Alfabeto filtrado: {filtered_alphabet}")
