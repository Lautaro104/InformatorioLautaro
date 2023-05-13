texto = input("Escriba un texto o una frase: ")
palabras = texto.split()  
for palabra in palabras:
    palabra_al_reves = palabra[::-1]  
    print(palabra_al_reves, end=" ")  