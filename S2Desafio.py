texto = input("Escriba un texto o frase: ")
letra1 = input("Ingrese una letra a eleccion: ")
letra2 = input("Ingrese otra letra a eleccion: ")
letra3 = input("Ingrese una ultima letra a eleccion: ")
texto = texto.lower()
letras = [letra1.lower(), letra2.lower(), letra3.lower()]
for letra in letras: 
    print(f"La letra {letra} aparece {texto.count(letra)} veces en todo el texto")
palabras = texto.replace(".", " ") 
palabras = palabras.replace(":", " ")
palabras = palabras.replace(";", " ")
espacio = palabras.split(" ")
print(f"Las Palabras sin caracteres de puntuacion: {palabras}")
canti_palanras = len(palabras)
print(f"La cantidad de palabras en el texto es: {canti_palanras} ")
print(f"La primera letra es: {palabras[0]}, La ultima letra es: {palabras[-1]}")
texto_inver = palabras[::-1]
print(f"Las palabras en forma inverso: {texto_inver} ")
palabras_inver = espacio[::-1]
print(f"Las palabras en forma inversa: {palabras_inver}")
texto_palabras_reversa = " ".join(palabras_inver)
print(f"Palabras en forma inversa como string: {texto_palabras_reversa}")
if ("python" in texto):
    print("La palabra python esta en el texto")