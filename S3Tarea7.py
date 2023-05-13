palabra = []
palabra = input("Escriba una palabra: ")
palabra_inver = ""
for letra in palabra:
    palabra_inver = letra + palabra_inver
if (palabra_inver == palabra):
    print("Es una palabra palíndromo")
else:
    print("No es una palabra palíndromo")