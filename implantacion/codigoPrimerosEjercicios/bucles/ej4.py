
numero_veces = int(input("numero de numeros"))
i = 0
numeros_mayores_cero = 0
numeros_menores_cero = 0
numeros_iguales_cero = 0

while i<numero_veces:
    numero = int(input("Dime un numero"))
    if numero > 0:
        numeros_mayores_cero += 1
    elif numero < 0:
        numeros_menores_cero += 1
    else:
        numeros_iguales_cero += 1
    i+=1 
