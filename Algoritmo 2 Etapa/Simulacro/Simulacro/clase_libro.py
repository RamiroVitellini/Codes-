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
    def __init__(self,id, nombre, autor, estado_libro):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.estado = estado_libro

class LibroNiños(Libro):
    def __init_(self, id, nombre, estado_libro, edad_minima :11):
        super().__init_subclass__(id, nombre, estado_libro)
        self.edad_minima = edad_minima

class LibroIdiomas(Libro):
    def __init_(self, id, nombre, estado_libro, idioma_libro):
        super().__init_subclass__(id, nombre, estado_libro)
        self.idioma_libro = idioma_libro

    def presentarse(self):
        print (f"El id del libro es {self.id}, nombre: {self.nombre}, autor: {self.autor} estado: {self.estado_libro}")

    def dar_tipo(self):
        print(f'Soy libro de tipo: {type(self).__name__}')

    def alquilar_libro(self,alquilado):
        self.estado_libro = alquilado

    def devolver_alquilado(self,no_alquilado):
        self.estado_libro = no_alquilado
