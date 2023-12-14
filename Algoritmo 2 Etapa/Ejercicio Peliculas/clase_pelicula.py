class Peliculas:
    
    def __init__(self, nombre: str, genero: str, anio: int, puntuacion: int, nacionalidad: str):
        self.nombre = nombre 
        self.genero = genero
        self.anio = anio
        self.puntuacion = puntuacion
        self.nacionalidad = nacionalidad
    
    def presentar_pelicula(self): 
        print (f'Nombre: {self.nombre}, Genero: {self.genero}, Año: {self.anio}, Puntuacion: {self.puntuacion}, Nacionalidad: {self.nacionalidad}')

    def retornar_anio(self, anio):
        if self.anio < anio:
            return "Es menor al pasado por parametro"
        elif self.anio == anio:
            return "Es igual al pasado por parámetro"
        elif self.anio > anio:
            return "Es mayor al pasado por parámetro"
        else:
            print ("Error")

    def cambiar_genero(self, nuevo_genero):
        self.genero = nuevo_genero

    def modificar_puntuacion(self, nueva_puntuacion): 
        self.puntuacion = nueva_puntuacion