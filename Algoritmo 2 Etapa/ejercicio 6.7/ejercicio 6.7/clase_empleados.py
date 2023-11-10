'''*   La Clase Empleados tiene los atributos (legajo, nombre, apellido, lista_animales_a_cuidar(clase animal))
      *  un empleado puede cuidar animales de diferentes sectores'''
from clase_animales import *
class Empleado:
    def __init__(self,legajo, nombre, apellido):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.lista_animales_a_cuidar : list[Animal] = []
    
    def presentar(self):
        print(f"Soy el empleado {self.nombre} {self.apellido} legajo: {self.legajo}, y cuido a {self.lista_animales_a_cuidar}")
    

    def agregar_animal(self,animal_a_agregar):
        self.lista_animales_a_cuidar.append(animal_a_agregar)