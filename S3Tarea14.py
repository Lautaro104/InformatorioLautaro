num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    for n in range(i):
        print(i, end = " ")
    print()
