import random

lista1 = [ random.randint(0,10) for _ in range(6) ]
lista2 = [ random.randint(0,10) for _ in range(5) ]

lista3 = []

for i in range(len(lista2)):
    lista3.append(lista1[i] + lista2[i])

print(lista1)
print(lista2)
print(lista3)



lista1[random.randint(0,len(lista1))]
