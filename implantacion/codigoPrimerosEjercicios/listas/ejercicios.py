import random

numeros = random.sample(range(10), 10)
for i in range(len(numeros)):
    numeros[i] +=1

numeros_random_medio_normal = [  random.randint(1,10) for _ in range(10) ]

numeros_random_comoyase = []
for i in range(10):
    numeros_random_comoyase.append(random.randint(1,10))

print(numeros)
print(numeros_random_comoyase)
print(numeros_random_medio_normal)
numeros_random_reverse = []
for i in range(len(numeros_random_medio_normal)-1,-1,-1):
    numeros_random_reverse.append(numeros_random_medio_normal[i])

print(numeros_random_medio_normal)


for i in range(len(numeros)):
    print(f" {numeros[i]} {numeros[i]**2} {numeros[i]**3}")