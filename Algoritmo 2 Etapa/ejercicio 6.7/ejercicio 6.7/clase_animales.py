'''*   Simular un programa de gestion de animales de un zoologico, que cuente con dos clases Animales y Empleados
*   La Clase Animales tiene los atributos (nombre, tipo_animal, fecha_nacimiento, encargado_cuidar (objeto empleado))
    *   Crear 3 clases que hereden de animal segun su sector del zoologico)
        1. Animales en jaulas.
        2. Animales sueltos.
        3. Animales en el agua'''
class Animal:
    def __init__(self,nombre,tipo_animal,fecha_nacimiento,encargado_cuidar):
        self.nombre = nombre
        self.tipo_animal = tipo_animal
        self.fecha_nacimiento = fecha_nacimiento
        self.encargado_cuidar = encargado_cuidar
    
    def cambiar_encargado(self,nuevo_encargado):
        self.encargado_cuidar = nuevo_encargado

    def presentar_animal(self):
        print(f"El animal es {self.nombre}, de tipo {self.tipo_animal}, fecha nacimiento: {self.fecha_nacimiento}, y cuidadado por {self.encargado_cuidar}")

class AnimalJaula(Animal):
    def __init__(self, nombre, tipo_animal, fecha_nacimiento, encargado_cuidar, tamanio_jaula):
        super().__init__(nombre, tipo_animal, fecha_nacimiento, encargado_cuidar)
        self.tamanio_jaula = tamanio_jaula

class AnimalSuelto(Animal):
    def __init__(self, nombre, tipo_animal, fecha_nacimiento, encargado_cuidar, habitad):
        super().__init__(nombre, tipo_animal, fecha_nacimiento, encargado_cuidar)
        self.habitad = habitad
    
class AnimalAcuatico(Animal):
    def __init__(self, nombre, tipo_animal, fecha_nacimiento, encargado_cuidar, tamanio_acuario):
        super().__init__(nombre, tipo_animal, fecha_nacimiento, encargado_cuidar)
        self.tamanio_acuario = tamanio_acuario
    