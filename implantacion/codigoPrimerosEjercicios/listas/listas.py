import random


# estatico
palabras_estatico = ["a","e","i","o","u"]
numeros = [0,0,0,0,0]


# dinamico
palabras_dinamico = []
for i in range(1):
    letra = input("dime una letra: ")
    palabras_dinamico.append(letra)

print(palabras_dinamico)
print(" ".join(palabras_dinamico))

# cambiar el contenido de un elemento de la lista
palabras_dinamico[0] = "cambiado"
palabras_dinamico.append("final")
palabras_dinamico.insert(0, "inicio")
palabras_dinamico.insert(3,"medio")


for i in range(len(palabras_dinamico)):
    palabras_dinamico[i] += " cambiado"

for i in range(len(palabras_dinamico)):
    print(palabras_dinamico[i])


numeros = [1,2,3,4,5,6,7,8,9,10]

suma = 0    
for i in range(len(numeros)):
    suma += numeros[i]

print(suma)
media = suma / len(numeros)
print(media)



print(palabras_dinamico)

# numeros = [ x  for x in range(10) ]
# numeros2 = random.sample(range(10), 10)



# print(numeros2)