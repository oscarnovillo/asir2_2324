from random import randint
veces = randint(1,20) # genera un número aleatorio entre 1 y 10

while 10 < veces < 15 and veces != 13:
    print(f"Esto se imprime para siempre {veces}")
    veces += 1
else:
   print(f"{veces} no está entre 1 y 10")

print ("Fin del programa")  


