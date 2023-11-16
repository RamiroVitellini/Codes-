class Habitacion: 

    def __init__(self, numero, max_personas, precio):
        self.numero = numero    
        self.max_personas = max_personas    
        self.precio = precio    

    def setear_max_personas(self,personas):
        self.max_personas = personas
    
    def setear_precio(self,precio):
        self.precio = precio
    
    def get_max_personas(self):
        return self.maxPesonas

    def get_precio(self):
        return self.precio
    
    def tipo_habitacion(self):
        print("Soy una habitacion del tipo", type(self).__name__)
        return type(self).__name__

class HabitacionComun (Habitacion):
    def __init__(self, numero, max_personas: int, precio: float):
        super().__init__(numero, max_personas, precio)
    
    def mostrar_info(self): 
        print (f'El numero de habitacion es {self.numero}, con una cantidad maxima de {self.max_personas} personas y cuesta {self.precio}')

class HabitacionClasico (Habitacion):
    def __init__(self, numero, max_personas: int, precio: float, cant_tv):
        super().__init__(numero, max_personas, precio)
        self.cant_tv = cant_tv
    
    def mostrar_info(self): 
            print (f'El numero de habitacion es {self.numero}, con una cantidad maxima de {self.max_personas} personas y cuesta {self.precio}')

class HabitacionPremium (Habitacion):
    def __init__(self, numero, max_personas: int, precio: float, Jacuzzi : True):
        super().__init__(numero, max_personas, precio)
        self.Jacuzzi = Jacuzzi

    def mostrar_info(self): 
            print (f'El numero de habitacion es {self.numero}, con una cantidad maxima de {self.max_personas} personas y cuesta {self.precio}')
    
