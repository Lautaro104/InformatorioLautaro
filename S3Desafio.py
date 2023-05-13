import random
nombre = input("Ingrese tu nombre: ")
print(f"Bienvenido {nombre}, jugemos a 'Adivina El Número', estoy pensando en un numero estre el 1 al 100 ")
numero_random = random.randint(1, 100)
intentos = 8
while intentos > 0:
    print(f"Solo tiene: {intentos} intentos")
    num = input("Ingresa un número entero: ")
    if not num.isdigit():
        print(f"Lo siento {num} no es un número entero.")
        continue
    num = int(num)
    if num < numero_random:
        print("El número a adivinar es mayor.")
    elif num > numero_random:
        print("El número a adivinar es menor.")
    else:
        print(f"¡Felicidades {nombre}! has adivinado el número en el intento {9 - intentos}")
        break
    intentos -= 1
if intentos == 0:
    print(f"Lo siento, se agotaron los intentos. El número a adivinar era {numero_random}. Mejor suerte la próxima vez.")
