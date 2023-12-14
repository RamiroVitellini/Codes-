from clase_autos import *
from clase_chofer import *

class GestorAutos:
    def __init__(self):
        self.lista_choferes : list[Chofer] = []
        self.lista_autos : list[Auto] = []
        

    def crear_chofer(self):
        nombre = input("Indique el nombre del chofer: ")
        apellido = input("Indique el apellido del chofer: ")
        dni = input("Indique el dni del chofer: ")
        nacimiento = input("Indique el nacimiento del chofer: ")
        residencia = input("Indique la residencia del chofer: ")
        chofer = Chofer(nombre,apellido,dni,nacimiento,residencia)
        self.lista_choferes.append(chofer)
    
    def verificar_chofer(self):
        while True:
            dni = pedir_int("Indique el dni del chofer a verificar: ")
            for chofer in self.lista_choferes:
                if chofer.dni == dni:
                    return chofer
                else:
                    print("Ese chofer no existe")
    
    def crear_auto(self):
        if self.lista_choferes:
            patente = input("Indique la patente del auto: ")
            modelo = pedir_str("Indique el modelo del auto: ")
            anio = pedir_int("Indique el año del auto: ")
            marca = pedir_str("Indique la marca del auto: ")
            chofer = pedir_str("Indique el chofer del auto: ")
            auto = Auto(patente, modelo, anio, marca, chofer)
            self.lista_autos.append(auto)
        else:
            print("No hay choferes, primero debe crear un chofer")
    
    def modificar_chofer(self):
        patente = pedir_str("Indique la patente del auto a cambiar chofer: ")
        for auto in self.lista_autos:
            if  auto.patente == patente: 
                auto.cambiar_chofer()
    
    def modificar_residencia(self):
        nueva_residencia = pedir_str("Indique la nueva residenica: ")
        self.verificar_chofer().ChangeResidencia(nueva_residencia)

    def imprimir_lista_choferes(self):
        for chofer in self.lista_choferes:
            chofer.presentar_chofer()
        
    def imprimir_lista_autos(self):
        for auto in self.lista_autos:
            auto.presentar_auto()

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