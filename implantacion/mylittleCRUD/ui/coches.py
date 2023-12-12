from domain.modelo.coche import Coche

coches : list = []

def crearCoche():
    matricula = input("Introduce la matricula: ")
    marca = input("Introduce la marca: ")
    modelo = input("Introduce el modelo: ")
    color = input("Introduce el color: ")
    coche = Coche(matricula, marca, modelo, color)
    coches.append(coche)

def buscarCoche():
    matricula = input("Introduce la matricula: ")
    for coche  in coches:
        if (coche.matricula == matricula):
            print(coche.matricula, coche.marca, coche.modelo, coche.color)
            break
    else:
        print("No se ha encontrado el coche")

def listar_coches():
    for coche in coches:
        print(coche.matricula,coche.maca,coche.modleo )


def main():
    while True:
        print(" 1. Crear coche")
        print(" 2. Listar coches")
        print(" 3. Buscar coche")
        print(" 4. Salir")
        opcion = input("Introduce una opcion: ")
        if (opcion == "1"):
            crearCoche()
        elif (opcion == "2"):
            listar_coches()
        elif (opcion == "3"):
            buscarCoche()
        elif (opcion == "4"):
            break
        else:
            print("Opcion incorrecta")








