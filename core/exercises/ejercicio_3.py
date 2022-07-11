print("3. Pide una cadena por teclado, mete los caracteres en una lista sin espacios")
print("")

phrase = input("Ingrese una frase: ")

print("")

trimmed_phrase = phrase.replace(" ", "")

print("Lista de caracteres: ", list(trimmed_phrase))
