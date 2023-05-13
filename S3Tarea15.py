texto = input("Escriba un texto: ")
texto = texto.lower()
letra = {}
for palabra in texto:
    if palabra in letra:
       letra[palabra] += 1
    else:
        letra[palabra] = 1     
for palabra, cantidad in letra.items():        
    print(f"{palabra} {cantidad}")
