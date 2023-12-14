from clase_chofer import *
class Auto:
    def __init__(self, patente, modelo, anio, marca, chofer: Chofer):
        self.patente = patente
        self.modelo = modelo
        self.anio = anio
        self.marca = marca
        self.chofer = chofer

    def cambiar_chofer(self, nuevo_chofer):
        self.chofer = nuevo_chofer

    def get_tipo(self):
        print (f'El auto es de tipo: {type(self).__name__}')

    def presentar_auto(self):
        print(f'Patente: {self.patente}, Modelo: {self.modelo}, Año: {self.anio}, Marca: {self.marca}, Chofer: {self.chofer}')