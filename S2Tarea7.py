caracter = input("Escriba un caracter: ")
if caracter.isupper():
    print(f"El caracter '{caracter}', esta en mayusulas")
elif caracter.islower():
    print(f"El caracter '{caracter}' esta en minusculas")
elif caracter.isdigit():
    print(f"El caracter '{caracter}' es un numero")
else:
    print(f"El caracter '{caracter}' es un caracter especial")