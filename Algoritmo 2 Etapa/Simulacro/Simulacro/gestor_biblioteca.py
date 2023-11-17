from clase_libro import *
class GestorBiblioteca:
    def __init__(self):
        self.lista_libros : list[Libro] =[]

    def verificar_id(self, id):
        while True:
            for id_existentes in self.lista_libros:
                if id_existentes.id == id:
                    print ("Ese id ya existe")
                return

    def verificar_estado(self):
            self.estado_libros = self.devolver_alquilado()

    def elegir_tipo(self):
        lista_tipos = []
        for i in Libro.__subclasses__():
            print(f"-{i.__name__}")
            lista_tipos.append(i.__name__)
        while True:
            tipo = input("elija el tipo de libro que desea crear: ")
            if tipo in lista_tipos:
                return str(tipo)
            else:
                print("este tipo de libro no es valido...")

    idiomas = {
    "IN":"ingles", 
    "AL":"aleman",
    "CH":"chino"
    }

    def crear_libros(self):
        id = self.verificar_id(input("Ingrese el id del libro"))
        nombre = input("Ingrese el nombre del libros: ")
        autor = input("Ingrese el autor del libros: ")
        tipo = self.elegir_tipo
        if tipo == "LibroNiño":
            Libro = LibroNiños(id, nombre, autor)
            self.lista_libros.append(Libro)
        elif tipo == "LibroIdioma":
            Libro = LibroIdiomas(id, nombre, autor)
            self.lista_libros.append(Libro)
        self.loguear(texto)
        texto = f'{id} {nombre} {autor}'

    def loguear(self,texto):
        try:
            fichero = open('archivo.txt','a+')
            fichero.write(texto+'\n')
            fichero.close()
        except Exception as e:
            print(e)

    def listar_libros(self):
        for i in self.lista_libros:
            print (f"Id libro: {i.id}, nombre:{i.nombre}, estado:{i.estado}")

    def cambiar_estado(self):
        id = input ("Ingrese el id del libro para cambiar su estado")
        if id.verficar_id():
            cambiar_estado = input("Ingrese si quiere que este alquilado o para alquilar")
        if cambiar_estado == ("Alquilado"):
            id.devolver_alquilado(self) 
        elif cambiar_estado == ("Disponible"):	
            id.alquilar_libro(self)