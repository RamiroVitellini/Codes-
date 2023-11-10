"""
Crear clase GestorComputadora que cuente con las siguientes funciones para un menu
1.   Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
2.   Listar Computadoras (presentandolos), indicando tipo.
3.   Cambiar SO de una Computadora, verificando una lista de SO disponibles
4.   Listar perifericos"""
from clase_computadoras import *
class GestorComputadora:
    # Atributos de clase
    lista_marcas = ['dell','hp','apple']
    lista_SO = ['macOS','linux','windows']
    
    def __init__(self):
        self.lista_computadoras : list[Computadora] = []
    
    def pedir_tipo(self):
        while True:
            print('------ Posibles pcs a crear ------')
            lista_tipos = []
            for i in Computadora.__subclasses__():
                # TAREA: buscar mejor forma
                print(f'- {i.__name__}')
                lista_tipos.append(i.__name__)
            tipo_clase = input('indique la pc: ')
            if tipo_clase in lista_tipos:
                return tipo_clase
            else:
                print('Esa clase no existe')
    
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
            periferico = input(f'indique un perisferico (exit para terminar): ')
            if periferico == 'exit':
                return lista_perifericos
            else:
                lista_perifericos.append(periferico)
    
    def crear_computadora(self):
        tipo_clase = self.pedir_tipo()
        id = input('Indique el id: ')
        marca = self.pedir_marca_SO('marca',self.lista_marcas)
        so = self.pedir_marca_SO('SO',self.lista_SO)
        lista_perisfericos = self.pedir_lista_perifericos()
        if tipo_clase == 'Notebook':
            peso = input('Indique el peso: ')
            object_pc = Notebook(id,lista_perisfericos,so,marca,peso)
        if tipo_clase == 'Escritorio':
            cables = input('Indique la cant de cables:' )
            object_pc = Escritorio(id,lista_perisfericos,so,marca,cables)
        
        self.lista_computadoras.append(object_pc)


    def listar_computadoras(self):
        for pc in self.lista_computadoras:
            pc.get_tipo()

    def cambiar_so(self):
        id_a_cambiar = input('Indique el id de la pc a cambiar el so: ')
        for pcs in self.lista_computadoras:
            if pcs.id_modelo == id_a_cambiar:
                so = self.pedir_marca_SO('SO',self.lista_SO)
                pcs.CambiarSO(so)
    
    def listar_perifericos(self):
        id = input('Indique el id de la pc a listar los perifericos: ')
        for pcs in self.lista_computadoras:
            if pcs.id_modelo == id:
                pcs.listar_perifericos()