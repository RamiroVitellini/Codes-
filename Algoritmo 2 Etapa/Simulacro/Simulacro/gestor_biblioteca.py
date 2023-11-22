from clase_libro import *

class Gestor_Libros:
    def __init__(self):
        self.lista_libros : list[Libro] = []
        self.idiomas_disponibles = {
    "IN":"ingles", 
    "AL":"aleman",
    "CH":"chino"
    }

    def crear_libro(self):
        id = self.validar_id()
        nombre = pedir_str('Ingrese el nombre del libro: ')
        autor = pedir_str('Ingrese el autor del libro: ')
        tipo = self.verificar_tipo()
        if tipo == Libro:
            libro = tipo(id, nombre, autor)
            self.lista_libros.append(libro)
        elif tipo == LibroNiño:
            libro = tipo (id, nombre, autor, estado = False, edad_minima = pedir_int('Ingrese la edad minima: '))
            self.lista_libros.append(libro)
        elif tipo == IdiomaLibro:
            libro = tipo (id, nombre, autor, estado = False, idioma = self.validar_idioma)
            self.lista_libros.append(libro)
    
    
    def validar_id(self):
        while True: 
            id = pedir_int("Ingrese el id del libro: ")
            for i in self.lista_libros:
                if i.id == id:
                    print ("Ese id ya existe")
            return id
        
    def verificar_tipo(self):
        print("-- LISTA LIBROS --")
        lista_tipos = []
        for i in Libro.__subclasses__():
            print(f"-{i.__name__}")
            lista_tipos.append(i.__name__)
        opcion = input("Ingrese el tipo de libro: ")
        if opcion in lista_tipos:
            return opcion
        else:
            print("El tipo de libro no existe!")
    
    def validar_idioma(self):
        for i in self.idiomas_disponibles.keys():
            print(i, end = ' - ')
        idioma = pedir_str('Ingrese el idioma del libro: ')
        return self.idiomas_disponibles.get(idioma, 'espanol')

    def logear(self):
        try:
            fichero = open('log.txt','a+')
            fichero.write(f'ID: {Libro.id}, Nombre: {Libro.nombre}, Autor: {Libro.autor}\n')
            fichero.close()
        except Exception as e:
            print(e)      

    def listar_libros(self):
        for i in self.lista_libros:
            if i.estado:
                i.presentar()

    def cambiar_estado(self):
        while True:
            id = pedir_int('Ingrese el ID del libro: ')
            for i in self.lista_libros:
                if i.id == id:
                    cambiar_estado = input("Ingrese si quiere que este -Alquilado o -Para alquilar")
                    if cambiar_estado == ("Alquilado"):
                        id.alquilar(self) 
                    elif cambiar_estado == ("Disponible"):	
                        id.alquilado(self)
            
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
