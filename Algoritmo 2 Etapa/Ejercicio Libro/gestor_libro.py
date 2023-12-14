from clase_libro import *

class GestorBiblioteca : 
    def __init__(self):
        self.lista_libros : list[Libro] = []
        self.idiomas_disponibles = {
    "IN":"ingles", 
    "AL":"aleman",
    "CH":"chino"
    }

    def crear_libro(self):
        id = self.verificar_id()
        nombre = input ("Ingrese el nombre del libro: ")
        autor = input ("Ingrese el autor del libro: ")
        tipo = self.verificar_tipo()
        if tipo == "Libro":
            obj_libro = Libro(id, nombre,autor)
            self.lista_libros.append(obj_libro)
        elif tipo == "LibroNiño":
            obj_libro = LibroNiño(id, nombre, autor, estado = False, edad_minima = input("Ingrese la edad minima: "))
            self.lista_libros.append(obj_libro)
        elif tipo == "LibroIdioma":
            obj_libro = LibroIdiomas(id, nombre, autor, estado=False, idioma_libros = self.verficar_idioma())
            self.lista_libros.append(obj_libro)
        
        self.fichero_log(obj_libro)

    def verificar_tipo(self):
        print("-- LISTA LIBROS --")
        lista_tipos = []
        for i in Libro.__subclasses__():
            print(f"-{i.__name__}")
            lista_tipos.append(i.__name__)
        while True:
            opcion = input("Ingrese el tipo de libro: ")
            if opcion in lista_tipos:
                return opcion
            else:
                print("El tipo de lbrio no existe!")

    def verificar_id(self):
        while True:
            flag_existe_id = True
            id = input('Ingrese el ID: ')
            for libro in self.lista_libros:
                if id ==  libro.id:
                    print('ID Incorrecto. El ID ya existe')
                    flag_existe_id = False
            if flag_existe_id:
                return id
       
    def verficar_idioma(self):
        for i in self.idiomas_disponibles.keys():
            print(i, end = ' - ')
        idioma = input('Ingrese el idioma del libro: ')
        return self.idiomas_disponibles.get(idioma, 'espanol')

    def fichero_log(self, libro):
        try:
            fichero = open('log.txt', 'a+')
            fichero.write(f'ID: {libro.id}, Nombre: {libro.nombre}, Autor: {libro.autor}\n')
            fichero.close()
        except Exception as e:
            print(e)  

    def estado_libro(self):
        while True:
            id = input("Ingrese el id del libro al cual se le quiere cambiar el estado: ")
            for libro in self.lista_libros:
                if libro.id == id:
                    estado = input("Escriba Alquilado si lo quiere alquilar, o Sin alquilar para que no este alquilado: ") 
                    if estado == "Alquilado":
                        libro.alquilar()
                    elif estado == "Sin alquilar":
                        libro.devolver_alquiler()
                    else:
                        print ("Error")

                

