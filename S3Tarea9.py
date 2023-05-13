num = int(input("Escriba un numero natural: ")) 
a = 0
b = 1
print (0)
print (1)
for i in range(num - 2):
     c = a + b
     a = b
     b = c
     print(c)