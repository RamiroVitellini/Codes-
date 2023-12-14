from clase_pelicula import *

class GestorPelicula:
    def __init__(self):
        self.lista_peliculas : list[Peliculas] = []


    def crear_peliculas(self):
        nombre = input ("Ingrese el nombre de la pelicula: ")
        genero = input ("Ingrese el genero de la pelicula: ")
        anio = input ("Ingrese el año de la pelicula: ")
        puntuacion = input ("Ingrese la puntuacion de la pelicula: ")
        nacionalidad = input ("Ingrese la nacionalidad de la pelicula: ")
        pelicula = Peliculas(nombre, genero, anio, puntuacion, nacionalidad)
        self.lista_peliculas.append(pelicula)

    def verificar_pelicula_existente(self): 
        nombre = input("Ingrese le nombre de la pelicula a verificar:")
        for pelicula in self.lista_peliculas:
            if nombre == pelicula.nombre:
                print (f'La pelicula {nombre} si existe en la lista!!!')

    def pedir_pelicula_anio(self):
        anio = input ("Ingrese el año de la pelicula: ")
        for pelicula in self.lista_peliculas:
            if anio == pelicula.anio:
                print (pelicula.nombre)

    def presentar_pelicula(self):
        nombre = input ("Indique el nombre de la pelicula a verificar: ")
        for pelicula in self.lista_peliculas:
            if nombre == pelicula.nombre:
                pelicula.presentar_pelicula()

    def cambiar_genero(self):
        nombre = input ("Indique el nombre de la pelicula a cambiar el genero: ")
        for pelicula in self.lista_peliculas:
            if nombre == pelicula.nombre:   
                nuevo_genero = input("Ingrese el nuevo genero:")
                pelicula.cambiar_genero(nuevo_genero)