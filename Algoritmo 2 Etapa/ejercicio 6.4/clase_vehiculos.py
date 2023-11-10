"""
Crear una clase padre Vehiculos:
*   Constructor debe incluir los atributos (patente,marca,año,origen)
*   Crear metodos para esta clase de:
    1.  Presentarse (patente,marca,año,origen)
    2.  Indicar tipos de vehiculo(Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. Acelerar, Retroceder, obtener_velocidad, setear_velocidad"""
class Vehiculos: 

    def __init__(self, patente, marca: str, anio: int, origen: str) :
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.origen = origen

    def presentar_pelicula(self):
        print(f"""La patente del auto es {self.patente}, de marca {self.marca}, año {self.anio} y su origen es de {self.origen}""")

    def get_tipo(self):
        print (f'Soy un vehiculo de tipo: {type(self).__name__}')

    def acelerar(self):
        pass
    
    def retroceder(self):
        pass
    
    def obtener_velocidad(self):
        pass
    
    def setear_velocidad(self):
        pass

    def cambiar_velocidad(self,nueva_velocidad):
        self.velocidad = nueva_velocidad


""" Crear 3 clases que hereden de la clase padre Vehiculos, con un atributo en particular para cada una
1.   Particular
2.   PickUp
3.   Deportivo"""

class Particular(Vehiculos):
    def __init__(self, patente, marca: str, anio: int, origen: str, tiempo_uso):
        super().__init__(patente, marca, anio, origen)
        self.tiempo_uso = tiempo_uso

class PickUp(Vehiculos):
    def __init__(self, patente, marca: str, anio: int, origen: str, capacidad_de_carga):
        super().__init__(patente, marca, anio, origen)
        self.capacidad_de_carga = capacidad_de_carga

class Deportivo(Vehiculos): 
    def __init__(self, patente, marca: str, anio: int, origen: str, caballos_fuerza):
        super().__init__(patente, marca, anio, origen)
        self.caballos_fuerza = caballos_fuerza