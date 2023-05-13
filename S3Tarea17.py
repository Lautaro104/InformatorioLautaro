texto = input("Escribe una cadena de texto: ")
palabras = texto.split()
palabras_invertidas = []
for i in range(len(palabras)-1, -1, -1):
    palabras_invertidas.append(palabras[i])
texto_invertida = " ".join(palabras_invertidas)
print("La cadena invertida es:", texto_invertida)
