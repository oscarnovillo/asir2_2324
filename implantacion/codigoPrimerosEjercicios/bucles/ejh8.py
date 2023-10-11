

limite_inferior = int(input("numero inicial"))
limite_superior = int(input("numero final"))
while (limite_inferior>=limite_superior):
    limite_inferior = int(input("numero inicial"))
    limite_superior = int(input("numero final"))

suma_dentro_intervalo = 0
suma_numeros_fuera = 0
suma_limite = 0

numero = int(input("Dime un numero"))


while numero != 0:
    
    if (limite_inferior <= numero <= limite_superior):
        suma_dentro_intervalo += numero
    if (limite_inferior== numero or limite_superior == numero):
        suma_limite +=1
    else:
        suma_numeros_fuera +=1
    numero = int(input("Dime un numero"))


    


while i<numero_veces:
    numero = int(input("Dime un numero"))
    if numero > 0:
        numeros_mayores_cero += 1
    elif numero < 0:
        numeros_menores_cero += 1
    else:
        numeros_iguales_cero += 1
    i+=1 
