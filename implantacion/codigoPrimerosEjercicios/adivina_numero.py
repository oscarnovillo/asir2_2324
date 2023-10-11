from random import randint

numero_secreto = randint(1, 100)

i = 0
while numero != numero_secreto:
    print(f"Intento {i+1}")
    numero = int(input("Dime un numero"))
    if (i >= 10):
        print("Has perdido")
        break
    elif (numero > numero_secreto):
        print("El numero secreto es menor")
    
    elif (numero < numero_secreto):
        print("El numero secreto es mayor")
    i+=1  
else:
    print(f"Has  el numero secreto era {numero_secreto}")   