num = 1
numero = int(input("Introduce el número de filas: "))
for i in range(numero):
    for j in range(  i + 1):
        print(num, end = " ")
        num += 1
    print()
