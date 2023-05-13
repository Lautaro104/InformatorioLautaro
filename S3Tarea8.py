texto = input("Ingrese un texto: ")
num_palabra = 1
i = 0
while i < len(texto):
        if texto[i] == " ":
          num_palabra += 1
        i += 1    
print(f"La cantidad de palabras en el texto es de: {num_palabra}")    