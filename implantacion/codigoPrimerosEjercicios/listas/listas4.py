numeros = []

while True:
    numero = int(input("dime un numero: "))
    if numero < 0:
        break
    numeros.append(numero)

print(numeros)