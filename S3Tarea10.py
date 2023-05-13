texto = input("Escriba un texto o una frase: ")
vocales = ["a", "e", "i", "o", "u"]
nuevo_texto = ""
for palabra in texto:
   if palabra in vocales:
       palabra = palabra.upper() 
   nuevo_texto += palabra 
print(f"El texto con las vocales destacades: {nuevo_texto}")