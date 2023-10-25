# elegir palabra al azar de una lista
from random import choice
from random import randint
palabras = [ "arbol caido","tu puta madre","el sol del cielo es amarillo",
            "el jilguero canta bien", "mercedes","delegado","a ver si te callas" 
            ]
palabra = choice(palabras)
palabra = palabras[randint(0, len(palabras))]

x= randint(0,10)


palabraOculta = []

for i in range(len(palabra)):
    if (palabra[i] == " "):
        palabraOculta.append(" ")
    else:
        palabraOculta.append("_")

print(palabraOculta)
print(" ".join(palabraOculta))

# tengo que tener palabra al azar con _
#AYUDA STRINGS
#print(len(palabra))
#print(palabra[1])
#for i in range(len(palabra)):



vidas = 7

# mientras tenga vidas
    # mostrar palabra con _
    # pedir letra
    # si la letra esta en la palabra
    # AYUDA "a" in palabra
        # cambiar _ por la letra
        # recorro la palabra y voy cambiando los _ por la letra

        # mostrar mensaje
    # sino
        # restar una vida
        # mostrar mensaje
    # si la palabra esta completa
        # mostrar mensaje
        # salir del bucle
print(" ".join(palabraOculta))
