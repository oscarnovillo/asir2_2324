tabla = []

for i in range(5):
    tabla.append([])
    for j in range(15):
        if (i==0) or (j==0) or (i==4) or (j==14):
            tabla[i].append(1)
        else:
            tabla[i].append(0)

print(tabla)

for i in range(len(tabla)):
    print(tabla[i])