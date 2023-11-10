"""
###**Ejercicio 6.2**
Crear una clase de FiguraGeometrica:
*   Cuyo constructutor debe inicializar los atributos tipo_de_figura, color, y tamaño (por defecto "pequeño")
*   Se deben crear 3 metodos en la clase:
    1.  Presentar la figura: Un {tipo_de_figura} de color {color} y tamaño {tamaño}
    2.  Cambiar color de figura e indicar nuevo color
    3.  verificar si la figura es tamaño pequeño, agrandar a tamaño grande"""

class FiguraGeometrica:
    def __init__(self,tipo_de_figura, color, tamanio): 
        self.tipo_de_figura = tipo_de_figura
        self.color = color
        self.tamanio  = tamanio

    def presentar(self):
        print(f'La figura es un {self.tipo_de_figura} , color {self.color} y tamaño {self.tamanio}')

    def cambiar_color(self): 
        nuevo_color = input("Ingrese un nuevo color para la figura")
        self.color == nuevo_color

    def verificar_tamanio(self): 
        if (self.tamanio) == ("pequeño"):
            self.tamanio == "grande"
        else:
            print ("El tamaño no es pequeño")

figura_1 = FiguraGeometrica ("cuadrado", "rojo", "pequeño")
figura_1.presentar()
figura_1.cambiar_color
figura_1.verificar_tamanio()