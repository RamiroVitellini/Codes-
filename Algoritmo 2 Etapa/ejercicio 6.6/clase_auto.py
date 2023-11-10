from clase_chofer import *
class Auto:
    def __init__(self,patente, modelo, anio, marca, chofer: Chofer):
        self.patente = patente
        self.modelo = modelo
        self.anio = anio
        self.marca = marca
        self.chofer = chofer
    
    def cambiar_chofer(self,nuevo_chofer: Chofer):
        self.chofer = nuevo_chofer

    def mostrar_informacion(self):
        print(f'patente: {self.patente} - modelo: {self.modelo} - anio: {self.anio} - marca: {self.marca} - chofer: {self.chofer.nombre}')