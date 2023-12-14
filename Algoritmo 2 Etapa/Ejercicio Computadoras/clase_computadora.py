class Computadora:
    def __init__(self, id_modelo, listaPerifericos, SO, marca):
        self.id_modelo = id_modelo
        self.listaPerifericos = listaPerifericos
        self.SO = SO
        self.marca = marca
        
    def presentar_computadora(self):
        print (f'Modelo de pc: {self.id_modelo}, Perifericos: {self.listaPerifericos}, SO: {self.SO}, Marca: {self.marca}')

    def get_tipo(self):
        print(f'Soy una computadora de tipo: {type(self).__name__}')
    
    def agragar_perifericos(self, nuevos_perifericos):
        self.listaPerifericos = nuevos_perifericos

    def cambiar_SO(self, nuevos_so):
        self.sO = nuevos_so
    
    def listar_per(self):
        for per in self.listaPerifericos:
            print (per)

class Escritorio (Computadora):
    def __init__(self, id_modelo, listaPerifericos, SO, marca, cables):
        super().__init__(id_modelo, listaPerifericos, SO, marca)
        self.cables = cables

class Notebook (Computadora):
    def __init__(self, id_modelo, listaPerifericos, SO, marca, bateria):
        super().__init__(id_modelo, listaPerifericos, SO, marca)
        self.bateria = bateria
