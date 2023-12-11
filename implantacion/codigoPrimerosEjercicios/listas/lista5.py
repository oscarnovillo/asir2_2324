import random

numeros = random.sample([1,2,3,4,5,6,7,8,9,10],10)
print(numeros)

numeros = [ random.randint(0,2) for _ in range(10) ]
print(numeros)

# para limpiar la lista
numeros.clear()
for i in range(10):
    numeros.append(random.randint(0,2))
print(numeros)


numeros.sort()

print(numeros)
