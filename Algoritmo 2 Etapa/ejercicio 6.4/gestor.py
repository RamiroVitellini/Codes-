"""
Crear clase GestorAutos que cuente con las siguientes funciones para un menu
1.   Crear auto, indicando tipo de auto y guardar en una lista
2.   Listar autos (presentandolos), indicando tipo de Vehiculo.
3.   Cambiar velocidad de un Vehiculo
4.   Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)"""

from clase_vehiculos import * 
class GestorVehiculos:

    def __init__(self):
        self.lista_vehiculos : list[Vehiculos] = []
    
    def pedir_tipo(self): 
        while True:
            print ("----AUTO A CREAR----")
            lista_tipos = []
            for i in Vehiculos.__subclasses__():
                print(f'- {i.__name__}')
                lista_tipos.append(i.__name__)
            tipo_clase = input('indique el auto: ')
            if tipo_clase in lista_tipos:
                return tipo_clase
            else:
                print('Esa clase no existe')
    
    def crear_auto(self):
        patente = input('Ingrese la patente: ')
        marca = input('Ingrese la marca: ')
        anio = input('Ingrese el año del modelo: ')
        origen = input('Ingrese el origen del vehiculo: ')
        vehiculo = vehiculo(patente,marca,anio,origen)
        self.lista_vehiculos.append(vehiculo)

    def listar_vehiculo(self): 
        for vehiculo in self.lista_vehiculos:
            vehiculo.get_tipo() 
    
    def cambiar_velocidad(self):
        patente = input('Indique la patente del vehiculo a cambiar su velocidad: ')
        for vehiculo in self.lista_vehiculos:
            if patente == vehiculo.patente:
                nueva_velocidad = input('Indique la nueva velocidad: ')
                vehiculo.cambiar_velocidad(nueva_velocidad)  

    def calcular_velocidad():
        pass
        