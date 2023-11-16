opcion = 0

alumnos = []
while True:
    print("1. añadir alumno")
    print("2. ver alumnos")
    print("3. salir")

    opcion = int(input("dime una opcion: "))
    if (opcion == 1):
        nombre = input("dime un nombre: ")
        edad = int(input("dime una edad: "))
        alumnos.append([nombre,edad])
    elif(opcion == 2):
        print(alumnos)
    elif(opcion == 3):
        break


