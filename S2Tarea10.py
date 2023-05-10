letra = input("Escreba una letra: ")
letra = letra.lower()  
if ("a", "e", "i", "o", "u" in letra):
    print("Es una vocal")
else:
    print("Es una consonante")