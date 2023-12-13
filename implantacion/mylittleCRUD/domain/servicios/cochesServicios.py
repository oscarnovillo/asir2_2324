
from domain.modelo.coche import Coche
from data.db import coches


class CochesServicios:

    def __init__(self):
        pass

    def crearCoche(self):
        matricula = input("Introduce la matricula: ")
        marca = input("Introduce la marca: ")
        modelo = input("Introduce el modelo: ")
        color = input("Introduce el color: ")
        coche = Coche(matricula, marca, modelo, color)
        coches.append(coche)

    def buscarCoche(self):
        matricula = input("Introduce la matricula: ")
        for coche  in coches:
            if (coche.matricula == matricula):
                print(coche.matricula, coche.marca, coche.modelo, coche.color)
                break
        else:
            print("No se ha encontrado el coche")

    def listar_coches(self):
        for coche in coches:
            print(coche.matricula,coche.maca,coche.modleo )