numero = float(input("Esciba un numero decimal: "))
entero = int(numero)
decimal = round(numero - entero,2)
print(f"La parte entera: {entero}")
print(f"La parte decimal: {decimal}")