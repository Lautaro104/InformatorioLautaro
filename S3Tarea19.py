num = int(input("Ingrese un número: "))
num_perfecto = 0
for i in range(1, num):
    if num % i == 0:
        num_perfecto += i
if num_perfecto == num:
    print(f"{num} Es un número perfecto.")
else:
    print(f"{num} No es un número perfecto.")
