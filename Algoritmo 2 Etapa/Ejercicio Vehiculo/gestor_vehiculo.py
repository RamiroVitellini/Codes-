from clase_vehiculo import *

class GestorVehiculo:
    def __init__(self):
        self.lista_vehiculos : list[Vehiculo] = []

    def crear_auto(self):
        patente = input("Ingrese la patente del vehiculo: ")
        marca = input("Ingrese la marca del vehiculo: ")
        año = pedir_int("Ingrese el año del vehiculo: ")
        origen = input("Ingrese el origen del vehiculo: ")
        velocidad = pedir_int("Ingrese la velocidad del vehiculo: ")
        tipo = self.verificar_tipo()
        if tipo == "Vehiculo":
            obj_vehiculo = vehiculo(patente, marca, año, origen, velocidad)
        elif tipo == "Particular":
            obj_vehiculo = Particular(patente, marca, año, origen,velocidad, kilometros = pedir_int('Indique los kilometros: '))
        elif tipo == "PickUp":
            llantas = input('Indique las llantas: ')
            obj_vehiculo = PickUp(patente, marca, año, origen, velocidad, llantas)
        elif tipo == "Deportivo":
            caballos = pedir_int('Indique los caballos: ')
            obj_vehiculo = Deportivo(patente, marca, año, origen, velocidad, caballos)

        self.lista_vehiculos.append(obj_vehiculo)

    def verificar_tipo(self):
        print("-- LISTA VEHICULOS --")
        lista_tipos = []
        for i in Vehiculo.__subclasses__():
            print(f"-{i.__name__}")
            lista_tipos.append(i.__name__)
        while True:
            opcion = input("Ingrese el tipo de vehiculo: ")
            if opcion in lista_tipos:
                return opcion
            else:
                print("El tipo de vehiculo no es existe!")
    
    def listar_vehiclo(self):
        for vehiculo in self.lista_vehiculos:
           vehiculo.presentar_vehiculo()
           vehiculo.indicar_tipo()

    def cambiar_velocidad(self):
        patente = input("Ingrese la patente del vehiclo a cmabiar la velocidad: ")
        for vehiculo in self.lista_vehiculos:
            if patente == vehiculo.patente:
                nueva_velocidad = pedir_int("Ingrese la nueva velocidad: ")
                vehiculo.setear_velocidad(nueva_velocidad)
    
    def calcular_tiempo_de_viaje(self):
        patente = input ("Ingrese la patente del auto: ")
        for i in self.lista_vehiculos:
            if i.patente == patente:
                km = pedir_int("Cuantos km recorrerá: ")
                print (" El tiempo en recorrer será de:", (km / i.velocidad))

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