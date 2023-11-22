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
    
    def crear_auto(self):
        patente = input('Ingrese la patente: ')
        marca = input('Ingrese la marca: ')
        anio = input('Ingrese el año del modelo: ')
        origen = input('Ingrese el origen del vehiculo: ')
        velocidad = pedir_int ("Ingrese la velocidad del vehiculo: ")
        tipo = self.validar_tipo ()
        if tipo == Particular:
            uso = input("Cuanto tiempo de uso tiene: ")
            vehiculo = tipo(patente, marca, anio, origen,velocidad, uso)
            self.lista_vehiculos.append(vehiculo)
        elif tipo == PickUp:
            vehiculo =  tipo(patente, marca, anio, origen,velocidad, capacidad_carga = input ("Ingrese la capacidad de carga"))
            self.lista_vehiculos.append(vehiculo)
        elif tipo == Deportivo:
            vehiculo =  tipo(patente, marca, anio, origen,velocidad, caballos_fuerza = input ("Ingrese los caballos fuerza"))
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

    def calcular_tiempo_de_viaje(self):
        patente = input ("Ingrese la patente del auto: ")
        for i in self.lista_vehiculos:
            if i.patente == patente:
                km = pedir_int("Cuantos km recorrerá: ")
                print (f' El tiempo en recorrer será de:' (km / i.velocidad))
           
    def validar_tipo(self):
        tipos_vehiculos = {'vehiculo particular':Particular, 'vehiculo PickUp':PickUp, 'vehiculo Deportivo':Deportivo}
        while True:
            for tipos in tipos_vehiculos.keys():
                print(tipos, end = ' - ')
            tipo_elegido = pedir_str('Ingrese el tipo de vehiculo: ')
            if tipo_elegido in tipos_vehiculos:
                return tipos_vehiculos[tipo_elegido]
            else:
                print(f'El tipo de vehiculo {tipo_elegido} no existe')
    

def pedir_int(text):
    while True:
        try:
            numero = int(input(text))
            return numero
        except Exception as e:
            print(f'Error: {e}. Ingrese un dato valido')
            
def pedir_float(text):
    while True:
        try:
            numero = float(input(text))
            return numero
        except Exception as e:
            print(f'Error: {e}. Ingrese un dato valido')
            
def pedir_str(text):
    while True:
        try:
            numero = str(input(text))
            return numero
        except Exception as e:
            print(f'Error: {e}. Ingrese un dato valido')
