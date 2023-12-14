from clase_evento import *

class GestorEvento: 
    def __init__(self):
        self.lista_evento: list[Evento] = []
        self.organizadores_disponibles = {
    "FA": "familia", 
    "AM": "amigos",
    "PR": "propio"
    }

    def crear_evento(self):
        nombre = self.verificar_nomber
        fecha = self.verificar_fecha
        hora = input("Ingrese la hora del evento: ")
        lugar = input("Ingrese el lugar del evento: ")
        tipo = self.verificar_tipo
        if tipo == "Evento":
            obj_evento = Evento(nombre, fecha, hora, lugar)
            self.lista_evento.append(obj_evento)
        elif tipo == "EventoPersonal":
            organizador = self.evento_key_perosnal
            obj_evento = Evento(nombre, fecha, hora, lugar, organizador)
            self.lista_evento.append(obj_evento)
        if tipo == "Evento":
            obligatorio = input("Ingrese si el evento es obligatorio")
            obj_evento = Evento(nombre, fecha, hora, lugar, obligatorio)
            self.lista_evento.append(obj_evento)
        texto = f"{nombre},{fecha},{hora},{lugar},{tipo}"
        self.crear_texto(texto)
    
    def verificar_nomber(self):
        while True:
            flag_existe = True
            nombre = input("Ingrese el nombre del evento: ")
            for evento in self.lista_evento:
                if evento.nombre == nombre:
                    print ("Incorrecto, nombre ya en uso!")
                    flag_existe = False
            if flag_existe:
                return nombre
    
    def verificar_fecha(self):
        while True:
            fecha = input ("Ingrese la fecha del evento") 
            if len(fecha) == 10:
                return fecha
            else:
                print("La fecha debe ser de una logitud de 10 caracteres")

    def verificar_tipo(self):
        while True:
            print("-- LISTA EVENTOS --")
            lista_tipos = []
            for i in Evento.__subclasses__():
                print(f"- {i.__name__}")
                lista_tipos.append(i.__name__)
            eleccion = input("Ingrese el evento a crear: ")
            if eleccion in lista_tipos:
                return eleccion
            else:
                print("No existe ese tipo de evento!")

    def evento_key_perosnal(self):
        for i in self.organizadores_disponibles.keys():
            print(i, end = ' - ')
        org = input('Ingrese el organizador del evento : ')
        return self.organizadores_disponibles.get(org, 'incognito')

    def crear_texto(self, texto):
        try:
            fichero = open("archivo.txt", "a+")
            fichero.write(texto)
            fichero.close()
        except Exception as e:
            print(e)

    def listar_txt(self):
        try:
            fichero = open("archivo.txt", "a+")
            fichero = fichero.readlines()
            for i in fichero:
                print (f' - {i}')
        except Exception as e:
            print(e)
    
    def listar_evento(self):
        for evento in self.lista_evento:
            evento.presentar() 