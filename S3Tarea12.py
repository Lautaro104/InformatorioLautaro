numeros = input("Escriba una lista de numeros (separado por comas): ")
list_num = [ int(num) for num in numeros.split(",")]
suma = 0
numero = 0
while numero < len(list_num):
    suma += list_num[numero]
    numero +=1
promedio = suma / len(list_num)    
print(f"Su promedio es: {promedio}") 