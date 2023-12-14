class Libro:
    def __init__(self, id, nombre, autor, estado: bool = False):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.estado = estado

    def presentar_libro(self):
        print (f'Id: {self.id}, Nombre: {self.nombre}, Autor: {self.autor}, Estado: {self.estado}')

    def get_tipo(self):
         print (f'Soy un libro de tipo {type(self).__name__}')

    def alquilar(self):
         self.estado = True
    
    def devolver_alquiler(self):
         self.estado = False
         
class LibroNiño(Libro):
    def __init__(self, id, nombre, autor, estado, edad_minima = 11):
        super().__init__(id, nombre, autor, estado)
        self.edad_minima = edad_minima
    
    def presentar_libro(self):
         print (f'Id: {self.id}, Nombre: {self.nombre}, Autor: {self.autor}, Estado: {self.estado}, Edad Minima: {self.edad_minima}')

class LibroIdiomas(Libro):
    def __init__(self, id, nombre, autor, estado, idioma_libros):
        super().__init__(id, nombre, autor, estado)
        self.idioma_libros = idioma_libros

    def presentar_libro(self):
            print (f'Id: {self.id}, Nombre: {self.nombre}, Autor: {self.autor}, Estado: {self.estado}, Idioma: {self.idioma_libros}')