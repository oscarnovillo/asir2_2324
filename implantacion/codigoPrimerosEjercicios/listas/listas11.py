tabla = []

for i in range(5):
    tabla.append([])
    for j in range(5):
        if (i==j) or (i+j==4):
            tabla[i].append(1)
        elif (i==4) and (j==2):
            tabla[i].append(8)   
        else:
            tabla[i].append(0)

print(tabla)

for i in range(len(tabla)):
    print(tabla[i])