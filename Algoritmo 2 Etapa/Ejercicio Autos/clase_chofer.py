class Chofer:
    def __init__(self,nombre,apellido,dni,nacimiento,residencia):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.nacimiento = nacimiento
        self.residencia = residencia
    
    def presentar_chofer(self):
        print(f"Soy el chofer {self.nombre} {self.apellido} con dni: {self.dni}\n naci el {self.nacimiento} y vivo en: {self.residencia}")

    def ChangeResidencia(self, nueva_residencia):
        self.residencia = nueva_residencia