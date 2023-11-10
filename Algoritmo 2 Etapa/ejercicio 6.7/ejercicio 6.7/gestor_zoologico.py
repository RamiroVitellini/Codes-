from clase_animales import *
from clase_empleados import *

class GestorZoologico:
    def __init__(self):
        self.lista_animales : list[self.lista_animales_jaula, self.lista_animales_suelto, self.lista_animales_acuatico] = []
        self.lista_animales_jaula : list[AnimalJaula] = []
        self.lista_animales_suelto : list[AnimalSuelto] = []
        self.lista_animales_acuatico : list[AnimalAcuatico] = []
        self.lista_empelados : list[Empleado] = []
    
    def crear_empleado(self):
        legajo = input('Ingrese el legajo: ')
        nombre = input('Ingrese el nombre: ')
        apellido = input('Ingrese el apellido: ')
        empleado = Empleado(legajo, nombre, apellido)
        self.lista_empelados.append(empleado)

    def crear_animal(self, sector):
        nombre = input ("Ingrese el nombre del animal: ")
        tipo = input ("Ingrese el tipo de animal que es: ")
        fecha_nacimiento = input ("Ingrese la fecha nacimiento del animal: ")
        encargado_a_cuidar = input ("Ingrese el nombre del empleado que lo cuidira: ")
        
        sector = input ("Ingrese el sector del animal\n 1- jaula\n 2- suelto\n 3- acuatico ")
        
        if sector == 1:
            tamanio_jaula = input ("Ingrese el tamaño de la jaula del animal: ")
            animal = AnimalJaula(nombre, tipo, fecha_nacimiento, encargado_a_cuidar, tamanio_jaula )
            self.lista_animales_jaula.append(animal)
        elif sector == 2:
            habitad = input ("Ingrese el habitad del animal: ")
            animal = AnimalSuelto(nombre, tipo, fecha_nacimiento, encargado_a_cuidar, habitad)
            self.lista_animales_suelto.append(animal)
        elif sector == 3:
            tamanio_acuario = input ("Ingrese el tamaño del acuario del animal: ")
            animal = AnimalAcuatico(nombre, tipo, fecha_nacimiento, encargado_a_cuidar, tamanio_acuario)
            self.lista_animales_acuatico.append(animal)
        else:
            print("Sector no válido.")
            return
        
        self.lista_animales.append(animal)
        print("Animal creado y añadido a la lista.")


    def asignar_empelado_a_cuidar(self): 
        pass 
        #Intento con IA, no lo utilizo debido que usa enumerate que no lo vimos 
        """
        if not self.lista_empelados or not self.lista_animales:
            print("No hay empleados o animales disponibles.")
            return
        print("--Lista de Empleados--")
        for i, empleado in enumerate(self.lista_empelados, start=1):
            print(f"{i}. {empleado.legajo} {empleado.nombre}")

        empleado = input("Seleccione el número de empleado al que asignar el animal: ") - 1

        print("\n--Lista de Animales--:")
        for i, animal in enumerate(self.lista_animales, start=1):
            print(f"{i}. {animal.nombre} {animal.tipo}")

        animal = input("Seleccione el número de animal a asignar: ") - 1

        empleado = self.lista_empelados[empleado]
        animal = self.lista_animales[animal]
           """

    def cambiar_encargado_un_animal(self):
        pass
    
    def imprimir_lista_empleados(self):
        for empleado in self.lista_empelados:
            empleado.presentar()


    def imprimir_lista_animales(self):
        print ("--Animales Jaula--")
        for animal in self.lista_animales_jaula:
            animal.presentar_animal()
        
        print ("--Animales Suelto--")
        for animal in self.lista_animales_suelto:
            animal.presentar_animal()
        
        print ("--Animales Acuatico--")
        for animal in self.lista_animales_acuatico:
            animal.presentar_animal()
    
        

