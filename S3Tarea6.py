palabra = input("Escribe una palabra: ")
palabra_invertida = ""
for letra in palabra:
    palabra_invertida = letra + palabra_invertida
print(f"La palabra invertida es: {palabra_invertida}")
