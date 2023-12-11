import random

matriz_numeros = []

for i in range(5):
    matriz_numeros.append([])
    for j in range(5):
        matriz_numeros[i].append(random.randint(0,10))


for i in range(len(matriz_numeros)):
    suma_fila = 0
    for j in range(len(matriz_numeros)):
        suma_fila += matriz_numeros[i][j]
    print(f"La suma de la fila {i} es {suma_fila}")


for i in range(len(matriz_numeros)):
    suma_fila = 0
    for j in range(len(matriz_numeros)):
        suma_fila += matriz_numeros[j][i]
    print(f"La suma de la columna {i} es {suma_fila}")


suma_total = 0
for i in range(len(matriz_numeros)):
    for j in range(len(matriz_numeros)):
        suma_total += matriz_numeros[i][j]

print(f"La suma total es {suma_total}")



