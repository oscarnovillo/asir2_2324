alumnos = [] 



while True:
    nombre = input("dime un nombre: ")
    if nombre == "*":
        break
    edad  = int(input("dime una edad: "))

    alumnos.append([nombre,edad])

for i in range(len(alumnos)):
    if alumnos[i][1] >= 18:
        print(f" {alumnos[i][0]} con {alumnos[i][1]} años")

alumnos.sort(reverse=True, key=lambda alumno: alumno[1])

mayor = alumnos[0][1]

for i in range(len(alumnos)):
    if (mayor == alumnos[i][1]):
        print(f" {alumnos[i][0]} con {alumnos[i][1]} años")
    else:
        break

