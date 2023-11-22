"""
Requerimientos:
El programa debe:
*   Contar con una Clase Libro con los atributos (Id(unico), Nombre, Autor y estado (ALQUILADO o NO ALQUILADO))
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo mas:
        - LibroNiños (Atributo: edad_minima (por defecto = 11))
        - LibroIdiomas (Atributo: idioma_libro)
        
*   Se deben crear 4 metodos para la clase padre Libro (que heredaran las clases hijas):
        1. Presentarse: Que indique el id, Nombre, autor y su estado 
        2. Indicar tipo de libro (tipo de clases heredadas o padre)
        3. Alquilar (Cambiaran el estado del libro a ALQUILADO)
        4. Devolver_alquiler (Cambiaran el estado del libro a NO ALQUILADO)
"""
class Libro:
    def __init__(self, id:int, nombre:str, autor:str, estado:bool = False):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.estado = estado

    def presentar(self):
        print (f'ID del libro: {self.id}, Nombre: {self.nombre}, Autor: {self.autor}, Estado: {self.estado} ')
    
    def get_tipo(self): 
        print (f'El tipo del libro es: {self.__name__}')

    def alquilar(self):
        self.estado = True 
    
    def alquilado(self):
        self.estado = False 

class LibroNiño (Libro):
    def __init__(self, id:int, nombre:str, autor:str, estado:bool = bool, edad_min = 11):
        super().__init__(id, nombre,autor,estado)
        self.edad_min = edad_min
    
    def presentar(self):
        print(f'Id: {self.id}, Nombre: {self.nombre}, Autor: {self.autor}, Edad minima: {self.edad_min}, Estado: {self.estado}, Edad minima: {self.edad_minima}')
    
class IdiomaLibro(Libro):
    def __init__(self, id:int, nombre:str, autor:str, estado:bool = bool, idioma_libro = str):
        super().__init__(id, nombre,autor,estado)
        self.idioma_libro = idioma_libro
    
    def presentar(self):
        print (f'ID del libro: {self.id}, Nombre: {self.nombre}, Autor: {self.autor}, Estado: {self.estado} ')

