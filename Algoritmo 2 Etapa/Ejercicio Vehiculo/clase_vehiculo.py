class Vehiculo:
    def __init__(self, patente, marca, anio, origen, velocidad):
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.origen = origen
        self.velocidad = velocidad

    def presentar_vehiculo(self):
        print (f' Patente vehiculo: {self.patente}, Marca: {self.marca}, Año: {self.anio}, Origen: {self.origen}, Velocidad: {self.velocidad}')

    def indicar_tipo(self):
        print (f'Soy un vehiculo de tipo: {type(self).__name__}')

    def acelerar(self):
        print (f'El vehiculo esta acelreando')
    
    def retroceder(self):
        print (f'El vehiculo esta retrocediendo')
    
    def dar_velocidad(self):
        print (f'La velocidad del vehiuclo es: {self.velocidad}')

    def setear_velocidad(self, nueva_velocidad):
        self.velocidad = nueva_velocidad
 
class vehiculo (Vehiculo):
    def __init__(self, patente, marca, anio, origen, velocidad):
        super().__init__(patente, marca, anio, origen, velocidad)

class Particular(Vehiculo):
    def __init__(self, patente, marca, anio, origen, velocidad, kilometros):
        super().__init__(patente, marca, anio, origen, velocidad)
        self.kilometros = kilometros

class PickUp(Vehiculo):
    def __init__(self, patente, marca, anio, origen,velocidad, llantas):
        super().__init__(patente, marca, anio, origen, velocidad)
        self.llantas = llantas

class Deportivo(Vehiculo):
    def __init__(self, patente, marca, anio, origen,velocidad, caballos):
        super().__init__(patente, marca, anio, origen, velocidad)
        self.caballos = caballos