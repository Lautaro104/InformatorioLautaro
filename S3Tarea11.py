num = int(input("Escriba un numero: "))
factorial = 1
for numero in range(1, num + 1):
    print(numero)
    factorial *= numero
print(f"El resultado es {factorial}")