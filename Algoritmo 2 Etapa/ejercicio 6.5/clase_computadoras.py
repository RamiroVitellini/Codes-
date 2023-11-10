"""
Crear una clase padre Computadora:
*   Constructor debe incluir los atributos (id_modelo,lista_perifericos,SO,marca)
*   Crear metodos para esta clase de:
    1.  Presentarse (id_modelo,lista_perifericos,SO)
    2.  Indicar tipo de Computadora (Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. agregar_perifericos,CambiarSO
    
Crear 2 clases que hereden de la clase padre Computadoras, con un atributo en particular para cada una
1.   Escritorio
2.   Notebook"""
class Computadora:

    def __init__(self,id_modelo: str,lista_perifericos: list,SO: str, marca:str):
        self.id_modelo = id_modelo
        self.lista_perifericos = lista_perifericos
        self.SO = SO
        self.marca = marca
    
    def get_tipo(self):
        print(f'Soy una computadora tipo: {type(self).__name__}')

    def agregar_perifericos(self):
        pass
    
    def CambiarSO(self,so_nuevo):
        self.SO = so_nuevo
    
    def listar_perifericos(self):
        for per in self.lista_perifericos:
            print(per)

class Escritorio(Computadora):
    def __init__(self, id_modelo: str, lista_perifericos: list, SO: str, marca: str,cant_cables: str):
        super().__init__(id_modelo, lista_perifericos, SO, marca)
        self.cant_cables = cant_cables
    
class Notebook(Computadora):
    def __init__(self, id_modelo: str, lista_perifericos: list, SO: str, marca: str,peso: str):
        super().__init__(id_modelo, lista_perifericos, SO, marca)
        self.peso = peso

        