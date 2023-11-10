from clase_auto import *
from clase_chofer import *

class GestorTaxis:
    def __init__(self):
        # dejo instanciado las listas con choferes y autos para probar
        self.lista_choferes : list[Chofer] = [Chofer('test','test','test','test','test')]
        self.lista_autos : list[Auto] = [Auto('test','test','test','test',self.lista_choferes[0])]

    def crear_chofer(self):
        nombre = input('Ingrese el nombre: ')
        apellido = input('Ingrese el apellido: ')
        dni = input('Ingrese el dni: ')
        nacimiento = input('Ingrese la nacimiento: ')
        residencia = input('Ingrese la residencia: ')
        chofer = Chofer(nombre,apellido,dni,nacimiento,residencia)
        self.lista_choferes.append(chofer)
    
    def buscar_chofer(self) -> Chofer:
        while True:
            dni = input('Dame el dni del chofer que busca: ')
            for chofer in self.lista_choferes:
                if chofer.dni == dni:
                    return chofer
            
            print('El dni no fue encontrado')

    def crear_auto(self):
        if self.lista_choferes:
            patente = input('Ingrese la patente: ')
            modelo = input('Ingrese el modelo: ')
            anio = input('Ingrese el anio: ')
            marca = input('Ingrese la marca: ')
            chofer = self.buscar_chofer()
            auto = Auto(patente,modelo,anio,marca,chofer)
            self.lista_autos.append(auto)
        else:
            print('No hay choferes, primero debe crear un chofer')

    def modificar_chofer(self):
        while True:
            patente = input('Dame la patente del auto que queres modificarle el chofer: ')
            for auto in self.lista_autos:
                if auto.patente == patente:
                    chofer = self.buscar_chofer()
                    auto.cambiar_chofer(chofer)
            
            print('El auto no fue encontrado')
    
    def modificar_residencia_v_pro(self):
        nueva_residencia = input('Dame la nueva residencia: ')
        self.buscar_chofer().changeResidencia(nueva_residencia)

    def modificar_residencia(self):
        while True:
            dni = input('Dame el dni del chofer que busca: ')
            for chofer in self.lista_choferes:
                if chofer.dni == dni:
                    nueva_residencia = input('Dame la nueva residencia: ')
                    chofer.changeResidencia(nueva_residencia)
                    return
            
            print('El dni no fue encontrado')
    
    def imprimir_lista_choferes(self):
        for chofer in self.lista_choferes:
            chofer.presentar()
    
    def imprimir_lista_autos(self):
        for auto in self.lista_autos:
            auto.mostrar_informacion()
        