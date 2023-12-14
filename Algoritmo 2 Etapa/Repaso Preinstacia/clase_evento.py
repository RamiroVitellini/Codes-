class Evento:
    def __init__(self, nombre, fecha, hora, lugar):
        self.nombre = nombre 
        self.fecha = fecha 
        self.hora = hora 
        self.lugar = lugar 

    def presentar(self):
        print (f' Nombre: {self.nombre}, Fecha: {self.fecha}, Hora: {self.hora}, Lugar: {self.lugar}')
    
    def get_tipo(self):
        print (f'Es un evento de tipo {type(self).__name__}')
    
    def setear_fecha_hora(self, nueva_fecha, nueva_hora):
        self.fecha = nueva_fecha
        self.hora = nueva_hora
    def setear_lugar(self, nuevo_lugar):
        self.lugar = nuevo_lugar

class EventoPersonal(Evento):
    def __init__(self, nombre, fecha, hora, lugar, orgnizador):
        super().__init__(nombre, fecha, hora, lugar)
        self.orgnizador = orgnizador 
    
    def presentar(self):
        print (f' Nombre: {self.nombre}, Fecha: {self.fecha}, Hora: {self.hora}, Lugar: {self.lugar}, Organizador: {self.orgnizador}')
    

class EventoLaboral(Evento):
    def __init__(self, nombre, fecha, hora, lugar, obligatorio = True):
        super().__init__(nombre, fecha, hora, lugar)
        self.obligatorio = obligatorio 

    def presentar(self):
        print (f' Nombre: {self.nombre}, Fecha: {self.fecha}, Hora: {self.hora}, Lugar: {self.lugar}, Obligatorio: {self.obligatorio}')
    
