"""    1.  Crear instancias de una habitacion y guárdalos en una lista de habitaciones. 
        1.1) Se debe verificar que tipo de instancia de Habitacion a crear y los parámetros. IMPORTANTE!: clase hijas verificar y pedir parámetros
             - numero: debe ser único
             - max_personas: verificar que sea un numero entero y este entre 2 y 6 inclusives.
             - precio: se debe pedir en pesos pero se debe guardar en dolares (1 dolar -> 900 pesos)
        1.2) Clases hijas:
             - cant_televisores: verificar que sea entero entre 0 y 3 incluses
             - Jacuzzi: verificar que sea True o False (boolean)
             
        1.3) Al crear una Habitacion es necesario logearlo (Escribir en una línea nueva: numero,max_personas,precio,tipo_de_clase)) 
             en un archivo llamado historial_habitaciones.txt (Crear función en el mismo gestor). IMPORTANTE!: verificar permisos y extension
    2.   Cambiar precio de habitacion, seleccionando su numero: Se debe cambiar el precio de la habitacion dependiendo de la cant max de 
         personas que contenga y el tipo de habitacion:
         - Se debe leer el diccionario por el tipo de habitacion y multiplicar ese precio por la cantidad de personas.
         Ej. Precio hab clasica = 400 (CL)* max_personas = 400 * 5 = 2000 IMPORANTE! solo se le pide el numero de habitacion al usuario
    3.   Pedir al usuario un numero y listar esa cantidad de habitaciones de la lista, verificando que hayan esa cantidad de habitaciones
    """
from clase_habitacion import *

class GestorHabitacion:
    def __init__(self):
        self.lista_habitaciones : list[Habitacion] = []

    def verificar_numero(self, numero):
        for habitacion_existente in self.lista_habitaciones:
            if habitacion_existente.numero == numero:
                print(f"Error: La habitación con número {numero} ya existe.")
                return
    
    def verificar_personas(self):
        while True:
            max_per = input ("Ingrese el numero de personas, (debe estar entre 2 y 6): ").capitalize
            if 6 >= max_per >= 2:
                return max_per
            else:
                print ("numero incorrecto")
    
    def verificar_precio(self):
        while True:
            pedir_precio = input("Ingrese el valor de la habitacion en pesos: ")
            if pedir_precio.isalnum:
                precio = (pedir_precio / 900)
                return precio
            else:
                print ("Valor incorrecto")

    def verificar_tv(self):
        while True:
            cantidad_tv = input("Ingrese la cantidad de tv que tendra la habitacion (debe tener entre 0 y 3):")
            if 3>= cantidad_tv >= 0:
                return cantidad_tv
            else:
                print ("Valor incorrecto de tv")
    
    def verificar_jacuzzi(self):
        while True:
            jacuzzi = input("Ingrese si habre jacuzzi (Si o No):").upper
            if jacuzzi == ("Si"):
                return True
            elif jacuzzi == ("No"):
                return False
            else:
                print ("Responde con Si o No")

    def elegir_tipo(self):
        lista_tipos = []
        for i in Habitacion.__subclasses__():
            print(f"-{i.__name__}")
            lista_tipos.append(i.__name__)
        while True:
            tipo = input("elija el tipo de habitacion que desea crear: ")
            if tipo in lista_tipos:
                return str(tipo)
            else:
                print("este tipo de habitacion no es valido...")


    def crear_habitacion(self):
        numero = self.verificar_numero(input('Ingrese el numero: '))
        personas = self.verificar_personas(input('Ingrese la cant de personas: '))
        precio = self.verificar_precio(input('Ingrese el precio: '))
        tipo = self.elegir_tipo()
        if tipo == "comun":
            habitacion = HabitacionComun(numero, personas, precio)
            self.lista_habitaciones.append(habitacion)
        elif tipo == "clasico":
            habitacion = HabitacionClasico(numero,personas,precio)
            self.lista_habitaciones.append(habitacion)
        elif tipo == "premium":
            habitacion = HabitacionPremium(numero,personas,precio)
            self.lista_habitaciones.append(habitacion)
        texto = f'{numero},{personas},{precio}'
        self.loguear(texto)


    def loguear(self,texto):
        try:
            fichero = open('archivo.txt','a+')
            fichero.write(texto+'\n')
            fichero.close()
        except Exception as e:
            print(e)

    def cambiar_precio(self):
        precio_habitaciones = {
        }
        while True:
            numero_habitacion = input('ingrese el num de habitacion: ')
            for hab in self.lista_habitaciones:
                if hab.numero == numero_habitacion:
                    nuevo_precio = precio_habitaciones.get(hab.tipo_habitacion()) * hab.get_max_personas()
                    hab.setear_precio(nuevo_precio)
                    print(nuevo_precio)
                    return
            print('No existe esa habitacion')


    def imprimir_toda_lista(self):
        for i in self.lista_habitaciones:
            print (f"Habitacion numero {i.numero}, Maximo de personas:{i.max_personas}, Precio: {i.precio}")

    def listar_habitaciones(self):
        if self.lista_habitaciones:
            cont = 0
            num_a_ver = input("dame el numero de habitaciones a ver: ")
            for i in self.lista_habitaciones:
                print(f"Habitacion numero: {i.numero} Maximo de Personas: {i.max_personas} Precio: {i.precio}")
                cont+=1
                if cont == num_a_ver:
                    return
