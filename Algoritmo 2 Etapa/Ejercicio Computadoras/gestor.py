from clase_computadora import *

class GestorComputadora:
    lista_marcas = ['dell','hp','apple']
    lista_SO = ['macOS','linux','windows']
    def __init__(self):
        self.lista_computadora: list[Computadora] = []


    def pedir_marca_SO(self,objeto_a_pedir,lista_objetos):
        while True:
            print(f'------ Posibles {objeto_a_pedir} a crear ------')
            for obj in lista_objetos:
                print(f'- {obj}')
            obj = input(f'indique el/la {objeto_a_pedir}: ')
            if obj in lista_objetos:
                return obj
            else:
                print(f'Esa/ese {objeto_a_pedir} no existe')

    def pedir_lista_perifericos(self):
        lista_perifericos = []
        while True:
            periferico = pedir_str(f'indique un periferico, (exit para terminar): ')
            if periferico == 'exit':
                return lista_perifericos
            else:
                lista_perifericos.append(periferico)

    def verificar_tipo(self):
        print("-- LISTA COMPUTADORAS --")
        lista_tipos = []
        for i in Computadora.__subclasses__():
            print(f"-{i.__name__}")
            lista_tipos.append(i.__name__)
        while True:
            opcion = input("Ingrese el tipo de computadora: ")
            if opcion in lista_tipos:
                return opcion
            else:
                print("El tipo de computadora no es existe!")

    def crear_computadora(self):
        id_modelo = pedir_str("Indique el id de la computadora")
        marca = self.pedir_marca_SO ('marca',self.lista_marcas)
        So = self.pedir_marca_SO ('SO',self.lista_SO)
        lista_perifericos = self.pedir_lista_perifericos()
        tipo = self.verificar_tipo()
        if tipo == "Notebook":
            bateria = input("Indique la bateria que tiene:")
            obj_pc = Notebook(id_modelo, lista_perifericos,So, marca, bateria)
        elif tipo == "Escritorio":
            cable = pedir_int("Indique la cantidad de cables: ")
            obj_pc = Escritorio(id_modelo, lista_perifericos,So, marca, cable)
        self.lista_computadora.append(obj_pc)

    def presentar_pc(self):
        for computadora in self.lista_computadora:
            computadora.presentar_computadora()
            computadora.get_tipo()
    
    def cambiar_SO(self):
        id = pedir_str("Indique el id de la computadora a cambiar SO: ")
        for computadora in self.lista_computadora:
            if id == computadora.id_modelo:
                so = self.pedir_marca_SO('SO',self.lista_SO)
                computadora.cambiar_SO (so)
    
    def listar_per(self):
        id = pedir_str("Indique el id de la computadora a listar sus perifericos: ")
        for pc in self.lista_computadora:
            if id == pc.id_modelo:
                pc.listar_per()

















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

