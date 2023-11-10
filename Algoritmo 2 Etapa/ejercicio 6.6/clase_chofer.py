class Chofer:
    def __init__(self,nombre,apellido,dni,nacimiento,residencia):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.nacimiento=nacimiento
        self.residencia=residencia
    
    def presentar(self):
        print(f"Soy el chofer {self.nombre} {self.apellido} con dni: {self.dni}\n naci el {self.nacimiento} y vivo en: {self.residencia}")
    
    def changeResidencia(self,nuevaResidencia):
        self.residencia = nuevaResidencia